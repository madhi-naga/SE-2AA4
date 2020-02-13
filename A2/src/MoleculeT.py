## @file MoleculeT.py
#  @title MoleculeT
#  @author Madhi Nagarajan
#  @brief This file acts as a data type for any Molecule. It inherits from the ChemEntity and Equality class.
#  @date Feburary 12, 2020

from ChemEntity import *
from Equality import Equality
from ElmSet import *

## @brief The class, MoleculeT, represents a data type for Molecules
#  @details The class, MoleculeT, represents a data type for Molecules and does related operations
class MoleculeT(ChemEntity, Equality):

    ## @brief Constructor for MoleculeT
    #  @details Constructor accepts two parameters for the element and number.
    #  @param n is an int value of the number of that element
    #  @param x is an enum value (of ChemTypes) for the respective element.
    def __init__(self, n, e):
        self.__elm = e
        self.__num = n

    def __eq__(self, other):
        return self.equals(other)

    ## @brief The function returns the elem constructor of MoleculeT
    #  @returns the element the molecule is made of
    def get_elm(self):
        return self.__elm

    ## @brief The function returns the num constructor of MoleculeT
    #  @returns the number of the element the molecule is made of
    def get_num(self):
        return self.__num

    ## @brief The function calculates the number of atoms of a specific element.
    #  @param e is a given element
    #  @returns the number of atoms of that specific element in a set of molecules
    def num_atoms(self, e):
        if self.__elm == e:
            return self.__num
        else:
            return 0

    ## @brief The function produces an ElmSet of all the elements in a molecule
    #  @returns a list (ElmSet) of all the elements in a molecule
    def constit_elems(self):
        return ElmSet([self.get_elm()])

    ## @brief The function checks if this MoleculeT equals another.
    #  @param m is a given MoleculeT
    #  @returns A boolean depending on if the current MoleculeT is equal to the given MoleculeT
    def equals(self, m):
        if self.__num == m.__num and self.__elm == m.__elm:
            return True
        else:
            return False

