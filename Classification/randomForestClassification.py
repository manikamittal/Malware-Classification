import sys
sys.path.append("../Scripts")
from config import conf
from csvToArray import featureArray
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

def randomForestClassify():
    trainData, trainLabel = featureArray(conf['train']['feature_vector'])
    testData, testLabel = featureArray(conf['test']['feature_vector'])

    print "RANDOM FOREST"
    for value in xrange(1,50):
        clf = RandomForestClassifier(n_estimators = value,criterion='entropy')
        clf = clf.fit(trainData,trainLabel)
        print str(value) + " " + str(clf.score(testData,testLabel))

    print ""
    print "GRADIENT BOOSTING"
    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(trainData, trainLabel)
    print str(clf.score(testData,testLabel))

randomForestClassify()