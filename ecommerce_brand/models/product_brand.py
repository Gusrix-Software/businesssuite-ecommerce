from odoo import api, fields, models, tools

class SaleReportBrand(models.Model):
    _inherit = 'sale.report'

    brand_id = fields.Many2one('product.brand', 'Brand')

    def _select(self):
        select_str = """
            WITH currency_rate as (%s)
             SELECT min(l.id) as id,
                    l.product_id as product_id,
                    t.uom_id as product_uom,
                    t.brand_id as brand_id,
                    sum(l.product_uom_qty / u.factor * u2.factor) as product_uom_qty,
                    sum(l.qty_delivered / u.factor * u2.factor) as qty_delivered,
                    sum(l.qty_invoiced / u.factor * u2.factor) as qty_invoiced,
                    sum(l.qty_to_invoice / u.factor * u2.factor) as qty_to_invoice,
                    sum(l.price_total / COALESCE(cr.rate, 1.0)) as price_total,
                    sum(l.price_subtotal / COALESCE(cr.rate, 1.0)) as price_subtotal,
                    sum(l.amt_to_invoice / COALESCE(cr.rate, 1.0)) as amt_to_invoice,
                    sum(l.amt_invoiced / COALESCE(cr.rate, 1.0)) as amt_invoiced,
                    count(*) as nbr,
                    s.name as name,
                    s.date_order as date,
                    s.confirmation_date as confirmation_date,
                    s.state as state,
                    s.partner_id as partner_id,
                    s.user_id as user_id,
                    s.company_id as company_id,
                    extract(epoch from avg(date_trunc('day',s.date_order)-date_trunc('day',s.create_date)))/(24*60*60)::decimal(16,2) as delay,
                    t.categ_id as categ_id,
                    s.pricelist_id as pricelist_id,
                    s.analytic_account_id as analytic_account_id,
                    s.team_id as team_id,
                    p.product_tmpl_id,
                    partner.country_id as country_id,
                    partner.commercial_partner_id as commercial_partner_id,
                    sum(p.weight * l.product_uom_qty / u.factor * u2.factor) as weight,
                    sum(p.volume * l.product_uom_qty / u.factor * u2.factor) as volume
        """ % self.env['res.currency']._select_companies_rates()
        return select_str

    def _from(self):
        from_str = """
                sale_order_line l
                      join sale_order s on (l.order_id=s.id)
                      join res_partner partner on s.partner_id = partner.id
                        left join product_product p on (l.product_id=p.id)
                            left join product_template t on (p.product_tmpl_id=t.id)
                    left join product_uom u on (u.id=l.product_uom)
                    left join product_uom u2 on (u2.id=t.uom_id)
                    left join product_pricelist pp on (s.pricelist_id = pp.id)
                    left join currency_rate cr on (cr.currency_id = pp.currency_id and
                        cr.company_id = s.company_id and
                        cr.date_start <= coalesce(s.date_order, now()) and
                        (cr.date_end is null or cr.date_end > coalesce(s.date_order, now())))
        """
        return from_str

    def _group_by(self):
        group_by_str = """
            GROUP BY l.product_id,
                    l.order_id,
                    t.uom_id,
                    t.brand_id,
                    t.categ_id,
                    s.name,
                    s.date_order,
                    s.confirmation_date,
                    s.partner_id,
                    s.user_id,
                    s.state,
                    s.company_id,
                    s.pricelist_id,
                    s.analytic_account_id,
                    s.team_id,
                    p.product_tmpl_id,
                    partner.country_id,
                    partner.commercial_partner_id
        """
        return group_by_str


class PosOrderBrand(models.Model):
    _inherit = 'report.pos.order'

    brand_id = fields.Many2one('product.brand', 'Brand')

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'report_pos_order')
        self._cr.execute("""
            CREATE OR REPLACE VIEW report_pos_order AS (
                SELECT
                    MIN(l.id) AS id,
                    COUNT(*) AS nbr_lines,
                    s.date_order AS date,
                    SUM(l.qty) AS product_qty,
                    SUM(l.qty * l.price_unit) AS price_sub_total,
                    SUM((l.qty * l.price_unit) * (100 - l.discount) / 100) AS price_total,
                    SUM((l.qty * l.price_unit) * (l.discount / 100)) AS total_discount,
                    (SUM(l.qty*l.price_unit)/SUM(l.qty * u.factor))::decimal AS average_price,
                    SUM(cast(to_char(date_trunc('day',s.date_order) - date_trunc('day',s.create_date),'DD') AS INT)) AS delay_validation,
                    s.id as order_id,
                    s.partner_id AS partner_id,
                    s.state AS state,
                    s.user_id AS user_id,
                    s.location_id AS location_id,
                    s.company_id AS company_id,
                    s.sale_journal AS journal_id,
                    l.product_id AS product_id,
                    pt.categ_id AS product_categ_id,
                    pt.brand_id AS brand_id,
                    p.product_tmpl_id,
                    ps.config_id,
                    pt.pos_categ_id,
                    pc.stock_location_id,
                    s.pricelist_id,
                    s.session_id,
                    s.invoice_id IS NOT NULL AS invoiced
                FROM pos_order_line AS l
                    LEFT JOIN pos_order s ON (s.id=l.order_id)
                    LEFT JOIN product_product p ON (l.product_id=p.id)
                    LEFT JOIN product_template pt ON (p.product_tmpl_id=pt.id)
                    LEFT JOIN product_uom u ON (u.id=pt.uom_id)
                    LEFT JOIN pos_session ps ON (s.session_id=ps.id)
                    LEFT JOIN pos_config pc ON (ps.config_id=pc.id)
                GROUP BY
                    s.id, s.date_order, s.partner_id,s.state, pt.categ_id,
                    s.user_id, s.location_id, s.company_id, s.sale_journal,
                    s.pricelist_id, s.invoice_id, s.create_date, s.session_id,
                    l.product_id,
                    pt.categ_id, pt.pos_categ_id,
                    pt.brand_id,
                    p.product_tmpl_id,
                    ps.config_id,
                    pc.stock_location_id
                HAVING
                    SUM(l.qty * u.factor) != 0
            )
        """)
