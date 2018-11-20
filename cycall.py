'''Presenter for CyCall application'''
from kivy.app import App # import for the View
from data.recalldb import Recall, RecallDB # import for the Model

class Cycall():
    rdb = RecallDB()

    def recent(self):
        # get recent recalls from Model database
        recalls = self.rdb.recent()
        recentlist = []
        for rc in recalls:
            recentlist.append(': '.join((rc.call[0:16], rc.description)))
        return recentlist

    def close(self):
        # close Model database
        self.rdb.closedb()

    def checkrecall(self):
        # check if there is some recall for that moment
        pass
