{
    "name": "Business Solutions eCommerce Notes",
    "version": "1.0",
    "author": "Business Suite Team",
    "category": "eCommerce",
    "summary": "Add notes fields in website shop product page and pass it to order lines",
    "description": "",
    "sequence": 1,
    "depends": [
        "account",
        "website",
        "ecommerce",
    ],
    "data": [
        "views/product_template_inherit_views.xml",
        "views/sale_order_inherit_views.xml",
        "views/ecommerce_inherit_views.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "ecommerce_notes/static/src/**/*",
        ]
    },
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
