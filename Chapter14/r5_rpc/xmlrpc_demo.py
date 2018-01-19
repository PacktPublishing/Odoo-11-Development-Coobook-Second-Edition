#!/usr/bin/env python3
from xmlrpc.client import ServerProxy

db = 'odoo11_demo'
user = 'admin'
password = 'admin'
uid = ServerProxy('http://localhost:8069/xmlrpc/2/common')\
    .authenticate(db, user, password, {})
odoo = ServerProxy('http://localhost:8069/xmlrpc/2/object')
installed_modules = odoo.execute_kw(
    db, uid, password, 'ir.module.module', 'search_read',
    [[('state', '=', 'installed')], ['name']], {}
)
for module in installed_modules:
    print(module['name'])
