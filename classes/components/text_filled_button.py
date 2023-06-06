from flet import *;

class TextFilledButton(UserControl):

    def __init__(self, text, icon, page, width=180, list_items=[], method=()):
        super().__init__();
        self.text = text;
        self.icon = icon;
        self.page = page;
        self.width = width;
        self.list_items = list_items;
        self.method = method;

    def build(self):
        return TextButton(
            text=self.text,
            icon=self.icon,
            width=self.width,
            style=ButtonStyle(
                bgcolor={
                    "": colors.PRIMARY_CONTAINER,
                },
                color={
                    "": colors.WHITE
                },
                shape= {
                    "": RoundedRectangleBorder(radius=3)
                }
            ),
            on_click=lambda _: self.method(self.list_items, self.page)
        )