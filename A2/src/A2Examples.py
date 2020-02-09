from ChemTypes import *
from Set import *
from ElmSet import *
from MolecSet import *
from MoleculeT import *
from CompoundT import *
from ReactionT import *

# Chem Type Examples


e1 = ElementT.H
e2 = ElementT.He

# Set Examples - with integers
S = Set([1, -6, 4, 0, 12])

S.add(5)

S.rm(4)

print(S.member(5))
print(S.member(4))
print(S.size())

R = Set([12, -6, 0, 1, 5])

print(S.equals(R))
print(S == R)

print(str(R.to_seq()))

for i in R.to_seq():
    print(i)

# ElmSet Examples
E = ElmSet([ElementT.H, ElementT.O])
E.add(ElementT.C)
print(E == ElmSet([ElementT.H, ElementT.C, ElementT.O]))

# MoleculeT Examples
M1 = MoleculeT(2, ElementT.H)
M2 = MoleculeT(7, ElementT.O)
print(M1.num_atoms(ElementT.C))
print(M1.constit_elems() == ElmSet([ElementT.H]))
print(M1.equals(M2))
print(M1 == M2)

# CompoundT Examples
C1 = CompoundT(MolecSet([M1, M2]))
print(C1.num_atoms(ElementT.H))
e = C1.constit_elems()
print(e.equals(ElmSet([ElementT.H, ElementT.O])))
print(C1.equals(CompoundT(MolecSet([M1]))))

# ReactionT Examples
# H2 + O2 --> H2O
M3 = MoleculeT(2, ElementT.H)
M4 = MoleculeT(2, ElementT.O)
C2 = CompoundT(MolecSet([M3]))
C3 = CompoundT(MolecSet([M4]))

M4 = MoleculeT(1, ElementT.O)
C4 = CompoundT(MolecSet([M3, M4]))

R1 = ReactionT([C2, C3], [C4])
# default coefficients for both sides is 1
print(R1.get_lhs_coeff())
print(R1.get_rhs_coeff())
