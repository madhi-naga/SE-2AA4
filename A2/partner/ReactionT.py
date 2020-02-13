## @file ReactionT.py
#  @author Hafez Issa
#  @brief Module to balance the chemical equation of sequences CompoundT's
#  @date February 08, 2020

from CompoundT import *
from ChemTypes import *
import numpy as np


## @brief ADT which represents a ReactionT object, a chemical equation
class ReactionT():

    ## @brief Constructor for a chemical equation, ReactionT object
    #  @details exception, ValueError
    #  @param L Sequence of CompoundT's
    #  @param R Sequence of CompoundT's
    def __init__(self, L, R):
        self.lhs = L
        self.rhs = R
        self.coeffL = []
        self.coeffR = []

        temp_coeffL = []
        temp_coeffR = []

        compounds_total = []
        elems_in_total = __elm_in_chem_eq(self.lhs.to_seq())

        for i in self.lhs:
            compounds_total.append(i)
        
        for i in self.rhs:
            compounds_total.append(i)

        for i in compounds_total:
            a.append(i.num_atoms())
            
        for l in L:
            temp = l.get_molec_set().to_seq()
            for i in temp:
                temp_coeffL.append(i.get_num())
        self.coeffL = temp_coeffL
        
        for r in R:
            temp = r.get_molec_set().to_seq()
            for i in temp:
                temp_coeffR.append(i.get_num())
        self.coeffR = temp_coeffR

    ## @brief Getter method
    #  @return Sequence of type CompoundT
    def get_lhs(self):
        return self.lhs

    ## @brief Getter method
    #  @return Sequence of type CompoundT
    def get_rhs(self):
        return self.rhs

    ## @brief Getter method
    #  @return Sequence of type Real
    def get_lhs_coeff(self):
        return self.coeffL

    ## @brief Getter method
    #  @return Sequence of type Real
    def get_rhs_coeff(self):
        return self.coeffR

    ## @brief Check if sequence is positive
    #  @param s Sequence of type Real
    #  @return Boolean representing whether all elements in the sequence is positive
    def __pos(s):
        for i in s:
            if (i <= 0):
                return False
        return True

    ## @brief Count number of atoms
    #  @param C Sequence of type CompoundT
    #  @param c Sequence of type Real
    #  @param e ElementT
    #  return Natural Number which represents the number of atoms
    def __n_atoms(C, c, e):
        count = 0
        for i in range(C.get_molec_set().size()):
            count += c[i] * C.get_molec_set().to_seq()[i].num_atoms(e)
        return count

    ## @brief Find elements in the sequence
    #  @param C Sequence of type CompoundT
    #  @return ElmSet containing the elements in the CompoundT
    def __elm_in_chem_eq(C):
        elem = ElmSet([])
        for c in C.get_molec_set().to_seq():
            elem.add(c.constit_elems())
        return elem

    ## @brief
    #  @param L Sequence of type CompoundT
    #  @param R Sequence of type CompoundT
    #  @param cL Sequence of type Real
    #  @param cR Sequence of type Real
    #  @param e ElementT
    #  @return Boolean
    def __is_bal_elm(L, R, cL, cR, e):
        if (n_atoms(L, cL, e) == n_atoms(R, cR, e)):
            return True
        return False

    ## @brief
    #  @param L Sequence of type CompoundT
    #  @param R Sequence of type CompoundT
    #  @param cL Sequence of type Real
    #  @param cR Sequence of type Real
    #  @return Boolean representing whether the equations are balanced
    def __is_balanced(L, R, cL, cR):
        if not (elm_in_chem_eq(L) == elm_in_chem_eq(R)):
            return False
        
        for e in elem_in_chem_eq(L):
            if not (is_bal_elm(L, R, cL, cR, e)):
                return False
        return True
