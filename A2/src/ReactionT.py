## @file ReactionT.py
#  @title ReactionT
#  @author Madhi Nagarajan
#  @brief This file acts as a data type for any Reaction.
#  @date Feburary 12, 2020


from numpy import linalg
from CompoundT import *
from MoleculeT import *
from Set import *
from ElmSet import *
from MolecSet import *


## @brief The class, ReactionT, represents a data type for Reactions
#  @details The class, ReactionT, represents a data type for Reactions and
#  does chemical reaction related operations
class ReactionT:

    ## @brief Constructor for ReactionT; fills out left-hand and right
    #  @details Constructor accepts two parameters, lhs and rhs. It fills out
    #  left-hand and right-hand
    # sides of the Reaction, as well as filling out the correct
    # LHS and RHS coefficients.
    #  @param L is a list/Set of Compounds of all LHS compounds in the reaction
    #  @param R is a list/Set of Compounds of all RHS compounds in the reaction
    def __init__(self, L, R):
        self.__lhs = L
        self.__rhs = R

        coeffs = self.chem_balance(L, R)
        self.__coeff_L = coeffs[0]
        self.__coeff_R = coeffs[1]

        if not (self.is_balanced(L, R, coeffs[0], coeffs[1]) and self.pos(
                coeffs[0]) and self.pos(coeffs[1])):
            raise ValueError('Unbalanced/invalid coefficients')

    ## @brief The function returns the LHS constructor of ReactionT
    #  @returns a list of LHS compounds
    def get_lhs(self):
        return self.__lhs

    ## @brief The function returns the RHS constructor of ReactionT
    #  @returns a list of RHS compounds
    def get_rhs(self):
        return self.__rhs

    ## @brief The function returns the LHS coefficient constructor of ReactionT
    #  @returns a list of LHS coefficients for all LHS compounds
    def get_lhs_coeff(self):
        return self.__coeff_L

    ## @brief The function returns the RHS coefficient constructor of ReactionT
    #  @returns a list of RHS coefficients for all RHS compounds
    def get_rhs_coeff(self):
        return self.__coeff_R

    ## @brief The function checks if all elements of a Set are positive
    #  @param s is the Set
    #  @returns a boolean value
    @staticmethod
    def pos(s):
        for i in s:
            if i <= 0:
                return False
        return True

    ## @brief The function finds the number of atoms in a compound
    #  @param C os a set of CompoundT
    #  @param c is a set of natural numbers
    #  @param e is a given element of type ElementT
    #  @returns the total number of atoms
    @staticmethod
    def n_atoms(C, c, e):
        atoms = 0
        for i in range(len(C)):
            atoms += c[i] * C[i].num_atoms(e)
        return atoms

    ## @brief The function finds the number of ...
    #  @param C os a set of CompoundT
    #  @param e is a given element of type ElementT
    #  @returns the total number of atoms
    @staticmethod
    def elem_num(C, e):
        atoms = []
        for i in range(len(C)):
            atoms.append(C[i].num_atoms(e))
        return atoms

    ## @brief The function finds all the ElementTs in a CompoundT set
    #  @param C os a set of CompoundT
    #  @returns a set of these elements
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

    ## @brief The function checks if the number of atoms of
    # an ElementT are the same on both LHS and RHS
    #  @param L is a LHS set of CompoundT
    #  @param R is a RHS set of CompoundT
    #  @param L is a LHS set of balancing coefficients
    #  @param R is a RHS set of balancing coefficients
    #  @param e is a given element of type ElementT
    #  @returns a set of these elements
    def is_bal_elm(self, L, R, cL, cR, e):
        return self.n_atoms(L, cL, e) == self.n_atoms(R, cR, e)

    ## @brief The function checks if the LHS and RHS are balanced
    #  @param L is a LHS set of CompoundT
    #  @param R is a RHS set of CompoundT
    #  @param L is a LHS set of balancing coefficients
    #  @param R is a RHS set of balancing coefficients
    #  @returns a set of these elements
    def is_balanced(self, L, R, cL, cR):
        eq_atoms = all([self.is_bal_elm(L, R, cL, cR, elm)
                        for elm in self.elm_in_chem_eq(R).to_seq()])
        return eq_atoms

    ## @brief The function forms a matrix of a given side
    #  @param C is a set of CompoundTs, either LHS or RHS
    #  @returns a list/2D matrix
    def matrix(self, C):
        comp_C = self.elm_in_chem_eq(C).to_seq()
        mat = []
        for comp_elms in comp_C:
            for elm in comp_elms:
                nums = self.elem_num(C, elm)
                mat.append(nums)
        return mat

    ## @brief The function balances the chemical reaction utilizing numpy
    #  @param L is a LHS set of CompoundT
    #  @param R is a RHS set of CompoundT
    #  @returns a list containing both LHS and RHS coefficients
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
        co_L = []
        co_R = []
        for i in range(len(calc)):
            if i < len(L):
                co_L.append(round(calc[i][0], 5))
            else:
                co_R.append(round(calc[i][0], 5))

        return [co_L, co_R]
