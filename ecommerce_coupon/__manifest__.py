# -*- coding: utf-8 -*-
{
    'name': "Coupons & Promotions for eCommerce",
    'summary': """Use coupon & promotion programs in your eCommerce store""",
    'description': """
Create coupon and promotion codes to share in order to boost your sales (free products, discounts, etc.). Shoppers can use them in the eCommerce checkout.

Coupon & promotion programs can be edited in the Catalog menu of the Website app.
    """,
    'category': 'Website/Website',
    'version': '1.0',
    'depends': ['ecommerce', 'website_links', 'sale_coupon'],
    'data': [
        'security/ir.model.access.csv',
        'views/coupon_share_views.xml',
        'views/ecommerce_templates.xml',
        'views/res_config_settings_views.xml',
        'views/sale_coupon_coupon_views.xml',
        'views/sale_coupon_program_views.xml',
    ],
    'auto_install': ['ecommerce', 'sale_coupon'],
    'assets': {
        'web.assets_frontend': [
            'ecommerce_coupon/static/src/js/coupon_toaster_widget.js',
        ],
        'web.assets_tests': [
            'ecommerce_coupon/static/tests/**/*',
        ],
    },
    'license': 'LGPL-3',
}
