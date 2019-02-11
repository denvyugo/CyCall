"""Presenter for CyCall application"""
from kivy.app import App # import for the View
from data.recalldb import Recall, RecallDB # import for the Model
from datetime import datetime, timedelta


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

    def addrecall(self, describe, start, period):
        # add new event to recall base
        # check start format of date-time string
        # strt = '2019-02-04 12:00'
        wrstrt = False
        try:
            dtstrt = datetime.strptime(start, '%Y-%m-%d %H:%M')
        except Exception as e:
            wrstrt = True

        # check and convert period string to number of minutes
        wrperd = False
        stperd = {'Y': 365*24*60,
                  'M': 30*24*60,
                  'W': 7*24*60,
                  'D': 24*60,
                  'H': 60,
                  'm': 1}
        perd = period.split(sep=' ')
        if len(perd) == 2:
            if perd[1] not in stperd:
                wrperd = True
            else:
                try:
                    nmperd = int(perd[0]) * stperd[perd[1]]
                except Exception as e:
                    wrperd = True
        else:
            wrperd = True
        print(wrstrt, wrperd)
        if wrstrt == False and wrperd == False:
            call = dtstrt + timedelta(minutes=nmperd)
            rcl = Recall(dtstrt, nmperd, call, describe)
            print('something to add to database')
            self.rdb.add_recall(rcl)
