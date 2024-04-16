from tkinter import ttk
from device_repository import DeviceRepository
from ui.device_frame import DeviceFrame


class UI:

    def __init__(self, root, deviceRepo):
        self._root = root
        self._device_repo = deviceRepo
        self._device_frame = DeviceFrame(root,deviceRepo, (0,0))

    def start(self):
        # device frame is placed in class for the updates to work smoothly
        self._device_frame.generate_device_frame()
        self._id_label = ttk.Label(master = self._root, text="id")
        self._name_label = ttk.Label(master = self._root, text="device name")
        self._user_label = ttk.Label(master = self._root, text="user name")
        self._add_button = ttk.Button(master = self._root, text="add", command=self._handle_add)
        self._id_entry = ttk.Entry(master = self._root)
        self._name_entry = ttk.Entry(master = self._root)
        self._user_entry = ttk.Entry(master = self._root)

        self._add_label = ttk.Label(master=self._root, text="Add a new device!")
        self._add_label.grid()
        self._id_label.grid()
        self._id_entry.grid(row = 4, column=1, pady = 5)
        self._name_label.grid()
        self._name_entry.grid(row=5, column=1, pady = 5)
        self._user_label.grid()
        self._user_entry.grid(row=6, column=1, pady = 5)
        self._add_button.grid(row=6, column=2, pady = 5)

    def _handle_add(self):
        id = self._id_entry.get()
        name = self._name_entry.get()
        user = self._user_entry.get()
        self._device_repo.create({"id":id,"name":name, "user":user})
        self._device_frame.update()




