# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2022 (https://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'CRM Activity Configurator Extension',
    # 'version': '15.0.0.1',
    'summary': 'Extends Auto schedule activity for different stages and make them enable mandatory to be close before stage move to another and can be configure for any stage with different no. of activities with and without mandatory to be closed.',
    'category': 'CRM',
    'author': 'Bista Solutions Inc./Monwar Adeeb',
    'maintainer': 'Bista Solutions Inc.',
    'website': 'https://www.bistasolutions.com',
    'depends' : ['crm', 'jt_crm_activity_configurator'],
    'data': [
        'views/auto_schedule_activity_views.xml',
    ],
    'license': 'OPL-1',
    'application': True,
    'installable': True,
    'auto_install': False,
}
