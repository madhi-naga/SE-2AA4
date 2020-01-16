## @file pos_adt.py
#  @author First and Last Name
#  @brief ?
#  @date ?

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
        pass

    def distance(self, p):
        pass

    def arrival_date(self, p, d, s):
        pass

    
