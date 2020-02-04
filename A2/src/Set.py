## @file Set.py
#  @author 

class Set:

    def __init__(self, list):
        self.T = list

    def add(self, e):
        self.T.append(e)

    def rm(self, e):
        self.T.remove(e)

    def rm(self, e):
        if e in self.T:
            return True
        else:
            return False

    def size(self):
        return self.T.length

    def to_seq(self):
        return self.T

    #def equals(self, R):
