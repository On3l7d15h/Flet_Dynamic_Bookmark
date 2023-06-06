#
from flet import *;

# Import route
from .router import router
from .alert import dynamic_alert, dynamic_alert_delete

"""
    This function will create, the actual user
"""
def create_session_user(list_items, page):

    if list_items[0].controls[0].controls[1].value == "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if list_items[1].controls[0].controls[1].value== "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if list_items[2].controls[0].controls[1].value == "" or (list_items[2].controls[0].controls[1].value != list_items[1].controls[0].controls[1].value):
        dynamic_alert(page, "¡Oops!", "Las contraseñas no son iguales... por favor, intentelo de nuevo.")
        return;

    page.client_storage.set("usuario", {
        "nombre": list_items[0].controls[0].controls[1].value,
        "contraseña": list_items[1].controls[0].controls[1].value
    });

    router(page, "/")

"""
    This function will create, a new card
"""
def create_widget(list_items, page):

    if list_items[0].controls[1].value == "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if list_items[1].controls[1].value== "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if list_items[2].controls[1].value == "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if list_items[3].controls[1].value == "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if list_items[4].value == None or list_items[4].value == "":
        dynamic_alert(page, "¡Oops!", "Categoría no seleccionada...")
        return;


    if page.client_storage.contains_key("widgets") != True:
        page.client_storage.set("widgets", 
            [{
                "index": 0,
                "titulo": list_items[0].controls[1].value,
                "imagen": list_items[1].controls[1].value,
                "enlace": list_items[2].controls[1].value,
                "desc": list_items[3].controls[1].value,
                "categoria": list_items[4].value
            }]
        )
    else:
        widgets = page.client_storage.get("widgets");
        widgets.append(
                {
                    "index": widgets.__len__(),
                    "titulo": list_items[0].controls[1].value,
                    "imagen": list_items[1].controls[1].value,
                    "enlace": list_items[2].controls[1].value,
                    "desc": list_items[3].controls[1].value,
                    "categoria": list_items[4].value
                }
            )
        page.client_storage.set("widgets", widgets)   

    router(page, "/place")


"""
    This function will update, the actual user
"""
def update_session_user(list_items, page):

    if list_items[0].controls[1].value == "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if list_items[1].controls[1].value== "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if list_items[2].controls[1].value == "" or (list_items[2].controls[1].value != list_items[1].controls[1].value):
        dynamic_alert(page, "¡Oops!", "Las contraseñas no son iguales... por favor, intentelo de nuevo.")
        return;

    page.client_storage.set("usuario", {
        "nombre": list_items[0].controls[1].value,
        "contraseña": list_items[1].controls[1].value
    });

    router(page, "/place")

"""
    This function will clear the session, deleting the actual user,
"""
def delete_session_user(list_items, page):

    # Calling all this stuff
    dynamic_alert_delete(page, "¡Espera!", "¿Estás seguro de eliminar su usuario? Después tendrá que crear un nuevo usuario")
        
"""
    This function will check and allows you to enter to the app,
"""
def login_user(list_items, page):

    if list_items[0].controls[0].controls[1].value == "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if list_items[1].controls[0].controls[1].value == "":
        dynamic_alert(page, "¡Oops!", "Campos vacíos, por favor... llene los campos para continuar.")
        return;

    if page.client_storage.contains_key("usuario") == False:
        dynamic_alert(page, "¡Oops!", "No existe ningún usuario en la aplicación... por favor, cree un nuevo usuario.")
        return;

    if list_items[0].controls[0].controls[1].value != page.client_storage.get("usuario")["nombre"]:
        dynamic_alert(page, "¡Oops!", "Credenciales incorrectas... intentelo de nuevo")
        return;

    if list_items[1].controls[0].controls[1].value != page.client_storage.get("usuario")["contraseña"]:
        dynamic_alert(page, "¡Oops!", "Credenciales incorrectas... intentelo de nuevo")
        return;

    router(page, "/place")