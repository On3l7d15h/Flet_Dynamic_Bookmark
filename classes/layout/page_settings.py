# Settings of the application
from flet import *;

#
from ..views.login_view import LoginView;
from ..components.app_bar import TopBar;

class Settings:

    def __init__(self):
        raise Exception("A01: A value is lost.")

    def __init__(self, page):

        from functions.router import router

        page.title = "App"
        page.window_width = 400;
        page.window_height = 600;
        page.theme_mode = "dark"
        page.spacing = 0;
        page.window_title_bar_buttons_hidden = True;
        page.window_title_bar_hidden = True;
        page.window_top = 150;
        page.window_left = 580;
        page.window_resizable = True;
        page.theme = Theme(
            color_scheme_seed=colors.TEAL,  
        )

        router(page, "/")
        
