{
    "name": "eCommerce Brand",
    "author": "Business Suite Team",
    "version": "1.0",
    "category": "eCommerce",
    "summary": "Show brands with filters, sort and search on website",
    "description": "",
    "sequence": 1,
    "depends": [
        "website",
        "ecommerce",
        "bs_brand"
    ],
    "data": [
        "views/template.xml",
    ],
    "demo": [],
    "assets": {
        "web.assets_frontend": [
            "ecommerce_brand/static/src/**/*",
        ],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
