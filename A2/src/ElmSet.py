## @file ElemSet.py
#  @title ElemSet
#  @author Madhi Nagarajan
#  @brief This file acts as a subclass of set
#  @date Feburary 12, 2020
from Set import *


## @brief The class, ElemSet, represents a subclass of set, for all Element Sets
#  @details ElemSet inherits all the common methods of Set.py, but acts
#  as a set for only elements.
class ElmSet(Set):

    ## @brief Constructor for ElmSet; inherits from Set
    #  @details Constructor accepts one parameter of a list to pass thru Set
    #  @param s is a list (of type Set) that gets passed thru Set
    def __init__(self, s):
        super().__init__(s)
