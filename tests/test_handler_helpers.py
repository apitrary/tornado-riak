# -*- coding: utf-8 -*-
"""

    tornado-riak tests

    Copyright (c) 2012-2013 apitrary

"""
import re
from tornadoriak.handler_helpers import pop_field
from tornadoriak.handler_helpers import filter_out_timestamps
from tornadoriak.handler_helpers import illegal_attributes_exist
from tornadoriak.handler_helpers import get_bucket_name
from tornadoriak.handler_helpers import get_current_time_formatted


def test_pop_field():
    dic = {'a': 'keyOne', 'b': 'keyTwo'}
    stripped_dic, stripped_obj = pop_field(dic, 'a')
    assert stripped_dic['b']
    assert dic['b']
    assert len(dic) == 1
    assert len(stripped_dic) == 1
    assert stripped_obj == 'keyOne'


def test_filter_out_timestamps():
    dic = {'a': 'keyOne', '_createdAt': 'aCreatedTime', '_updatedAt': 'anUpdatedTime'}
    stripped_dic, created_at, updated_at = filter_out_timestamps(dic)
    assert stripped_dic['a']
    assert dic['a']
    assert '_created_at' not in stripped_dic
    assert '_created_at' not in dic
    assert '_updated_at' not in stripped_dic
    assert '_updated_at' not in dic
    assert len(stripped_dic) == 1
    assert len(dic) == 1


def test_illegal_attributes_exist():
    illegal_dic = {'a': 'keyOne', '_illegal_key': 'someValue'}
    assert illegal_attributes_exist(illegal_dic)
    legal_dic = {'a': 'keyOne', 'legalKey': 'someOtherValue'}
    assert not illegal_attributes_exist(legal_dic)


def test_get_current_time_formatted():
    # Should match a date of format '06 Jul 2013 11:47:45 +0000'
    matches = re.match('^\d{2} \w{3} \d{4} \d{2}:\d{2}:\d{2} \+\d{4}$', get_current_time_formatted())
    assert matches


def test_validate_user_agent():
    pass


def test_get_bucket_name():
    assert get_bucket_name('SomeAPIID', 'anEntity') == 'SomeAPIID_anEntity'