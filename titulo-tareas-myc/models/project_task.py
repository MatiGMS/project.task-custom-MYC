# -*- coding: utf-8 -*-

from odoo import api, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def default_get(self, fields_list):
        # llamamos primero al default_get original
        res = super().default_get(fields_list)

        # si ya viene un name por contexto, no lo pisamos
        if res.get('name'):
            return res

        # intentamos obtener el partner desde el contexto
        partner_id = self.env.context.get('default_partner_id')
        if not partner_id:
            return res

        partner = self.env['res.partner'].browse(partner_id)

        # si el partner tiene x_studio_nombre_fantasa, lo usamos como título
        nombre_fantasia = getattr(partner, 'x_studio_nombre_fantasa', False)
        if nombre_fantasia:
            res['name'] = nombre_fantasia

        return res