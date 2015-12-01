import sys
sys.path.append("../Scripts")
from config import conf
from csvToArray import featureArray
from sklearn import linear_model

def regression():
    trainData, trainLabel = featureArray(conf['train']['feature_vector'])
    testData, testLabel = featureArray(conf['test']['feature_vector'])

    print "RIDGE REGRESSION"
    clf = linear_model.Ridge (alpha = .5)
    clf = clf.fit(trainData,trainLabel)
    print str(clf.score(testData,testLabel))

    print("")
    print("LOGISTIC REGRESSION")
    clf = linear_model.LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='newton-cg', max_iter=100, multi_class='ovr', verbose=0, warm_start=False, n_jobs=2)
    clf = clf.fit(trainData,trainLabel)
    print str(clf.score(testData,testLabel))

