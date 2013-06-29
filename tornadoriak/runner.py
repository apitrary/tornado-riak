# -*- coding: utf-8 -*-
"""

    tornado-riak

    Copyright (c) 2012-2013 apitrary

"""
import logging
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.httputil
import tornado.httpclient
from tornadoriak.config import TORNADO_APP_SETTINGS


def routes(parsed_opts):
    """
        Setup the URL routes with regex
    """
    pass


def _start_tornado_server(port, routes_configuration, cookie_secret=None):
    """
        Start the Tornado server
    """
    app_settings = TORNADO_APP_SETTINGS
    if cookie_secret is not None:
        app_settings['cookie_secret'] = cookie_secret

    application = tornado.web.Application(handlers=routes_configuration, **app_settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


def show_all_settings(opts, routes_configuration):
    """
        Show all routes configured for this service
    """
    assert opts.logging
    assert opts.port
    assert opts.riak_host
    assert opts.api_id
    assert opts.api_version

    logging.info('LOGGING LEVEL: {}'.format(opts.logging))
    logging.info('SERVER PORT: {}'.format(opts.port))
    logging.info('RIAK HOST: {}'.format(opts.riak_host))
    logging.info('ENTITIES: {}'.format(opts.entity))
    logging.info('API ID: {}'.format(opts.api_id))
    logging.info('API VERSION: {}'.format(opts.api_version))
    logging.info('API KEY PROVIDED: {}'.format(opts.api_key is not None))
    for route in routes_configuration:
        logging.info('NEW ROUTE: {} -- Handled by: "{}"'.format(repr(route[0]), route[1]))


def start_server(parsed_opts, cookie_secret=None):
    """
        Start the general server
    """
    routes_configuration = routes(parsed_opts)
    show_all_settings(parsed_opts, routes_configuration)

    assert parsed_opts.port
    _start_tornado_server(parsed_opts.port, routes_configuration, cookie_secret)

