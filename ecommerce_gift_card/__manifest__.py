# -*- coding: utf-8 -*-


{
    'name': "eCommerce Gift Card",
    'summary': "Use gift card in eCommerce",
    'description': """Integrate gift card mechanism in your ecommerce.""",
    'category': 'Website/Website',
    'version': '1.0',
    'depends': ['ecommerce', 'sale_gift_card'],
    'data': [
        'views/template.xml',
        'views/gift_card_views.xml',
        'views/gift_card_menus.xml',
        ],
    'demo': [
        'data/product_demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'ecommerce_gift_card/static/**/*',
        ],
    },
    'license': 'LGPL-3',
}
