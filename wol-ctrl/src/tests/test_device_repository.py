import unittest
from device_repository import DeviceRepository
from db_connection import get_test_connection
from init_db import init_test_db

class TestDeviceRepo(unittest.TestCase):
    def setUp(self):
        init_test_db()
        test_connection = get_test_connection()
        self.deviceRp = DeviceRepository(test_connection)

    def test_initial_repo_is_empty_list(self):
        self.assertEqual(self.deviceRp.find_all(), [])

    def test_adding_device_works(self):
        self.deviceRp.create({ "name":"machine1", "user":"user1", "mac":"23:A1", "ip": "123.121"})
        self.assertEqual(self.deviceRp.find_all(), [{ "id":1,"name":"machine1", "user":"user1", "mac":"23:A1", "ip": "123.121"}])

    def test_find_by_id_works(self):
        self.deviceRp.create({ "name":"machine1", "user":"user1", "mac":"23:A1", "ip": "123.121"})
        self.assertEqual(self.deviceRp.find_by_device_id(1), [{ "id":1,"name":"machine1", "user":"user1", "mac":"23:A1", "ip": "123.121"}])

    def test_remove_by_id_works(self):
        self.deviceRp.create({ "name":"machine1", "user":"user1", "mac":"23:A1", "ip": "123.121"})
        self.assertEqual(self.deviceRp.remove_by_device_id(1), [{ "id":1,"name":"machine1", "user":"user1", "mac":"23:A1", "ip": "123.121"}])
        self.assertEqual(self.deviceRp.find_all(), [])


