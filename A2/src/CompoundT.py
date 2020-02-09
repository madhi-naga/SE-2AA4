## @file CompoundT.py
#  @author
from ChemEntity import ChemEntity
from ElmSet import ElmSet
from Equality import Equality


class CompoundT(ChemEntity, Equality):

    def __init__(self, M):
        self.__molec_set = M

    def get_molec_set(self):
        return self.__molec_set

    def num_atoms(self, e):
        sum = 0
        for molec in self.__molec_set.to_seq():
            if molec.get_elm() == e:
                sum += molec.get_num()
        return sum

    def constit_elems(self):
        return ElmSet([m.get_elm() for m in self.__molec_set.to_seq()])

    def equals(self, D):
        if len(self.__molec_set.to_seq()) == len(D.__molec_set.to_seq()):
            if all(elem in D.molec_set for elem in self.__molec_set):
                return True
        return False
