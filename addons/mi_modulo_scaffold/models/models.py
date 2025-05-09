# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mi_modulo_scaffold(models.Model):
    _name = 'mi_modulo_scaffold.mi_modulo_scaffold'
    _description = 'Mi Módulo Scaffold' # Added description

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self: # Added loop
            record.value2 = float(record.value) / 100
