username_helper = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "panda"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None 
    width: 270
"""

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: list_container
            ThreeLineAvatarIconListItem:
                text: "List Item" + str(x)
                secondary_text: "Hey, How you doing?"
                tertiary_text: "00:30Am"
"""

screen_helper = """
ScreenManager:
    AgroBotScreen:
    ServiceScreen:
    LoginScreen:
    HomeScreen:

<HomeScreen>:
    name: 'home'  
    MDScreen:
    NavigationLayout:
        ScreenManager:
            MDScreen: 
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Agro Smart'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state() ]]
                        right_action_items: [['dots-vertical', lambda x: nav_drawer.set_state() ]]
                        elevation: 10
                    Screen:
                        ScrollView:
                            MDList:
                                id: list_container
                                ThreeLineAvatarIconListItem:
                                    text: "List Item"
                                    secondary_text: "Hey, How you doing?"
                                    tertiary_text: "00:30Am"
                                ThreeLineAvatarIconListItem:
                                    text: "List Item"
                                    secondary_text: "Hey, How you doing?"
                                    tertiary_text: "00:30Am"
                                ThreeLineAvatarIconListItem:
                                    text: "List Item"
                                    secondary_text: "Hey, How are you doing?"
                                    tertiary_text: "00:30Am"
                                    
                    MDBottomAppBar:
                        height: 60
                        MDToolbar:
                            mode: 'end'
                            type: 'bottom'
                            left_action_items: []
                            on_action_button: root.manager.current= 'agrobot'
                            icon: 'robot'
                                        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                MDBoxLayout:
                    size_hint_y: None
                    height: self.height
                    size_hint_x: None
                    width: self.width
                    allow_stretch: True
                    Image: 
                        source: 'cutebox.jpg'
                        size_hint_x: None
                        width: 264
                        size_hint_y: None
                        height: 180
                        allow_stretch: True
                MDBoxLayout:
                    size_hint_y: None
                    height: self.height
                    spacing: '8px'
                    padding: '8px'
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Mearaf Tadewos'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel: 
                        text: 'mearafagro@gmail.com'
                        font_style: 'Caption'
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel: 
                        text: 'Apple | Large Scale Farm'
                        font_style: 'Caption'
                        size_hint_y: None
                        height: self.texture_size[1]
                    
                ScrollView:
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: '0px'
                        padding: '9px'
                        padding_top: '9px'
                        BoxLayout:
                            orientation: 'horizontal'
                            MDIconButton:
                                icon: 'home' 
                            MDIconButton:
                                icon: 'nature'
                            MDIconButton:
                                icon: 'food-apple' 
                            MDIconButton:
                                icon: 'room-service' 
                        MDList:
                            OneLineIconListItem:
                                text: 'Profile'
                                IconLeftWidget: 
                                    icon: 'face'
                            
                            OneLineIconListItem:
                                text: 'Precision AI'
                                IconLeftWidget: 
                                    icon: 'slot-machine'
                              
                            OneLineIconListItem:
                                text: 'Logout'
                                IconLeftWidget: 
                                    icon: 'logout' 


<LoginScreen>
    name: 'login'  
    MDTextField:
        hint_text: "Username"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "face"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None 
        width: 250
    MDTextField:
        hint_text: "Password"
        text_type: "hidden"
        helper_text: "password must be 8 characters long or more"
        helper_text_mode: "on_focus"
        icon_right: "eye"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None 
        width: 250
    MDRectangleFlatButton:  
        text: 'Login'
        pos_hint: {'center_x': 0.5, 'center_y':0.4}
        on_press: root.manager.current= 'home'

<ServiceScreen>:
    name: 'services'
    Screen:
        BoxLayout:
            adaptive_height: True
            orientation: "vertical"
            MDToolbar:
                title: 'Services'
            MDFlatButton:
                text: "ADD TAB"
                on_release: root.manager.current= 'agrobot'
            Widget:
                           
        

<AgroBotScreen>:
    name: 'agrobot'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Agro Bot'
            right_action_items: [['dots-horizontal-circle', lambda x: app.navigation_draw()]]
            elevation: 10
        MDLabel:
            text: 'Hello'
            halign: 'center'
        
        MDBottomAppBar:
            MDToolbar:
                mode: 'end'
                type: 'bottom'
                left_action_items: [['skip-backward', lambda x: app.navigation_draw() ]]
                on_action_button: root.manager.current= 'services'
                icon: 'orbit'
       
"""

tab_helper = """
  
            
<Tab>:
    name: tab
    MDIconButton:
        id: icon
        icon: 'arrow-right'
        user_font_size: "48px"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_release: app.switch_tab() 
    MDList:
        MDBoxLayout:
            adaptive_height: True
            MDFlatButton:
                text: "ADD TAB"
                on_release: app.add_tab()
            MDFlatButton:
                text: "REMOVE LAST TAB"
                on_release: app.remove_tab()
            MDFlatButton:
                text: "GET TAB LIST"
                on_release: app.get_tab_list()
"""

toolbar_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Agro App'
            left_action_items: [['menu', lambda x: app.navigation_draw() ]]
            right_action_items: [['clock', lambda x: app.navigation_draw() ]]
            elevation: 10
        MDLabel:
            text: 'Hello'
            halign: 'center'
        
        MDBottomAppBar:
            MDToolbar:
                mode: 'center'
                type: 'bottom'
                left_action_items: [['poll-box', lambda x: app.navigation_draw() ]]
                on_action_button: app.navigation_draw()
                icon: 'orbit'
"""

navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen: 
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Agro Smart'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state(true) ]]
                        elevation: 10
                    Widget:
                    
                    
        MDNavigationDrawer:
            id: nav_drawer
            size_hint_y: None
            height: self.texture_size[1]
            GridLayout:
                spacing: '8px'
                padding: '8px'
                orientation: 'vertical'                
                Image:
                    size_hint_y: None
                    height: self.texture_size[1] 
                    source: 'mine.jpg'
                MDLabel:
                    text: 'Mearaf Tadewos'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel: 
                    text: 'Large Scale Farm'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                                 
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget: 
                                icon: 'face-profile-woman'
                        
                        OneLineIconListItem:
                            text: 'Call'
                            IconLeftWidget: 
                                icon: 'phone'
                          
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget: 
                                icon: 'logout'    
                            
"""
