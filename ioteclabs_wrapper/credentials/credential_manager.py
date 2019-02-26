#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For setting and returning labs passwords (visible only to current environment user).
"""
from __future__ import unicode_literals

import keyring
import getpass


def store_labs_credentials(username, password):
    """
    Store iotec labs API credentials in os profiles keyring

    :param str|unicode username: iotec labs API username
    :param str|unicode password: iotec labs API password
    """
    user = getpass.getuser()
    keyring.set_password("ioteclabs_username", user, username)
    keyring.set_password("ioteclabs_password", user, password)


def get_labs_credentials():
    """
    Retrieve stored iotec labs API credentials from os profile
    :rtype: dict[str|unicode, str|unicode]
    :return: labs credentials, e.g. {"username":"foo", "password":"bar"}
    """
    user = getpass.getuser()
    return {
        'username': keyring.get_password("ioteclabs_username", user),
        'password': keyring.get_password("ioteclabs_password", user)
    }
