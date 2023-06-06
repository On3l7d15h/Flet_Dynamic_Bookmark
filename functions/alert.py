from flet import *;


def dynamic_alert(page, title, brief_desc):

    def close_alert():
        alert.open = False;
        page.update();

    alert = AlertDialog(
        title=Text(
            title,
            size=40,
            weight=FontWeight.BOLD,
            text_align=TextAlign.CENTER
        ),
        shape=RoundedRectangleBorder(radius=3),
        content=Text(
            brief_desc,
            text_align=TextAlign.CENTER
        ),
        actions=[
            TextButton(
                text="Aceptar", 
                icon=icons.CHECK, 
                on_click=lambda _:close_alert(),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=3)
                    },
                    bgcolor={
                    "": colors.PRIMARY_CONTAINER,
                },
                color={
                    "": colors.WHITE
                },
                )
            )
        ],
        modal=True,
        actions_alignment=MainAxisAlignment.CENTER
    )

    page.dialog = alert;
    alert.open = True;
    page.update();

def dynamic_alert_delete(page, title, brief_desc):

    from functions.router import router;

    def close_alert():
        alert.open = False;
        page.update();
    
    def accept_alert():
        alert.open = False;
        page.update();
        
        # actions
        page.client_storage.clear();
        router(page, "/")

    alert = AlertDialog(
        title=Text(
            title,
            size=40,
            weight=FontWeight.BOLD,
            text_align=TextAlign.CENTER
        ),
        shape=RoundedRectangleBorder(radius=3),
        content=Text(
            brief_desc,
            text_align=TextAlign.CENTER
        ),
        actions=[
            TextButton(
                text="Cancelar", 
                icon=icons.CLOSE, 
                on_click=lambda _:close_alert(),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=3)
                    },
                    bgcolor={
                    "": colors.PRIMARY_CONTAINER,
                },
                color={
                    "": colors.WHITE
                },
                )
            ),
            TextButton(
                text="Aceptar", 
                icon=icons.CHECK, 
                on_click=lambda _:accept_alert(),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=3)
                    },
                    bgcolor={
                    "": colors.PRIMARY_CONTAINER,
                },
                color={
                    "": colors.WHITE
                },
                )
            ),
        ],
        modal=True,
        actions_alignment=MainAxisAlignment.CENTER,
    )

    page.dialog = alert;
    alert.open = True;
    page.update();

def dynamic_alert_delete_widget(page, title, brief_desc, position):

    from functions.router import router;

    def close_alert():
        alert.open = False;
        page.update();
    
    def accept_alert():
        alert.open = False;
        page.update();
        
        # actions
        widgets = page.client_storage.get("widgets")
        widgets.pop(position)
        page.client_storage.set("widgets", widgets)
        router(page, "/place")

    alert = AlertDialog(
        title=Text(
            title,
            size=40,
            weight=FontWeight.BOLD,
            text_align=TextAlign.CENTER
        ),
        shape=RoundedRectangleBorder(radius=3),
        content=Text(
            brief_desc,
            text_align=TextAlign.CENTER
        ),
        actions=[
            TextButton(
                text="Cancelar", 
                icon=icons.CLOSE, 
                on_click=lambda _:close_alert(),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=3)
                    },
                    bgcolor={
                    "": colors.PRIMARY_CONTAINER,
                },
                color={
                    "": colors.WHITE
                },
                )
            ),
            TextButton(
                text="Aceptar", 
                icon=icons.CHECK, 
                on_click=lambda _:accept_alert(),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=3)
                    },
                    bgcolor={
                    "": colors.PRIMARY_CONTAINER,
                },
                color={
                    "": colors.WHITE
                },
                )
            ),
        ],
        modal=True,
        actions_alignment=MainAxisAlignment.CENTER,
    )

    page.dialog = alert;
    alert.open = True;
    page.update();

def dynamic_alert_update_widget(page, title, brief_desc, position):

    from functions.router import router;
    from classes.components.header_divider import Header;
    from classes.components.text_filled_button import TextFilledButton;
    from classes.components.text_field_label import TextFieldWithLabel;

    # Variables:
    title_field = TextFieldWithLabel("Titulo:").build();
    link_field = TextFieldWithLabel("Enlace Imágen:").build();
    page_field = TextFieldWithLabel("Enlace página:").build()
    brief_field = TextFieldWithLabel("Descripción breve:").build();
    drop_field = Dropdown(
        label="Categoría",
        hint_text="Seleccione una categoría:",
        options=[
            dropdown.Option("Estudio"),
            dropdown.Option("Trabajo"),
            dropdown.Option("Otros"),
        ],
        border_color=colors.PRIMARY_CONTAINER,
        width=610,
    )

    # get values from the specific values...
    title_field.controls[1].value = page.client_storage.get("widgets")[position]["titulo"];
    link_field.controls[1].value = page.client_storage.get("widgets")[position]["imagen"];
    page_field.controls[1].value = page.client_storage.get("widgets")[position]["enlace"];
    brief_field.controls[1].value = page.client_storage.get("widgets")[position]["desc"];
    drop_field.value = page.client_storage.get("widgets")[position]["categoria"];


    def close_alert():
        alert.open = False;
        page.update();
    
    def accept_alert():
        alert.open = False;
        page.update();

        #
        title:str = title_field.controls[1].value;
        img:str = link_field.controls[1].value;
        link:str = page_field.controls[1].value;
        desc:str = brief_field.controls[1].value;

        # actions
        specific_widgets = page.client_storage.get("widgets")[position]
        specific_widgets["titulo"] = title;
        specific_widgets["imagen"] = img;
        specific_widgets["enlace"] = link;
        specific_widgets["desc"] =  desc;
        specific_widgets["categoria"] = drop_field.value

        # 
        update_widgets = page.client_storage.get("widgets")
        update_widgets[position] = specific_widgets;
        page.client_storage.set("widgets", update_widgets)
        print(page.client_storage.get("widgets"))
        page.update();
    
        router(page, "/place")

    alert = AlertDialog(
        title=Text(
            title,
            size=40,
            weight=FontWeight.BOLD,
            text_align=TextAlign.CENTER
        ),
        shape=RoundedRectangleBorder(radius=3),
        content=Column(
            [
                Text(
                    brief_desc,
                    text_align=TextAlign.CENTER,
                ),
                Divider(
                    color=colors.TEAL,
                    opacity=.2
                ),
                Row(
                    [
                        title_field,
                        link_field
                    ],
                ),
                Row(
                    [
                        page_field,
                        brief_field
                    ],
                ),
                Row(
                    [
                        drop_field
                    ],
                )
            ],
            width=600,
            height=300,
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER
        ),
        actions=[
            TextButton(
                text="Cancelar", 
                icon=icons.CLOSE, 
                on_click=lambda _:close_alert(),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=3)
                    },
                    bgcolor={
                    "": colors.PRIMARY_CONTAINER,
                },
                color={
                    "": colors.WHITE
                },
                )
            ),
            TextButton(
                text="Aceptar", 
                icon=icons.CHECK, 
                on_click=lambda _:accept_alert(),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=3)
                    },
                    bgcolor={
                    "": colors.PRIMARY_CONTAINER,
                },
                color={
                    "": colors.WHITE
                },
                )
            ),
        ],
        modal=True,
        actions_alignment=MainAxisAlignment.CENTER
    )

    page.dialog = alert;
    alert.open = True;
    page.update();