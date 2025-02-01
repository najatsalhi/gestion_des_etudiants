from odoo import models, fields, api

class MyWizard(models.TransientModel):
    _name = 'gestion.wizard'
    _description = 'Example Wizard'

    date_start = fields.Date(string="Date Début")
    date_end = fields.Date(string="Date Fin")

    def confirm_action(self):
        # Action déclenchée à la confirmation
        print(f"Dates sélectionnées : {self.date_start} à {self.date_end}")