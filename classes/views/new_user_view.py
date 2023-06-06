# importing
from flet import *;

#
from ..components.header_divider import Header;
from ..components.text_field_label import TextFieldWithLabel;
from ..components.text_filled_button import TextFilledButton;

class NewUserView(UserControl):

    
    def __init__ (self, bar, route, page):
        super().__init__()
        self.bar = bar;
        self.route = route;
        self.page = page;

    def build(self):
        from ..components.text_empty_button import TextEmptyButton;
        from functions.general import create_session_user;

        name_field = TextFieldWithLabel("Nombre:");
        password_field = TextFieldWithLabel("Contraseña:", True, True);
        confirm_field = TextFieldWithLabel("Confirmar Contraseña:", True, True);

        return View(
            route=self.route,
            controls=[
                Header("Nuevo usuario", "Indique su nombre, y su contraseña... es importante saber que cuando el usuario sea creado... no podrá acceder a la plataforma a menos que entre a la app."),
                name_field,
                password_field,
                confirm_field,
                Row(
                    [
                        TextFilledButton("Crear", icons.PERSON, self.page, 180, [name_field, password_field, confirm_field], create_session_user),
                        TextEmptyButton("Volver", icons.U_TURN_LEFT, "/", self.page, 180, False)
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            ],
            appbar=self.bar,
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
