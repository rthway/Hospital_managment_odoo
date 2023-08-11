{
    'name': 'Doctor Management',
    'version': '1.0',
    'summary': 'Manage doctor details',
    'description': 'Module to manage doctor details including name, age, address, education, specialization, phone, and email.',
    'author': 'Roshan Kumar Thapa',
    'website': 'https://github.com/rthway',
    'sequence':'-131',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/doctor_view.xml',
        'views/menu.xml',
    ],
    'application': True,
    'auto_install': True,
    'icon': 'patient_app/static/images/icon.png',
}