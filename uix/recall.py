from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import os

puix = os.getcwd()

class RecallScreen(Screen):
    '''Экран создания напоминания'''
    events_callback = ObjectProperty(None)
    fkv = f'{puix}\\uix\\recall.kv'
    with open(fkv, encoding='utf-8') as f:
        Builder.load_string(f.read())

    # Builder.load_file(f'{puix}\\uix\\recall.kv')

    def switch_screen(self, screen_name, trans_dir):
        App.get_running_app().switch_screen(screen_name, trans_dir)

    def exit(self):
        App.get_running_app().quit()

    def new_recall(self):
        App.get_running_app().addrecall()