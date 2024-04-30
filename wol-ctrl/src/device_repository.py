class DeviceRepository:
    """Class for managing device instances.

    Attributes:
        connection: Database connection instance
    """

    def __init__(self, connection):
        """Initialising constructor for class.
        Args:
            connection: database connection
        """
        self._connection = connection

    def find_all(self):
        """Returns all device instances from the db.

        Returns:
            Devices: list of dicts in the form.
            {id,name,user,mac,ip}
        """
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
        """Returns the specific device that the function is called with.
        Args:
            dev_id: Numeric id of the wanted device object.
        Returns:
            List with single decive object
        """
        devices = self.find_all()
        return list(filter(lambda device: device["id"] == dev_id, devices))

    def remove_by_device_id(self, dev_id):
        """Removes a device by id.
        Args:
            dev_id: Id of the device to be removed.
        Returns:
            Device: Either the removed device or empty dict
            to indicate failure.
        """

        to_remove = self.find_by_device_id(dev_id)
        if len(to_remove) == 0:
            return {}
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM devices
                       WHERE id = ?''', str(dev_id))
        return to_remove

    def create(self, new_device):
        """Add a new device object to the database.
        Arg:
            new_device: Device in the most used dict form.
        Returns:
            new_device: Either returns the added device or
            empty dict to indicate failure.
        """
        devices = self.find_all()
        for d in devices:
            if d["mac"] == new_device["mac"]:
                return {}
        device_list = [new_device["name"],new_device["user"],new_device["mac"],new_device["ip"]]
        self._write(device_list)
        return new_device

    def _read(self):
        """Handles the SQL query for getting device
        entries from the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('''SELECT * FROM devices''')
        rows = cursor.fetchall()
        return rows

    def _write(self, device_list):
        """Handles the SQL query of adding a
        object to the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO devices
                       (name, user,mac,ip) VALUES (?,?,?,?)''',
                       device_list)
        self._connection.commit()
