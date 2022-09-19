from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    order_cod_available = fields.Boolean('Allow Cash on Delivery For Sale order', default=False)
