import os
import math
import numpy as np
import pyqpanda.pyQPanda as pq
from itertools import chain
from pyqpanda import *

from .. config import *
auth = Authorization()

class QuantumAssociationRulesMining:
    """
    Association rule mining finds interesting associations or correlations between item sets in
    a large amount of data . Mining the implicit relationship between objects from large-scale
    data is called association analysis or association rule learning, which can reveal the hidden
    association pattern in data and help people to carry out market operation and decision support.
    For example, on the same trip to the supermarket, if the customer buys milk, what is the
    likelihood that he will also buy bread?

    Based on the famous classical association rule mining algorithm Apriori algorithm,
    a quantum association rule mining algorithm is proposed to realize the core task.
    Specifically, given a quantum black box accessing a trading database,
    the algorithm first uses the quantum parallel amplitude estimation algorithm
    to estimate the support of all candidate K term sets in a quantum parallel manner,
    and store it in a quantum superposition state.  Next, the quantum amplitude
    amplification algorithm is used to search the candidate K term sets that are not
    less than the predetermined threshold from the superposition quantum states.

    Parameters
        transaction_data: ``list``\n
            The input datasets,you can prepare TXT documents.There are
            several lines in the document,each column is separated by a comma.
            Each element represents an associated thing.
            
        min_support: ``float``\n
            Minimum support, a hyper parameter,the value ranges from 0 to 1.
            The default minimum support is set to 0.2

        min_conf: ``float``\n
            Minimum confidence,a hyper parameter,the value ranges from 0 to 1.
            The default minimum confidences set to 0.3

    """
    def __init__(self, transaction_data, min_support=0.2, min_conf=0.3):
        pass

    def run(self, show=None, file_name="", machine_type="CPU", **kwargs):
        """
        Parameters:
            show: ``string``\n
                Enumeration of the circuit show type,should be one of"None", "Picture"and"OriginIR"\n
                - None : no output;\n
                - Picture : Console output the quantum circuit,output default file name;\n
                - OriginIR : Console does not output,output the IR of the circuit.\n

            file_name: ``string``\n
                the output file namethat record the circuit information.

            machine_type: ``string``\n
                enumeration of QVM type, should be one of "CPU", and "QCloud"

            **kwargs: ``dict args``\n
                Use keywords to pass parameters,the twoparameters areapi_keyand ip_compute.\n
                - api_key : API key of the local platform account\n
                - ip_compute : The IP address of the local request computing task\n

        Returns:
            out: ``dict``\n
                confidence result

        Examples
            .. code-block:: python

                import os
                from pyqpanda_alg.QARM.qarm import QuantumAssociationRulesMining
                from pyqpanda_alg import QARM


                def read(file_path):
                    if os.path.exists(file_path):
                        trans_data = []
                        with open(file_path, 'r', encoding='utf8') as f:
                            data_line = f.readlines()
                            if data_line:
                                for line in data_line:
                                    if line:
                                        data_list = line.strip().split(',')
                                        trans_data.append([data.strip() for data in data_list])
                            else:
                                raise ValueError("The file {} has no any data!".format(file_path))
                    else:
                        raise FileNotFoundError('The file {} does not exists!'.format(file_path))
                    return trans_data


                if __name__ == '__main__':
                    data_path = QARM.__path__[0]
                    data_file = os.path.join(data_path, 'dataset/data2.txt')
                    trans_data = read(data_file)
                    support = 0.2
                    conf = 0.5
                    qarm = QuantumAssociationRulesMining(trans_data, support, conf)
                    result = qarm.run()
                    print(result)
        """
        pass
