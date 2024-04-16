class DeviceRepository:
    def __init__(self):
        self._devices = []

    def find_all(self):
        return self._read()

    def find_by_device_id(self, dev_id):
        devices = self.find_all()
        return list(filter(lambda device: device["id"] == dev_id, devices))

    def remove_by_device_id(self, dev_id):
        to_remove = self.find_by_device_id(dev_id)
        devices = self.find_all()
        devices_updated = list(filter(lambda device: device["id"] != to_remove[0]["id"], devices))
        self._write(devices_updated)
        return to_remove

    def create(self, device):
        devices = self.find_all()
        devices.append(device)
        self._write(devices)
        return device

    def _read(self):
        return self._devices

    def _write(self, devices):
        self._devices = devices
