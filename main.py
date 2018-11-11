from kivy.app import App
from kivy.properties import ObjectProperty
from uix.recentscrn import RecentScreen

class CyCalling(App):
    recentscrn = ObjectProperty(None)

    # def __init__(self, **kwargs):
    #     super(Program, self).__init__(**kwargs)

    def build(self):
        self.recentscrn = RecentScreen()

        return self.recentscrn


if  __name__ == '__main__':
    app = CyCalling()
    app.run()
