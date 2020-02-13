## @file Set.py
#  @author Hafez Issa
#  @brief Module which holds a Set of an abstract type
#  @details Inherits Equality
#  @date February 08, 2020

from Equality import *


## @brief An abstract data type for storing and
#  operating on sequences of type T
class Set(Equality):

    ## @brief Set constructor
    #  @details Initializes a Set object whose states
    #  consist of a sequence of abstract type
    #  @param s Sequence of abstract type
    def __init__(self, s):
        self.S = set(s)

    ## @brief Union sequence S with element e of abstract type
    #  @param e Element to be added into sequence S
    def add(self, e):
        self.S.add(e)

    ## @brief Remove element e of abstract type from sequence S
    #  @details exception, if element e is not contained in
    #  sequence S, raise ValueError
    #  @param e Element to be removed from sequence S
    def rm(self, e):
        if (e in self.to_seq()):
            self.S.remove(e)
        else:
            raise ValueError

    ## @brief Check if element e of abstract type is in sequence S
    #  @param e Element to compare
    #  @return Boolean representing whether the sequence S contains element e
    def member(self, e):
        return True if e in self.to_seq() else False

    ## @brief Measure length of sequence of abstract type
    #  @return Natural representing the length of the sequence
    def size(self):
        return len(self.to_seq())

    ## @brief Return a sequence of all the elements in the set
    #  @return Sequence representing the set of all elements
    def to_seq(self):
        return list(self.S)

    ## @brief Compare two sequences of abstract type
    #  @details Equality is reflexive, order should not matter
    #  check if size is equal and if all elements of one sequence is
    #  in the other sequence
    #  @param R Sequence of abstract type
    #  @return Boolean representing whether Sequence S is equal
    #  to Sequence R
    def equals(self, R):
        if not (self.size() == R.size()):
            return False

        for elem_s in self.to_seq():
            if (R.member(elem_s)):
                continue
            else:
                return False
        return True
