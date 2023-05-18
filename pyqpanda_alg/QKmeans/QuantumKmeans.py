import numpy as np
from copy import deepcopy
from numpy import pi
import pyqpanda as pq
from pyqpanda import *

from .. config import *
auth = Authorization()


class QuantumKmeans:
    """
    QKMeans (Quantum K-Means) is a quantum algorithm that is used for clustering data into k clusters. 
    
    Parameters:
            k: ``int``\n
                k is a user-specified parameter.

    """
    def __init__(self, k=2, tol=0.01):
        pass

    def fit(self, data):
        """
        Classify the input data.

        Parameters:
            data: ``ndarray``\n
                Input array, can be complex.

        Returns:
            centers_new: ``int``\n
                      Cluster center of input data.
            clusters: ``int``\n
                   Category number of the entered data.

        Examples
            .. code-block:: python

                import os
                import numpy as np
                import matplotlib.pyplot as plt
                from sklearn.cluster import KMeans
                from sklearn.preprocessing import MinMaxScaler
                from pyqpanda_alg.QKmeans.QuantumKmeans import QuantumKmeans
                from pyqpanda_alg import QKmeans


                def ReadCSV(path):
                    import csv
                    csvFile = open(path, "r")
                    reader = csv.reader(csvFile)
                    data = []
                    label = []
                    for item in reader:
                        data0 = []
                        if reader.line_num == 1:
                            continue
                        for i in range(1, 5):
                            data0.append(np.float64(item[i]))
                        data.append(data0)
                        label.append(item[5])
                    csvFile.close()
                    return np.array(data), label


                if __name__ == '__main__':
                    data_path = QKmeans.__path__[0]
                    data_file = os.path.join(data_path, 'dataset/Iris.csv')
                    data, label = ReadCSV(data_file)
                    data = data[:, 2:]
                    label = [i for i in label]
                    for _ in range(len(label)):
                        if label[_] == 'Iris-setosa':
                            label[_] = 'r'
                        elif label[_] == 'Iris-versicolor':
                            label[_] = 'b'
                        else:
                            label[_] = 'g'
                    rows, col = data.shape[0], data.shape[1]

                    scaler = MinMaxScaler(feature_range=(-1, 1))
                    data = scaler.fit_transform(data)

                    n_clusters = 3
                    Colors = ['black', 'blue', 'green', 'yellow', 'red', 'purple', 'orange', 'brown', 'pink']

                    print('Classical K_means start...')
                    Ctest = KMeans(n_clusters)
                    Ctest.fit(data)
                    Ccenter = Ctest.cluster_centers_
                    print('Final Classical Result:', Ccenter)

                    print('Quantum K_means start...')
                    Qtest = QuantumKmeans(n_clusters)
                    Qcenters, clusters = Qtest.fit(data)
                    print('Final Quantum Result:', Qcenters)

                    x0 = data[clusters == 0]
                    x1 = data[clusters == 1]
                    x2 = data[clusters == 2]
                    plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')
                    plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')
                    plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')

                    plot_title = 'Iris Quantum K_means Result'
                    plt.title(plot_title)
                    plt.show()
        """
        pass
