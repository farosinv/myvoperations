# -*- coding: utf-8 -*-
# Copyright 2017 MyV Operaciones Logisticas & Faros Inversiones Ltda.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class Operaciones(models.Model):

    _name = 'operaciones'
    _description = 'Operaciones'  # TODO

    name = fields.Char()
