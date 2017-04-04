# -*- encoding: utf-8 -*-

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