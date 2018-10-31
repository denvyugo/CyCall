from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('cycall.kv')


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
        return sm


if __name__ == '__main__':
    CyCallApp().run()