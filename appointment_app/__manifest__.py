{
    'name': 'Appointment App',
    'version': '1.0',
    'summary': 'Manage appointments with doctor details',
    'description': 'Module to manage appointments with doctor details including appointment date and notes.',
    'author': 'Your Name',
    'sequence':'-132',
    'depends': ['base', 'doctor_app','patient_app'],
    'data': [
        'security/ir.model.access.csv',
        'views/appointment_view.xml',
    ],
    'application': True,
}