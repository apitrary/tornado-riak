# -*- coding: utf-8 -*-
"""

    tornado-riak tests

    Copyright (c) 2012-2013 apitrary

"""
import tornado
from tornado import httpclient
from tornadoriak.pre_hooks import curl_http_client
from tornadoriak.pre_hooks import database_bucket_url
from tornadoriak.pre_hooks import database_base_http_url


def test_store_init_object():
    pass


def test_curl_http_client():
    assert type(curl_http_client()) == type(tornado.httpclient.HTTPClient())


def test_precommit_hook_exists():
    pass


def test_precommit_hook():
    pass


def test_send_precommit_hook():
    pass


def test_database_base_http_url():
    assert database_base_http_url(db_host='localhost', db_port=8098) == 'http://localhost:8098'


def test_database_bucket_url():
    assert database_bucket_url(
        db_host='localhost',
        db_port=8098,
        bucket_name='some_bucket'
    ) == 'http://localhost:8098/riak/some_bucket'


def test_setup_indexing():
    pass


def test_initialize_buckets():
    pass


def test_pre_start_hook():
    pass