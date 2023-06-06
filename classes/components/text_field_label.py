from flet import *;

class TextFieldWithLabel(UserControl):

    def __init__(self, label, is_pass=False, is_revealed=False):
        super().__init__();
        self.label = label;
        self.is_pass = is_pass;
        self.is_revealed = is_revealed;

    def build(self):
        return Column(
            controls=[
                Text(
                    value=self.label,
                    size=15,
                    color=colors.GREY_50,
                ),
                TextField(
                    border_color=colors.PRIMARY_CONTAINER, 
                    password=self.is_pass,
                    can_reveal_password=self.is_revealed,
                    content_padding=5.6,
                    color=colors.PRIMARY,
                    cursor_color=colors.PRIMARY
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.START
        )