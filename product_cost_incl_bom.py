# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Alexandre Fayolle
#    Copyright 2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv.orm import Model
from openerp.osv import fields
import decimal_precision as dp

class Product(Model):
    _inherit = 'product.product'

    _columns = {
        'cost_price_db': fields.float(string='Cost Price stored',
                                      digits_compute = dp.get_precision('Sale Price'))
        }

    def store_cost_price(self, cr, uid, ids, context=None):
        res = self.get_cost_field(cr, uid, ids, context=context)
        
        for prod_id, price in res.iteritems():
            self.write(cr, uid, [prod_id], {'cost_price_db': price}, context=context)

