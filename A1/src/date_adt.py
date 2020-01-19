## @file date_adt.py
#  @author First and Last Name
#  @brief ?
#  @date ?

## @brief An ADT ...
class DateT:

    ## @brief ?
    #  @details ?
    #  @param m ...

    calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    ## @brief ?
    def day(self):
        return self.d

    ## @brief ?
    #  @return ?
    def month(self):
        return self.m

    ## @brief ?
    #  @return ?
    def year(self):
        return self.y

    def next(self):
        date = DateT(self.day(), self.month(), self.year())
        if DateT.calendar[date.m] == date.d:
            if date.m == 12:
                date.y = date.y + 1
                date.m = 1
                date.d = 1
            elif date.m == 2 and date.y % 4 == 0:
                if self.y % 100 == 0 and self.y % 400 != 0:
                    date.m = 3
                    date.d = 1
                else:
                    date.d = 29
            else:
                date.m = date.m + 1
                date.d = 1
        elif date.m == 2 and date.d == 29:
            date.m = date.m + 1
            date.d = 1
        else:
            date.d = date.d + 1
        return date

    def prev(self):
        date = DateT(self.day(), self.month(), self.year())
        if date.d == 1:
            if date.m == 1:
                date.y = date.y - 1
                date.m = 12
                date.d = 31
            elif date.m == 3 and date.y % 4 == 0:
                if (date.y % 100 == 0) and (date.y % 400 != 0):
                    date.d = 28
                    date.m = date.m - 1
                else:
                    date.d = 29
                    date.m = date.m - 1
            else:
                date.d = DateT.calendar[date.m-1]
                date.m = date.m - 1
        else:
            date.d = date.d - 1
        return date

    def before(self, d):
        if d.y == self.year():
            if d.m == self.month():
                if d.d > self.day():
                    return True
                else:
                    return False
            elif d.m > self.month():
                return True
            else:
                return False
        elif d.y > self.year():
            return True
        else:
            return False

    def after(self, d):
        if d.y == self.year():
            if d.m == self.month():
                if d.d < self.day():
                    return True
                else:
                    return False
            elif d.m < self.month():
                return True
            else:
                return False
        elif d.y < self.year():
            return True
        else:
            return False

    def equal(self, d):
        if d.d == self.day() and d.m == self.month() and d.y == self.year():
            return True
        else:
            return False

    def add_days(self, n):
        d = DateT(self.day(), self.month(), self.year())
        for i in range(n):
            d = d.next()
        return d

    def days_between(self, d):
        n = 0
        if self.after(d):
            while not(self.equal(d)):
                d = d.next()
                n = n + 1
        else:
            while not(self.equal(d)):
                d = d.prev()
                n = n + 1
        return n

# etc.
