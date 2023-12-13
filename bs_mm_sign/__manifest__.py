# -*- coding: utf-8 -*-
{
    'name': "bs_mm_sign",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sign', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/custom_snippets.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'bs_mm_sign/static/src/js/*.js'
    #     ],
    #     'website.assets_wysiwyg': [
    #         'bs_mm_sign/static/src/js/snippets/wesite_employee_editor.js',
    #     ]
    # }
}

