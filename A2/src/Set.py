## @file Set.py
#  @author
from Equality import Equality


class Set(Equality):

    def __init__(self, s):
        self.T = s

    def __eq__(self, other):
        return self.equals(other)

    def add(self, e):
        if not self.member(e):
            self.T.append(e)

    def rm(self, e):
        self.T.remove(e)

    def member(self, e):
        if e in self.T:
            return True
        else:
            return False

    def size(self):
        return len(self.T)

    def to_seq(self):
        return self.T

    def equals(self, R):
        if len(self.T) == len(R.T):
            if all(elem in R.T for elem in self.T):
                return True
        return False