import unittest
from device_repository import DeviceRepository

class TestDeviceRepo(unittest.TestCase):
    def setUp(self):
        deviceRp = DeviceRepository()
    
    def test_initial_repo_is_empty_list(self):
        self.assertEqual(deviceRp.find_all(), [])
