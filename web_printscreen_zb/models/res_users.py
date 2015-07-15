# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2015 Savoir-faire Linux
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import pytz
from datetime import datetime
from openerp.osv import orm


class ResUsers(orm.Model):
    _inherit = 'res.users'

    def get_printscreen_report_context(
        self, cr, uid, ids, context=None
    ):
        if isinstance(ids, (int, long)):
            ids = [ids]

        assert len(ids) == 1, 'Expected single record'

        user = self.browse(cr, uid, ids[0], context=context)

        tz = pytz.timezone(user.tz) if user.tz else pytz.utc
        date = datetime.now(tz)

        lang_name = user.lang or 'en_US'
        lang_pool = self.pool['res.lang']
        lang_id = lang_pool.search(
            cr, uid, [('code', '=', lang_name)], context=context)[0]
        lang = lang_pool.browse(cr, uid, lang_id, context=context)

        current_date = date.strftime(lang.date_format)

        return {
            'company_name': user.company_id.name,
            'company_logo': user.company_id.logo,
            'current_date': current_date,
        }
