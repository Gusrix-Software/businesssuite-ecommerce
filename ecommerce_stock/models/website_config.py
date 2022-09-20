# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
import logging
_logger = logging.getLogger(__name__)

class ProductInherit(models.Model):
	_inherit = 'product.template'

	is_onhand = fields.Boolean(string='Is Onhand',compute='check_is_avaialable', default=True)
	is_avaialable = fields.Boolean(string='Is Available',compute='check_is_avaialable')


	def check_is_avaialable(self):
		for temp in self:
			is_positive = False
			is_avail = False
			if temp.type == 'product':
				prod = self.env['product.product'].search([('product_tmpl_id','=',temp.id)])
				for var in prod:
					avail = var.qty_available + var.incoming_qty - var.outgoing_qty
					if var.qty_available > 0 :
						is_positive = True
					if  avail > 0 :
						is_avail = True

			temp.is_onhand = is_positive
			temp.is_avaialable = is_avail

class website(models.Model):
	_inherit = 'website'
	
	def get_website_config(self):
		config_ids = self.env["ir.config_parameter"].sudo().get_param('ecommerce_stock.stock_type') 
		return str(config_ids) 


class website_config(models.TransientModel):
	_inherit = 'res.config.settings'
	
	stock_type = fields.Selection([('available', 'Qty On Hand'), ('outgoing', 'Qty Available')], default='available', string='Stock Type', help='Display Different stock type in Website.')
	

	def get_values(self):
		res = super(website_config, self).get_values()
		res.update(stock_type = self.env['ir.config_parameter'].sudo().get_param('ecommerce_stock.stock_type', default='available'))
		return res
	def set_values(self):
		super(website_config, self).set_values()
		self.env['ir.config_parameter'].sudo().set_param('ecommerce_stock.stock_type', self.stock_type)


	

