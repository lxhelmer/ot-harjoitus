import unittest
from services.wol_service import wol
from classes.objects import Device

class TestWolService(unittest.TestCase):
    
    def test_wol_message(self):
        dev = Device(1,"machine1",1,"AB:CD:AC:BD","123.121")

        self.assertEqual(wol(dev),
                        "ffffffffffffabcdacbdabcdacbdabcdacbd" + \
                        "abcdacbdabcdacbdabcdacbdabcdacbdabcd" + \
                        "acbdabcdacbdabcdacbdabcdacbdabcdacbd" + \
                        "abcdacbdabcdacbdabcdacbdabcdacbd"
                         )


