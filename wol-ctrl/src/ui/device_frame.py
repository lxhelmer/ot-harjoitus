from tkinter import ttk

class DeviceFrame:
    def __init__(self, root, deviceRepo, pos):
        self._root = root
        self._dRepo = deviceRepo
        self._pos_row = pos[0]
        self._pos_col = pos[1]

    def generate_device_frame(self):
        self._frame = ttk.Frame(self._root)
        for i, dev in enumerate(self._dRepo.find_all()):
            device_label = ttk.Label(master=self._frame, text=dev, borderwidth=2, relief="solid")
            device_label.grid(row=i, column=0, padx=20,pady=5)
            delete_button = ttk.Button(
                    master=self._frame,
                    text="Delete",
                    command=lambda dev=dev: self.handle_delete(dev["id"]))

            delete_button.grid(row=i, column=2, pady=5)
        self._frame.grid(columnspan = 2, rowspan = 3, row = self._pos_row,column = self._pos_col)

    def update(self):
        self._frame.destroy()
        self.generate_device_frame()

    def handle_delete(self,id):
        self._dRepo.remove_by_device_id(id)
        self.update()
