from odoo import fields, models


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    website_note = fields.Text(string="Note")
