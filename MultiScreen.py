from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from helpers import screen_helper
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


#  remove this line before production
Window.size = (320, 600)


class AgroBotScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class ServiceScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class Demo(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        screen = Builder.load_string(screen_helper)

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='loin'))
        sm.add_widget(AgroBotScreen(name='agrobot'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ServiceScreen(name='services'))
        return sm


    def on_start(self):
        #for name_tab in list(self.icons):
           # self.root.ids.tabs.add_widget(Tab(name='tabs'))
        print("STARTED")

    def switch_tab(self):
        # '''Switching the tab by name.'''

        try:
            #  self.root.ids.tabs.switch_tab(next(self.iter_list))
            print("switch_tab")
        except StopIteration:
            pass

    def navigation_draw(self):
        print('NAVIGATION')


Demo().run()
