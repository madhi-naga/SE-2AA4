## @file MoleculeT.py
#  @author Hafez Issa
#  @brief Template module used to store and access objects of MoleculeT
#  @Date February 08, 2020

from ChemTypes import *
from Equality import *
from ChemEntity import *
from ElmSet import *


## @brief ADT of a MoleculeT object with its attributes
class MoleculeT(ChemEntity, Equality):

    ## @brief Constructor method for MoleculeT
    #  @param n Natural representing number of elements in MoleculeT
    #  @param e ElementT representing the element in MoleculeT
    def __init__(self, n, e):
        self.num = n
        self.elm = e

    ## @brief Getter method, returns ElementT type
    #  @return ElementT representing element of type ElementT
    def get_elem(self):
        return self.elm

    ## @brief Getter method, return Natural
    #  @return Natural representing the number of elements in MoleculeT
    def get_num(self):
        return self.num

    ## @brief Getter for number of atoms of specific element in MoleculeT
    #  @param e ElementT object to be described
    #  @return Natural number representing the number of atoms of the ElementT
    def num_atoms(self, e):
        if e == self.get_elem():
            return self.get_num()
        else:
            return 0

    ## @brief Convert elements of MoleculeT into ElmSet
    #  @return ElmSet representing the sequence of elements in MoleculeT
    def constit_elems(self):
        return ElmSet([self.get_elem()])

    ## @brief Check if two MoleculeT object are equal
    #  @param m MoleculeT object used to compare
    #  @return Boolean representing equality between two MoleculeT objects
    def equals(self, m):
        if (m.get_elem() == self.get_elem() and m.get_num() == self.get_num()):
            return True
        return False
