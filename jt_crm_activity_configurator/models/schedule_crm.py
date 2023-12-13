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

from odoo import fields, models, _

class ScheduleCrm(models.Model):

	_name = "schedule.auto.activity"

	name = fields.Char("Name")
	description = fields.Text("Description")
	due_day = fields.Integer("Due Day")
	code = fields.Char("Code")
	activity_type_id = fields.Many2one("mail.activity.type")
	activity_name = fields.Char(related="activity_type_id.name", store=True, string="Activity Name")
	how = fields.Selection([('manual','Manual'), ('automatic','Automatic')], default="manual", string="How?")
	stage_id = fields.Many2one("crm.stage", string="Status")
	is_mandatory = fields.Boolean("Is Mandatory?")

class MailActivity(models.Model):

	_inherit = 'mail.activity'

	is_mandatory = fields.Boolean("Is Mandatory?")
	stage_id = fields.Many2one("crm.stage", string="Status")



