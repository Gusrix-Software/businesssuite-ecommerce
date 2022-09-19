from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    website_id = fields.Many2one('website', related='partner_id.website_id', string='Website',
                                 help='Website through which this invoice was created.',
                                 store=True, readonly=True, tracking=True)
