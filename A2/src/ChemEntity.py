## @file ChemEntity.py
#  @title ChemEntity
#  @author Madhi Nagarajan
#  @brief This file is an abstract class which other classes utilize its methods
#  @date February 12, 2020
from abc import abstractmethod, ABC


## @brief The class, ChemEntity, represents an abstract class
#  @details The class, ChemEntity, represents an abstract class which other classes
#  utilize its methods
class ChemEntity(ABC):

    ## @brief The function is an abstract method
    #  @param R is a given value
    @abstractmethod
    def num_atoms(self, elem):
        pass

    ## @brief The function is an abstract method
    #  @param R is a given value
    @abstractmethod
    def constit_elems(self):
        pass
