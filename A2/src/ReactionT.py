## @file ReactionT.py
#  @author

class ReactionT:

    def __init__(self, L, R):
        self.__lhs = L
        self.__rhs = R
        self.__coeff_L = L
        self.__coeffr_R = R

    def get_lhs(self):
        return self.__lhs

    def get_rhs(self):
        return self.__rhs

    def get_lhs_coeff(self):
        return self.__coeff_L

    def get_lhs(self):
        return self.__coeffr_R

