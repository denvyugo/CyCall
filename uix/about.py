from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import os

puix = os.getcwd()

class AboutScreen(Screen):
    '''Экран о приложении'''
    events_callback = ObjectProperty(None)

    Builder.load_file(f'{puix}\\uix\\about.kv')
