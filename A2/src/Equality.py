## @file Equality.py
#  @title Equality
#  @author Madhi Nagarajan
#  @brief This file is an abstract class which other classes utilize its methods
#  @date February 12, 2020
from abc import ABC, abstractmethod


## @brief The class, Equality, represents an abstract class
#  @details The class, Equality, represents an abstract class which other classes
#  utilize its methods
class Equality(ABC):

    ## @brief The function is an abstract method
    #  @param R is a given value
    @abstractmethod
    def equals(self, R):
        pass
