from tkinter import ttk
from device_repository import DeviceRepository
from ui.device_frame import DeviceFrame


class UI:

    def __init__(self, root, deviceRepo):
        self._root = root
        self.device_frame = DeviceFrame(root,deviceRepo)

    def start(self):
        self.device_frame.generate_device_frame()


