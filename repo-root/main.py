from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class TestPopupApp(App):
    def build(self):
        root = AnchorLayout(anchor_x="center", anchor_y="center")

        open_btn = Button(
            text="Say Hello",
            size_hint=(None, None),
            size=(220, 80),
            font_size="22sp",
        )
        open_btn.bind(on_release=self.show_hello_popup)

        root.add_widget(open_btn)
        return root

    def show_hello_popup(self, _instance):
        content = BoxLayout(orientation="vertical", padding=16, spacing=12)
        message = Label(text="Hello from Kivy!", font_size="20sp")
        close_btn = Button(text="Close", size_hint_y=None, height=60, font_size="18sp")

        content.add_widget(message)
        content.add_widget(close_btn)

        popup = Popup(
            title="Test Popup",
            content=content,
            size_hint=(0.8, 0.35),
            auto_dismiss=False,
        )
        close_btn.bind(on_release=popup.dismiss)
        popup.open()


if __name__ == "__main__":
    TestPopupApp().run()