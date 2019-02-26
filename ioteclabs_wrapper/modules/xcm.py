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
        files = {}
        params = kwargs.pop('params', {})

        if any(isinstance(value, bytes) for key, value in kwargs):
            files = {key: (key, value) for key, value in kwargs}
            files['name'] = ('name', name)

        call_kwargs = {'files': files} if files else {'json': kwargs}

        return self._call('POST', params=params, **call_kwargs).json()

    # noinspection PyShadowingBuiltins
    def update(self, id, **kwargs):
        """
        :type id: str
        :type kwargs: dict
        :rtype: dict
        """
        files = {}
        params = kwargs.pop('params', {})

        if any(isinstance(value, bytes) for key, value in kwargs):
            files = {key: (key, value) for key, value in kwargs}
            files['id'] = ('id', id)

        call_kwargs = {'files': files} if files else {'json': kwargs}

        return self._call('PUT', params=params, **call_kwargs).json()

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
    def retrieve(self, id, field, **kwargs):
        """
        :type id: str
        :type field: str
        :type kwargs: dict
        :rtype: bytes
        """
        return self._dal.call('GET', self.paths + [id, field], params=kwargs).content
