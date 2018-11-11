from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import os

puix = os.getcwd()

class About(BoxLayout):
    events_callback = ObjectProperty(None)

    Builder.load_file(f'{puix}\\uix\\about.kv')
