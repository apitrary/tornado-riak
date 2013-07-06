# -*- coding: utf-8 -*-
"""

    tornado-riak tests

    Copyright (c) 2012-2013 apitrary

"""
from tornado import httputil
from tornadoriak.header_service import HeaderService

VALID_HEADERS = {
    'Accept-Language': 'en-us', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'CocoaRestClient/10 CFNetwork/596.4.3 Darwin/12.4.0 (x86_64) (MacBookPro8%2C3)',
    'Host': 'localhost:7000',
    'X-Api-Key': '12345'
}

INVALID_HEADERS = {
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Accept': 'plain/text', # ILLEGAL FOR tornado-riak!
    'Content-Type': 'plain/text', # ILLEGAL FOR tornado-riak!
    'User-Agent': 'CocoaRestClient/10 CFNetwork/596.4.3 Darwin/12.4.0 (x86_64) (MacBookPro8%2C3)',
    'Host': 'localhost:7000',
    'X-Api-Key': '12345'
}


class SampleClass(HeaderService):
    def __init__(self, headers):
        http_headers = httputil.HTTPHeaders(headers)
        super(SampleClass, self).__init__(http_headers)


def test_has_valid_content_type():
    assert SampleClass(headers=VALID_HEADERS).has_valid_content_type()
    assert not SampleClass(headers=INVALID_HEADERS).has_valid_content_type()


def test_has_valid_accept_type():
    assert SampleClass(headers=VALID_HEADERS).has_valid_accept_type()
    assert not SampleClass(headers=INVALID_HEADERS).has_valid_accept_type()


def test_has_valid_headers():
    assert SampleClass(headers=VALID_HEADERS).has_valid_headers()
    assert not SampleClass(headers=INVALID_HEADERS).has_valid_headers()


def test_get_key_from_header():
    assert SampleClass(headers=VALID_HEADERS).get_key_from_header('X-Api-Key') == '12345'
