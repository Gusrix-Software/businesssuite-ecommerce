from odoo import api, fields, models


class WebsiteConfig(models.TransientModel):
    _inherit = "res.config.settings"

    category_sync = fields.Boolean(string="eCommerce new Category Sync", default=False)
    product_sync = fields.Boolean(string="eCommerce new Product Sync", default=False)

    def get_values(self):
        res = super(WebsiteConfig, self).get_values()
        category_sync = self.env['ir.config_parameter'].sudo().get_param('ecommerce_categories_sync.category_sync')
        product_sync = self.env['ir.config_parameter'].sudo().get_param('ecommerce_categories_sync.product_sync')
        res.update(
            category_sync=category_sync,
            product_sync=product_sync
        )
        return res

    def set_values(self):
        super(WebsiteConfig, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'ecommerce_categories_sync.category_sync', self.category_sync
        )
        self.env['ir.config_parameter'].sudo().set_param(
            'ecommerce_categories_sync.product_sync', self.product_sync
        )


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def create(self, vals):
        res = super(ProductTemplate, self).create(vals)
        settings = self.env['res.config.settings'].search([], limit=1, order="id desc")
        if res:
            if settings.product_sync:
                e_cat = self.env['ecommerce.product.public.category'].search([('name', '=', res.categ_id.name)])
                res.update({
                    'public_categ_ids': e_cat.ids
                })
        return res


class ProductPublicCategory(models.Model):
    _inherit = "ecommerce.product.public.category"

    internal_cat_id = fields.Many2one('product.category', string="Internal Category")


class Productcategory(models.Model):
    _inherit = "product.category"

    public_cat_id = fields.Many2one('ecommerce.product.public.category', string='eCommerce category')

    @api.model
    def create(self, vals):
        res = super(Productcategory, self).create(vals)
        if res:
            settings = self.env['res.config.settings'].search([], limit=1, order="id desc")
            ecommerce_cat = self.env['ecommerce.product.public.category']
            if settings.category_sync:
                for cat in res:
                    available = ecommerce_cat.search([('name', '=', cat.name)])
                    if not available:
                        new_cat = ecommerce_cat.create({
                            'name': cat.name,
                            'internal_cat_id': cat.id
                        })
                        cat.update({'public_cat_id': new_cat.id})
                        parent_id = cat.parent_id
                        if parent_id:
                            self.check_parent(new_cat, parent_id)
        return res

    def check_parent(self, new_cat, parent):
        e_parent_available = self.env['ecommerce.product.public.category'].search([('name', '=', parent.name)])
        if not e_parent_available:
            e_parent = self.env['ecommerce.product.public.category'].create(
                {'name': parent.name, 'internal_cat_id': parent.id})
            new_cat.update({'parent_id': e_parent.id})
            parent.update({'public_cat_id': e_parent.id})
            if parent.parent_id:
                parent_id = parent.parent_id
                self.check_parent(e_parent, parent_id)
        else:
            new_cat.update({'parent_id': e_parent_available.id, 'internal_cat_id': parent.id})
            if parent.parent_id:
                parent_id = parent.parent_id
                self.check_parent(e_parent_available, parent_id)
        return

    def write(self, vals):
        res = super(Productcategory, self).write(vals)
        settings = self.env['res.config.settings'].search([], limit=1, order="id desc")
        if settings.category_sync:
            if self.public_cat_id:
                if self.public_cat_id.name != self.name:
                    self.public_cat_id.name = self.name
                if self.public_cat_id.parent_id.name != self.parent_id.name:
                    e_parent_available = self.env['ecommerce.product.public.category'].search(
                        [('name', '=', self.parent_id.name)])
                    if e_parent_available:
                        self.public_cat_id.parent_id = e_parent_available.id
                    else:
                        self.check_parent(self.public_cat_id, self.parent_id)
        return res
