# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2019 Compassion CH (http://www.compassion.ch)
#    Releasing children from poverty in Jesus' name
#    @author: Emanuel Cino <ecino@compassion.ch>
#
#    The licence is in the file __manifest__.py
#
##############################################################################


def migrate(cr, version):
    if not version:
        return

    # Remove problematic view before removing abroad field
    cr.execute("""
        delete from ir_ui_view
        where arch_db like '%abroad%' and model='res.partner' or
        inherit_id IN (
            select id from ir_ui_view
            where arch_db like '%abroad%' and model='res.partner'
        )
    """)
