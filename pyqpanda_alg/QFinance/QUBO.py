from typing import Union, Optional, List

import numpy as np
import pyqpanda as pq
import sympy as sp

from .. config import *
auth = Authorization()

from . import grover
from pyqpanda_alg.QAOA import qaoa


class QuadraticBinary:
    """
    Represent a quadratic form and compute the function value using a quantum circuit

    .. math::
        Q(x) = x^T A x + x^T b + c

    .. math::
        |x\\rangle_n |0\\rangle_m \mapsto |x\\rangle_n |(Q(x) + 2^m) \mod 2^m \\rangle_m

    According to the above formula, a negative value can also be represent by this
    method using two's complement.

    Parameters
        problem : ``sympy.Basic`` or ``dict``\n
            A quadratic form function with binary variables to be optimized. Support an expression in sympy.
            Keys followed should be included if expression in dict:

            ``quadratic`` : A, Optional ``[Union[np.ndarray, List[List[float]]]]`` , the quadratic coefficients matrix.\n
            ``linear`` : b, Optional ``[Union[np.ndarray, List[float]]]`` , the linear coefficients array.\n
            ``constant`` : c, ``float``, a constant.\n

    """

    def __init__(self, problem):
        pass

    def query_qnumber(self) -> List[int]:
        """
        Returns
            [n_key, n_res] : ``list[int]``\n
                Returns the size(number of qubits) of the variable and result registers for the given problem.

        Examples
            An example for function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2

        >>> from pyqpanda_alg.QFinance import QUBO
        >>> import sympy as sp
        >>> import numpy as np
        >>> import pyqpanda as pq
        >>> x0, x1, x2 = sp.symbols('x0 x1 x2')
        >>> function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2
        >>> test0 = QUBO.QuadraticBinary(function)
        >>> n_key, n_res = test0.query_qnumber()
        >>> print(n_key, n_res)
        3 2

        """
        pass

    def cir(self, q_key, q_res):
        """
        Parameters
            q_key : ``QVec``\n
                Qubit(s) for the variable register.
            q_res : ``QVec``\n
                Qubit(s) for the result register.

        Returns
            main_cir : ``QCircuit``\n
                Returns the quantum circuit for computing the function.

        Examples
            An example for function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2

        >>> from pyqpanda_alg.QFinance import QUBO
        >>> import sympy as sp
        >>> import numpy as np
        >>> import pyqpanda as pq
        >>> x0, x1, x2 = sp.symbols('x0 x1 x2')
        >>> function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2
        >>> test0 = QUBO.QuadraticBinary(function)
        >>> n_key, n_res = test0.query_qnumber()
        >>> m = pq.CPUQVM()
        >>> m.initQVM()
        >>> q_key = m.qAlloc_many(n_key)
        >>> q_res = m.qAlloc_many(n_res)
        >>> print(test0.cir(q_key, q_res))
        
        .. parsed-literal::
            q_0:  |0>──── ───────■────── ───────■─────────────── ─────────────────────── ───────■────────────────────── >
                                 │              │                                               │                       >
            q_1:  |0>──── ───────┼────── ───────┼───────■─────── ───────■─────────────── ───────■────────────────────── >
                                 │              │       │               │                       │                       >
            q_2:  |0>──── ───────┼────── ───────┼───────┼─────── ───────┼───────■─────── ───────┼──────────────■─────── >
                      ┌─┐ ┌──────┴─────┐        │┌──────┴──────┐        │┌──────┴──────┐ ┌──────┴──────┐       │        >
            q_3:  |0>─┤H├ ┤U1(2.042035)├ ───────┼┤U1(-1.570796)├ ───────┼┤U1(-0.785398)├ ┤U1(-1.884956)├───────┼─────── >
                      ├─┤ └────────────┘ ┌──────┴┴────┬────────┘ ┌──────┴┴─────┬───────┘ └─────────────┘┌──────┴──────┐ >
            q_4:  |0>─┤H├ ────────────── ┤U1(4.084070)├───────── ┤U1(-3.141593)├──────── ───────────────┤U1(-1.570796)├ >
                      └─┘                └────────────┘          └─────────────┘                        └─────────────┘ >

            
            q_0:  |0>───────■─────── ────────────── ────────────── ─ ─── ────────────────── ───
                            │
            q_1:  |0>───────■─────── ───────■────── ───────■────── ─ ─── ────────────────── ───
                            │               │              │
            q_2:  |0>───────┼─────── ───────■────── ───────■────── ─ ─── ────────────────── ───
                            │        ┌──────┴─────┐        │         ┌─┐
            q_3:  |0>───────┼─────── ┤U1(1.413717)├ ───────┼────── X ┤H├ ─────────■──────── ───
                     ┌──────┴──────┐ └────────────┘ ┌──────┴─────┐ │ └─┘ ┌────────┴───────┐ ┌─┐
            q_4:  |0>┤U1(-3.769911)├ ────────────── ┤U1(2.827433)├ X ─── ┤CR(1.570796).dag├ ┤H├
                     └─────────────┘                └────────────┘       └────────────────┘ └─┘

        """
        pass

    def function_value(self, var_array):
        """
        Parameters
            var_array : ``array_like``\n
                An array of binary values.

        Returns
            res : ``float``\n
                The result of the function under given variables array.

        Examples
            An example for function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2

        >>> from pyqpanda_alg.QFinance import QUBO
        >>> import sympy as sp
        >>> x0, x1, x2 = sp.symbols('x0 x1 x2')
        >>> function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2
        >>> test0 = QUBO.QuadraticBinary(function)
        >>> # calculate the quadratic function value above with x0, x1, x2= 0, 1, 0
        >>> print(test0.function_value([0, 1, 0]))
        -1.0

        """
        pass

    def qubobytraversal(self):
        """
        Traversing the entire solution space to find the minimum value solution.

        Returns
            index_list, min_value : ``list``, ``float``\n
                The solution obtained by traversing the entire solution space.

        Examples
            An example for function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2

        >>> from pyqpanda_alg.QFinance import QUBO
        >>> import sympy as sp
        >>> import numpy as np
        >>> import pyqpanda as pq
        >>> x0, x1, x2 = sp.symbols('x0 x1 x2')
        >>> function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2
        >>> test0 = QUBO.QuadraticBinary(function)
        >>> # find the minimum function value by traversing
        >>> res0 = test0.qubobytraversal()
        >>> print('result of traversal: ', res0)
        result of traversal:  ([[0, 1, 0]], -1.0)

        """
        pass

class QUBO_GAS_origin(QuadraticBinary):

    """
     .. math::
        \\
    Inheritance class of QuadraticBinary. Using GAS to find the minimum value solution
    of given quadratic binary optimization problem.

    .. math::
        Q(x) = x^T A x + x^T b + c

    .. math::
        |x\\rangle_n |0\\rangle_m \mapsto |x\\rangle_n |(Q(x) + 2^m) \mod 2^m \\rangle_m

    According to the above formula, a negative value can also be represent by this
    method using two's complement.

    Parameters
        problem : ``sympy.Basic`` or ``dict``\n
            A quadratic form function with binary variables to be optimized. Support an expression in sympy.
            Keys followed should be included if expression in dict:\n
                ``quadratic`` : A, Optional ``[Union[np.ndarray, List[List[float]]]]`` , the quadratic coefficients matrix.\n
                ``linear`` : b, Optional ``[Union[np.ndarray, List[float]]]`` , the linear coefficients array.\n
                ``constant`` : c, ``float`` , a constant.\n

    """

    def __init__(self, problem):
        pass

    def run(self, continue_times: int = 5, init_value=None, process_show=False):
        """
        Run the solver to find the minimum.

        Parameters
            continue_times : ``int``\n
                The maximum number of repeated searches at the current optimal point in GAS algorithm.
            init_value : ``float``\n
                The given initial value of the optimization function. Default the constant item of the problem.
            process_show : ``bool``\n 
                Set to True to print the detail during search.

        Returns
            minimum_indexes, minimum_res : ``list[list[int]]``, ``float``\n
                The optimization result including the solution array and the optimal value.

        Examples
            An example for minimization of quadratic binary function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2

        >>> from pyqpanda_alg.QFinance import QUBO
        >>> import sympy as sp
        >>> import numpy as np
        >>> import pyqpanda as pq
        >>> x0, x1, x2 = sp.symbols('x0 x1 x2')
        >>> function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2
        >>> # find the minimum function value using GAS
        >>> test1 = QUBO.QUBO_GAS_origin(function)
        >>> res1 = test1.run(init_value=0, continue_times=10, process_show=False)
        >>> print('result of Grover adaptive search: ', res1)
        result of Grover adaptive search:  ([[0, 1, 0]], -1.0)

        """
        pass


class QUBO_QAOA(QuadraticBinary):
    """
     .. math::
        \\
    Inheritance class of QuadraticBinary. Using QAOA to find the minimum value solution
    of given quadratic binary optimization problem.

    .. math::
        Q(x) = x^T A x + x^T b + c

    .. math::
        |x\\rangle_n |0\\rangle_m \mapsto |x\\rangle_n |(Q(x) + 2^m) \mod 2^m \\rangle_m

    According to the above formula, a negative value can also be represent by this
    method using two's complement.

    Parameters
        problem : ``sympy.Basic`` or ``dict``\n
            A quadratic form function with binary variables to be optimized. Support an expression in sympy.
            Keys followed should be included if expression in dict:
                ``quadratic`` : A, Optional ``[Union[np.ndarray, List[List[float]]]]``, the quadratic coefficients matrix.\n
                ``linear`` : b, Optional ``[Union[np.ndarray, List[float]]]``, the linear coefficients array.\n
                ``constant`` : c, ``float``, a constant.\n
    """

    def __init__(self, problem):
        pass

    def run(self, layer=None, optimizer='SLSQP', optimizer_option=None):
        """
        Run the solver to find the minimum.

        Parameters
            layer : ``int``\n
                Layers number of QAOA circuit.
                If optimize type is interp, then it represents the final layer of the optimization progress.
            optimizer : ``str``, ``optional``\n
                Type of solver. Should be one of

                    - ``SPSA`` : See :ref: ``<spsa.spsa_minimize>``\n
                    - one of  ``['Nelder-Mead', 'Powell', 'CG', 'BFGS', 'Newton-CG', 'TNC', 'COBYLA', 'SLSQP', 'trust-constr','dogleg', 'trust-ncg', 'trust-exact', 'trust-krylov']``. See ``scipy.optimize.minimize``.

                If not given, default by ``SLSQP``.
            optimizer_option : ``dict``, ``optional``\n
                A dictionary of solver options. Accept the following generic options:\n
                    - bounds : ``List[tuple]``, ``optional``\n
                        Bounds for the variables. Sequence of ``(min, max)`` pairs for each element in `x`.
                        If specified, variables are clipped to fit inside the bounds after each iteration.
                        None is used to specify no bound.
                    - options : ``int``\n
                        Maximum number of iterations to perform. Depending on the
                        method each iteration may use several function evaluations.

                        For `TNC` use `maxfun` instead of `maxiter`.

        Returns
            qaoa_result : ``list[tuple]``\n
                List of all possible solutions with corresponding probabilities.
                The solution of the problem we are looking for should generally be the maximum probability.

        Examples
            An example for minimization of quadratic binary function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2

        >>> from pyqpanda_alg.QFinance import QUBO
        >>> import sympy as sp
        >>> import numpy as np
        >>> import pyqpanda as pq
        >>> x0, x1, x2 = sp.symbols('x0 x1 x2')
        >>> function = -0.5 * x0 * x1 - 0.7 * x0 * x1 + 0.9 * x1 * x2 + 1.3 * x0 - x1 - 0.5 * x2
        >>> # find the minimum function value using QAOA
        >>> test2 = QUBO.QUBO_QAOA(function)
        >>> res2 = test2.run(layer=5, optimizer='SLSQP',
        >>>                  optimizer_option={'options':{'eps':1e-3}})
        >>> print('result of QAOA: ', res2)
        result of QAOA:  {'000': 0.0004125955977882364, '001': 0.020540129989231624, '010': 0.9152063391500159, '011': 0.003439453872904533, '100': 6.389251180087758e-05, '101': 0.0013381332738120826, '110': 0.034300546853266084, '111': 0.024698908751180276}

        """
        pass
