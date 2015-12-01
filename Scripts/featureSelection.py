import shutil
from config import conf
import numpy as np
import csv

def selectFeatures():
    print ">Select Features Executing"
    data = np.genfromtxt(conf['train']['feature_vector'],delimiter=',')
    data = np.delete(np.delete(data,0,1),0,0)  # remove the ID names and the feature names
    threshold = data.shape[0]

    if threshold/9 >= 40:   threshold = threshold - 20
    else:                   threshold = threshold - (threshold/(9*2))

    columns = (data == 0).sum(0)
    remove = np.where(columns>=threshold,True,False)
    arr = np.delete(remove,0)

    wr = csv.reader(open(conf['train']['feature_vector'],'r'))
    count = 0
    for line in wr:
        if count==0:
            testFeatures = line
            count +=1
        else:
            break

    shutil.copy(conf['train']['feature_vector'], conf['train']['copy_feature_vector'])

    del testFeatures[0:2]

    mask = np.array([np.logical_not(arr)])
    selectedFeatures = np.extract(np.logical_not(arr),testFeatures)
    wholeMask = np.repeat(mask,data.shape[0],axis=0)
    selectedData = np.extract(wholeMask,np.delete(data,0,1)).reshape(data.shape[0],len(selectedFeatures))
    featureHeader = ['Id','Class'] + selectedFeatures.tolist()
    read = csv.reader(open(conf['train']['labels'],'r'))

    writ = csv.writer(open(conf['train']['feature_vector'],'w+'))
    writ.writerow(featureHeader)
    count = 0
    for r in read:
        if count == 0:
            count +=1
            continue

        writeStuff = r + selectedData[count-1].tolist()
        count += 1
        writ.writerow(writeStuff)
    print ">Select Features Completed"