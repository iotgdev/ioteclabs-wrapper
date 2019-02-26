import unittest

import mock

from ioteclabs_wrapper.core.access import get_labs_dal, LabsDAL
from ioteclabs_wrapper.core.exceptions import LabsBadRequest, LabsException, LabsNotAuthenticated, \
    LabsPermissionDenied, LabsResourceNotFound, LabsAPIException


class TestLabsDalPrivateCall(unittest.TestCase):

    def setUp(self):
        self.dal = LabsDAL()

    def test_bad_response_400(self):
        self.dal.endpoint_url = ''  # for safety
        with mock.patch('ioteclabs_wrapper.core.access.LabsDAL.session', new_callable=mock.PropertyMock) as p:
            p.return_value = p.get = p
            p.status_code = 400
            with self.assertRaises(LabsBadRequest):
                self.dal._call('get', [])

    def test_bad_response_401(self):
        self.dal.endpoint_url = ''  # for safety
        with mock.patch('ioteclabs_wrapper.core.access.LabsDAL.session', new_callable=mock.PropertyMock) as p:
            p.return_value = p.get = p
            p.status_code = 401
            with self.assertRaises(LabsNotAuthenticated):
                self.dal._call('get', [])

    def test_bad_response_403(self):
        self.dal.endpoint_url = ''  # for safety
        with mock.patch('ioteclabs_wrapper.core.access.LabsDAL.session', new_callable=mock.PropertyMock) as p:
            p.return_value = p.get = p
            p.status_code = 403
            with self.assertRaises(LabsPermissionDenied):
                self.dal._call('get', [])

    def test_bad_response_404(self):
        self.dal.endpoint_url = ''  # for safety
        with mock.patch('ioteclabs_wrapper.core.access.LabsDAL.session', new_callable=mock.PropertyMock) as p:
            p.return_value = p.get = p
            p.status_code = 404
            with self.assertRaises(LabsResourceNotFound):
                self.dal._call('get', [])

    def test_bad_response_500(self):
        self.dal.endpoint_url = ''  # for safety
        with mock.patch('ioteclabs_wrapper.core.access.LabsDAL.session', new_callable=mock.PropertyMock) as p:
            p.return_value = p.get = p
            p.status_code = 500
            with self.assertRaises(LabsAPIException):
                self.dal._call('get', [])

    def test_bad_response_unsupported_exception(self):
        self.dal.endpoint_url = ''  # for safety
        with mock.patch('ioteclabs_wrapper.core.access.LabsDAL.session', new_callable=mock.PropertyMock) as p:
            p.return_value = p.get = p
            p.status_code = 418  # i'm a teapot
            with self.assertRaises(LabsException):
                self.dal._call('get', [])

    def test_good_response(self):
        self.dal.endpoint_url = ''
        with mock.patch('ioteclabs_wrapper.core.access.LabsDAL.session', new_callable=mock.PropertyMock) as p:
            p.return_value = p.get = p
            p.status_code = 200
            self.assertEqual(self.dal._call('get', []), p)


class TestLabsDalAuthenticate(unittest.TestCase):

    def setUp(self):
        self.dal = LabsDAL()
        self.dal._call = mock.Mock()
        self.dal._call.return_value = self.dal._call
        # noinspection PyUnresolvedReferences
        self.dal._call.json.return_value = {'token': 'token'}

    def test_get_credentials(self):
        with mock.patch('ioteclabs_wrapper.core.access.get_labs_credentials') as f:
            self.dal.authenticate()
            self.assertEqual(f.called, True)
        # noinspection PyUnresolvedReferences
        self.assertEqual(self.dal._call.called, True)

    def test_not_get_credentials(self):
        with mock.patch('ioteclabs_wrapper.core.access.get_labs_credentials') as f:
            self.dal.authenticate('username', 'password')
            self.assertEqual(f.called, False)
        # noinspection PyUnresolvedReferences
        self.assertEqual(self.dal._call.called, True)


class TestLabsDalCall(unittest.TestCase):

    def setUp(self):
        self.dal = LabsDAL()
        self.dal.authenticate = mock.Mock()

    def test_recurse(self):
        self.dal._call = mock.Mock(side_effect=[LabsNotAuthenticated('Test'), None])
        self.dal.call('method', [])
        # noinspection PyUnresolvedReferences
        self.assertEqual(self.dal.authenticate.called, True)


class TestGetLabsDal(unittest.TestCase):

    def test_singleton(self):
        dal1 = get_labs_dal()
        dal2 = get_labs_dal()
        self.assertIs(dal1, dal2)
