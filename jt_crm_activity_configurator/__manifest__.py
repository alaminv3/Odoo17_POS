# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'CRM Activity Configurator',
    # 'version': '15.0.0.1',
    'summary': 'Auto schedule activity for different stages and make them enable mandatory to be close before stage move to another and can be configure for any stage with different no. of activities with and without mandatory to be closed.',
    'category': 'CRM',
    'author': 'Jupical Technologies Pvt. Ltd.',
    'maintainer': 'Jupical Technologies Pvt. Ltd.',
    'website': 'https://www.jupical.com',
    'depends' : ['crm'],
    #'depends': ['web_notify'],
    'data': [
        'security/ir.model.access.csv',
        'views/auto_schedule_activity.xml',
    ],
    'license': 'OPL-1',
    'application': True,
    'installable': True,
    'auto_install': False,
    'price': 49.00,
    'currency': 'EUR',
    'images': ['static/description/poster.gif'],
}