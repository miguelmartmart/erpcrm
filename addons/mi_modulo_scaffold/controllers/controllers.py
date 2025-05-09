# -*- coding: utf-8 -*-
from odoo import http


class MiModuloScaffold(http.Controller):
    @http.route('/mi_modulo_scaffold/mi_modulo_scaffold', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/mi_modulo_scaffold/mi_modulo_scaffold/objects', auth='public')
    def list(self, **kw):
        return http.request.render('mi_modulo_scaffold.listing', {
            'root': '/mi_modulo_scaffold/mi_modulo_scaffold',
            'objects': http.request.env['mi_modulo_scaffold.mi_modulo_scaffold'].search([]),
        })

    @http.route('/mi_modulo_scaffold/mi_modulo_scaffold/objects/<model("mi_modulo_scaffold.mi_modulo_scaffold"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('mi_modulo_scaffold.object', {
            'object': obj
        })
