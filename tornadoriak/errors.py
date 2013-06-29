# -*- coding: utf-8 -*-
"""

    tornado-riak

    by hgschmidt

    Copyright (c) 2012-2013 apitrary

"""
import logging


class TornadoRiakBaseException(Exception):
    """
        Thrown when a received message is of unknown type
    """

    def __init__(self, message, *args, **kwargs):
        """
            Log the message
        """
        super(TornadoRiakBaseException, self).__init__(*args, **kwargs)
        self.message = message
        logging.error(message)

    def __str__(self):
        """
            Message as string
        """
        return self.message


class NoDictionaryException(TornadoRiakBaseException):
    """
        Thrown when a received message is of unknown type
    """

    def __init__(self, message=None, *args, **kwargs):
        error_message = 'No dictionary provided!'
        if message:
            error_message = message
        super(NoDictionaryException, self).__init__(error_message, *args, **kwargs)


class RiakObjectNotFoundException(TornadoRiakBaseException):
    """
        Thrown when a received message is of unknown type
    """

    def __init__(self, message=None, *args, **kwargs):
        error_message = 'Object with given id not found!'
        if message:
            error_message = message
        super(RiakObjectNotFoundException, self).__init__(error_message, *args, **kwargs)


class RiakObjectIdNotProvidedException(TornadoRiakBaseException):
    """
        Thrown when an object ID was required but not provided
    """

    def __init__(self, message=None, *args, **kwargs):
        error_message = 'No object ID provided! Object ID required.'
        if message:
            error_message = message

        super(RiakObjectIdNotProvidedException, self).__init__(error_message, *args, **kwargs)
