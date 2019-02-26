#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
classes to access iotec labs API beeswax services
"""
from ioteclabs_wrapper.core.base_classes import BaseAPI


class Beeswax(BaseAPI):
    """iotec labs API beeswax stub"""

    paths = ['beeswax']

    def __init__(self, *args, **kwargs):
        super(Beeswax, self).__init__(*args, **kwargs)
        self.right_person = BeeswaxRightPerson(self._dal)
        self.xcm = BeeswaxXCM(self._dal)


class BeeswaxRightPerson(BaseAPI):
    """iotec labs API beeswax right-person endpoint class"""

    paths = ['beeswax', 'right-person']

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


class BeeswaxXCM(BaseAPI):
    paths = ['beeswax', 'xcm']

    # noinspection PyShadowingBuiltins
    def retrieve(self, id, **kwargs):
        """
        :type id: str
        :type kwargs: dict
        :rtype: dict
        """
        parameters = dict(id=id, **kwargs)
        return self._call('GET', json=parameters).json()

    def list(self, **kwargs):
        """
        :type kwargs: dict
        :rtype: dict
        """
        return self._call('GET', json=kwargs).json()

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