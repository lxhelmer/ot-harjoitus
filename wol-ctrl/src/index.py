from tkinter import Tk
from repositories.device_repository import DeviceRepository
from repositories.user_repository import UserRepository
from services.login_service import LoginService
from ui.ui import UI
from db_connection import get_database_connection

def starter():
    """Program starting function to generate necessary
    instances and starting the ui using them.
    """
    connection = get_database_connection()
    devices = DeviceRepository(connection)
    users = UserRepository(connection)
    login_service = LoginService(users)

    window = Tk()
    window.title("TkInter example")
    window.geometry("800x600")
    ui = UI(window, devices, users, login_service)
    #populate devices for preliminary testing
    devices.create({ "name":"machine1", "user_id":1, "mac":"23:A1", "ip": "123.121"})
    devices.create({ "name":"machine2", "user_id":1, "mac":"23:A2", "ip": "123.122"})
    devices.create({ "name":"machine3", "user_id":2, "mac":"23:A3", "ip": "123.123"})

    #populate with default user
    users.create("admin","admin")
    ui.start()
    window.mainloop()

starter()
