#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
iotec labs API access classes
"""
from __future__ import unicode_literals

import requests

from ioteclabs_wrapper.core.exceptions import get_exception, LabsNotAuthenticated
from ioteclabs_wrapper.credentials.credential_manager import get_labs_credentials
from ioteclabs_wrapper.modules import account, admin, beeswax, right_person, xcm

try:
    unicode = unicode
except NameError:  # 2to3
    unicode = str


LABS_DAL = None


class LabsDAL(object):
    """
    DAL specific to iotec labs API
    Creates a session and authenticates it using the iotec labs API authentication endpoint
    """

    def __init__(self, username=None, password=None):
        self.url = 'https://api.ioteclabs.com/rest/'
        self.token = None
        self._session = None
        self.username = username
        self.password = password

    @property
    def session(self):
        """
        Get or create a requests Session
        :rtype: requests.Session
        """
        if not self._session:
            self._session = requests.Session()
        return self._session

    def _call(self, method, paths, **kwargs):
        """
        returns the results of an endpoint _call
        :rtype: requests.Response
        """
        url = self.url + '/'.join(map(unicode, paths))
        print(url)

        call_func = getattr(self.session, method.lower())
        response = call_func(url, **kwargs)

        if response.status_code == requests.codes.ok:
            return response
        else:
            raise get_exception(response)

    def authenticate(self, username=None, password=None):
        """
        Authenticates the user credentials provided
        :type username: str
        :type password: str
        :rtype: dict
        """
        if not (username and password):
            credentials = get_labs_credentials()
            username = username or credentials['username']
            password = password or credentials['password']

        parameters = {'username': username, 'password': password}

        resp = self._call('POST', ['authenticate', 'login'], json=parameters).json()

        if 'token' not in resp:
            raise LabsNotAuthenticated('Failed to authenticate.')

        self.token = resp['token']
        self.session.headers.update({'Authorization': 'Bearer ' + self.token})
        return resp

    def call(self, method, paths, **kwargs):
        """
        returns the results of an endpoint _call
        auto authenticates if connections go stale
        :rtype: requests.Response
        """
        if not self.token:
            self.authenticate(self.username, self.password)
        try:
            return self._call(method, paths, **kwargs)
        except LabsNotAuthenticated:
            self.authenticate(self.username, self.password)
            return self.call(method, paths, **kwargs)


def get_labs_dal():
    """
    'Singleton' iotec labs DAL.
    All LabsAPI classes share the same session per process by default
    """
    global LABS_DAL
    if LABS_DAL is None:
        LABS_DAL = LabsDAL()
    return LABS_DAL


class LabsAPI(object):
    """interface for communicating with the iotec labs API"""

    def __init__(self, username=None, password=None, dal=get_labs_dal()):
        """
        :type username: str
        :type password: str
        """
        self._dal = dal
        self.accounts = account.Account(self._dal)
        self.authentication = admin.Authentication(self._dal)
        self.beeswax = beeswax.Beeswax(self._dal)
        self.right_person = right_person.RightPerson(self._dal)
        self.xcm = xcm.XCM(self._dal)

        if username != self._dal.username or password != self._dal.password:
            self.change_user(username, password)

    def change_user(self, username, password):
        """
        Change the sessions user token
        :type username: str
        :type password: str
        :rtype: dict
        """
        self._dal.authenticate(username, password)
