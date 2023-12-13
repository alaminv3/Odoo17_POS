# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (https://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'Users Role',
    'version': '1.0',
    'summary': 'Create Users based on the selected Role',
    'author': 'Bista Solutions Pvt.Ltd',
    'description': """
        Create users based on the selected the role.
        """,
    'category': 'Base',
    'website': 'https://www.bistasolutions.com',
    'depends': ['base', 'mail'],
    'data': [
        'views/res_users.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
