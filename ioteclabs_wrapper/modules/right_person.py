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


class RightPersonResource(BaseAPI):
    """iotec labs API right-person resource endpoint class"""

    paths = ['right-person', 'resource']

    # noinspection PyShadowingBuiltins
    def retrieve(self, id, field):
        return self._dal.call('GET', self.paths + [id, field]).content
