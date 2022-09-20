odoo.define('ecommerce_stock.ecommerce_stock', function (require) {
    "use strict";
    var core = require('web.core');
    var _t = core._t;

    var ajax = require('web.ajax');
    $(document).ready(function () {
        $('.oe_ecommerce').each(function () {
            var oe_ecommerce = this;

            show_hide_stock_change();
            $(oe_ecommerce).on('change', function (ev) {
                show_hide_stock_change();
            });


            $(oe_ecommerce).on("change", 'input[name="add_qty"]', function (event) {
                var product_ids = [];
                var product_dom = $(".js_product .js_add_cart_variants[data-attribute_value_ids]");
                var qty = $(event.target).closest('form').find('input[name="add_qty"]').val();
                var $form_data = $('div.js_product').closest('form');
                let prod_type = $form_data.find('.show_hide_stock_change').attr('ptype');
                if (prod_type === 'product') {
                    var $js_qty = $form_data.find('.css_quantity.input-group.oe_website_spinner');
                    if ($("input[name='product_id']").is(':radio')) {
                        var product_id = $form_data.find("input[name='product_id']:checked").val();
                    } else {
                        var product_id = $form_data.find("input[name='product_id']").val();
                        var qty_available = $form_data.find('#' + product_id).attr('value');
                        if (qty_available < parseFloat(qty || 0)) {

                            var qty = $(event.target).closest('form').find('input[name="add_qty"]').val(parseInt(qty_available));
                            $('input[name="add_qty"]').popover({
                                animation: true,
                                title: _t('DENIED'),
                                container: 'body',
                                trigger: 'focus',
                                placement: 'top',
                                html: true,
                                content: _t('You Can Not Add More than Available Quantity'),
                            });
                            $('input[name="add_qty"]').popover('show');
                            setTimeout(function () {
                                $('input[name="add_qty"]').popover('hide')
                            }, 5000);

                        }
                    }
                }

            });


            $(oe_ecommerce).on("change", '.oe_cart input.js_quantity[data-product-id]', function (event) {
                var product_ids = [];
                var product_dom = $(".js_product .js_add_cart_variants[data-attribute_value_ids]");
                var qty = $(this).val();

                var $form_data = $('div.js_product').closest('form');
                /*let prod_type = $form_data.find('.show_hide_stock_change').attr('ptype');
                if(prod_type == 'product'){*/
                var $js_qty = $form_data.find('.css_quantity.input-group.oe_website_spinner');
                if ($("input[name='product_id']").is(':radio')) {
                    var product_id = $form_data.find("input[name='product_id']:checked").val();
                } else {
                    var product_id = $form_data.find("input[name='product_id']").val();
                    var qty_available = parseInt($(this).data('qty'), 10);
                    if (qty_available < qty) {
                        var qty = $(this).val(qty_available);
                        $('.js_quantity').popover({
                            animation: true,
                            //html: true,
                            title: _t('DENIED'),
                            container: 'body',
                            trigger: 'focus',
                            placement: 'top',
                            html: true,
                            content: _t('You Can Not Add More than Available Quantity'),
                        });
                        $('.js_quantity').popover('show');
                        setTimeout(function () {
                            $('.js_quantity').popover('hide')
                        }, 1000);
                    }
                }
                //}

            });
        });

        function show_hide_stock_change() {
            var $form_data = $('div.js_product').closest('form');
            var $js_qty = $form_data.find('.css_quantity.input-group.oe_website_spinner');
            if ($("input[name='product_id']").is(':radio')) {
                var product_id = $form_data.find("input[name='product_id']:checked").val();
            } else {
                var product_id = $form_data.find("input[name='product_id']").val();

                var inventory_availability = $form_data.find('#' + product_id).attr('available');

                var qty_available = $form_data.find('#' + product_id).attr('value');
                $form_data.find('.show_hide_stock_change').hide();
                $form_data.find('#' + product_id).show();
                let prod_type = $form_data.find('.show_hide_stock_change').attr('ptype');
                if (prod_type === 'product') {
                    if (qty_available <= 0 || inventory_availability === 'never') {
                        $('#add_to_cart').hide();
                        $js_qty.hide();
                    } else {
                        $('#add_to_cart').show();
                        $js_qty.show();
                    }
                }

            }
        }
    });
});
