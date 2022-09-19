# -*- encoding: utf-8 -*-
{
    'name': 'eCommerce Digital',
    'version': '1.0',
    'summary': 'Sell digital products in your eCommerce store',
    'category': 'Website/Website',
    'description': """
Sell e-goods in your eCommerce store (e.g. webinars, articles, e-books, video tutorials).
To do so, create the product and attach the file to share via the *Files* button of the product form.
Once the order is paid, the file is made available in the order confirmation page and in the customer portal.
    """,
    'depends': [
        'attachment_indexation',
        'ecommerce',
    ],
    'installable': True,
    'data': [
        'views/ecommerce_digital.xml',
        'views/ecommerce_digital_view.xml',
    ],
    'demo': [
        'data/product_demo.xml',
    ],
    'license': 'LGPL-3',
}
