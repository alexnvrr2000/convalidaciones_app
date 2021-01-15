 #-*- coding: utf-8 -*-
from odoo import models, fields, api


class modulo_model(models.Model):
    _name = 'convalidaciones_app.modulo_model'
    _description = 'convalidaciones_app.modulo_model'

    name = fields.Char(string="Nombre",required=True,help="Nombre del modulo")
    descripcion = fields.Html(string="Descripción",required=False,help="Descripcion del modulo")
    horas = fields.Integer(string="Horas del módulo",required=False,default=0,help="Horas del modulo")
    ciclo = fields.Many2one("convalidaciones_app.ciclo_model",string="Ciclo")
