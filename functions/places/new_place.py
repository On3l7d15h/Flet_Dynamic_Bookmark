from flet import *;

def _new_place_ (page):

    from classes.components.header_divider import Header;
    from classes.components.text_filled_button import TextFilledButton;
    from classes.components.text_field_label import TextFieldWithLabel;
    from functions.general import create_widget
    
    # 
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
    )

    return Column(
        visible=False,
        controls=[
            Header("Nuevo", "Crea un nuevo atajo para alguna página", True),
            Row(
                [
                    title_field,
                    link_field
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER
            ),
            Row(
                [
                    page_field,
                    brief_field
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER
            ),
            Row(
                [
                    drop_field
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER
            ),
            Header("Acción", "", True),
            Row(
                [
                    TextFilledButton("Crear", icons.CREATE_SHARP, page, 250, [title_field, link_field, page_field, brief_field, drop_field], create_widget),
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=MainAxisAlignment.CENTER
            ),
        ]
    )