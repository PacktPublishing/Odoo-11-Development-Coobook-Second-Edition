#!/usr/bin/env python3
import json
from urllib.request import Request, urlopen

db = 'odoo11_demo'
user = 'admin'
password = 'admin'

request = Request(
    'http://localhost:8069/web/session/authenticate',
    json.dumps({
        'jsonrpc': '2.0',
        'params': {
            'db': db,
            'login': user,
            'password': password,
        },
    }).encode('utf8'),
    {'Content-type': 'application/json'})
result = urlopen(request).read()
result = json.loads(result)
session_id = result['result']['session_id']
request = Request(
    'http://localhost:8069/web/dataset/call_kw',
    json.dumps({
        'jsonrpc': '2.0',
        'params': {
            'model': 'ir.module.module',
            'method': 'search_read',
            'args': [
                [('state', '=', 'installed')],
                ['name'],
            ],
            'kwargs': {},
        },
    }).encode('utf8'),
    {
        'X-Openerp-Session-Id': session_id,
        'Content-type': 'application/json',
    })
result = urlopen(request).read()
result = json.loads(result)
for module in result['result']:
    print(module['name'])
