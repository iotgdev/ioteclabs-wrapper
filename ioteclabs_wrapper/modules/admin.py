#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
classes to access iotec labs API authentication services
"""
from __future__ import unicode_literals

from ioteclabs_wrapper.core.base_classes import BaseAPI


class Authentication(BaseAPI):
    """iotec labs API authentication endpoint class"""

    paths = ['authenticate']

    def login(self, username, password):
        """
        :type username: str
        :type password: str
        :rtype: dict
        """
        return self._dal.authenticate(username, password)

    def refresh(self, token):
        """
        :type token: str
        :rtype: dict
        """
        return self._dal.call('POST', self.paths + ['refresh'], json={'token': token}).json()

    def verify(self, token):
        """
        :type token: str
        :rtype: dict
        """
        return self._dal.call('POST', self.paths + ['verify'], json={'token': token}).json()

    def masquerade(self, account=None):
        """
        Changes the user account
        :type account: str
        :rtype: dict
        """
        return self._dal.call('PATCH', self.paths + ['masquerade'], json={'account', account}).json()
