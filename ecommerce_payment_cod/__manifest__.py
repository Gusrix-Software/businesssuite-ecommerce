{
    "name": "eCommerce Payment Cash on Delivery",
    "author": "Business Suite Team",
    "category": "eCommerce",
    "summary": "Add Cash on Delivery payment method to website",
    "version": "1.0",
    "description": "",
    "sequence": 1,
    "depends": [
        "sale",
        "account",
        "website",
        "ecommerce",
        "payment",
        "sale_management"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/cod_view.xml",
        "views/template.xml",
        "views/cod_collection_report.xml",
        "views/report_cod_collection.xml",
        "data/payment_acquirer_data.xml",
        "data/email.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "ecommerce_payment_cod/static/src/**/*",
        ]
    },
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
