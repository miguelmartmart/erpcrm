from odoo import http

class XataController(http.Controller):
    @http.route('/xata/data', auth='public')
    def get_xata_data(self):
        # Lógica para interactuar con el contenedor Docker de Xata
        return "Xata Data"
