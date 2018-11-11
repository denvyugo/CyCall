from kivy.app import App
#from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManagerException, SlideTransition

from screenmanager import scrn_mangr, screens
#from uix.recentscrn import RecentScreen


class CyCalling(App):
    screen_manager = None
    #recentscrn = ObjectProperty(None)

    def initialize(self):
        self.screen_manager = scrn_mangr
        self.switch_screen('main')

    def switch_screen(self, screen_name, trans_dir=''):
        if screen_name in screens:
            screen = screens[screen_name](name=screen_name)
            if len(trans_dir)>0:
                self.screen_manager.transition.direction = trans_dir
            self.screen_manager.switch_to(screen)
            return
        else:
            raise ScreenManagerException(f'Screen {screen_name} not found')

    # def __init__(self, **kwargs):
    #     super(Program, self).__init__(**kwargs)

    def build(self):
        #self.recentscrn = RecentScreen()
        #return self.recentscrn
        self.initialize()
        return self.screen_manager


if  __name__ == '__main__':
    app = CyCalling()
    app.run()
