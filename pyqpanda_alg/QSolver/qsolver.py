from .. config import *
auth = Authorization()

def iter_sparse_mixed_subspace_solver(A,b,maxdim,iter_Kyrlov_subspace_pre):
    """
    The mixed HHL solver is an optimization of the HHL algorithm, which is mainly applied to solve large-scale linear equations, such as computational fluid dynamics.\n

    Parameters:
        :math:`A`: ``numpy.array`` \n
            represents the matrix ``A of Ax = b`` \n
        :math:`b` : ``List[float]`` \n
            represent the ``b of Ax = b`` \n
        maxdim : ``int``\n
            represent max dimension of Kyrlov subspace\n
        iter_Kyrlov_subspace_pre: ``double``\n
            represent min iterative residual error\n

    Return:
        solution x.\n

    Example:

    .. code-block:: python

        from pyqpanda_alg.QSolver.qsolver import iter_sparse_mixed_subspace_solver
        import numpy as np

        if __name__ == '__main__':

	        A = np.matrix([[1,0,0,0], [0,2,0,0],[0,0,2,0],[0,0,0,4]])
	        b = np.array([1,1,1,1]) 
	        result_x = iter_sparse_mixed_subspace_solver(A, b, 2, 1e-8)
	        print(result_x)

    The function above would give results:

    .. code-block:: python

        [0.999998561636645, 0.5000004774207323, 0.5000004774207323, 0.25000004284598887]

    """
    pass