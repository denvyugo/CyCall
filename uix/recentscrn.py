from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
import os

puix = os.getcwd()

class RecentScreen(BoxLayout):
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

