from odoo import models, fields

class Doctor(models.Model):
    _name = 'doctor.management'
    _description = 'Doctor Details'

    name = fields.Char(string='Doctor Name', required=True)
    age = fields.Integer(string='Age')
    address = fields.Text(string='Address')
    education = fields.Char(string='Education')
    specialization = fields.Char(string='Specialization')
    phone_no = fields.Char(string='Phone Number')
    email_id = fields.Char(string='Email')