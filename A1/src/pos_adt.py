## @file pos_adt.py
#  @author First and Last Name
#  @brief ?
#  @date ?
import math
from date_adt import DateT


class GPosT:

    # y is latitude, x is longitude
    def __init__(self, y, x):
        self.latitude = y
        self.longitude = x

    def lat(self):
        return self.latitude

    def long(self):
        return self.longitude

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
        R = 6371
        rlat = math.radians(self.lat())
        rlong = math.radians(self.long())
        rb = math.radians(b)
        d2 = d / R
        rlat2 = math.asin((math.sin(rlat) * math.cos(d2)) + (math.sin(d2) * math.cos(rlat) * math.cos(rb)))
        rlong2 = rlong + math.atan2(math.sin(rb) * math.sin(d2) * math.cos(rlat),
                                    math.cos(d2) - math.sin(rlat) * math.sin(rlat2))
        self.latitude = math.degrees(rlat2)
        self.longitude = math.degrees(rlong2)

    def distance(self, p):
        R = 6371
        rlat1 = math.radians(self.lat())
        rlat2 = math.radians(p.lat())
        latdiff = math.radians(p.lat() - self.lat())
        longdiff = math.radians(p.long() - self.long())

        a = math.sin(latdiff / 2) * math.sin(latdiff / 2) + math.cos(rlat1) * math.cos(rlat2) * math.sin(
            longdiff / 2) * math.sin(longdiff / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        dist = R * c
        return dist

    def arrival_date(self, p, d, s):
        dist = GPosT.distance(self, p)
        days = round(dist / s)
        d2 = DateT.add_days(d, days)
        return d2
