## @file date_adt.py
#  @author First and Last Name
#  @brief ?
#  @date ?

## @brief An ADT ...
class DateT:

    ## @brief ?
    #  @details ?
    #  @param m ...
    M30 = [4, 6, 9, 11]
    M31 = [1, 3, 5, 7, 8, 10, 12]
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
        date = DateT(self.day, self.month, self.year)
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


        return date

    def prev(self):
        date = DateT(self.day, self.month, self.year)
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

    def before(self, d):



    def after(self, d):

# etc.
