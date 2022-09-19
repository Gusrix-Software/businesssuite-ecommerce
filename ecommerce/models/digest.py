from odoo import fields, models, _
from odoo.exceptions import AccessError


class Digest(models.Model):
    _inherit = 'digest.digest'

    kpi_ecommerce_total = fields.Boolean('eCommerce Sales')
    kpi_ecommerce_total_value = fields.Monetary(compute='_compute_kpi_ecommerce_total_value')

    def _compute_kpi_ecommerce_total_value(self):
        if not self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            confirmed_website_sales = self.env['sale.order'].search([
                ('date_order', '>=', start),
                ('date_order', '<', end),
                ('state', 'not in', ['draft', 'cancel', 'sent']),
                ('website_id', '!=', False),
                ('company_id', '=', company.id)
            ])
            record.kpi_ecommerce_total_value = sum(confirmed_website_sales.mapped('amount_total'))

    def _compute_kpis_actions(self, company, user):
        res = super(Digest, self)._compute_kpis_actions(company, user)
        res['kpi_ecommerce_total'] = 'website.backend_dashboard&menu_id=%s' % self.env.ref(
            'website.menu_website_configuration').id
        return res
