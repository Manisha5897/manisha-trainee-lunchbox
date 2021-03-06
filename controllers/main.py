# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request


class Customer(http.Controller):
    @http.route('/customer/', auth='public', website=True)
    def index(self, **kw):
        data = request.env['customer.detail'].search([])
        print("********************\n", data)
        return request.render('manisha_trainee_lunchbox.index', {
            'data': data,
        })

    @http.route(['/insert/', '/edit/<model("customer.detail"):d>'], auth='public', website=True, csrf=False)
    def insert(self, d=None):
        if d:
            d = request.env['customer.detail'].browse([d.id])
            return request.render('manisha_trainee_lunchbox.insert', {'d': d})
        return request.render('manisha_trainee_lunchbox.insert')

    @http.route(['/form/', '/form/<model("customer.detail"):d>'], method="POST", auth='public', type='http', website=True, csrf=False)
    def editable(self, d=None, **post):
        if post:
            if d:
                print("----------------", request.env)
                request.env['customer.detail'].browse([d.id]).write(post)
            else:
                request.env['customer.detail'].create(post)
        return request.redirect('/customer/')

    @http.route('/drop/<model("customer.detail"):d>', auth='public', type='http', website=True, csrf=False)
    def drop(self, d=None):
        d.unlink()
        return request.redirect('/customer/')

    @http.route('/userregister/', auth="public", type="http", csrf=False)
    def custmoer_register(self, **kw):
        currency = http.request.env['res.currency'].sudo().search([])
        return http.request.render('yourModuleName.TemplateLoginName', {'currency': currency})
