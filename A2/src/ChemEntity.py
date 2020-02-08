## @file ChemEntity.py
#  @author
from abc import abstractmethod, ABC

from ChemTypes import *


class ChemEntity(ABC):

    @abstractmethod
    def num_atoms(self, elem):
        pass

    @abstractmethod
    def constit_elems(self):
        pass
