from kivy.app import App
#from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManagerException, SlideTransition

from screenmanager import scrn_mangr, screens
#from uix.recentscrn import RecentScreen
#from data.recalldb import Recall, RecallDB
from cycall import Cycall


class CyCalling(App):
    screen_manager = None
    #recentscrn = ObjectProperty(None)
    cyl = Cycall()

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

    def build(self):
        self.initialize()
        return self.screen_manager

    def recent(self):
        # get list of description of recent recalls
        recalls = self.cyl.recent()
        return recalls

    def quit(self):
        self.cyl.close() # say close to Presenter
        app.stop()

    def addrecall(self, describe, start, period):
        self.cyl.addrecall(describe, start, period)
        self.switch_screen('main', 'left')




if  __name__ == '__main__':
    app = CyCalling()
    app.run()
