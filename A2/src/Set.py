## @file Set.py
#  @author
from src.Equality import Equality


class Set(Equality):

    def __init__(self, list):
        self.T = list

    def add(self, e):
        self.T.append(e)

    def rm(self, e):
        if not self.member(e):
            raise ValueError()
        else:
            self.T.remove(e)

    def member(self, e):
        if e in self.T:
            return True
        else:
            return False

    def size(self):
        return self.T.length

    def to_seq(self):
        return self.T

    def equals(self, R):
        if self.T.length == R.T.length:
            for i in range(self.T.length):
                if self.T[i] != R.T[i]:
                    return False
            return True
        else:
            return False
