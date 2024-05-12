from tkinter import ttk, constants, END
from services.wol_service import wol

class DeviceView:
    """Class for generating the general view of
    displaying device objects in ui.

    Attributes:
        frame: Master frame for view
        root: Root to set the view frame in
        dRepo: Device repostory to get devices to ui.
    """
    def __init__(self, root, deviceRepo, handle_logout, user_id):
        """Initialising function for the class
        Args:
            frame: Master frame for view
            root: Root to set the view frame in
            dRepo: Device repostory to get devices to ui.
        """
        self.user_id = user_id
        self._frame = None
        self._root = root
        self._dRepo = deviceRepo
        self._handle_logout = handle_logout
        self.generate_device_view()

    def pack(self):
        """Packs the class frame to be displayed.
        """
        self._frame.pack(side=constants.TOP)

    def destroy(self):
        """Destroys the current frame.
        """
        self._frame.destroy()

    def generate_device_view(self):
        """Function for generating the view and
        setting the ui objects in the right spots.
        """
        rendered_devices = self._dRepo.find_by_user_id(self.user_id)
        self._frame = ttk.Frame(self._root)
        for i, dev in enumerate(rendered_devices):
            device_label = ttk.Label(master=self._frame, text=dev, borderwidth=2, relief="solid")
            device_label.grid(row=i, column=0,columnspan = 2, padx=10,pady=5)
            wol_button = ttk.Button(
                    master=self._frame,
                    text="WOL",
                    command=lambda dev=dev: self._handle_wakeup(dev))
            delete_button = ttk.Button(
                    master=self._frame,
                    text="Delete",
                    command=lambda dev=dev: self.handle_delete(dev.id))
            wol_button.grid(row=i, column=2, padx=10, pady=5)
            delete_button.grid(row=i, column=3, pady=5)
        l_l = len(rendered_devices)

        self._name_label = ttk.Label(master = self._frame, text="device name")
        self._mac_label = ttk.Label(master = self._frame, text="mac-addr")
        self._ip_label = ttk.Label(master = self._frame, text="ip-addr")
        self._add_button = ttk.Button(master = self._frame, text="add", command=self._handle_add)
        self._name_entry = ttk.Entry(master = self._frame)
        self._mac_entry = ttk.Entry(master = self._frame)
        self._ip_entry = ttk.Entry(master = self._frame)
        self._add_label = ttk.Label(master=self._frame, text="Add a new device!")
        self._logout_button = ttk.Button(
                master=self._frame,
                text="Log out",
                command=self._handle_logout
                )
        self._text_area = ttk.Entry(master=self._frame)
        self._text_area.grid(row = l_l, columnspan=2, column=2)
        l_l += 1


        self._add_label.grid(row= l_l, column=1, pady = 5)
        self._name_label.grid()
        self._name_entry.grid(row=l_l+1, column=1, pady = 5)
        self._mac_label.grid()
        self._mac_entry.grid(row=l_l+2, column=1, pady = 5)
        self._ip_label.grid()
        self._ip_entry.grid(row=l_l+3, column=1, pady = 5)

        self._add_button.grid(row=l_l+3, column=2, pady = 3)
        self._logout_button.grid(row=l_l+3, column=3, padx=5)
        self.pack()

    def update(self):
        """Updates the current frame. Is used to update the
        list that is displayed when it's updated.
        """
        self.destroy()
        self.generate_device_view()

    def handle_delete(self,id):
        """Handles the deletion of device and calls the needed
        update of displayed list.
        """
        self._dRepo.remove_by_device_id(id)
        self.update()

    def _handle_add(self):
        """Handles the addition of device and calls the needed
        update of displayed list.
        """
        name = self._name_entry.get()
        user_id = self.user_id
        mac = self._mac_entry.get()
        ip = self._ip_entry.get()
        if not(name == "" or mac == "" or ip == ""):
            self._dRepo.create({"name":name, "user_id":user_id, "mac":mac, "ip":ip})
            self.update()
    
    def _handle_wakeup(self, dev):
        magic = wol(dev)
        self._text_area.delete(0,END)
        self._text_area.insert(0,magic)

