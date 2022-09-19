from odoo import models


class ResCountry(models.Model):
    _inherit = 'res.country'

    def get_ecommerce_countries(self, mode='billing'):
        return self.sudo().search([])

    def get_ecommerce_states(self, mode='billing'):
        return self.sudo().state_ids
