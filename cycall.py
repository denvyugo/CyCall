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

    def addrecall(self):
        # add new event to recall base
        dscr = 'Some new event'
        strt = '2019-02-04 12:00'
        perd = 360000
        call = '2019-02-04 12:00'
        rcl = Recall(strt, perd, call, dscr)
        print('something to add to database')
        self.rdb.add_recall(rcl)
        pass
