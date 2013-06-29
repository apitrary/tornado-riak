# -*- coding: utf-8 -*-
"""

    tornado-riak

    Copyright (c) 2012-2013 apitrary

"""

APP_DETAILS = {
    'name': 'Tornado-Riak',
    'version': '0.1.1',
    'company': 'apitrary',
    'support': 'http://apitrary.com/support',
    'contact': 'support@apitrary.com',
    'copyright': '(c) 2012 - 2013 apitrary.com',
}

ILLEGAL_ATTRIBUTES_SET = ['_createdAt', '_updatedAt', '_init']
ILLEGAL_CHARACTER_SET = ['_', '__']

COOKIE_SECRET = 'foh<Fei^joY(oo0hoh8eih4jumahx9toothahlah7eidieshei7ophiew7Oor1zudah^beefei1Zei;rauNeeTh9pu?wai3Ra'
TORNADO_APP_SETTINGS = {
    'cookie_secret': COOKIE_SECRET,
    'xheaders': True
}
