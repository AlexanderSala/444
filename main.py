from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
class MainSalanginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return (
            MDScreen(
                MDRectangleFlatButton(
                    text="Salangin Alexander",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )
        )


MainSalanginApp().run()