{
    "name": "Brand",
    "author": "Business Suite Team",
    "category": "Sales",
    "version": "1.0",
    "summary": "Add Brand functionalities to products",
    "description": "",
    "sequence": 1,
    "depends": [
        "sale",
        "stock",
        "product"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/brand_view.xml",
        "views/product_view_inh.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
