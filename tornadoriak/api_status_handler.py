# -*- coding: utf-8 -*-
"""

    tornado-riak

    Copyright (c) 2012-2013 apitrary

"""
import tornado.ioloop
import tornado.web
import tornado.escape
from tornado import gen
import tornado.httpserver
import tornado.httputil
from tornadoriak.config import APP_DETAILS
from tornadoriak.base_handlers import BaseHandler


class ApiStatusHandler(BaseHandler):
    """
        GET '/'
        Shows status information about this about this deployed API
    """

    def __init__(self, application, request, api_version, api_id, schema, api_status_details=None, **kwargs):
        """
            Set up the basic Api Status handler responding on '/'
        """
        super(ApiStatusHandler, self).__init__(application, request, **kwargs)
        self.api_version = api_version
        self.api_id = api_id
        self.schema = schema
        self.api_status_details = APP_DETAILS
        if api_status_details is not None:
            self.api_status_details = api_status_details

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, *args, **kwargs):
        """
            Provides a basic hash with information for this deployed API.
        """
        # create status
        riak_ping_url = '{}/ping'.format(self.riak_url)
        response = yield tornado.gen.Task(self.async_http_client.fetch, riak_ping_url)
        riak_db_status = response.body

        status = {
            'db_status': riak_db_status,
            'api': {
                'api_version': self.api_version,
                'api_id': self.api_id
            }
        }

        application_status = {
            'info': self.api_status_details,
            'status': status,
            'schema': self.schema
        }

        self.write(application_status)
        self.finish()
