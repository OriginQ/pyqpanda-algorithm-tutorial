"""
Simultaneous Perturbation Stochastic Approximation

"""
import numpy as np
from .. config import *
auth = Authorization()


def spsa_minimize(func, x0, args=(), tol=None, bounds=None, callback=None, **options):
    """
    Simultaneous Perturbation Stochastic Approximation (SPSA) algorithm of two-measurement.
    Stochastic Approximation (SA) is a class of theories for noisy function optimization.
    SPSA, proposed by J.C. Spall around 1991, requires only two evaluation of
    the objective function in each iteration.
    This function provides a simple approach for two-measurement SPSA method.

    Parameters
        func : ``callable``\n
            The objective function to be optimized.
            ``fun(x, *args) -> float``
            where ``x`` is a 1-D array with shape (n,).
            It is warned that we do not check with the return
            type of func to ensure a minimum query to
            the objective function.
        x0 : ``ndarray``, shape (n,)\n
            Initial guess. Array of real elements of size (n,),
            where ``n`` is the number of independent variables.
        args : ``tuple``, ``optional``\n
            Extra arguments passed to the objective function.
        tol : ``float``, ``optional``\n
            Tolerance for termination. Algorithm stops when gradient lies between
            the range of the specified tolerance. Otherwise, it stops until
            the maximum iteration is reached.
        bounds : ``List[tuple]``, ``optional``\n
            Bounds for the variables. Sequence of ``(min, max)`` pairs for each element in `x`.
            If specified, variables are clipped to fit inside the bounds after each iteration.
            None is used to specify no bound.
        callback : ``callable``, ``optional``\n
            Called after each iteration.
            ``callback(xk)``
            where ``xk`` is the current parameter vector.
        options : ``dict``, ``optional``\n
            A dictionary of parameter options. See details in Notes.

    Return
        x : ``ndarray``, shape (n,)\n
            Optimized variables.

    Raises
        ValueError\n
            If any parameter ``a, c, alpha, gamma, A`` is too small  :math:`(< 1e-8)`
            or less than  :math:`0`.
        TypeError\n
            If the user-provided objective function return a non-scalar value.

    Notes
        The update rule for SPSA is:\n  
             :math:`\\vec x_{k+1}=\\vec x_{k}-\\frac{a_{k}}{c_{k}}\cdot\\frac{[f(\\vec x_k+c_k\\vec b)-f(\\vec x_k-c_k\\vec b)]}{2\\vec b}` 
        where b is uniformly chosen from {-1, 1} (symmetric Bernoulli perturbation).
        The learning rate a(k) is defined as\n
           :math:`a(k) = \\frac{a}{(A + k + 1) ^ {\\alpha}}`
        The perturbation strength is defined as\n
           :math:`c(k) = \\frac{c}{(k + 1) ^ {\gamma}}`

        The ``option`` dictionary includes following parameters:\n
             :math:`maxiter` : ``int``\n
                Maximum iteration after which the algorithm stops.\n
             :math:`a` : ``float``, a > 0\n
                Learning rate amplitude. A value between 0 and 1 is recommended.\n
             :math:`c` : ``float``, c > 0\n
                Perturbation strength. A value between 0 and 1 is recommended.\n
             :math:`alpha` : ``float``, alpha > 0\n
                Scaling of learning rate on the round of iteration.\n
             :math:`gamma` : ``float``, gamma > 0\n
                Scaling of perturbation strength on the round of iteration.\n
             :math:`A` : ``int``, ``float``, A > 0\n
                Modification of learning rate scaling. It is recommended to be about maxiter / 10.\n

    Reference
        [1] Spall J C.\n
            Multivariate stochastic approximation using a simultaneous perturbation gradient approximation[J].
            IEEE transactions on automatic control, 1992, 37(3): 332-341.
            https://doi.org/10.1109/9.119632\n
        [2] Spall J C.\n
            Implementation of the simultaneous perturbation algorithm for stochastic optimization[J].
            IEEE Transactions on aerospace and electronic systems, 1998, 34(3): 817-823.
            https://doi.org/10.1109/7.705889\n

    Example
        Suppose we are going to minimize a function:\n
         :math:`f(x) = x^2 + N(0, 1)`
        where  :math:`N(0, 1)` is Gaussian noise. Each query of  :math:`f(x)` contains an
        unavoidable perturbation. We consider a dimension of  :math:`4` and given
        an initial guess  :math:`x = (1, 2, 3, 4)`.

    .. code-block:: python

        from pyqpanda_alg.QAOA.spsa import spsa_minimize
        from scipy.optimize import minimize
        import numpy as np

        class NoiseF:
            def __init__(self):
                self.eval = 0
                self.history = []

            def eval_f(self, x):
                self.eval += 1
                return np.linalg.norm(x**2 + np.random.normal(0, 1, size=len(x)))

            def record(self, x):
                self.history.append([np.linalg.norm(x) / len(x), self.eval])

        x0 = np.array([1, 2, 3, 4])
        noise_f = NoiseF()

        # SLSQP, a typical gradient-based algorithm
        print('SLSQP results')
        scipy_dict = {'method': 'SLSQP', 'callback': noise_f.record}
        minimize(noise_f.eval_f, x0, **scipy_dict)
        print('Norm    Evaluation')
        for nx, count in noise_f.history:
            print('{:<12f} {:d}'.format(nx, count))

        # SPSA
        print('SPSA results')
        noise_f.eval = 0  # reset evaluation count
        noise_f.history = []
        spsa_minimize(noise_f.eval_f, x0, callback=noise_f.record)
        print('Norm    Evaluation')
        for nx, count in noise_f.history:
            print('{:<12f} {:d}'.format(nx, count))

    The given example would return results like (results may vary
    due to random number generator):

    .. parsed-literal::
        SLSQP results
        Norm    Evaluation
        414.201381   6
        700.681984   21
        93280.595475 36
        ...
        9.587875     196
        SPSA results
        Norm    Evaluation
        0.572110     2
        0.309455     4
        ...
        0.077685     196
        0.098687     198
        0.103702     200

    It indicates that gradient based optimization algorithms
    suffer greatly from unavoidable noise. On the other hand,
    SPSA could provide reliable performance and less query
    call to the objective function.

    """
    pass
