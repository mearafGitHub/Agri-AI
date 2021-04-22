from kivymd.app import MDApp
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineAvatarIconListItem, IconLeftWidget, ImageLeftWidget
from kivy.lang import Builder
from helpers import list_helper


list_helper = """
Screen:
    ScrollView:
        MDList:
            id: list_container
            
"""


class AgroList(MDApp):
    def build(self):
        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):
        avatar_img = ImageLeftWidget(source="cutebox.jpg")
        for i in range(50):
            items = ThreeLineListItem(text="List Item" + str(i),
                                                secondary_text="Hey, How you doing?",
                                                tertiary_text="00:30Am")
            self.root.ids.list_container.add_widget(items)

AgroList().run()
