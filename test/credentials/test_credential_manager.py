import unittest
import mock


from ioteclabs_wrapper.credentials.credential_manager import get_labs_credentials, store_labs_credentials


class TestStoreBeeswaxCredentials(unittest.TestCase):

    def test_keyring(self):
        with mock.patch('ioteclabs_wrapper.credentials.credential_manager.keyring') as f:
            store_labs_credentials('a', 'b')
            self.assertEqual(f.set_password.call_count, 2)


class TestGetBeeswaxCredentials(unittest.TestCase):

    def test_keyring(self):
        with mock.patch('ioteclabs_wrapper.credentials.credential_manager.keyring') as f:
            get_labs_credentials()
            self.assertEqual(f.get_password.call_count, 2)
