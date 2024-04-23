from tkinter import ttk, constants
from werkzeug.security import check_password_hash, generate_password_hash
from ui.device_view import DeviceView
from ui.login_view import LoginView



class UI:

    def __init__(self,
                 root,
                 deviceRepo,
                 userRepo,
                 login_service
                 ):
        self._root = root
        self._active_view = None
        self._device_repo = deviceRepo
        self._user_repo = userRepo
        self._login_service = login_service

    def start(self):
        # device frame is placed in class for the updates to work smoothly
        self._active_view = LoginView(self._root, self._handle_login)
        self._active_view.pack()

    def _handle_login(self, user, pswd):
        users = self._user_repo.find_all()
        if self._login_service.check_passwd(user, pswd):
            self._active_view.destroy()
            self._active_view = DeviceView(self._root,self._device_repo)
        


