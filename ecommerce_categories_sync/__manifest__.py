{
    "name": "eCommerce Categories Sync",
    "version": "1.0",
    "author": "Business Suite Team",
    "category": "eCommerce",
    "summary": "Sync eCommerce categories with Product categories",
    "description": "",
    "sequence": 1,
    "depends": [
        "base",
        "ecommerce",
        "stock"
    ],
    "data": [
        "security/category_security.xml",
        "security/ir.model.access.csv",
        "views/res_config_settings.xml",
        "wizard/ecommerce_convert.xml",
    ],
    "demo": [],
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
