from classes.objects import Device

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
            Devices: list of Device objects in the form.
            Device(id,name,user,mac,ip)
        """
        rows = self._read()
        devices = []
        for row in rows:
            devices.append(Device(
                row["id"],
                row["name"],
                row["user_id"],
                row["mac"],
                row["ip"],
                ))
        return devices

    def find_by_user_id(self, user_id):
        """Return all devices for specified user
        Args:
            user_id: Unique numeric identifier for user
        Returns:
            List with specified users devices

        """
        cursor = self._connection.cursor()
        cursor.execute('''SELECT * FROM device WHERE user_id == ?''', [user_id])
        rows = cursor.fetchall()
        devices = []
        for row in rows:
            devices.append(Device(
                row["id"],
                row["name"],
                row["user_id"],
                row["mac"],
                row["ip"],
                ))
        return devices


    def find_by_device_id(self, dev_id):
        """Returns the specific device that the function is called with.
        Args:
            dev_id: Numeric id of the wanted device object.
        Returns:
            Single decive object
        """
        devices = self.find_all()
        return list(filter(lambda device: device.id == dev_id, devices))

    def remove_by_device_id(self, dev_id):
        """Removes a device by id.
        Args:
            dev_id: Id of the device to be removed.
        Returns:
            Device: Either the removed device or None
            to indicate failure.
        """

        to_remove = self.find_by_device_id(dev_id)
        if len(to_remove) == 0:
            return None
        cursor = self._connection.cursor()
        cursor.execute('''DELETE FROM device
                       WHERE id = ?''', str(dev_id))
        self._connection.commit()
        return to_remove

    def create(self, new_device):
        """Add a new device object to the database.
        Arg:
            new_device: Device as dict in it's class based order
        Returns:
            new_device: Either returns the added device or
            None to indicate failure.
        """
        devices = self.find_all()
        for device in devices:
            if device.mac == new_device["mac"]:
                return None
        device_list = [new_device["name"],new_device["user_id"],new_device["mac"],new_device["ip"]]
        self._write(device_list)
        return new_device

    def _read(self):
        """Handles the SQL query for getting device
        entries from the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('''SELECT * FROM device''')
        rows = cursor.fetchall()
        return rows

    def _write(self, device_list):
        """Handles the SQL query of adding a
        object to the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('''INSERT INTO device
                       (name, user_id,mac,ip) VALUES (?,?,?,?)''',
                       device_list)
        self._connection.commit()
