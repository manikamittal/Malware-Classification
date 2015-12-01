import sys
sys.path.append("../Scripts")
from config import conf
from csvToArray import featureArray
from sklearn.svm import LinearSVC

def linearSVCClass():
    trainData, trainLabel = featureArray(conf['train']['feature_vector'])
    testData, testLabel = featureArray(conf['test']['feature_vector'])

    print "Linear SVC"
    clf = LinearSVC(penalty='l2', loss='hinge', dual=True, tol=0.0001, C=1.0, multi_class='crammer_singer', fit_intercept=True, intercept_scaling=1, class_weight=None, verbose=0, random_state=None, max_iter=1000)
    clf = clf.fit(trainData,trainLabel)
    print str(clf.score(testData,testLabel))

linearSVCClass()