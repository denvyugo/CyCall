from kivy.uix.screenmanager import ScreenManager, SlideTransition

from uix.recentscrn import RecentScreen
from uix.about import AboutScreen
from uix.recall import RecallScreen

'''менеджер экранов'''
scrn_mangr = ScreenManager(transition=SlideTransition())
screens = {
    'main': RecentScreen,
    'about': AboutScreen,
    'recall': RecallScreen
}