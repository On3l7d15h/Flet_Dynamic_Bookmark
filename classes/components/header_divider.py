from flet import *;

class Header(UserControl):

    def __init__(self, title, brief_desc, is_place=False):
        super().__init__();
        self.title = title;
        self.brief_desc = brief_desc;
        self.is_place = is_place;

    def build(self):

        if self.is_place:
            return Column(
            [
                Row(
                    [
                        Text(
                            self.title, 
                            size=30,
                            weight=FontWeight("bold"),
                            text_align=TextAlign.START,
                        ),
                        Text(
                            self.brief_desc,
                            color=colors.TEAL_200,
                            opacity=.5,
                            text_align=TextAlign.END
                        )
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=MainAxisAlignment.CENTER
                ),
                Divider(
                    color=colors.TEAL,
                    opacity=.2
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
        else:
            return Column(
            [
                Text(
                    self.title, 
                    size=30,
                    weight=FontWeight("bold"),
                    text_align=TextAlign.CENTER,
                ),
                Text(
                    self.brief_desc,
                    color=colors.TEAL_200,
                    opacity=.5,
                    text_align=TextAlign.CENTER
                ),
                Divider(
                    color=colors.TEAL,
                    opacity=.2
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
        