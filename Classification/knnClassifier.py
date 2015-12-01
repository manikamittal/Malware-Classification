import sys
sys.path.append("../Scripts")
from config import conf
from csvToArray import featureArray
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier

def knnClassifier():
    trainData, trainLabel = featureArray(conf['train']['feature_vector'])
    testData, testLabel = featureArray(conf['test']['feature_vector'])

    neigh = KNeighborsClassifier(n_neighbors=1, algorithm='auto', p=2)
    neigh.fit(trainData, trainLabel)
    print(neigh.score(testData,testLabel))


    neighRadius = RadiusNeighborsClassifier(radius=500, weights='distance',algorithm='auto', p=2,metric='minkowski')
    neighRadius.fit(trainData, trainLabel)
    print(neighRadius.score(testData, testLabel))


knnClassifier()