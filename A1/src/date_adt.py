## @file date_adt.py
#  @title Date ADT
#  @author Madhi Nagarajan
#  @brief This file is meant to act as an ADT for a calendar and to perform date-related calculations
#  @date January 20, 2020

## @brief The class, DateT, represents an ADT of a calendar
#  @details This class represents represents an ADT of a calendar with the ability
#  to perform date-related calculations, utilizing the day (d), month (m), and year (y)
class DateT:

    ## dictionary that stores the corresponding number of days for each month
    calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    ## @brief Constructor for DateT
    #  @details Constructor accepts three parameters for the day, month, and year.
    #  @param d is an int value for the respective day.
    #  @param m is an int value for the respective month.
    #  @param y is an int value for the respective year.
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    ## @brief Getter method for returning day
    #  @returns the d value for the day
    def day(self):
        return self.d

    ## @brief Getter method for returning month
    #  @returns the m value for the month
    def month(self):
        return self.m

    ## @brief Getter method for returning year
    #  @returns the y value for the year
    def year(self):
        return self.y

    ## @brief This function calculates the next date of the given date
    #  @return Returns the next day of the given date
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

    ## @brief This function calculates the previous date of the given date
    #  @return Returns the previous day of the given date
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
                date.d = DateT.calendar[date.m - 1]
                date.m = date.m - 1
        else:
            date.d = date.d - 1
        return date

    ## @brief This function checks if the current date is before the given date
    # @param The parameter passed through is a given date, d
    #  @return Returns a boolean based on whether or not the current date is before the given date
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

    ## @brief This function checks if the current date is after the given date
    # @param The parameter passed through is a given date, d
    #  @return Returns a boolean based on whether or not the current date is after the given date
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

    ## @brief This function checks if the current date is equal to the given date
    # @param The parameter passed through is a given date, d
    #  @return Returns a boolean based on whether or not the current date is equal to the given date
    def equal(self, d):
        if d.d == self.day() and d.m == self.month() and d.y == self.year():
            return True
        else:
            return False


    ## @brief This function adds a certain number of days to the current date and returns the calculated date
    # @param The parameter passed through is a given number of days, n
    #  @return Returns the calculated date, d, after the days have been added
    def add_days(self, n):
        d = DateT(self.day(), self.month(), self.year())
        for i in range(n):
            d = d.next()
        return d


    ## @brief This function finds the number of days between the current and given dates
    # @param The parameter passed through is a given date, d
    #  @return Returns an int value, n, the number of days between the current & given dates
    def days_between(self, d):
        n = 0
        if self.after(d):
            while not (self.equal(d)):
                d = d.next()
                n = n + 1
        else:
            while not (self.equal(d)):
                d = d.prev()
                n = n + 1
        return n
