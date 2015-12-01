import sys
sys.path.append("../Scripts")
from config import conf
from csvToArray import featureArray
from sklearn.svm import NuSVC

trainData, trainLabel = featureArray(conf['train']['feature_vector'])
testData, testLabel = featureArray(conf['test']['feature_vector'])

# gamma = [4**(-7),4**(-6),4**(-5),4**(-4),4**(-3),4**(-2),4**(-1),4**(0),4**(1),4**(2),4**(3),4**(4),4**(5),4**(6),4**(7)]

print "Nu- SUPPORT VECTOR CLASSIFICATION"
def svmClassifier():
    for deg in xrange(1,200):
        print deg
        print "RBF Nu-SVC"
        clf = NuSVC(gamma=deg)
        clf.fit(trainData, trainLabel)
        print(clf.score(testData,testLabel))

        print "LINEAR Nu-SVC"
        clf = NuSVC(kernel="linear")
        clf.fit(trainData, trainLabel)
        print(clf.score(testData,testLabel))

        print "POLYNOMIAL Nu-SVC"
        clf = NuSVC(kernel="poly",gamma=deg)
        clf.fit(trainData, trainLabel)
        print(clf.score(testData,testLabel))

        print "SIGMOID Nu-SVC"
        clf = NuSVC(kernel="sigmoid",gamma=deg)
        clf.fit(trainData, trainLabel)
        print(clf.score(testData,testLabel))

svmClassifier()