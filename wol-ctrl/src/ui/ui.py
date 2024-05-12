from tkinter import ttk, constants
from werkzeug.security import check_password_hash, generate_password_hash
from ui.device_view import DeviceView
from ui.login_view import LoginView
from ui.user_creation_view import UserCreationView



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
        self._active_view = LoginView(
                self._root,
                self._handle_login,
                self._handle_show_user_creation
                )

    def _handle_login(self, user, pswd):
        users = self._user_repo.find_all()
        accept, user_id = self._login_service.check_passwd(user, pswd)
        if accept:
            self._active_view.destroy()
            self._active_view = DeviceView(
                    self._root,
                    self._device_repo,
                    self._handle_logout,
                    user_id
                    )

    def _handle_show_user_creation(self):
        self._active_view.destroy()
        self._active_view = UserCreationView(self._root, self._user_repo, self._handle_login)

    def _handle_logout(self):
        self._active_view.destroy()
        self._active_view = LoginView(
                self._root,
                self._handle_login,
                self._handle_show_user_creation
                )



        


