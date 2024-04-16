from tkinter import ttk

class DeviceFrame:
    def __init__(self, root, deviceRepo):
        self._root = root
        self._dRepo = deviceRepo

    def generate_device_frame(self):
        self._frame = ttk.Frame(self._root)
        for i, dev in enumerate(self._dRepo.find_all()):
            label = ttk.Label(master=self._frame, text=dev, borderwidth=2, relief="solid")
            label.grid(row=i, column=0, padx=20,pady=5)
            delete_button = ttk.Button(
                    master=self._frame,
                    text=dev["id"],
                    command=lambda dev=dev: self.handle_delete(dev["id"]))

            delete_button.grid(row=i, column=1, pady=5)
        self._frame.pack()

    def update(self):
        self._frame.destroy()
        self.generate_device_frame()

    def handle_delete(self,id):
        print(id)
        self._dRepo.remove_by_device_id(id)
        self.update()
