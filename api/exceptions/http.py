# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.exceptions import APIException


class BadGateway(APIException):
    """Bad gateway exception, used when one server on the internet received
    an invalid response from another server.

    In our case, if the request headers does not contains REMOTE_ADDR, it may be
    an invalid web server configuration / proxy forwarding, so we raise this error as
    a side-effect.
    """

    status_code = 502
    default_detail = 'Bad gateway, please try later.'
    default_code = 'bad_gateway'
