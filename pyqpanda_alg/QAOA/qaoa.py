import pyqpanda as pq
import numpy as np
from scipy.optimize import minimize
from scipy.interpolate import barycentric_interpolate as b_interp
import sympy as sp
from . import spsa
from .default_circuits import *

from .. config import *
auth = Authorization()

def p_1(n):
    """
    Transfer binary variable :math:`x_n` to pauli operator :math:`\\frac{I-Z_n}{2}`

    Parameters
        n : ``int``\n
            index of the variable, start with 0.

    Return
        operator : ``pq.PauliOperator``\n
            Pauli operator :math:`\\frac{I-Z_n}{2}`

    Examples
        Transfer :math:`x_0` into pauli operator :math:`\\frac{I-Z_0}{2}`
    
    >>> from pyqpanda_alg.QAOA import qaoa
    >>> operator_0 = qaoa.p_1(0)
    >>> print(operator_0)
        {
        "" : 0.500000,
        "Z0" : -0.500000
        }

    """
    pass


def p_0(n):
    """
    Transfer binary variable :math:`x_n` to pauli operator :math:`\\frac{I+Z_n}{2}`

    Parameters
        n : ``integer``\n
            index of the variable, start with 0.

    Return
        operator : ``pq.PauliOperator``\n
            Pauli operator :math:`\\frac{I+Z_n}{2}`

    Examples
        Transfer :math:`x_0` into pauli operator :math:`\\frac{I+Z_0}{2}`
    
    >>> from pyqpanda_alg.QAOA import qaoa
    >>> operator_0 = qaoa.p_0(0)
    >>> print(operator_0)
        {
        "" : 0.500000,
        "Z0" : 0.500000
        }
    """
    pass


def problem_to_z_operator(problem, norm=False):
    """
    Transfer polynomial function with binary variables :math:`f(x_0, \cdots, x_n)` to
    pauli operator :math:`f(\\frac{I-Z_0}{2}, \cdots, \\frac{I-Z_n}{2})`

    Parameters
        problem : ``expression`` in sympy\n

    Return
        hamiltonian : ``list[tuple]``\n
            Pauli operators :math:`f(\\frac{I-Z_n}{2})` in list form.

    Examples
        Transfer :math:`2 x_0 x_1 + 3 x_2 - 1` into pauli operators

    >>> import sympy as sp
    >>> from pyqpanda_alg.QAOA import qaoa
    >>> vars = sp.symbols('x0:3')
    >>> f = 2*vars[0]*vars[1] + 3*vars[2] - 1
    >>> print(f)
        2*x0*x1 + 3*x2 - 1
    >>> hamiltonian = qaoa.problem_to_z_operator(f)
    >>> print(hamiltonian)
        {
        "" : 1.000000,
        "Z2" : -1.500000,
        "Z1" : -0.500000,
        "Z0" : -0.500000,
        "Z0 Z1" : 0.500000
        }

    """
    pass


def parameter_interpolate(pm):
    """
    Use INTERP heuristic strategy to guess the initial parameter of :math:`p+1` layer QAOA
    from the optimal parameter found from :math:`p` layer QAOA circuit.

    Parameters
        pm : ``array-like``\n
            Optimal parameters of :math:`p` layer QAOA circuit, with length :math:`2\times p`

    Return
        operator : ``array-like``\n
            A guess for the initial parameter of :math:`p+1` layer QAOA, with length :math:`2\times (p+1)`

    References
        [1] ZHOU L, WANG S T, CHOI S, et. Quantum Approximate Optimization Algorithm: Performance, Mechanism, and
        Implementation on Near-Term Devices[J/OL]. Physical Review X, 2020, 10(2): 021067.
        :DOI: `10.1103/PhysRevX.10.021067.`


    Examples
        Transfer :math:`x_0` into pauli operator :math:`\\frac{I-Z_0}{2}`

        >>> import numpy as np
        >>> from pyqpanda_alg.QAOA import qaoa
        >>> initial_parameter = np.array([0.1, 0.2, 0.2, 0.1])
        >>> new_parameter = qaoa.parameter_interpolate(initial_parameter)
        >>> print(new_parameter)
            [0.1  0.15 0.25 0.2  0.15 0.05]

    """
    pass


def pauli_z_operator_to_circuit(operator, qlist, gamma=np.pi):
    """
    Circuit of simulation diagonal Hamiltonian :math:`e^{-iH\theta}`.

    Parameters
        operator : ``list``\n
            Pauli Operator in list form. (By method `operator.toHamiltonian(1)`)
        qlist : ``qubit list``\n
        gamma : ``float``\n
            Value of theta in :math:`e^{-iH\theta}`.

    Return
        circuit : ``pq.QCircuit``\n
            Circuit of simulation diagonal Hamiltonian :math:`e^{-iH\theta}`.

        constant : ``float``\n
            Constant number in the hamiltonian.

    Example
        Print a circuit of hamiltonian for problem :math:`f(\\vec{x})=2x_0x_1 + 3x_2 - 1` with :math:`\\theta=0`

    .. code-block:: python

        import pyqpanda as pq
        import sympy as sp
        from pyqpanda_alg.QAOA import qaoa
        vars = sp.symbols('x0:3')
        f = 2*vars[0]*vars[1] + 3*vars[2] - 1
        operator = qaoa.problem_to_z_operator(f).toHamiltonian(True)

        machine = pq.CPUQVM()
        machine.initQVM()
        qubits = machine.qAlloc_many(3)

        circuit = qaoa.pauli_z_operator_to_circuit(operator, qubits, 0)[0]

        print(circuit)

    .. parsed-literal::

                  ┌────────────┐                              ┌─┐
        q_0:  |0>─┤RZ(0.000000)├ ───■── ────────────── ───■── ┤I├
                  ├────────────┤ ┌──┴─┐ ┌────────────┐ ┌──┴─┐ ├─┤
        q_1:  |0>─┤RZ(0.000000)├ ┤CNOT├ ┤RZ(0.000000)├ ┤CNOT├ ┤I├
                  ├────────────┤ ├─┬──┘ └────────────┘ └────┘ └─┘
        q_2:  |0>─┤RZ(0.000000)├ ┤I├─── ────────────── ────── ───
                  └────────────┘ └─┘


    """
    pass


class QAOA:
    """
    This class provides the quantum alternative operator ansatz algorithm optimizer. It assumes a polynomial problem
    consisting only of binary variables. The problem is then translated into an Ising Hamiltonian whose minimal eigen
    vector and corresponding eigenstate correspond to the optimal solution of the original optimization problem.
    The provided solver is then used to approximate the ground state of the Hamiltonian to find a good solution for the
    optimization problem.

    Parameters
        problem : ``expression`` in sympy or ``pq.PauliOperator``\n
            A polynomial function with binary variables to be optimized. Support an expression in sympy. Next version will
            support an object from pypanda PauliOperator.

        init_circuit : ``function``,  ``optional``\n
            The quantum circuit to create the initial state of QAOA algorithm. Default is Hadamard circuit to create an
            equal superposition state :math:`\ket{\psi} = 2^{-n/2}\sum_{i=0}^{2^n-1}\ket{i}`.

        mixer_circuit : ``function``, ``optional``\n
            The function which returns a mixer quantum circuit :math:`U_M(\\beta)=\exp(-i\\beta H_M)`.
            The function should accept two parameters (qubit list, array-like angles) as input, and return a quantum
            circuit as output. Default is X mixer circuit :math:`\exp(-i\\beta \sum_i X_i)=RX(2\\beta)^{\otimes n}`

        norm : ``bool``\n


    Attributes
        energy_dict : ``dict``\n
            The dict which stores the function value for solutions being sampled during the optimization.
        problem_dimension : ``integer``\n
            The problem dimension, and also the qubit number.
        circuit iter : ``integer``\n
            The number of times the quantum circuit being called during optimization.

    Methods
        calculate_energy : Calculate the function value for one solution.

        run_qaoa_circuit : Given parameters, run the qaoa circuit and get the theoretical probability distribution.

        run : run the optimization process



    Reference
        [1] FARHI E, GOLDSTONE J, GUTMANN S. A Quantum Approximate Optimization Algorithm[J/OL]. 2014[2022-03-09].
        https://arxiv.org/abs/1411.4028v1. DOI:10.48550/arXiv.1411.4028.\n
        [2] ZHOU L, WANG S T, CHOI S, et. Quantum Approximate Optimization Algorithm: Performance, Mechanism,
        and Implementation on Near-Term Devices[J/OL]. Physical Review X, 2020, 10(2): 021067.
        DOI:10.1103/PhysRevX.10.021067.

    """

    def __init__(self, problem, init_circuit=None,
                 mixer_circuit=None, norm=False):
        pass

    def calculate_energy(self, x):
        """
        Calculate the function value for one solution.

        Parameter
            x : ``array-like``\n
                one binary variables solution in vector form.

        Return 
            ``float``\n
            function value of the solution :math:`f(x)`.

        Example
            Let :math:`f(\\vec{x})=2x_0x_1 + 3x_2 - 1`, calculate :math:`f(1,0,0)`

        >>> import sympy as sp
        >>> from pyqpanda_alg.QAOA.qaoa import *
        >>> vars = sp.symbols('x0:3')
        >>> f = 2*vars[0]*vars[1] + 3*vars[2] - 1
        >>> print(f)
            2*x0*x1 + 3*x2 - 1
        >>> qaoa_f = QAOA(f)
        >>> solution_1 = [1, 0, 0]
        >>> print(qaoa_f.calculate_energy(solution_1))
            -1
        >>> solution_2 = [0, 1, 1]
        >>> print(qaoa_f.calculate_energy(solution_2))
            2
        >>> ham_f = 2 * p_1(0) * p_1(1) + 3 * p_1(2)- 1
        >>> qaoa_ham = QAOA(ham_f)
        >>> print(qaoa_ham.calculate_energy(solution_1))
            -1

        """
        pass

    def run_qaoa_circuit(self, gammas, betas, shots=-1):
        """
        Given parameters, run the qaoa circuit and get the theoretical probability distribution.

        Parameters
            gammas : ``array-like``\n
                Parameter gamma for QAOA phase circuit\n

            betas : ``array-like``\n
                Parameter beta for QAOA mixer circuit\n

            shots : ``integer``, ``optional``\n
                Times of running the same circuit. Must be positive integer or -1.
                If it is -1, the results are given as amplitudes of all state vectors,
                which can be viewed as running the circuit infinite times. Default is -1.

        Return
            prob_result : ``dict``\n
                Probability of each computational basis state. The keys are binary form
                of qubits where the first qubit sits at the right-most position and the
                items are the corresponding probability (if shots = -1) or frequency (if shots > 0).

        Example
            Run a two-layer QAOA algorithm circuit of problem :math:`f(\\vec{x})=2x_0x_1 + 3x_2 - 1` with parameters
            :math:`[0, 0, 0, 1, 1, 1]`

        .. code-block:: python

            import pyqpanda as pq
            import sympy as sp
            from pyqpanda_alg.QAOA.qaoa import *

            vars = sp.symbols('x0:3')
            f = 2*vars[0]*vars[1] + 3*vars[2] - 1
            qaoa_f = QAOA(f)

            gammas = [0, 0]
            betas = [1, 1]

            qaoa_result = qaoa_f.run_qaoa_circuit(gammas, betas, -1)
            print(qaoa_result)
            qaoa_result = qaoa_f.run_qaoa_circuit(gammas, betas, 500)
            print(qaoa_result)

        The codes above would give results like (with errors due to randomness):

        .. parsed-literal::
            {'000': 0.12500000000000008, '001': 0.12500000000000008, '010': 0.12500000000000008,
            '011': 0.12500000000000008, '100': 0.12500000000000008, '101': 0.12500000000000008,
            '110': 0.12500000000000008, '111': 0.12500000000000008}

            {'000': 0.132, '001': 0.134, '010': 0.112, '011': 0.136, '100': 0.094, '101': 0.13,
            '110': 0.122, '111': 0.14}

        """
        pass

    def run(self, layer=1, initial_para=None, shots=-1, loss_type=None, optimize_type=None, optimizer=None,
            optimizer_option=None, **loss_option):
        """
        Optimize the function by QAOA algorithm.

        Parameters
            layer : ``integer``, ``optional``\n
                Layers number of QAOA circuit. Default is 1.
                If optimize type is interp, then it represents the final layer of the optimization progress.

            initial_para : ``array-like``, ``optional``\n
                initial parameters of :math:`p` layer QAOA circuit, with length :math:`2\\times p`. If not given, a random
                distribution from :math:`U(0, \pi)` of size :math:`2p` is generated.

            shots : ``integer``, ``optional``\n
                Circuit measured times. If shots takes -1, then use theoretical probability (by state vector) instead.
                Default is -1

            loss_type : ``string``, ``optional``\n
                The loss function used by the optimizer. Should be one of

                    - ``default`` : Given a result, calculate the energy expectation.\n
                        See Note ``Energy expectation``
                    - ``Gibbs`` : Given a result and argument temperature :math:`T`, calculate the Gibbs energy expectation.\n
                        See Note ``Gibbs energy``
                    - ``CVaR`` : Given a result and argument :math:`\\alpha`, calculate the CVaR loss function.\n
                        See Note ``CVaR loss functio``

                If not given, default by ``default``.

            optimize_type : ``string``, ``optional``\n
                The method to optimize the QAOA circuit. Should be one of

                    - ``default``: Directly optimize the :math:`p` layer QAOA circuit.\n
                    - ``interp``: Use interpolate method to train a big QAOA circuit.\n
                        See Note ``interp method``

                If not given, default by ``default``.

            optimizer : ``string``, ``optional``\n
                Type of solver. Should be one of

                    - ``SPSA`` : See ``spsa.spsa_minimize``\n

                    - one of ``Nelder-Mead``, ``Powell``, ``CG``, ``BFGS``, ``Newton-CG``, ``TNC``, ``COBYLA``, ``SLSQP``,
                    ``trust-constr``, ``dogleg``, ``trust-ncg``, ``trust-exact``, ``trust-krylov``.
                    See ``scipy.optimize.minimize``.

                If not given, default by ``SLSQP``.

            optimizer_option : ``dict``, ``optional``\n
                A dictionary of solver options. Accept the following generic options:\n
                    - bounds : ``List[tuple]``, ``optional``\n
                        Bounds for the variables. Sequence of ``(min, max)`` pairs for each element in `x`.
                        If specified, variables are clipped to fit inside the bounds after each iteration.
                        None is used to specify no bound.
                    - options : ``integer``\n
                        Maximum number of iterations to perform. Depending on the
                        method each iteration may use several function evaluations.

                        For `TNC` use `maxfun` instead of `maxiter`.

            loss_option :\n

                temperature : ``float``, ``optional``\n
                    parameter calculated in _loss_function_Gibbs. Default is 1. See Note ``Gibbs energy``.

                alpha : ``float``, ``optional``\n
                    parameter calculated in _loss_function_cvar. Default is 1. See Note ``Gibbs energy``.

        Return
            qaoa_result : ``dict``\n
                dict of all possible solutions with corresponding probabilities.
                The elements are arranged in descending order of probability.

            para_result : ``array-like``\n
                Array of the optimized QAOA parameters.

            loss_result : ``float``\n
                Loss function value of the optimized QAOA parameters.

        Example
            Run a two-layer QAOA algorithm circuit of problem :math:`f(\\vec{x})=2x_0 + x_1 + 3x_2 - 1` with parameters
            ``[0, 0, 0, 1, 1, 1]``

        .. code-block:: python

            import sympy as sp
            from pyqpanda_alg.QAOA import qaoa
            vars = sp.symbols('x0:3')
            f = 2*vars[0]*vars[1] + 3*vars[2] - 1
            qaoa_f = qaoa.QAOA(f)

            qaoa_result = qaoa_f.run(layer=3)
            sorted_result = sorted(qaoa_result[0].items(), key=lambda k:k[1], reverse=True)[:5]
            print(sorted_result[:5])

        .. parsed-literal::
            [('000', 0.6848946054168573),
             ('010', 0.1575526972909123), 
             ('001', 0.15755269729091226), 
             ('100', 7.957749518311524e-13), 
             ('110', 1.8305953815081342e-13)]


        Notes
            - Energy expectation:\n
                In traditional QAOA algorithm, the parameter is optimized by minimize the energy expectation

                :math:`\\bra{\psi(\gamma, \\beta}H\ket{\psi(\gamma, \\beta)}`

                If measure type is sample, it is calculated by

                :math:`E=\\frac{1}{N_{\\rm{shots}}}\sum_{i=0}^{2^n-1} n_iE_i`.


                If measure type is theoretical, it is calculated by

                :math:`E=\sum_{i=0}^{2^n-1} p_iE_i`.

            - Gibbs energy:\n

                Inspired by Ref[1]. Instead of the traditional energy expectation value, using the Gibbs function as the
                object function. The function is

                    :math:`f_G=-\ln \langle e^{-E/T}\\rangle`

                Here :math:`T` is the hyperparameter of temperature, as :math:`T` decreases, the weight of the lower
                energy states in the loss function then becomes larger. When :math:`T=1`, it turns back to energy
                expectation function.

                If measure type is sample, it is calculated by

                    :math:`G=-\log (\\frac{1}{N_{\\rm{shots}}}\sum_{i=0}^{2^n-1} n_i \exp(-E_i/T))`.

                If measure type is theoretical, it is calculated by

                    :math:`G=-\log (\sum_{i=0}^{2^n-1} p_i \exp(-E_i/T))`.


            - CVaR loss function:\n
                Inspired by Ref[3].Instead of the traditional energy expectation value, using the Conditional Value at
                Risk function as the object function. The function is

                    :math:`CVaR_\\alpha(X) = \mathbb{E}[X|X\leq F_X^{-1}(alpha)]`

                Here :math:`\\alpha` is the confidence level. CVaR is the expected value of the lower α-tail of the
                distribution of X. :math:`\\alpha=0` corresponds to the minimum, and :math:`\\alpha=1` corresponds to the
                expectation value.

                If measure type is sample, it is calculated by

                    :math:`E=\\frac{1}{\\alpha N}(\sum_{i=0}^{k} n_iE_i + (\\alpha N - n_{k+1})E_{k+1}),\sum_{i=0}^k n_i < \\alpha N`

                If measure type is theoretical, it is calculated by

                    :math:`E=\sum_{i=0}^{k} p_iE_i + (\\alpha - p_{k+1})E_{k+1}, \sum_{i=0}^k p_i < \\alpha`

            - Interpolate method:\n
                Inspired by Ref[2].

        Reference
            [1] LI L, FAN M, CORAM M, et. Quantum Optimization with a Novel Gibbs Objective Function and Ansatz
            Architecture Search[J/OL]. Physical Review Research, 2020, 2(2): 023074. DOI:10.1103/PhysRevResearch.2.023074.\n

            [2] ZHOU L, WANG S T, CHOI S, et. Quantum Approximate Optimization Algorithm:
            Performance, Mechanism, and Implementation on Near-Term Devices[J/OL].
            Physical Review X, 2020, 10(2): 021067. DOI:10.1103/PhysRevX.10.021067.\n

            [3] BARKOUTSOS P K, NANNICINI G, ROBERT A, et. Improving Variational Quantum Optimization using CVaR[J/OL].
            Quantum, 2020, 4: 256. DOI:10.22331/q-2020-04-20-256.\n



        """
        pass

