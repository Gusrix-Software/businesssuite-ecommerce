from odoo import fields, models


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    is_website_note = fields.Boolean(string="Website Notes")
