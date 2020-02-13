## @file Set.py
#  @title Set
#  @author Madhi Nagarajan
#  @brief This file acts as a data type for any Set. It inherits from the Equality class.
#  @date February 12, 2020

from Equality import Equality

## @brief The class, Set, represents a data type for all Sets
#  @details The class, Set, represents a data type for all Sets and does related operations
class Set(Equality):

    ## @brief Constructor for Set
    #  @details Constructor accepts one parameters that is a list.
    #  @param s is a parameter of type list.
    def __init__(self, s):
        self.T = s

    def __eq__(self, other):

        return self.equals(other)

    ## @brief The function adds a new value to the Set
    #  @param e is a new value that is being added to the Set
    #  @returns the Set after adding in the new value.
    def add(self, e):
        if not self.member(e):
            self.T.append(e)

    ## @brief The function removes a value from the Set
    #  @param e is the value being removed
    #  @returns the Set after removing the value.
    def rm(self, e):
        if self.member(e):
            self.T.remove(e)

    ## @brief The function checks if a value is in the Set
    #  @param e is the value being checked
    #  @returns a boolean value depending on whether the item is in the list
    def member(self, e):
        if e in self.T:
            return True
        else:
            return False

    ## @brief The function finds the size of the Set
    #  @returns an int value corresponding to the size of the Set
    def size(self):
        return len(self.T)

    ## @brief The function produces a list (of the Set) that is iterable
    #  @returns an iterable list value of the Set
    def to_seq(self):
        return self.T

    ## @brief The function checks whether current set is equal to a given set
    #  @param R is a given set
    #  @returns a boolean depending on if both sets equal
    def equals(self, R):
        if len(self.T) == len(R.T):
            if all(elem in R.to_seq() for elem in self.to_seq()):
                return True
        return False
