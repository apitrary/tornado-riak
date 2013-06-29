# -*- coding: utf-8 -*-
"""

    tornado-riak

    Copyright (c) 2012-2013 apitrary

"""

APP_DETAILS = {
    'name': 'Tornado-Riak',
    'version': '0.1.5',
    'company': 'apitrary',
    'support': 'http://apitrary.com/support',
    'contact': 'support@apitrary.com',
    'copyright': '(c) 2012 - 2013 apitrary.com',
}

ILLEGAL_ATTRIBUTES_SET = ['_createdAt', '_updatedAt', '_init']
ILLEGAL_CHARACTER_SET = ['_', '__']

TORNADO_APP_SETTINGS = {
    'cookie_secret': 'PUT_YOUR_SECRET_HERE',
    'xheaders': True
}
