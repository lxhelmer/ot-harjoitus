from tkinter import ttk, constants

class UserCreationView:
    def __init__(self, root, user_repo, login_handler):
        """Initialising function for the class
        Args:
            frame: Master frame for view
            root: Root to set the view frame in
            user_repo: Repository for accessing users
            login_handler: Handles the login after user is created
        """
        self._root = root
        self._frame = None
        self._user_repo = user_repo
        self._handle_login = login_handler
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
        self._add_label = ttk.Label(master=self._frame, text="Add a new user!")
        self._name_label = ttk.Label(master = self._frame, text="username")
        self._name_entry = ttk.Entry(master = self._frame)
        self._psw_label = ttk.Label(master = self._frame, text="password")
        self._psw_entry = ttk.Entry(master = self._frame, show="*")

        add_button = ttk.Button(
                master=self._frame,
                command=self._handle_add_user,
                text="add user"
                )

        self._add_label.grid(column=1)
        self._name_label.grid()
        self._name_entry.grid(row=1,column=1)
        self._psw_label.grid()
        self._psw_entry.grid(row=2,column=1)
        add_button.grid(column=1, pady=5)
        self.pack()

    def _handle_add_user(self):
        name = self._name_entry.get()
        psw = self._psw_entry.get()
        if not(name == "" or psw == ""):
            self._user_repo.create(name,psw)
            self._handle_login(name,psw)
    

