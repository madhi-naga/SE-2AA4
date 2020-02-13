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
print(M1.constit_elems().to_seq())
print(M1.equals(M2))
print(M1 == M2)

# CompoundT Examples
C1 = CompoundT(MolecSet([M1, M2]))
print(C1.num_atoms(ElementT.H))
e = C1.constit_elems()
print("helloo")
print(e.to_seq())
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

print(R1.get_lhs_coeff())
print(R1.get_rhs_coeff())
e1 = R1.elm_in_chem_eq(R1.get_lhs())
e2 = R1.elm_in_chem_eq(R1.get_rhs())
print(R1.chem_balance(R1.get_lhs(), R1.get_rhs()))

M4 = MoleculeT(1, ElementT.O)
M5 = MoleculeT(1, ElementT.Mg)
M6 = MoleculeT(2, ElementT.O)
M7 = MoleculeT(2, ElementT.H)

C5 = CompoundT(MolecSet([M5, M6, M7]))
C6 = CompoundT(MolecSet([M5, M4]))
C7 = CompoundT(MolecSet([M7, M4]))
R2 = ReactionT([C5], [C6, C7])
print(R2.chem_balance(R2.get_lhs(), R2.get_rhs()))

M8 = MoleculeT(1, ElementT.N)
M9 = MoleculeT(2, ElementT.N)
C8 = CompoundT(MolecSet([M8]))
C9 = CompoundT(MolecSet([M9]))
R3 = ReactionT([C8], [C9])
print(R3.chem_balance(R3.get_lhs(), R3.get_rhs()))

M8 = MoleculeT(1, ElementT.Cu)
M9 = MoleculeT(2, ElementT.N)
M10 = MoleculeT(6, ElementT.O)
M11 = MoleculeT(1, ElementT.O)
M12 = MoleculeT(2, ElementT.O)
M13 = MoleculeT(1, ElementT.N)
C8 = CompoundT(MolecSet([M8, M9, M10]))  # CuN2O6
C9 = CompoundT(MolecSet([M8, M11]))  # CuO
C10 = CompoundT(MolecSet([M13, M12]))  # NO2
C11 = CompoundT(MolecSet([M12]))  # O2
R4 = ReactionT([C8], [C9, C10, C11])
print(R4.chem_balance(R4.get_lhs(), R4.get_rhs()))
