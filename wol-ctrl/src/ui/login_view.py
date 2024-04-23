from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self.generate()


    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def generate(self):
        self._frame = ttk.Frame(master=self._root)
        usr_label = ttk.Label(master=self._frame, text="username")
        pswd_label = ttk.Label(master=self._frame, text="password")
        usr_entry = ttk.Entry(master=self._frame)
        pswd_entry = ttk.Entry(master=self._frame)
        login_button = ttk.Button(
                master=self._frame,
                command=lambda : self._handle_login(usr_entry.get(),pswd_entry.get()),
                text="log in"
                )

        usr_label.grid()
        usr_entry.grid(row = 0, column = 1)
        pswd_label.grid()
        pswd_entry.grid(row = 1, column = 1)
        login_button.grid()



