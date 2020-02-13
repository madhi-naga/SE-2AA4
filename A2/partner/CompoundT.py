## @file CompoundT.py
#  @author Hafez Issa
#  @brief Template module used to store and access objects of CompoundT
#  @date February 08, 2020

from MoleculeT import *
from MolecSet import *
from Equality import *
from ElmSet import *
from MolecSet import *


## @brief ADT of a CompoundT object with its attributes
class CompoundT(ChemEntity, Equality):

    ## @brief Constructor of CompoundT object
    #  @param M MolecSet of MoleculeTs in the compound
    def __init__(self, M):
        self.C = M

    ## @brief Getter method
    #  @return MolecSet of all molecules in the CompoundT object
    def get_molec_set(self):
        return self.C

    ## @brief Get number of atoms of specific element e in the CompoundT object
    #  @param e ElementT to be described
    #  @return Natural number representing the number of e atoms in CompoundT object
    def num_atoms(self, e):
        num = 0
        for m in self.get_molec_set().to_seq():
            num += m.num_atoms(e)
        return num

    ## @brief Get list of elements in the CompoundT object
    #  @return ElmSet of all elements in the CompoundT object
    def constit_elems(self):
        atom = ElmSet([])
        for m in self.get_molec_set().to_seq():
            atom.add(m.get_elem())
        return atom

    ## @brief Check if two CompoundT object are equal
    #  @param D CompoundT object used to compare
    #  @return Boolean representing equality between two CompoundT objects
    def equals(self, D):
        return True if self.get_molec_set().equals(D.get_molec_set()) else False
