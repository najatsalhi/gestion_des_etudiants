# -*- coding: utf-8 -*-
{
    'name': "gestion",

    'summary': "Application pour la gestion des étudiants de la filière MGSI",

    'description': """
	Cette application vous permet de gérer tous les étudiants de la filière MGSI
    """,

    'author': "salhi najat",
    'website': "http://ensao.ump.ma/fr",

    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/gestion_security.xml',
        'views/gestion_menu.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/gestion_views.xml',
        'wizard/view_wizard.xml',
        'wizard/menu_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
