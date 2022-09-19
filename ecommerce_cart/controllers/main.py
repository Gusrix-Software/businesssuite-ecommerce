import json

from odoo import _, http
from odoo.addons.ecommerce.controllers.main import Ecommerce
from odoo.http import request


class AdvanceCartSetting(Ecommerce):

    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        """This route is called when adding a product to cart (no options)."""
        # res = super(AdvanceCartSetting,self).cart_update()
        sale_order = request.website.sale_get_order(force_create=True)
        if sale_order.state != 'draft':
            request.session['sale_order_id'] = None
            sale_order = request.website.sale_get_order(force_create=True)

        product_custom_attribute_values = None
        if kw.get('product_custom_attribute_values'):
            product_custom_attribute_values = json.loads(kw.get('product_custom_attribute_values'))

        no_variant_attribute_values = None
        if kw.get('no_variant_attribute_values'):
            no_variant_attribute_values = json.loads(kw.get('no_variant_attribute_values'))

        sale_order._cart_update(
            product_id=int(product_id),
            add_qty=add_qty,
            set_qty=set_qty,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_values=no_variant_attribute_values
        )

        res_config_obj = request.env['res.config.settings']
        redirect_opt = res_config_obj.sudo().search([], limit=1, order="id desc").redirect_opt
        subtotal_of_orderline = res_config_obj.sudo().search([], limit=1, order="id desc").subtotal_of_orderline

        return_url = ''
        if redirect_opt and redirect_opt == 'same':
            path = request.httprequest.headers.environ.get("HTTP_REFERER")
            if path and 'shop' in str(path):
                if path.split('/shop')[1]:
                    return_url = request.redirect(request.httprequest.headers.environ.get("HTTP_REFERER"))
                elif not path.split('/shop')[1]:
                    return_url = request.redirect("/shop")
            else:
                return_url = request.redirect("/shop/cart")
        elif redirect_opt == 'cart':
            return_url = request.redirect("/shop/cart")
        else:
            if kw.get('express'):
                return request.redirect("/shop/checkout?express=1")

            return request.redirect("/shop/cart")

        return return_url

    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **post):

        order = request.website.sale_get_order()
        cart_total = order.amount_total

        res_config_obj = request.env['res.config.settings']
        min_cart_value = res_config_obj.sudo().search([], limit=1, order="id desc").min_cart_value

        if float(min_cart_value) > float(cart_total):
            return request.redirect(
                "/shop/cart?error_msg=%s" % _('Minimum cart amount is %s and your current order amount %s.') % (
                    min_cart_value, cart_total))

        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection

        if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
            return request.redirect('/shop/address')

        for f in self._get_mandatory_fields_billing():
            if not order.partner_id[f]:
                return request.redirect('/shop/address?partner_id=%d' % order.partner_id.id)

        values = self.checkout_values(**post)

        if post.get('express'):
            return request.redirect('/shop/confirm_order')

        values.update({'website_sale_order': order})

        # Avoid useless rendering if called in ajax
        if post.get('xhr'):
            return 'ok'
