{
    "name": "eCommerce Stock",
    "version": "1.0",
    "author": "Business Suite Team",
    "category": "eCommerce",
    "summary": "Add product stock availability, back in stock and other information to eCommerce",
    "description": "",
    "sequence": 1,
    "depends": [
        "website",
        "ecommerce",
        "stock"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/template.xml",
    ],
    "demo": [],
    "assets": {
        "web.assets_frontend": [
            "ecommerce_stock/static/src/**/*",
        ]
    },
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
