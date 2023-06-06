from flet import *;

class TextEmptyButton(UserControl):

    def __init__(self, text, icon, route, page, width=180, disabled=False):
        super().__init__();
        self.text = text;
        self.icon = icon;
        self.page = page;
        self.route = route;
        self.width = width;
        self.disabled = disabled;

    def build(self):
        #
        from functions.router import router;

        return TextButton(
            text=self.text,
            icon=self.icon,
            width=self.width,
            disabled=self.disabled,
            style=ButtonStyle(
                bgcolor={
                    "": colors.TRANSPARENT,
                },
                color={
                    "": colors.PRIMARY
                },
                shape= {
                    "": RoundedRectangleBorder(radius=3)
                }
            ),
            on_click=lambda _: router(self.page, self.route)
        )