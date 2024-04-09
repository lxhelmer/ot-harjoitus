class DeviceRepository:
    def __init__(self):
        self._devices = []

    def find_all(self):
        return self._read()

    def find_by_device_id(self, id):
        devices = self.find_all()
        return list(filter(labmda device: device.id == id, devices))

    def create(self, device):
        devices = self.find_all()
        devices.append(devices)
        self._write(devices)
        return todo

    def _read(self):
        return self._devices

    def _write(self, devices):
        self._devices = devices



