{
    'name': 'Patient App',
    'summary': """
            core modules for Patient Application
        """,
    'author': 'Roshan kumar Thapa',
    'website': 'https://github.com/rthway',
    'version': '1.0',
    'sequence':'-130',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient_views.xml',
        'views/menu.xml',
    ],
    'application': True,
    'auto_install': True,
    'application': True,
    'icon': 'patient_app/static/images/patient.png',
}
