from odoo import models, fields

class ModuloMinInstalable(models.Model):
    _name = 'modulo.min.instalable'
    _description = 'Módulo Mínimo Instalable'

    name = fields.Char('Name')
