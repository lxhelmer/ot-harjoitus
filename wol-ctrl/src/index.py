from tkinter import Tk
from device_repository import DeviceRepository
from user_repository import UserRepository
from services.login_service import LoginService
from ui.ui import UI

def starter():
    devices = DeviceRepository()
    users = UserRepository()
    login_service = LoginService(users)

    window = Tk()
    window.title("TkInter example")
    window.geometry("500x500")
    ui = UI(window, devices, users, login_service)
    #populate devices for preliminary testing
    devices.create({ "id":"121","name":"machine1", "user":"user1"})
    devices.create({ "id":"122","name":"machine2", "user":"user2"})
    devices.create({ "id":"123","name":"machine3", "user":"user3"})

    ui.start()
    window.mainloop()

#
#    while (True):
#        command = input("What do you wan't to do? input 'h' for help: ")
#
#        if command == "h":
#            print("input 'a' to add a new machine")
#            print("input 'l' to list machines")
#            print("input 'f' to find devices by id")
#            print("input 'r' to remove a machine")
#            print("input 'q' to quit")
#
#        elif command == "a":
#            id = input("input device id: ")
#            dev_name = input("input device name: ")
#            usr_name = input("input managing user: ")
#            added = devices.create({"id":id,"name":dev_name, "user":usr_name})
#            print("device", added, "added")
#
#
#        elif command == "l":
#            for dev in devices.find_all():
#                print(dev)
#        elif command == "f":
#            id = input("input device id: ")
#            devices_by_id = devices.find_device_by_id(id)
#            for dev in devices_by_id:
#                print(dev)
#
#        elif command == "r":
#            id = input("input device id: ")
#            removed = devices.remove_by_device_id(id)
#            for rem_device in removed:
#                print("device: ", rem_device, "removed")
#
#        elif command == "q":
#            print("goodbye")
#            break

starter()
