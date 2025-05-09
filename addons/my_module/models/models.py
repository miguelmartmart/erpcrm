# -*- coding: utf-8 -*-

from odoo import models, fields, api

class my_module(models.Model):
    _name = 'my_module.my_module'
    _description = 'My Module' # Added description for clarity

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self: # Added loop as compute fields should iterate
            record.value2 = float(record.value) / 100
