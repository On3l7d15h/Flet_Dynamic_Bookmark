from flet import *;

def _setting_place_ (page):

    from classes.components.header_divider import Header;
    
    # 
    from classes.components.text_empty_button import TextEmptyButton;
    from classes.components.text_filled_button import TextFilledButton;
    from classes.components.text_field_label import TextFieldWithLabel;

    #
    from functions.general import update_session_user, delete_session_user

    # vars
    name_field = TextFieldWithLabel("Nombre").build();
    pass_field = TextFieldWithLabel("Contraseña", True, True).build();
    confirm_field = TextFieldWithLabel("Confirmar Contraseña", True, True).build();

    # filling the data
    if page.client_storage.contains_key("usuario"):
        name_field.controls[1].value = page.client_storage.get("usuario")["nombre"]
        pass_field.controls[1].value = page.client_storage.get("usuario")["contraseña"]
        confirm_field.controls[1].value = page.client_storage.get("usuario")["contraseña"]


    return Column(
        visible=False,
        controls=[
            Header("Información", "Cambio de sus datos personales.", True),
            Row(
                [
                    name_field,
                    pass_field
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=MainAxisAlignment.CENTER
            ),
            Row(
                [
                    confirm_field
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=MainAxisAlignment.CENTER
            ),
            Row(
                [
                    TextFilledButton("Actualizar!", icons.UPDATE, page, 250, [name_field, pass_field, confirm_field], update_session_user),
                    TextFilledButton("Eliminar!", icons.DELETE_FOREVER, page, 250, [], delete_session_user),
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=MainAxisAlignment.CENTER
            ),
            Header("Sesión", "Salir de la sesión.", True),
            Row(
                [
                    TextEmptyButton("Cerrar Sesión", icons.LOGOUT, "/", page, 250)
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=MainAxisAlignment.CENTER
            ),
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER
    )