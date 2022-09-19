odoo.define('ecommerce_payment_cod.website_cod_payment', function (require) {
    "use strict";
    var core = require('web.core');
    var _t = core._t;
    var flag = 0;

    var ajax = require('web.ajax');
    $(document).ready(function () {
        var oe_ecommerce = this;
        var $payment = $("panel panel-default");
        var $carrier = $("#delivery_carrier");
        var payment_form = $('.o_payment_form');

        payment_form.find('.card-body').each(function () {
            if ($(this).find('label').length == 0) {
                $(this).hide();
            }
        });

        if (payment_form.find('.card-body').css('display') == 'none') {
            payment_form.parent().hide()
        }

    });

});
