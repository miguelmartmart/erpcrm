{
    'name': 'Módulo Mínimo Instalable 3',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Un tercer módulo básico para Odoo 18',
    'author': 'Tu Nombre',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/modulo_min_instalable_3_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
