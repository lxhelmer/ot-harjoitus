import unittest
from repositories.device_repository import DeviceRepository
from db_connection import get_test_connection
from init_db import init_test_db
from classes.objects import Device

class TestDeviceRepo(unittest.TestCase):
    def setUp(self):
        init_test_db()
        test_connection = get_test_connection()
        self.deviceRp = DeviceRepository(test_connection)

    def test_initial_repo_is_empty_list(self):
        self.assertEqual(self.deviceRp.find_all(), [])

    def test_adding_device_works(self):
        self.deviceRp.create({ "name":"machine1", "user_id":1, "mac":"23:A1", "ip": "123.121"})
        self.assertEqual(
                self.deviceRp.find_all(),
                [Device(1,"machine1",1,"23:A1","123.121")]
                )

    def test_find_by_id_works(self):
        self.deviceRp.create({ "name":"machine1", "user_id":1, "mac":"23:A1", "ip": "123.121"})
        self.assertEqual(
                self.deviceRp.find_by_device_id(1),
                [Device(1,"machine1",1,"23:A1","123.121")]
                )

    def test_remove_by_id_works(self):
        self.deviceRp.create({ "name":"machine1", "user_id":1, "mac":"23:A1", "ip": "123.121"})
        self.assertEqual(
                self.deviceRp.remove_by_device_id(1),
                [Device(1,"machine1",1,"23:A1","123.121")]
                )
        self.assertEqual(self.deviceRp.find_all(), [])

    def test_remove_with_bad_id(self):
        self.assertEqual(
                self.deviceRp.remove_by_device_id(1), None)

    def test_find_with_bad_id(self):
        self.assertEqual(
                self.deviceRp.find_by_device_id(1), [])

    def test_find_by_user_id(self):
        self.deviceRp.create({ "name":"dev1", "user_id":1, "mac":"23:A1", "ip": "123.121"})
        self.deviceRp.create({ "name":"dev2", "user_id":1, "mac":"23:A2", "ip": "123.122"})
        self.deviceRp.create({ "name":"dev3", "user_id":2, "mac":"23:A3", "ip": "123.123"})
        devs = self.deviceRp.find_by_user_id(1)
        self.assertEqual(len(devs),2)
        self.assertEqual(devs[0].name,"dev1")
        self.assertEqual(devs[1].name,"dev2")

