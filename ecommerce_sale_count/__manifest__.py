{
    "name": "eCommerce Sale Count",
    "version": "1.0",
    "author": "Business Suite Team",
    "category": "eCommerce",
    "summary": "Shows sales counter on website/shop page",
    "description": "",
    "sequence": 1,
    "depends": [
        "ecommerce"
    ],
    "data": [
        "views/template.xml"
    ],
    "demo": [],
    "assets": {
        "web.assets_frontend": [
            "ecommerce_sale_count/static/src/**/*",
        ],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
