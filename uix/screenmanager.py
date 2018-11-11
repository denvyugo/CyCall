from kivy.uix.screenmanager import ScreenManager, SlideTransition

from uix import RecentScreen, AboutScreen


scrn_mangr = ScreenManager(transition=SlideTransition())
screens = {
    'main': RecentScreen,
    'about': AboutScreen
}