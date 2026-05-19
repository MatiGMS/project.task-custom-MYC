# -*- coding: utf-8 -*-

from odoo import api, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)

        if res.get('name'):
            return res

        partner_id = self.env.context.get('default_partner_id')
        if not partner_id:
            return res

        partner = self.env['res.partner'].browse(partner_id)

        nombre_fantasia = getattr(partner, 'x_studio_nombre_fantasa', False)
        if nombre_fantasia:
            res['name'] = nombre_fantasia

        return res