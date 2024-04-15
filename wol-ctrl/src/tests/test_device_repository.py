import unittest
from device_repository import DeviceRepository

class TestDeviceRepo(unittest.TestCase):
    def setUp(self):
        self.deviceRp = DeviceRepository()

    def test_initial_repo_is_empty_list(self):
        self.assertEqual(self.deviceRp.find_all(), [])

    def test_adding_device_works(self):
        self.deviceRp.create({"id":"123","name":"machine1", "user":"user1"})
        self.assertEqual(self.deviceRp.find_all(), [{"id":"123","name":"machine1", "user":"user1"}])

    def test_find_by_id_works(self):
        self.deviceRp.create({"id":"123","name":"machine1", "user":"user1"})
        self.assertEqual(self.deviceRp.find_by_device_id("123"), [{"id":"123","name":"machine1", "user":"user1"}])

    def test_remove_by_id_works(self):
        self.deviceRp.create({"id":"123","name":"machine1", "user":"user1"})
        self.assertEqual(self.deviceRp.remove_by_device_id("123"), [{"id":"123","name":"machine1", "user":"user1"}])
        self.assertEqual(self.deviceRp.find_all(), [])


