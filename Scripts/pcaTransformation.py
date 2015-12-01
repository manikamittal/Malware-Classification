from config import conf
import numpy as np
from sklearn.decomposition import PCA

def featureArray1(featureCSV):
    data = np.genfromtxt(featureCSV,delimiter=',')
    data = np.delete(np.delete(data,0,1),0,0)  # remove the ID names and the feature names
    return (np.delete(data,0,1),data[:,0])  # return data and labels


def pcaTransformation():
    trainData, trainLabel = featureArray1("/Users/manikamittal/PycharmProjects/Malware-Classification/trainFeatures.csv")
    print(trainData.shape)
    pca = PCA(n_components=2)
    pca.fit(trainData)
    print(trainData.shape)
    trainData = pca.transform(trainData)
    print(trainData.shape)
pcaTransformation()