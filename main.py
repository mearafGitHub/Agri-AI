from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDFlatButton, MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from helpers import username_helper


class Agro(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Light"
        screen = MDScreen()
        #  username_input = MDTextField(text='Enter user name', pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #  size_hint_x=None, width=300)
        label = MDLabel(text='Hello world', halign='center',
                        font_size=30, theme_text_color='Primary')
        self.username_input = Builder.load_string(username_helper)
        btn_rect = MDRectangleFlatButton(text='Login', pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                         on_release=self.show_data)
        screen.add_widget(btn_rect)
        screen.add_widget(self.username_input)
        return screen

    def show_data(self, obj):
        close_flat = MDFlatButton(text="Close", on_release=self.close_dialog)
        close_icon_btn = MDIconButton(icon='close', on_release=self.close_dialog)
        more_flat = MDFlatButton(text="More")
        self.dialog = MDDialog(title="Login", text=self.username_input.text, size_hint=(0.7, 1),
                          buttons=[more_flat, close_icon_btn])

        if self.username_input.text is not "":
            self.dialog.open()
            print('dialog is up')
        else:
            dialog = MDDialog(title="Login", text="Please enter username", size_hint=(0.7, 1),)
            dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

Agro().run()
