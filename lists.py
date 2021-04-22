from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, ThreeLineIconListItem, ThreeLineAvatarIconListItem, IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView


class AgroList(MDApp):
    def build(self):
        screen = MDScreen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)
        for x in range(45):
            icon_left = IconLeftWidget(icon="android")
            avatar_img = ImageLeftWidget(source="cutebox.jpg")
            items = ThreeLineAvatarIconListItem(text="List Item" + str(x),
                                                secondary_text="Hey, How you doing?",
                                                tertiary_text="00:30Am")

            items.add_widget(avatar_img)
            list_view.add_widget(items)

        screen.add_widget(scroll)
        return screen


AgroList().run()
