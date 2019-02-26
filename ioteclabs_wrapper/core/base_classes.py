#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base Classes for the beeswax wrapper
Components in this module should not be used but built upon
"""
from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod

from ioteclabs_wrapper.core.exceptions import LabsException

try:
    from boltons.funcutils import wraps
except ImportError:
    from functools import wraps

from six import with_metaclass


class LabsABCMeta(ABCMeta):

    def __new__(mcs, name, bases, attrs):
        """Wrap methods in LabsException raising"""
        for attr, pos_func in attrs.items():

            if callable(pos_func) and attr in {'retrieve', 'create', 'list', 'update', 'delete'}:
                attrs[attr] = LabsABCMeta.wrap_errors(pos_func)

        return super(LabsABCMeta, mcs).__new__(mcs, name, bases, attrs)

    @staticmethod
    def wrap_errors(func):
        @wraps(func)
        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except LabsException:
                raise
            except Exception as e:
                raise LabsException(e)
        return new_func


class BaseAPI(with_metaclass(LabsABCMeta, object)):
    """Base API class for attribute API structures"""

    def __init__(self, dal):
        """
        :type dal: ioteclabs_wrapper.core.access.LabsDAL
        """
        self._dal = dal

    @property
    @abstractmethod
    def paths(self):
        pass

    def _call(self, method, **kwargs):
        """
        Call to the DAL
        :type method: str
        :type kwargs: dict
        """
        return self._dal.call(method, self.paths, **kwargs)
