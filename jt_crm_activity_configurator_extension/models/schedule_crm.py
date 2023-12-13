# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2022 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, _

class ScheduleCrm(models.Model):

	_inherit = "schedule.auto.activity"
	_description = "Inherits schedule.auto.activity model"

	assign_automatically = fields.Boolean("Assign Activity to Responsible User")