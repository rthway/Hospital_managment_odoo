from odoo import models, fields

class Appointment(models.Model):
    _name = 'appointment.appointment'
    _description = 'Appointment'

    _inherit = ['doctor.management', 'patient.app']


    name = fields.Many2one('doctor.management', string='Doctor', required=True, ondelete='cascade')
    patient = fields.Many2many('patient.app', string='Patient', required=True, ondelete='cascade')
    appointment_date = fields.Datetime(string='Appointment Date', required=True)
    notes = fields.Text(string='Notes')

