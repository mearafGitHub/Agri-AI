from kivymd.app import MDApp
from kivy.lang import Builder
from helpers import navigation_helper
from kivy.core.window import Window

#  remove this line before production
Window.size = (320, 600)


class Demo(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(navigation_helper)
        return screen

    def navigation_draw(self):
        print('NAVIGATION')


Demo().run()
