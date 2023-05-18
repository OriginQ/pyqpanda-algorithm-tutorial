'''
The VQE(Variational Quantum Eigensolver) module provides functions to compute the smallest eigenvalue of a real Hermitian matrix.  

VQE module includes two functions: HardwareEfficientCircuit and vqe_solver. 
The former function generates parameterized quantum circuit that is frequently used in various VQAs. We provide a template to construct a universal quantum circuit, which consists of single-qubit rotations (Rz Rx Rz) on every qubit and two-qubit entangling gates (CZ and CNOT) on neighboring qubits. The circuit in this function is one layer, generally the hardware-efficient ansatz consists of many layers, you can customize your own circuit by repeating this layer multiple times. 

The vqe_solver function can be used to compute the smallest eigenvalue of a real Hermitian matrix using Hardware-Efficient ansatz.  By inputing a real Hermitian matrix and initial parameter list, you will get the smallest eigenvalue. 
'''


from . import vqe

__all__ = [vqe]
 