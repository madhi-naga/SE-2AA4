## @file ReactionT.py
#  @author
import numpy
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

    # def matrix(self, L, R):
    #     comp_L = self.elm_in_chem_eq(L).to_seq()
    #     comp_R = self.elm_in_chem_eq(R).to_seq()
    #     comp_C = comp_L + comp_R
    #
    #     mat = []
    #     for comp_elms in comp_C[0]:
    #         for elm in comp_elms:
    #             nums = self.elem_num(L, elm)
    #             mat.append(nums)
    #     i = 0
    #     for comp_elms in comp_R:
    #         for elm in comp_elms:
    #             nums = self.elem_num(R, elm)
    #             mat.append(-1*nums)
    #             i += 1
    #     return mat

    def matrix(self, C):
        comp_C = self.elm_in_chem_eq(C).to_seq()
        mat = []
        for comp_elms in comp_C:
            for elm in comp_elms:
                nums = self.elem_num(C, elm)
                mat.append(nums)
        return mat

    def chem_balance(self, L, R):
        mat1 = self.matrix(L)
        mat2 = self.matrix(R)

        mat = []
        for i in range(len(mat1)):
            neg = [-x for x in mat2[i]]
            mat.append(mat1[i] + neg)
        mat.append([0 for i in range(len(L) + len(R) - 1)])
        mat[-1].append(1)

        mat_B = [[0] for i in range(len(mat) - 1)]
        mat_B.append([1])
        # print(mat, mat_B)
        calc = linalg.lstsq(mat, mat_B)[0].tolist()

        co_L = []
        co_R = []
        for i in range(len(calc)):
            if i < len(mat1):
                co_L.append(calc[i][0])
            else:
                co_R.append(calc[i][0])

        return [co_L, co_R]

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
