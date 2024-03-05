# -*- coding: utf-8 -*-
{
    'name': 'Raja Ongkir',
    'version': '1.0.0',
    'summary': 'Raja Ongkir Belajar',
    'sequence': -10,
    'description': """Raja Ongkir Belajar""",
    'category': 'hr',
    'author': 'raka',
    'maintainer': 'raka',
    'website': '',
    'license': 'AGPL-3',
    'depends':[ 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/daerah.xml',
        'wizards/wz_get_data_ro_view.xml',
    ],    
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
    }
}