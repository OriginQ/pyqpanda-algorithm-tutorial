.. pyqpanda algorithm documentation master file, created by
   sphinx-quickstart on Tue Jan 22 14:31:31 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyqpanda algorithm
====================================

**A Quantum Algorithm Development and Runtime Environment Kit, based on pyqpanda**

The **pyqpanda_alg** is a collection of fundamental quantum algorithms and functions that are commonly used in developer's quantum algorithm.

Some of the key functions included in the pyqpanda_alg are:

     ``Grover's Search Algorithm`` : This is a quantum algorithm that can be used to search an unsorted database of N items in O(sqrt(N)) time. It is faster than classical algorithms, which require O(N) time for the same task. Developer can CALL interface grover(arg1, arg2…) directly to support their user-defined algorithm. 

     ``Mixed HHL Solver`` : First use the "Krylov subspace" method to reduce the dimensions of the original linear space, and then use the HHL algorithm to solve it.  The advantage of the subspace method Full Orthogonalization Method (FOM) is that it converges quickly, but is unstable.  The advantage of the Generalized Minimum Residual (GMRES) method is that it is absolutely stable, but converges slowly.  Therefore, the hybrid HHL solver combines the advantages of both, resulting in a more stable solution performance and faster convergence speed.

     ``VQE Solver`` :  VQE is a hybrid quantum-classical algorithm for computing the ground state energy of a Hamiltonian, which is one of the most promising quantum algorithms applied in quantum chemistry. Comparing to classical algorithms where computational costs grow exponentially to size of the system, the VQE algorithm increases polynomial in execution time of quantum circuit and the number of measurement. Here we extract this algorithm out of the chemical context and provide functions to compute the smallest eigenvalue of a real Hermitian matrix. 

Overall, it provides a standardized set of tools for developers, allowing them to write quantum programs that can be easily ported across different quantum computing platforms. It is an important resource for the development of quantum software and the advancement of quantum computing research.

.. toctree::
    :maxdepth: 2
    :caption: Introduction

    GettingStarted

.. toctree::
    :caption: API Reference
    :maxdepth: 3

    autoapi/pyqpanda_alg/VQE/index
    autoapi/pyqpanda_alg/QAOA/index
    autoapi/pyqpanda_alg/QARM/index
    autoapi/pyqpanda_alg/QFinance/index
    autoapi/pyqpanda_alg/QKmeans/index
    autoapi/pyqpanda_alg/QLuoShu/index
    autoapi/pyqpanda_alg/QPCA/index
    autoapi/pyqpanda_alg/QSolver/index
    autoapi/pyqpanda_alg/QSVM/index
