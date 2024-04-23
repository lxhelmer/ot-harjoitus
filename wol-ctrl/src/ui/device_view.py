from tkinter import ttk, constants

class DeviceView:
    def __init__(self, root, deviceRepo):
        self._frame = None
        self._root = root
        self._dRepo = deviceRepo
        self.generate_device_view()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def generate_device_view(self):
        rendered_devices = self._dRepo.find_all()
        self._frame = ttk.Frame(self._root)
        for i, dev in enumerate(rendered_devices):
            device_label = ttk.Label(master=self._frame, text=dev, borderwidth=2, relief="solid")
            device_label.grid(row=i, column=0,columnspan = 2, padx=10,pady=5)
            delete_button = ttk.Button(
                    master=self._frame,
                    text="Delete",
                    command=lambda dev=dev: self.handle_delete(dev["id"]))

            delete_button.grid(row=i, column=2, pady=5)
        l_l = len(rendered_devices)

        self._id_label = ttk.Label(master = self._frame, text="id")
        self._name_label = ttk.Label(master = self._frame, text="device name")
        self._user_label = ttk.Label(master = self._frame, text="user name")
        self._add_button = ttk.Button(master = self._frame, text="add", command=self._handle_add)
        self._id_entry = ttk.Entry(master = self._frame)
        self._name_entry = ttk.Entry(master = self._frame)
        self._user_entry = ttk.Entry(master = self._frame)

        self._add_label = ttk.Label(master=self._frame, text="Add a new device!")
        self._add_label.grid()
        self._id_label.grid()
        self._id_entry.grid(row = l_l+1 , column=1, pady = 5)
        self._name_label.grid()
        self._name_entry.grid(row=l_l+2, column=1, pady = 5)
        self._user_label.grid()
        self._user_entry.grid(row=l_l+3, column=1, pady = 5)
        self._add_button.grid(row=l_l+3, column=2, pady = 5)
        self.pack()

    def update(self):
        self.destroy()
        self.generate_device_view()

    def handle_delete(self,id):
        self._dRepo.remove_by_device_id(id)
        self.update()

    def _handle_add(self):
        id = self._id_entry.get()
        name = self._name_entry.get()
        user = self._user_entry.get()
        self._dRepo.create({"id":id,"name":name, "user":user})
        self.update()

