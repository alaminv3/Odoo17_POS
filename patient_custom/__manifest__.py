# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2022 (https://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'Patient Custom',
    'version': '1.0',
    'summary': 'Added some custom functionality to manage patient',
    'author': 'Bista Solutions Pvt.Ltd',
    'description': """
        Added some custom functionality to manage patient.
        """,
    'category': 'Base',
    'website': 'https://www.bistasolutions.com',
    'depends': ['base', 'mail', 'sale', 'contacts', 'stock',],
    'data': [
        'security/patients_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/patient_custom_contact.xml',
        'views/patient_contact.xml',
        # 'views/contact_type_views.xml',
        # 'views/rcp_program_views.xml',
        # 'views/rcp_status_views.xml',
        # 'views/sale_order_views.xml',
        # 'views/stock_picking_views.xml',
        # 'views/stock_move_line_views.xml',
        # 'views/stock_picking_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
