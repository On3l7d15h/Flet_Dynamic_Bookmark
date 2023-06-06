from flet import *;


def _home_place_ (page):

    from classes.components.header_divider import Header;
    from functions.alert import dynamic_alert_delete_widget, dynamic_alert_update_widget;
    from classes.components.card_widget import card_widget
    
    #
    widgets = page.client_storage.get("widgets") if page.client_storage.get("widgets") != None else []
    list_w = []
    
    if widgets.__len__() != 0:
    
        for val in widgets:
            new_card = card_widget(page, val)

            #
            list_w.append(new_card)

    else:
        list_w = [
            Text(
                "No tiene ninguna página registrada aún...",
                size=30,
                opacity=.5
            )
        ]

    return Column(
        visible=True,
        controls=[
            Header("Hogar", "Tu lugar principal", True),
            Row(
                controls=list_w,
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                scroll=ScrollMode.ADAPTIVE,
                spacing=50
            )
        ]
    )