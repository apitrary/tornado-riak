# -*- coding: utf-8 -*-
"""

    tornado-riak tests

    Copyright (c) 2012-2013 apitrary

"""
import json
from tornadoriak.response_types import Response, ErrorResponse


response = Response(status_code=200, status_message='OK', result={'key': 'some_value'})
error_response = ErrorResponse(error_message='BAD')


def test_response_str():
    assert str(response) == "Response(status_code=200, status_message=\"OK\", result=\"{\'key\': \'some_value\'}\")"


def test_response_repr():
    assert repr(response) == "Response(status_code=200, status_message=\"OK\", result=\"{\'key\': \'some_value\'}\")"


def test_response_get_data():
    assert response.get_data() == json.dumps({"result": {"key": "some_value"}})


def test_error_response_str():
    assert str(error_response) == "ErrorResponse(error_message=\"BAD\")"


def test_error_response_repr():
    assert repr(error_response) == "ErrorResponse(error_message=\"BAD\")"


def test_error_response_get_data():
    resp = json.loads(error_response.get_data())
    assert 'error' in resp
    assert 'message' in resp['error']
    assert resp['error']['message'] == 'BAD'
