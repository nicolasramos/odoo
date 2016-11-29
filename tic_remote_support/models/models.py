#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
#
# Difusión Visual
# Copyright (C) Difusión Visual
# all rights reserved
# http://difusionvisual.com
# contacto@difusionvisual.com
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs.
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/> or
# write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
###############################################

from odoo import api, fields, models, _


class TicRemoteSupportService(models.Model):
    _name = 'tic.remote.support.service'

    name = fields.Char(string="Name", required=True )
    remote_type = fields.Selection(string="Remote Type", selection=[
        ('teamviewer', 'TeamViewer'),
        ('weezo', 'Weezo'),
        ('ammyy', 'AMMYY'),
        ('vnc', 'VNC'),
        ('chrome', 'Chrome'),
        ('remotedesktop', 'Remote Desktop'),
        ('ssh', 'SSH'),
        ('web', 'Web'),
        ('other', 'Other')], required=False, )
    pc_type = fields.Selection(string="Device Type", selection=[
        ('workstation', 'WorkStation'),
        ('server', 'Server'),
        ('backup', 'Backup'),
        ('print', 'Print'),
        ('camera', 'Camera'),
        ('swich', 'Swich'),
        ('router', 'Router'),
        ('other', 'Other')], required=False, )
    remote_id = fields.Char(string="ID", required=False, )
    remote_serial = fields.Char(string="Serial", required=False, )
    remote_ip = fields.Char(string="IP", required=False, )
    remote_port = fields.Integer(string="Port", required=False, )
    remote_username = fields.Char(string="Username", required=False, )
    remote_password = fields.Char(string="Password", required=False, )
    remote_notes = fields.Text(string="Notes", required=False, )

class TicRemoteSupport(models.Model):
    _inherit = 'res.partner'

    supportbool = fields.Boolean(string="Remote Support?")
    remotes_ids = fields.Many2many(comodel_name="tic.remote.support.service", string="Remote Support", store=True)