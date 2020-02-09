## @file ReactionT.py
#  @author

from numpy import linalg
from CompoundT import *

class ReactionT:

    def __init__(self, L, R):
        self.__lhs = L
        self.__rhs = R
        self.__coeff_L = [1 for i in range(len(L))]
        self.__coeff_R = [1 for i in range(len(R))]

        # if elem


    def get_lhs(self):
        return self.__lhs

    def get_rhs(self):
        return self.__rhs

    def get_lhs_coeff(self):
        return self.__coeff_L

    def get_rhs_coeff(self):
        return self.__coeff_R

    def n_atoms(self, C, c, e):
        atoms = 0
        for i in range(len(C)):
            atoms += c[i] * C[i].num_atoms(e)
        return atoms

    def elm_in_chem_eq(self, C):
        ret = []
        for c in C:
            ret.append(c.constit_elem().to_seq())
        return ret

    def is_bal_elm(self, e):
        return self.n_atoms(self.__lhs, self.__coeff_L, e) == self.n_atoms(self.__rhs, self.__coeff_R, e)


    def is_balanced(self):
        eq_elms = self.elm_in_chem_eq(1).equals(self.elm_in_chem_eq(self.))

    def chem_balance(self):

