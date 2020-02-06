## @file MoleculeT.py
#  @author
from src.ChemEntity import ChemEntity
from src.ChemTypes import ElementT
from src.ElmSet import ElmSet
from src.Equality import Equality


class MoleculeT(ChemEntity, Equality):

    def __init__(self, e, n):
        self.elm = e
        self.num = n

    def get_elm(self):
        return self.elm

    def get_num(self):
        return self.num

    def num_atoms(self, e):
        if self.elm == e:
            return self.num
        else:
            return 0

    def constit_elems(self):
        return ElmSet()

    def equals(self, m):
        if self.num == m.num and self.elm == m.elm:
            return True
        else:
            return False

