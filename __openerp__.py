# -*- coding: utf-8 -*-
{
    'name': "BOM-Generator",

    'summary': """ Automatically generate BOMs for product variants.""",

    'description': """
        This module only serves the purpose of creating BOMs
    """,
    'sequence': 3,
    'author': "Benjamin Ulm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mrp', 'product'],

    # always loaded
    'data': [
        'wizard/bom_generator_wizard_view.xml',
        'bom_generator_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}