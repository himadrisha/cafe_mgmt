# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Cafe Management',
    'version': '16.0',
    'summary': 'Cafe Management',
    'sequence': 4,
    'description': """
Invoicing & Payments
====================
managing the affairs of a Cafe. Cafe management means running the school along the desired educational policies. 
It takes into account all aspects of the Cafe 
 and integrates them into a fruitful whole. """,
    'category': 'Cafe',


    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product.xml',
        'views/sale.xml',
        'views/tax.xml',
        'views/order_lines.xml',
        'views/tax_lines.xml',
        'wizard/report.xml',
        'report/report_sale.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',



}
