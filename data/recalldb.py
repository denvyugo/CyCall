import sqlite3

# number of recalls in list
LIMITRECALLS = 5

class Recall:
    __slots__ = ('number', 'start', 'period', 'call', 'description')

    def __init__(self, start, period, call, description, number=0):
        self.number = number
        self.start = start
        self.period = period # period of repeating of event in whole number of minutes
        self.call = call # date & time when the reminder is on
        self.description = description

class RecallDB:

    #database connection
    _cnn = sqlite3.connect('data\\recalldb.sqlite')
    #cursor
    _cur = _cnn.cursor()

    def closedb(self):
        print('close db')
        self._cnn.close()

    def add_recall(self, recall):
        # get last number
        sql = 'select ID from CyCall order by ID desc limit 1'
        try:
            self._cur.execute(sql)
            numb = self._cur.fetchone()
        except Exception as e:
            print(e)
        else:
            if numb is not None:
                recall.number = numb[0] + 1
            else:
                recall.number = 1
        sql = 'insert into CyCall (ID, Start, Period, Call, Description) values \
                (?, ?, ?, ?, ?)'
        try:
            self._cur.execute(sql, (recall.number, recall.start, recall.period, recall.call, recall.description))
        except Exception as e:
            print(e)
        else:
            self._cnn.commit()

    def recent(self, sday=''):
        # get proximate recalls
        if len(sday) == 0:
            sql = 'select * from CyCall order by Call desc limit ?'
            prms = (LIMITRECALLS,)
        else:
            sql = 'select * from CyCall where date(Call) = ? order by Call limit ?'
            prms = (sday, LIMITRECALLS)
        try:
            self._cur.execute(sql, prms)
            result = self._cur.fetchall()
        except Exception as e:
            print('Error in ''recent'':', e)
        else:
            if len(result) > 0:
                recalls = []
                for tpl in result:
                    # 0 = ID = number
                    num = tpl[0]
                    # 1 = Call
                    cll = tpl[1]
                    # 2 = Description
                    dsc = tpl[2]
                    # 3 = Period
                    per = tpl[3]
                    # 4 = Start
                    sti = tpl[4]
                    rc = Recall(sti, per, cll, dsc, num)
                    recalls.append(rc)
                return recalls
            else:
                return []
