from odoo import models, fields, api

class WizardAfficherEtudiants(models.TransientModel):
    _name = 'gestion.wizard_afficher_etudiants'
    _description = "Wizard pour afficher les étudiants par filière"

    filiere_id = fields.Many2one('gestion.filiere', string="Filière", required=True)
    etudiant_ids = fields.One2many('gestion.etudianttemp', 'wizard_id', string="Étudiants")

    @api.onchange('filiere_id')
    def _onchange_filiere_id(self):
        if self.filiere_id:
            etudiants = self.env['gestion.etudiant'].search([('filiere_id', '=', self.filiere_id.id)])
            self.etudiant_ids = [(5, 0, 0)]  # Supprime les lignes existantes
            for etudiant in etudiants:
                self.etudiant_ids = [(0, 0, {
                    'num_apogee': etudiant.NumApogee,
                    'nom': etudiant.Nom,
                    'prenom': etudiant.Prenom,
                    'email': etudiant.Email,
                    'ville': etudiant.Ville,
                })]

class TempEtudiant(models.TransientModel):
    _name = 'gestion.etudianttemp'
    _description = "Modèle temporaire pour afficher les étudiants"

    num_apogee = fields.Integer(string="Numéro Apogée")
    nom = fields.Char(string="Nom")
    prenom = fields.Char(string="Prénom")
    email = fields.Char(string="Email")
    ville = fields.Selection(selection=[
        ('oujda', "Oujda"),
        ('nador', "Nador"),
        ('berkane', "Berkane"),
    ], string="Ville")
    wizard_id = fields.Many2one('gestion.wizard_afficher_etudiants', string="Wizard")
