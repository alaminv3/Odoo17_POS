# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models


class ResCountryState(models.Model):
    _inherit = "res.country.state"

    active = fields.Boolean("Active",default=True)