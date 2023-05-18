import numpy as np
from pyqpanda import *
import pyqpanda as pq

from .. config import *
auth = Authorization()

class QuantumKernel_vqnet:
    """
    A help class to create Quantum Kernal Matrix.The evaluate function can be used in ``sklearn.svm`` .
    
    Parameters
            batch_size: ``int``\n
                Data number to build quantum kernel, default: 100.
            n_qbits: ``int``\n
                number of quantum bits.
    """

    def __init__(
            self,
            batch_size: int = 100,
            n_qbits=None,
    ) -> None:
        pass

    def evaluate(self, x_vec: np.ndarray, y_vec: np.ndarray = None) -> np.ndarray:
        """
        Evaluation function to build quantum kernel.

        Parameters
            x_vec: ``ndarray``\n
                Train or test dataset features.
            y_vec: ``ndarray``\n
                Train or test dataset labels.

        Returns
            out: ``ndarray``\n
                Kernal matrix.

        Examples
            .. code-block:: python

                import os
                import numpy as np
                import pyqpanda as pq
                from sklearn.svm import SVC
                import matplotlib
                try:
                    matplotlib.use('TkAgg')
                except:
                    pass
                import matplotlib.pyplot as plt


                from pyqpanda_alg.QSVM.quantum_kernel_svm import QuantumKernel_vqnet

                from pyqpanda_alg import QSVM
                data_path = QSVM.__path__[0]


                def _read_vqc_qsvm_data(path):
                    train_features = np.loadtxt(os.path.join(path, "dataset/qsvm_train_features.txt"))
                    test_features = np.loadtxt(os.path.join(path, "dataset/qsvm_test_features.txt"))
                    train_labels = np.loadtxt(os.path.join(path, "dataset/qsvm_train_labels.txt"))
                    test_labels = np.loadtxt(os.path.join(path, "dataset/qsvm_test_labels.txt"))
                    samples = np.loadtxt(os.path.join(path, "dataset/qsvm_samples.txt"))
                    return train_features, test_features, train_labels, test_labels, samples
                def qsvm_classification():
                    train_features, test_features, train_labels, test_labels, samples = _read_vqc_qsvm_data(data_path)
                    plt.figure(figsize=(5, 5))
                    plt.ylim(0, 2 * np.pi)
                    plt.xlim(0, 2 * np.pi)
                    plt.imshow(
                        np.asmatrix(samples).T,
                        interpolation="nearest",
                        origin="lower",
                        cmap="RdBu",
                        extent=[0, 2 * np.pi, 0, 2 * np.pi],
                    )

                    plt.scatter(
                        train_features[np.where(train_labels[:] == 0), 0],
                        train_features[np.where(train_labels[:] == 0), 1],
                        marker="s",
                        facecolors="w",
                        edgecolors="b",
                        label="A train",
                    )
                    plt.scatter(
                        train_features[np.where(train_labels[:] == 1), 0],
                        train_features[np.where(train_labels[:] == 1), 1],
                        marker="o",
                        facecolors="w",
                        edgecolors="r",
                        label="B train",
                    )
                    plt.scatter(
                        test_features[np.where(test_labels[:] == 0), 0],
                        test_features[np.where(test_labels[:] == 0), 1],
                        marker="s",
                        facecolors="b",
                        edgecolors="w",
                        label="A test",
                    )
                    plt.scatter(
                        test_features[np.where(test_labels[:] == 1), 0],
                        test_features[np.where(test_labels[:] == 1), 1],
                        marker="o",
                        facecolors="r",
                        edgecolors="w",
                        label="B test",
                    )

                    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0.0)
                    plt.title("samples dataset for classification")

                    plt.show()
                    samples_datasets_kernel = QuantumKernel_vqnet(n_qbits=2)
                    samples_datasets_svc = SVC(kernel=samples_datasets_kernel.evaluate)
                    samples_datasets_svc.fit(train_features, train_labels)
                    samples_datasets_score = samples_datasets_svc.score(test_features, test_labels)

                    print(f"Callable kernel classification test score: {samples_datasets_score}")

                    samples_datasets_matrix_train = samples_datasets_kernel.evaluate(x_vec=train_features)
                    samples_datasets_matrix_test = samples_datasets_kernel.evaluate(x_vec=test_features, y_vec=train_features)

                    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
                    axs[0].imshow(
                        np.asmatrix(samples_datasets_matrix_train), interpolation="nearest", origin="upper", cmap="Blues"
                    )
                    axs[0].set_title("samples training kernel matrix")
                    axs[1].imshow(np.asmatrix(samples_datasets_matrix_test), interpolation="nearest", origin="upper", cmap="Reds")
                    axs[1].set_title("samples testing kernel matrix")
                    plt.show()


                if __name__ == "__main__":
                    qsvm_classification()

        """
        pass
