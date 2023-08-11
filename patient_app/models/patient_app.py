
from datetime import datetime
from odoo import models,fields,api

class Patient(models.Model):
    
    _name = 'patient.app'
    _description = 'Patient Information'
    # _inherit = 'res.partner'

    # Auto-incremental patient identifier
    patient_identifier = fields.Char(string='Patient Identifier', required=True, copy=False, readonly=True, default=lambda self: self._generate_patient_identifier())

    patient_name = fields.Many2one('res.partner', string='Patient Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender', required=True)
    address = fields.Text(string='Address')
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    insurance_id = fields.Char(string='Insurance ID')

    # Age calculation
    patient_age = fields.Integer(string='Patient Age', compute='_compute_patient_age', store=True)

    # Function to auto-generate the patient identifier
    @api.model
    def _generate_patient_identifier(self):
        seq = self.env['ir.sequence'].sudo().next_by_code('patient.app.sequence') or ''
        return seq


    # Function to compute the patient's age based on the date of birth
    @api.depends('date_of_birth')
    def _compute_patient_age(self):
        today = datetime.today().date()
        for patient in self:
            if patient.date_of_birth:
                dob = patient.date_of_birth
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                patient.patient_age = age
            else:
                patient.patient_age = 0