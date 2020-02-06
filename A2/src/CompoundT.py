## @file CompoundT.py
#  @author
from src.ChemEntity import ChemEntity
from src.MolecSet import MolecSet
from src.Equality import Equality

class CompoundT(ChemEntity, Equality):

    def __init__(self, M):
        self.molec_set = M

    def get_molec_set(self):
        return self.molec_set

    def num_atoms(self, e):
        if m in sel

    def constit_elems(self):
        return MolecSet()

    def equals(self, D):
        if self.molec_set.equals(D.molec_set):
            return True
        else:
            return False
