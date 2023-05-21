# -*- coding: utf-8 -*-
from odoo import api, fields, models

import datetime


class voitureCars(models.Model):
    _name = "voiture.cars"
    _description = "Voiture Page"

    name = fields.Char('Model name', required=True)
    active = fields.Boolean(default=True)
    brand_id = fields.Many2one('vehicle.brand', 'Manufacturer', required=True, help='Manufacturer of the vehicle')
    image_128 = fields.Image(related='brand_id.image_128', readonly=True)
    nbrplace = fields.Char(string="Nombre de Places")
    longeur = fields.Char(string="Longeur(mm)")
    largeur = fields.Char(string="Largeur(mm)")
    hauteur = fields.Char(string="Hauteur(mm)")
    matricule = fields.Char(string="Matricule")
    coffre = fields.Char(string="Coffre")
    nbrcylinder = fields.Char(string="Nombre de Cylinder")
    prix = fields.Char(string="Prix DH/Jour")

    energie = fields.Selection([('essence', 'Essence'),
                                ('diesel', 'Diesel'), ('hybride', 'Hybride'),
                                ], required=False, string='Energie', default='essence')

    transmission = fields.Selection([('manuelle 5', 'Manuelle 5'),
                                     ('manuelle 6', 'Manuelle 6'), ('automatique', 'Automatique'),
                                     ], required=False, string='Transmission', default='manuelle 5')

    couleur = fields.Selection([('rouge', 'Rouge'), ('bleu', 'Bleu'), ('vert', 'Vert'), ('jaune', 'Jaune'),
                                ('violet', 'Violet'), ('orange', 'Orange'), ('rose', 'Rose'), ('marron', 'Marron'),
                                ('gris', 'Gris'), ('noir', 'Noir'), ('blanc', 'Blanc'),
                                ], string='Couleur', default='blanc')

    @api.depends('name', 'brand_id')
    def name_get(self):
        res = []
        for record in self:
            name = record.name
            if record.brand_id.name:
                name = record.brand_id.name + '/' + name
            res.append((record.id, name))
        return res


class vehicleBrand(models.Model):
    _name = 'vehicle.brand'
    _description = 'Brand of the vehicle'
    _order = 'model_count desc, name asc'

    name = fields.Char('Brand', required=True)
    image_128 = fields.Image("Logo", max_width=128, max_height=128)
    model_count = fields.Integer(compute="_compute_model_count", string="", store=True)
    model_ids = fields.One2many('voiture.cars', 'brand_id')

    @api.depends('model_ids')
    def _compute_model_count(self):
        Model = self.env['voiture.cars']
        for record in self:
            record.model_count = Model.search_count([('brand_id', '=', record.id)])
