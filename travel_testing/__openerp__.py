# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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


{
    'name': 'Cuba Tourism Initial Data For Testing',
    'version': '1.0',
    "author": "JAF S.A.",
    "website": "http://www.jaf.com",
    'category': '?',
    'depends': ['travel_data'],
    "description": """ List of types of products and some data about them.""",
    'data': ['testing/product.car.xml',
             'testing/product.flight.xml',
             'testing/product.transfer.xml', 'testing/product.hotel.xml'
             ],
    'update_xml': [],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
    # 'certificate': '0071515601309',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
# 'data/destination.csv', 'data/res.partner.csv', 'data/product.product.csv', 'data/product.hotel.csv',
#                  'testing/option.value.xml', 'testing/product.car.xml', 'testing/product.flight.xml',
#                 'testing/product.transfer.xml', 'testing/product.hotel.xml'
