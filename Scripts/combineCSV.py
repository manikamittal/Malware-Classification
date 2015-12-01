import csv, os, glob,sys
from config import conf
from collections import OrderedDict

# combine the feature vectors csv of all training / testing files
def combineCSV(env):
    featureVectorLoc = conf[env]['feature_vector']
    csvDirectory = os.path.dirname(featureVectorLoc)
    counter = True  # only generate the new dictionary for 2nd feature csv file

    for name in glob.glob(csvDirectory + "/" + env + "Feature?.csv"):
        if os.path.basename(name) == env + 'Feature1.csv':
            r = csv.reader(open(name,'rb'))
            mainDict = OrderedDict((row[0], row[1:]) for row in r)
        else:
            r = csv.reader(open(name,'rb'))
            if counter:
                secondDict = dict({row[0]: row[1:] for row in r})
                counter = False
            else:
                for keys,values in dict({row[0]: row[1:] for row in r}).iteritems():
                    secondDict[keys].extend(values[0:])

    result = OrderedDict()
    for d in (mainDict, secondDict):
        for key, value in d.iteritems():
            result.setdefault(key, []).extend(value)

    # write the combine csb file to feature vector location
    with open(featureVectorLoc, 'w+') as f:
        w = csv.writer(f)
        for key, value in result.iteritems():
            w.writerow([key] + value)
