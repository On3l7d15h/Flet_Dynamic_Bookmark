# importing
from flet import *;

#
from ..components.text_field_label import TextFieldWithLabel;
from ..components.header_divider import Header;
from ..components.text_filled_button import TextFilledButton;
from ..components.text_empty_button import TextEmptyButton;
from functions.general import login_user;

class LoginView(UserControl):

    def __init__ (self, bar, route, page):
        super().__init__()
        self.bar = bar;
        self.route = route;
        self.page = page;

    def build(self):

        name_field = TextFieldWithLabel("Usuario:");
        password_field = TextFieldWithLabel("Contraseña:", True, True);

        return View(
            route=self.route,
            controls=[
                Header("Inicio Sesión", "Por favor, llene los siguientes campos para poder acceder:"),
                name_field,
                password_field,
                Divider(
                    color=colors.TEAL,
                    opacity=.2
                ),
                Row(
                    [
                        TextFilledButton("Iniciar", icons.LOGIN, self.page, 180, [name_field, password_field], login_user),
                        TextEmptyButton("Nuevo Usuario", icons.PERSON_2, "/new", self.page, 180, self.page.client_storage.contains_key("usuario")),
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            ],
            appbar=self.bar,
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
