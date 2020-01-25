## @file date_adt.py
#  @author Almen Ng
#  @brief Provides the DateT ADT class for representing dates
#  @date January 20, 2020

from datetime import date, timedelta

## @brief An ADT that represents a date
class DateT:

  ## @brief DateT constructor
  #  @details Initializes a DateT object with day, month, and year of date
  #  @param d The day of the date
  #  @param m The month of the date
  #  @param y The year of the date
  def __init__(self, d, m, y):
      self.__d = d
      self.__m = m
      self.__y = y

  ## @brief Gets the day of the date
  #  @return The day of the date
  def day(self):
      return self.__d

  ## @brief Gets the month of the date
  #  @return The month of the date
  def month(self):
      return self.__m

  ## @brief Gets the year of the date
  #  @return The year of the date
  def year(self):
      return self.__y

  ## @brief Gets the date one day later than the current object
  #  @return Date one day later than the current object
  def next(self):
      next_date = date(self.__y, self.__m, self.__d) + timedelta(days=1)
      return DateT(next_date.day, next_date.month, next_date.year)

  ## @brief Gets the date one day before the current object
  #  @return Date one day before the current object
  def prev(self):
      prev_date = date(self.__y, self.__m, self.__d) - timedelta(days=1)
      return DateT(prev_date.day, prev_date.month, prev_date.year)

  ## @brief Checks to see if the current date is before d
  #  @param d Date object of type DateT to compare the current date with
  #  @return True if the current date is before d. False otherwise.
  def before(self, d):
      if date(self.__y, self.__m, self.__d) < date(d.__y, d.__m, d.__d):
          return True
      else:
          return False

  ## @brief Checks to see if the current date is after d
  #  @param d Date object of type DateT to compare the current date with
  #  @return True if the current date is after d. False otherwise.
  def after(self, d):
      if date(self.__y, self.__m, self.__d) > date(d.__y, d.__m, d.__d):
          return True
      else:
          return False

  ## @brief Checks to see if the current date is equal to d
  #  @param d Date object of type DateT to compare the current date with
  #  @return True if the current date is equal to d. False otherwise.
  def equal(self, d):
      if date(d.__y, d.__m, d.__d)  == date(self.__y, self.__m, self.__d):
          return True
      else:
          return False

  ## @brief Adds a certain amount of dates to the current date (assuming that negative days cannot be added)
  #  @param n Integer representing the number of days needed to add to the current date
  #  @return The date that is n days later than the date of the current object
  def add_days(self, n):
      days_added = date(self.__y, self.__m, self.__d) + timedelta(days=n)
      return DateT(days_added.day, days_added.month, days_added.year)

  ## @brief Calculates the number of days between 2 dates
  #  @param d Date object of type DateT to compare the current date with
  #  @return The number of days between 2 dates, the current and d
  def days_between(self, d):
      return abs((date(self.__y, self.__m, self.__d) - date(d.__y, d.__m, d.__d)).days)
