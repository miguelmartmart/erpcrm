{
    'name': 'Xata Integration',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Integrate Xata for Diagnostics, Monitoring, and Prediction',
    'author': 'Your Name',
    'depends': ['base', 'web'],
    'data': [
        'views/xata_menu.xml',
        'views/xata_dashboard.xml',
        'security/ir.model.access.csv',
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
