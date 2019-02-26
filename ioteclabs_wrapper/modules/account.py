#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
classes to access iotec labs API account services
"""
from __future__ import unicode_literals
from ioteclabs_wrapper.core.base_classes import BaseAPI


class Account(BaseAPI):
    """iotec labs Account endpoint class"""

    paths = ['account']

    def __init__(self, *args, **kwargs):
        super(Account, self).__init__(*args, **kwargs)

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

    def create(self, name, **kwargs):
        """
        :type name: str
        :type kwargs: dict
        :rtype: dict
        """
        parameters = dict(account_name=name, **kwargs)
        return self._call('POST', json=parameters).json()

    # noinspection PyShadowingBuiltins
    def update(self, id, **kwargs):
        """
        :type id: str
        :type kwargs: dict
        :rtype: dict
        """
        parameters = dict(id=id, **kwargs)
        return self._call('PUT', json=parameters)

    # noinspection PyShadowingBuiltins
    def delete(self, id):
        """
        :type id: str
        """
        self._call('DELETE', json=dict(id=id))
        return
