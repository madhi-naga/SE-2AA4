## @file MoleculeT.py
#  @author
from ChemEntity import ChemEntity
from ElmSet import *
from Equality import Equality


class MoleculeT(ChemEntity, Equality):

    def __init__(self, n, e):
        self.__elm = e
        self.__num = n

    def get_elm(self):
        return self.__elm

    def get_num(self):
        return self.__num

    def num_atoms(self, e):
        if self.__elm == e:
            return self.__num
        else:
            return 0

    def constit_elems(self):
        return ElmSet([self.get_elm()])

    def equals(self, m):
        if self.__num == m.__num and self.__elm == m.__elm:
            return True
        else:
            return False

