from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class MainScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


# create ScreenManager
sm = ScreenManager()
sm.add_widget(MainScreen(name='recalls'))
sm.add_widget(SettingsScreen(name='settings'))


class CyCallApp(App):

    def build(self):
        self.root = Builder.load_file('cycall.kv')
        self.create()
        return sm

    def create(self):
        listitems = []

        for n in range(0, 10):
            listitems.append({
                'item_text': ''.join(('item',str(n))),
                'viewclass': 'Item',
                'color': [1,1,1,1]
            })

        self.ids.rv.data = listitems


if __name__ == '__main__':
    CyCallApp().run()
