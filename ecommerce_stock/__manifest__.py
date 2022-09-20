# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo Website Product Stock',
    'description': """This module is used to manage stock on webshop, stock on website, stock on eCommerce inculding following feature.
    Website Stock Webshop stock Stock on website Show out of stock on website Show Stock Quantity on webshop
     Stock Quantity on Website product stock on website product quantity on website website product quantity 
     website item quantity webshop feature manage website stock manage stock Out of stock in webshop stock counter
     website item counter product counter Stock in website stock in webshop stock in shop shop stock
     stock shop Quantity on shop item on shop Shop Quantity item Shop Item quantity on shop. 
     Show Product stock on website Display Out of stock tag when stock not available
      display stock in Webshop interface also the seller can select and display different type of stock like 
      Qty on hand Qty Available in Website Configuration from back-end and 
      also Enable/disable stock messages and validation from the webshop.
      website stock notify on website
      website stock notification on website

website stock
website item stock
website inventory

Website Product Stock Info
In Stock and Out of Stock Products 
show out of stock alert 

InStock and Out of Stock Products 

website Out of Stock Products 
 Odoo stock alert
 out of stock products
 Track out-of-stock

    """ ,
    'summary': 'website Show Product stock on website stock not available Back in Stock Product Alerts shop Stock Notifier website low stock alerts low stock notification Out of Stock Notification Product Stock Alert Back in stock Restocked Alerts website Stock visibility',
    'category': 'eCommerce',
    'version': '1.0',
    'author': 'BrowseInfo',
    'depends': ['website','ecommerce','stock'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/template.xml',
    ],
    'application': True,
    "auto_install": False,
    'installable': True,
    'license': 'OPL-1',
    'assets':{
        'web.assets_frontend':[
        '/ecommerce_stock/static/src/js/custom.js',
        ]
    },
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
