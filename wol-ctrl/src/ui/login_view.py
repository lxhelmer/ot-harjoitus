from tkinter import ttk, constants

class LoginView:
    """Class for generating the login view of
    displaying device objects in ui.

    Attributes:
        frame: Master frame for view
        root: Root to set the view frame in
        handle_login: handler fuction for login
    """
    def __init__(self, root, handle_login, show_create):
        """Initialising function for the class
        Args:
            frame: Master frame for view
            root: Root to set the view frame in
            handle_login: handler fuction for login
            show_create: handler functior for moving to
            user createion view
        """

        self._root = root
        self._handle_login = handle_login
        self._handle_show_create = show_create
        self._frame = None
        self.generate()


    def pack(self):
        """Packs the class frame to be displayed.
        """
        self._frame.pack(expand=True,fill=None)

    def destroy(self):
        """Destroys the current frame.
        """
        self._frame.destroy()

    def generate(self):
        """Function for generating the view and
        setting the ui objects in the right spots.
        """
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
        create_button = ttk.Button(
                master=self._frame,
                command=self._handle_show_create,
                text="create user"
                )

        usr_label.grid()
        usr_entry.grid(row = 0, column = 1)
        pswd_label.grid()
        pswd_entry.grid(row = 1, column = 1)
        create_button.grid(pady=5) 
        login_button.grid(row=2, column = 1, pady=5) 
        self.pack()
