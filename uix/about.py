from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import os

puix = os.getcwd()

class AboutScreen(Screen):
    '''Экран о приложении'''
    events_callback = ObjectProperty(None)

    Builder.load_file(f'{puix}\\uix\\about.kv')

    def switch_screen(self, screen_name):
        App.get_running_app().switch_screen(screen_name)
