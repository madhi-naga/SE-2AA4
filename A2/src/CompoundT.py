## @file CompoundT.py
#  @title CompoundT
#  @author Madhi Nagarajan
#  @brief This file acts as a data type for any Compound. It inherits from the
#  ChemEntity and Equality class.
#  @date February 12, 2020

from ChemEntity import ChemEntity
from ElmSet import ElmSet
from Equality import Equality


## @brief The class, CompoundT, represents a data type for Compounds
#  @details The class, CompoundT, represents a data type for Compounds
#  and does related operations
class CompoundT(ChemEntity, Equality):

    ## @brief Constructor for CompoundT
    #  @details Constructor accepts one parameter of a molecule set
    #  @param M is a MolecSet of the compound
    def __init__(self, M):
        self.__molec_set = M

    ## @brief The function returns the molec_set constructor the MoleculeT
    #  @returns a molecule set of all elements in a compound
    def get_molec_set(self):
        return self.__molec_set

    ## @brief The function calculates the number of atoms of a specific element in a Compound
    #  @param e is a given element
    #  @returns the number of atoms of that specific element in a Compound set.
    def num_atoms(self, e):
        sum = 0
        for molec in self.__molec_set.to_seq():
            if molec.get_elm() == e:
                sum += molec.get_num()
        return sum

    ## @brief The function produces an ElmSet of all the elements in a Compound
    #  @returns a list (ElmSet) of all the elements in a Compound
    def constit_elems(self):
        return ElmSet([m.get_elm() for m in self.__molec_set.to_seq()])

    ## @brief The function checks if this CompoundT equals another.
    #  @param D is a given CompoundT
    #  @returns A boolean depending on if the current CompoundT is equal to the
    #  given CompoundT
    def equals(self, D):
        if len(self.__molec_set.to_seq()) == len(D.__molec_set.to_seq()):
            if all(elem in D.molec_set for elem in self.__molec_set):
                return True
        return False
