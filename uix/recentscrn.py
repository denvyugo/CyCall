from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
import os

puix = os.getcwd()

class RecentScreen(Screen):
    '''экран списка напоминаний'''
    events_callback = ObjectProperty(None)

    Builder.load_file(f'{puix}\\uix\\recentscrn.kv')

    def __init__(self, **kwargs):
        super(RecentScreen, self).__init__(**kwargs)
        listitems = []
        for x in range(0,10):
            listitems.append({
                'item_text': ''.join(('item', str(x))),
                'viewclass': 'Item',
                'height': dp(40)
            })
        self.ids.rv.data = listitems

    def switch_screen(self, screen_name, trans_dir):
        App.get_running_app().switch_screen(screen_name, trans_dir)
