# -*- coding: utf-8 -*-

from odoo import models, fields

class ModuloMinInstalable3(models.Model):
    _name = 'modulo.min.instalable.3'
    _description = 'Módulo Mínimo Instalable 3'

    name = fields.Char('Name')
