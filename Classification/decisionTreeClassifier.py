import sys
sys.path.append("../Scripts")
from config import conf
from csvToArray import featureArray
from sklearn import tree

def decisionTreeClassifier():
    trainData, trainLabel = featureArray(conf['train']['feature_vector'])
    testData, testLabel = featureArray(conf['test']['feature_vector'])

    clf = tree.DecisionTreeClassifier(criterion='gini')
    clf.fit(trainData, trainLabel)
    print(clf.score(testData,testLabel))

decisionTreeClassifier()