from odoo import models, fields

class XataConfig(models.Model):
    _name = 'xata.config'
    _description = 'Xata Configuration'

    name = fields.Char('Name', required=True)
    api_key = fields.Char('API Key')
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], default='active')
    last_sync = fields.Datetime('Last Sync')
    system_performance = fields.Char('System Performance')
    database_queries = fields.Integer('Database Queries')
    anomalies_detected = fields.Integer('Anomalies Detected')
    monitoring_data = fields.Text('Monitoring Data')
    suggestions = fields.Text('Suggestions')
    slow_queries_ids = fields.One2many('xata.slow.query', 'config_id', string='Slow Queries')

class XataSlowQuery(models.Model):
    _name = 'xata.slow.query'
    _description = 'Xata Slow Query'

    calls = fields.Integer('Calls')
    average_time = fields.Float('Average Time (s)')
    query = fields.Text('Query')
    config_id = fields.Many2one('xata.config', string='Xata Configuration')
