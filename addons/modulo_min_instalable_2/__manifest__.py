{
    'name': 'Módulo Mínimo Instalable 2',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Un segundo módulo básico para Odoo 18',
    'author': 'Tu Nombre',
    'depends': ['base'],
    'data': [
        'views/modulo_min_instalable_2_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
