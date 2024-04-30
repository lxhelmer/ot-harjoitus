class DeviceRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def find_all(self):
        rows = self._read()
        devices = []
        for row in rows:
            devices.append({
                "id":row["id"],
                "name":row["name"],
                "user":row["user"],
                "mac":row["mac"],
                "ip":row["ip"],
                })
        return devices

    def find_by_device_id(self, dev_id):
        devices = self.find_all()
        return list(filter(lambda device: device["id"] == dev_id, devices))

    def remove_by_device_id(self, dev_id):
        to_remove = self.find_by_device_id(dev_id)
        if len(to_remove) == 0:
            return {}
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM devices
                       WHERE id = ?''', str(dev_id))
        return to_remove

    def create(self, new_device):
        devices = self.find_all()
        for d in devices:
            if d["mac"] == new_device["mac"]:
                return {}
        device_list = [new_device["name"],new_device["user"],new_device["mac"],new_device["ip"]]
        self._write(device_list)
        return new_device

    def _read(self):
        cursor = self._connection.cursor()
        cursor.execute('''SELECT * FROM devices''')
        rows = cursor.fetchall()
        return rows
    
    def _write(self, device_list):
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO devices
                       (name, user,mac,ip) VALUES (?,?,?,?)''',
                       device_list)
        self._connection.commit()
