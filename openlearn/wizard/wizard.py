# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openlearn.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    session_id = fields.Many2one('openlearn.session',
        string="Session", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")