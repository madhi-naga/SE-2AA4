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

        coeffs = self.chem_balance(L, R)
        self.__coeff_L = coeffs[0]
        self.__coeff_R = coeffs[1]

        # if not (self.is_balanced(L, R, coeffs[0], coeffs[1]) and self.pos(coeffs[0])
        #         and self.pos(coeffs[1])):
        #     raise ValueError('Unbalanced/invalid coefficients')

    def get_lhs(self):
        return self.__lhs

    def get_rhs(self):
        return self.__rhs

    def get_lhs_coeff(self):
        return self.__coeff_L

    def get_rhs_coeff(self):
        return self.__coeff_R

    @staticmethod
    def pos(s):
        for i in s:
            if i <= 0:
                return False
        return True

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

    @staticmethod
    def elm_in_chem_eq_2(C):
        elms = []
        for comp in C:
            elms.append(comp.constit_elems().to_seq())
        ret = Set([])
        for elm in elms:
            ret.add(elm)
        return Set(ret)

    def is_bal_elm(self, L, R, cL, cR, e):
        return self.n_atoms(L, cL, e) == self.n_atoms(R, cR, e)

    def is_balanced(self, L, R, cL, cR):
        # eq_elms = self.elm_in_chem_eq(L).equals(self.elm_in_chem_eq(R))
        eq_atoms = all([self.is_bal_elm(L, R, cL, cR, elm) for elm in self.elm_in_chem_eq(R).to_seq()])
        return eq_atoms

    def matrix(self, C):
        comp_C = self.elm_in_chem_eq(C).to_seq()
        comp_C2 = self.elm_in_chem_eq_2(C).to_seq()
        mat = []
        for comp_elms, comp in comp_C:
            for elm in comp_elms:
                nums = self.elem_num(C, elm)
                mat.append(nums)
        # for comp_elms in comp_C:
        #     for elm in comp_elms:
        #         nums = self.elem_num(C, elm)
        #         mat.append(nums)
        # return mat
        #
        # for col, compound in enumerate(lhs_compounds):
        #     for el, num in compound.items():
        #         row = els_index[el]
        #         A[row][col] = num
        # for col, compound in enumerate(rhs_compounds, len(lhs_compounds)):
        #     for el, num in compound.items():
        #         row = els_index[el]
        #         A[row][col] = -num

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
        calc = linalg.lstsq(mat, mat_B)[0].tolist()
        print((mat, mat_B))
        co_L = []
        co_R = []
        for i in range(len(calc)):
            if i < len(L):
                co_L.append(round(calc[i][0], 5))
            else:
                co_R.append(round(calc[i][0], 5))

        return [co_L, co_R]
