{
    "name": "eCommerce Product Labels",
    "version": "1.0",
    "author": "Business Suite Team",
    "category": "eCommerce",
    "summary": "Assign & Customize Product Labels, Stickers and Ribbons on products",
    "description": "",
    "sequence": 1,
    "depends": [
        "website",
        "ecommerce",
        "sale_management"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/product_label.xml",
        "views/template.xml",
    ],
    "demo": [],
    "assets": {
        "web.assets_frontend": [
            "ecommerce_labels/static/src/**/*",
        ],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
