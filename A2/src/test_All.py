## @file test_All.py
#  @title test_Al
#  @author Madhi Nagarajan
#  @brief This file is the test class
#  @date Feburary 12, 2020

import pytest
from CompoundT import *
from MoleculeT import *
from Set import *
from ElmSet import *
from MolecSet import *
from ChemTypes import *
from ReactionT import *


class Test_All:

    def setup_method(self, method):
        self.s1 = Set([3, -6, 4, 0, 12, 9])
        self.e1 = ElmSet([ElementT.H, ElementT.O])

        self.m1 = MoleculeT(2, ElementT.H)
        self.m2 = MoleculeT(7, ElementT.O)
        self.m3 = MoleculeT(2, ElementT.H)
        self.m4 = MoleculeT(2, ElementT.O)

        self.c1 = CompoundT(MolecSet([self.m1, self.m2]))
        self.c2 = CompoundT(MolecSet([self.m3]))
        self.c3 = CompoundT(MolecSet([self.m4]))
        self.c4 = CompoundT(MolecSet([self.m3, self.m4]))

        self.r1 = ReactionT([self.c2, self.c3], [self.c4])

    def teardown_method(self, method):
        pass

    def test_Set_add(self):
        self.s1.add(6)
        self.s1.equals(Set([3, -6, 4, 0, 12, 9, 6]))

    def test_Set_rm(self):
        pass # assert self.s1.rm(3) == Set([-6, 4, 0, 12, 9])

    def test_Set_member(self):
        assert self.s1.member(3)
        assert not(self.s1.member(5))

    def test_Set_to_seq(self):
        assert self.s1.to_seq() == [3, -6, 4, 0, 12, 9]

    def test_Set_equals(self):
        assert self.s1.equals(Set([3, -6, 4, 0, 12, 9]))
        assert not(self.s1.equals(Set([5])))

    def test_ElmSet_add(self):
        self.e1.add(ElementT.C)
        assert self.e1 == ElmSet([ElementT.H, ElementT.O, ElementT.C])

    def test_MoleculeT_num_atoms(self):
        assert self.m1.num_atoms(ElementT.H) == 2
        assert self.m2.num_atoms(ElementT.C) == 0


    def test_MoleculeT_constit_elems(self):
        assert self.m1.constit_elems().to_seq() == [ElementT.H]

    def test_MoleculeT_equals(self):
        assert self.m1.equals(MoleculeT(2, ElementT.H))
        assert self.m1 == MoleculeT(2, ElementT.H)

    def test_CompoundT_get_molec_set(self):
        assert self.c1.get_molec_set() == MolecSet([self.m1, self.m2])

    def test_CompoundT_num_atoms(self):
        assert self.c1.num_atoms(ElementT.C) == 0
        assert self.c1.num_atoms(ElementT.H) == 2

    def test_CompoundT_constit_elems(self):
        assert self.c1.constit_elems() == ElmSet([ElementT.H, ElementT.O])


    def test_ReactionT_get_lhs(self):
        assert self.r1.get_lhs() == MolecSet(self.c2, self.c3)

    def test_ReactionT_get_rhs(self):
        pass

    def test_ReactionT_get_lhs_coeff(self):
        pass

    def test_ReactionT_get_rhs_coeff(self):
        pass
