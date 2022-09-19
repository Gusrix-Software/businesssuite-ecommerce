odoo.define('ecommerce_notes.custom_checks', function (require) {
    'use strict';

    var core = require('web.core');
    var ajax = require('web.ajax');
    var config = require('web.config');
    var concurrency = require('web.concurrency');
    var publicWidget = require('web.public.widget');
    var VariantMixin = require('sale.VariantMixin');
    var wSaleUtils = require('ecommerce.utils');
    const cartHandlerMixin = wSaleUtils.cartHandlerMixin;

    require("web.zoomodoo");

    var qweb = core.qweb;

    publicWidget.registry.WebsiteProductNotes = publicWidget.Widget.extend(VariantMixin, {
        selector: '.oe_ecommerce',
        events: {
            'click a.js_check_product.a-submit': '_onClickSubmitNotes',
        },

        _onClickSubmitNotes: function (ev) {
            var check_value = $('.add_value').val()
            var $parent;
            if ($(ev.currentTarget).closest('.oe_optional_products_modal').length > 0) {
                $parent = $(ev.currentTarget).closest('.oe_optional_products_modal');
            } else if ($(ev.currentTarget).closest('form').length > 0) {
                $parent = $(ev.currentTarget).closest('form');
            } else {
                $parent = $(ev.currentTarget).closest('.o_product_configurator');
            }
            var note;
            if ($('.product_note').val()) {
                var note = $('.product_note').val();
            } else {
                var note = "";
            }
            ev.currentTarget;ev.currentTarget;
            if (check_value === 'True') {
                ajax.jsonRpc('/shop/cart/update_json', 'call', {
                    'note': note,
                    'product_id': this._getProductId($parent),
                }).then(function (data) {
                });
            } else {
                ajax.jsonRpc('/update/product/note', 'call', {
                    'note': note,
                    'product_id': this._getProductId($parent),
                }).then(function (data) {
                });
            }
        },

    });
});
