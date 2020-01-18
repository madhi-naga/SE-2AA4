## @file pos_adt.py
#  @author First and Last Name
#  @brief ?
#  @date ?
import math
from date_adt import DateT

class GPosT:

    #y is latitude, x is longitude
    def __init__(self, x, y):
        self.lat = y
        self.long = x

    def lat(self):
        return self.lat

    def long(self):
        return self.long

    def west_of(self, d):
        if d.long() > self.long():
            return True
        else:
            return False

    def north_of(self, d):
        if d.lat() < self.lat():
            return True
        else:
            return False

    def equal(self, d):
        if d.lat() == self.lat() and d.long() == self.long():
            return True
        else:
            return False

    def move(self, b, d):
        R = 6371e3
        rlat = self.lat()
        rlong = self.long()
        self.lat = math.asin(math.cos(d/R)*math.sin(rlat) + math.sin(d/R)*math.cos(rlat)*math.cos(b))
        self.long = rlong + math.atan2(math.sin(b)*math.sin(d/R)*math.cos(rlat), math.cos(d/R) -
                                               math.sin(rlat)*math.sin(rlat))

    def distance(self, p):
        R = 6371e3
        rlat1 = math.radians(self.lat())
        rlat2 = math.radians(p.lat())
        latdiff = math.radians(rlat2 - rlat1)
        longdiff = math.radians(p.long() - self.long())

        a = math.sin(latdiff/2) * math.sin(latdiff/2) + math.cos(rlat1) * math.cos(rlat2) * math.sin(longdiff/2) *math.sin(longdiff/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return R * c

    def arrival_date(self, p, d, s):
        dist = GPosT.distance(self, p)
        days = dist / s
        d2 = DateT.add_days(d, days)
        return d2


