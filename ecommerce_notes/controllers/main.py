from odoo import http
from odoo.addons.ecommerce.controllers.main import Ecommerce
from odoo.http import request


class WebsiteSaleProductNote(Ecommerce):

    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        rec = super(WebsiteSaleProductNote, self).cart_update(product_id, add_qty, set_qty, **kw)
        if 'product_note' in request.session:
            product_note = request.session["product_note"]
            if product_note['note']:
                sale_order = request.website.sale_get_order(force_create=True)
                line = sale_order.order_line.filtered(lambda s: s.product_id.id == int(product_note['product_id']))
                line.website_note = product_note['note']
            request.session.pop('product_note')
        return rec

    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, product_id, line_id=None, note=None, add_qty=None, set_qty=None, display=True, **kw):
        rec = super(WebsiteSaleProductNote, self).cart_update_json(product_id, line_id, note, add_qty, set_qty, **kw)
        if note:
            request.session['product_note'] = {'note': note, 'product_id': product_id, }
        if 'product_note' in request.session:
            product_note = request.session["product_note"]
            if product_note['note']:
                sale_order = request.website.sale_get_order(force_create=True)
                line = sale_order.order_line.filtered(lambda s: s.product_id.id == int(product_note['product_id']))
                line.website_note = product_note['note']
            request.session.pop('product_note')
        return rec

    @http.route(['/update/product/note'], type='json', auth="public", methods=['POST'], website=True)
    def update_product_note(self, note, product_id):
        if note:
            request.session['product_note'] = {'note': note, 'product_id': product_id, }
        return 0
