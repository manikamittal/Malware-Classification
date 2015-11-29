import pylab as pl
import matplotlib.pyplot as plt
import numpy as np

def plotAccuracy(accuracy):
    jet = plt.get_cmap('jet')
    N = len(accuracy)
    plt.bar(range(N), accuracy.values(), align='center', width=0.5,color=jet(np.linspace(0, 1.0, N)))
    X = np.arange(len(accuracy))
    pl.xticks(X, accuracy.keys(),rotation=90)
    ymax = max(accuracy.values()) + 1
    plt.legend(prop={'size': 10})
    plt.title("Classification Accuracy")
    plt.xlabel("Classifier")
    plt.ylabel("Accuracy")
    plt.show()



