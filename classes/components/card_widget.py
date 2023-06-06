from flet import *;

def card_widget(page, val):

    from functions.alert import dynamic_alert_update_widget, dynamic_alert_delete_widget

    return Card(
        content=Column(
            [
                Image(
                    src=val["imagen"], 
                    width=300, 
                    height=150, 
                    fit=ImageFit.FIT_WIDTH, 
                    border_radius=border_radius.all(3),
                ),
                Text(
                    val["titulo"],
                    weight=FontWeight.BOLD,
                    size=20,
                ),
                Text(
                    val["desc"],
                    color=colors.TEAL_200,
                    opacity=.5,
                ),
                Row(
                    [
                        IconButton(
                            icon=icons.UPDATE,
                            on_click= lambda _: dynamic_alert_update_widget(page, "Actualizar Página", "Por favor, cambie los datos necesarios.", val["index"]),
                            style=ButtonStyle(
                                bgcolor={
                                    "": colors.PRIMARY_CONTAINER
                                },
                                shape={
                                    "": RoundedRectangleBorder(radius=3)
                                },
                                color=colors.WHITE,
                            ),
                        ),
                        TextButton(
                            text=val["categoria"],
                            style=ButtonStyle(
                                bgcolor={
                                    "": colors.PRIMARY_CONTAINER
                                },
                                shape={
                                    "": RoundedRectangleBorder(radius=3)
                                },
                                color=colors.WHITE
                            ),
                            on_click=lambda _: page.launch_url(val["enlace"])
                        ),
                        IconButton(
                            icon=icons.DELETE,
                            style=ButtonStyle(
                                bgcolor={
                                    "": colors.PRIMARY_CONTAINER
                                },
                                shape={
                                    "": RoundedRectangleBorder(radius=3)
                                },
                                color=colors.WHITE
                            ),
                            on_click=lambda _: dynamic_alert_delete_widget(page, "¡Espera!", "¿Desea borrar la siguiente página? No la volverá a recuperar.", val["index"])
                        ),                                
                    ],
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    alignment=MainAxisAlignment.CENTER
                )
            ],
            spacing=10,
            horizontal_alignment=CrossAxisAlignment.CENTER
        ),
        width=250,
        height=300,        
    )