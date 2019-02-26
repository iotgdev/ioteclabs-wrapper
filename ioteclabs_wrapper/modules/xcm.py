#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
classes to access iotec labs API xcm services
"""
from ioteclabs_wrapper.core.base_classes import BaseAPI


class XCM(BaseAPI):
    """iotec labs API xcm endpoint class"""

    def __init__(self, *args, **kwargs):
        super(XCM, self).__init__(*args, **kwargs)
        self.resources = XCMResource(*args, **kwargs)

    paths = ['xcm']

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
        return self._call('PUT', json=parameters).json()

    # noinspection PyShadowingBuiltins
    def delete(self, id):
        """
        :type id: str
        """
        self._call('DELETE', json=dict(id=id))
        return


class XCMResource(BaseAPI):
    """iotec labs API xcm resource endpoint class"""

    paths = ['xcm', 'resource']

    # noinspection PyShadowingBuiltins
    def retrieve(self, id, field):
        """
        :type id: str
        :type field: str
        :rtype: bytes
        """
        return self._dal.call('GET', self.paths + [id, field]).content
