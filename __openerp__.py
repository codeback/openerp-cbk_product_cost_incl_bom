# -*- coding: utf-8 -*-
##############################################################################
#
#    Author:  Alexandre Fayolle, Codeback Software
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
{'name' : 'CBK Product Cost incl. BOM',
 'version' : '0.1',
 'author' : 'codeback',
 'maintainer': 'codeback',
 'category': 'Products',
 'complexity': "normal",  # easy, normal, expert
 'depends' : ['product_cost_incl_bom'],
 'description': """
  Add a button to store cost price in db
""",
 'website': 'http://www.codeback.es/',
 'init_xml': [],
 'update_xml': [],
 'data': ['wizard/store_price.xml'],
 'demo_xml': [],
 'tests': [],
 'installable': True,
 'auto_install': False,
 'license': 'AGPL-3',
 'application': False}
