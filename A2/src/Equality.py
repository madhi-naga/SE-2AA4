## @file Equality.py
#  @author
from abc import ABC, abstractmethod


class Equality(ABC):

    @abstractmethod
    def equals(self, R):
        pass
