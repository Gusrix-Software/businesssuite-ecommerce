from odoo import fields, models


class ProductCategoryChanges(models.TransientModel):
    _name = 'product.category.changes'
    _description = "Product Category Changes"

    action_details = fields.Selection([
        ('c2c', 'Create all internal categories on website'),
        ('c2p', 'All product links with eCommerce categories'),
    ], string='operation doing', default='c2c')
    category_ids = fields.Many2many('product.category', 'cat_id', 'prod_cat_change', string="Product Category")

    def check_parent(self, new_cat, parent):
        e_parent_available = self.env['ecommerce.product.public.category'].search([('name', '=', parent.name)])
        if not e_parent_available:
            e_parent = self.env['ecommerce.product.public.category'].create({
                'name': parent.name,
                'internal_cat_id': parent.id
            })
            new_cat.update({'parent_id': e_parent.id})
            parent.update({
                'public_cat_id': e_parent.id
            })
            if parent.parent_id:
                parent_id = parent.parent_id
                self.check_parent(e_parent, parent_id)
        else:
            new_cat.update({'parent_id': e_parent_available.id})
            if parent.parent_id:
                parent_id = parent.parent_id
                self.check_parent(e_parent_available, parent_id)
        return

    def update_changes(self):
        ecommerce_cat = self.env['ecommerce.product.public.category']
        if self.action_details == "c2c":
            for cat in self.category_ids:
                available = ecommerce_cat.search([('name', '=', cat.name)])
                if not available:
                    new_cat = ecommerce_cat.create({
                        'name': cat.name,
                        'internal_cat_id': cat.id
                    })
                    cat.update({
                        'public_cat_id': new_cat.id
                    })
                    parent_id = cat.parent_id
                    if parent_id:
                        self.check_parent(new_cat, parent_id)
        if self.action_details == "c2p":
            for cat in self.category_ids:
                available = ecommerce_cat.search([('name', '=', cat.name)])
                if not available:
                    new_cat = ecommerce_cat.create({
                        'name': cat.name,
                        'internal_cat_id': cat.id
                    })
                    cat.update({
                        'public_cat_id': new_cat.id
                    })
                    parent_id = cat.parent_id
                    if parent_id:
                        self.check_parent(new_cat, parent_id)
            product_tmpl_id = self.env['product.template'].search([])
            for tmpl in product_tmpl_id:
                e_cat = self.env['ecommerce.product.public.category'].search([('name', '=', tmpl.categ_id.name)])
                tmpl.update({
                    'public_categ_ids': e_cat.ids
                })
