# -*- coding: utf-8 -*-

from odoo import models, fields, api

class filiere(models.Model):
     _name = 'gestion.filiere'
     _description = 'Modèle pour la gestion des filières'
     ID_filiere= fields.Integer()
     intitule = fields.Char()
     code = fields.Char()
     cycle = fields.Char(default='Ingénieur', readonly=True)
     def changerCycle(self):
       if self.cycle == 'Ingénieur':
        self.cycle = 'Préparatoire'
       else:
        self.cycle = 'Ingénieur'

class module(models.Model):
     _name = 'gestion.module'
     _description = 'Modèle pour la gestion des modules'
     ID_Module = fields.Integer()
     codeModule = fields.Char()
     NomModule = fields.Char()
     description = fields.Char()
     filiere_id = fields.Many2one('gestion.filiere', string="Filière")

class etudiant(models.Model):
     _name = 'gestion.etudiant'
     _description = 'Modèle pour la gestion des étudiants'
     NumApogee = fields.Integer()
     Nom = fields.Char()
     Prenom = fields.Char(string="Prénom")
     Email = fields.Char()
     Tel = fields.Integer()
     villes = [('oujda', "Oujda"), ('nador', "Nador"), ('berkane', "Berkane")]
     Ville = fields.Selection(selection=villes, default='oujda')
     Image = fields.Binary('Photo')
     filiere_id = fields.Many2one('gestion.filiere', 'ID_filiere')

