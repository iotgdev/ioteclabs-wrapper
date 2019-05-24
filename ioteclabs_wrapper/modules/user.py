#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
classes to access iotec labs API user services
"""
from __future__ import unicode_literals
from ioteclabs_wrapper.core.base_classes import BaseAPI


class User(BaseAPI):
    """iotec labs User endpoint class"""

    paths = ['user']

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    # noinspection PyShadowingBuiltins
    def retrieve(self, id, **kwargs):
        """
        :type id: str
        :type kwargs: dict
        :rtype: dict
        """
        parameters = dict(id=id, **kwargs)
        return self._call('GET', params=parameters).json()

    def list(self, **kwargs):
        """
        :type kwargs: dict
        :rtype: dict
        """
        return self._call('GET', params=kwargs).json()

    # noinspection PyShadowingBuiltins
    def update(self, id, **kwargs):
        """
        :type id: str
        :type kwargs: dict
        :rtype: dict
        """
        parameters = dict(id=id, **kwargs)
        return self._call('PUT', json=parameters)
