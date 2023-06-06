from flet import *;

class TopBar(UserControl):

    def __init__ (self, page):
        super().__init__();
        self.page = page;

    def build(self):

        from functions.general import dynamic_alert;

        return AppBar(
            title=WindowDragArea(Text("Dynamic D", color=colors.PRIMARY)),
            toolbar_height=45,
            actions=[
                IconButton(
                    icons.QUESTION_MARK,
                    icon_color=colors.PRIMARY,
                    on_click= lambda _: dynamic_alert(self.page, "Biblioteca de Páginas v1.0", "Desarrollado por On3l7d15h, usando la tecnología Flet."),
                    style=ButtonStyle(
                        shape={
                            "": RoundedRectangleBorder(radius=3)
                        },
                    ),
                ),
                IconButton(
                    icons.CLOSE,
                    icon_color=colors.PRIMARY,
                    on_click=lambda _: self.page.window_close(),
                    style=ButtonStyle(
                        shape={
                            "": RoundedRectangleBorder(radius=3)
                        },
                    )
                )
            ]
        )