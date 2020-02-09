## @file ReactionT.py
#  @author

from numpy import linalg
from CompoundT import *
from MoleculeT import *
from Set import *
from ElmSet import *

from MolecSet import *

from src.ElmSet import ElmSet


class ReactionT:

    def __init__(self, L, R):
        self.__lhs = L
        self.__rhs = R
        self.__coeff_L = [1 for i in range(len(L))]
        self.__coeff_R = [1 for i in range(len(R))]
        # if elem)


    def get_lhs(self):
        return self.__lhs

    def get_rhs(self):
        return self.__rhs

    def get_lhs_coeff(self):
        return self.__coeff_L

    def get_rhs_coeff(self):
        return self.__coeff_R

    # C is CompoundTs, c is coeff, e is elem
    @staticmethod
    def n_atoms(C, c, e):
        atoms = 0
        for i in range(len(C)):
            atoms += c[i] * C[i].num_atoms(e)
        return atoms

    @staticmethod
    def elem_num(C, e):
        atoms = []
        for i in range(len(C)):
            atoms.append(C[i].num_atoms(e))
        return atoms

    @staticmethod
    def elm_in_chem_eq(C):
        ret = []
        for comp in C:
            ret.append(comp.constit_elems().to_seq())
        return Set(ret)

    def is_bal_elm(self, L, R, cL, cR, e):
        return self.n_atoms(L, cL, e) == self.n_atoms(R, cR, e)

    def is_balanced(self, L, R, cL, cR):
        eq_elms = self.elm_in_chem_eq(L).equals(self.elm_in_chem_eq(R))
        eq_atoms = all([self.is_bal_elm(L, R, cL, cR, elm) for elm in self.elm_in_chem_eq(R).to_seq()])
        return eq_elms and eq_atoms

    def matrix(self, C):
        comp_C = self.elm_in_chem_eq(C).to_seq()
        mat = []
        for comp_elms in comp_C:
            for elm in comp_elms:
                nums = self.elem_num(C, elm)
                mat.append(nums)
        return mat

    def chem_balance(self, L, R):
        comp_L = self.elm_in_chem_eq(L).to_seq()
        comp_R = self.elm_in_chem_eq(R).to_seq()

        mat_L = self.matrix(L)
        mat_R = self.matrix(R)

        total_comps = len(L) + len(R)

        calc = linalg.lstsq(mat_L, mat_R)
        print(mat_L, mat_R)
        return calc

        # for comp_elms in comp_L:
        #     for elm in comp_elms:
        #         nums = self.elem_num(L, elm)
        #         row.append(nums)
        #
        #
        # # for comp in L:
        # #     for mol in comp.get_molec_set().to_seq():
        # #         numlist.append(mol.get_num())
        #
        # return row
