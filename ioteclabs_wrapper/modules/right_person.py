#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
classes to access iotec labs API right-person services
"""
from ioteclabs_wrapper.core.base_classes import BaseAPI


class RightPerson(BaseAPI):
    """iotec labs API right-person endpoint class"""

    def __init__(self, *args, **kwargs):
        super(RightPerson, self).__init__(*args, **kwargs)
        self.resources = RightPersonResource(*args, **kwargs)

    paths = ['right-person']

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


class RightPersonResource(BaseAPI):
    """iotec labs API right-person resource endpoint class"""

    paths = ['right-person', 'resource']

    # noinspection PyShadowingBuiltins
    def retrieve(self, id, field, **kwargs):
        """
        :type id: str
        :type field: str
        :type kwargs: dict
        :rtype: bytes
        """
        return self._dal.call('GET', self.paths + [id, field], params=kwargs).content
