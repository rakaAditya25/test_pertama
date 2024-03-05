# -*- coding: utf-8 -*-
{
    'name': 'Product Filter',
    'version': '1.0.0',
    'summary': 'Product Filter Task 1',
    'sequence': -10,
    'description': """Product Filter Task 1""",
    'category': 'hr',
    'author': 'raka',
    'maintainer': 'raka',
    'website': '',
    'license': 'AGPL-3',
    'depends':[ 'base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/wz_filter_product_view.xml',
    ],    
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
    }
}