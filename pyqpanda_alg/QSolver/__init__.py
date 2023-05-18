'''
The mixed-HHL solver does not directly use quantum algorithm to solve the original system of equations, but first uses the "Krylov subspace" method to reduce the dimension of the original linear space and then uses the HHL algorithm to solve the problem. Since the Full Orthogonalization Method(FOM) belongs to the orthogonal projection method, the solution stability existence requires A to be positive definite, and this condition is often not satisfied in practical computations. For the oblique projection methods such as Generalized Minimum Residual（GMRES), the requirement that matrix A is non-singular is easy to be satisfied, so the GMRES method has very high stability in practical calculation. However, the convergence speed of GMRES method is much slower than that of FOM method.Combining the advantages of the two methods, a Mixed-HHL linear solution algorithm is proposed.
'''

from . import qsolver

__all__ = [qsolver]

