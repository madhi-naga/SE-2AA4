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
        self.day = d
        self.month = m
        self.year = y

    ## @brief ?
    def day(self):
        return self.day

    ## @brief ?
    #  @return ?
    def month(self):
        return self.month

    ## @brief ?
    #  @return ?
    def year(self):
        return self.year

    def next(self):

        date = DateT(self.day(), self.month(), self.year())
        """
        if self.month == 2 and self.day == 28:
            date.day = 1
            date.month = date.month + 1
        if self.day == 30 and (self.month in DateT.M30):
            date.day = 1
            date.month = date.month + 1
        if self.day == 31 and (self.month in DateT.M31):
            if self.month == 12:
                date.month = 1
                date.y = date.y + 1
            else:
                date.month = date.month + 1
            date.day = 1
        else:
            date.day = date.day + 1
        """
        if DateT.calendar[date.month] == date.day:
            if date.month == 12:
                date.year = date.year + 1
                date.month = 1
                date.day = 1
            else:
                date.month = date.month + 1
                date.day = 1
        else:
            date.day = date.day + 1
        return date

    def prev(self):

        date = DateT(self.day(), self.month(), self.year())
        """
        if self.day == 1:
            if self.month - 1 == 2:
                date.day = 28
                date.month = date.month - 1
            if self.day == 31 and (self.month - 1 in DateT.M30):
                date.day = 30
                date.month = date.month - 1
            if self.day == 31 and (self.month - 1 in DateT.M31):
                date.day = 1
                date.month = date.month - 1
        else:
            date.day = date.day - 1
        return date
        """
        if date.day == 1:
            if date.month == 1:
                date.year = date.year - 1
                date.month = 12
                date.day = 31
            else:
                date.day = DateT.calendar[date.month-1]
                date.month = date.month - 1
        else:
            date.day = date.day - 1
        return date

    def before(self, d):
        if d.year == self.year:
            if d.month == self.month():
                if d.day < self.day():
                    return True
                else:
                    return False
            elif d.month < self.month():
                return True
            else:
                return False
        elif d.year < self.year():
            return True
        else:
            return False

    def after(self, d):
        if d.year == self.year():
            if d.month == self.month():
                if d.day > self.day():
                    return True
                else:
                    return False
            elif d.month > self.month():
                return True
            else:
                return False
        elif d.year > self.year():
            return True
        else:
            return False

    def equal(self, d):
        if d.day == self.day() and d.month == self.month() and d.year == self.year():
            return True
        else:
            return False

    def add_days(self, n):
        d = DateT(self.day, self.month, self.year)
        for i in range(n):
            d.next()
        return d

    def days_between(self, d):
        n = 0
        if self.before(self, d):
            while not(self.equal(self, d)):
                d.next()
                n = n + 1
        else:
            while not(self.equal(self, d)):
                d.prev()
                n = n + 1
        return n

# etc.
