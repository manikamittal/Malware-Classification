import os,sys,csv
import shutil
from collections import Counter
from config import conf

# get class labels from csv file
def getClassLabels():
    reader = csv.reader(open(conf['script']['labels'],'rb'))
    trainLabels = {}

    for row in reader:
        key = row[0]
        if key in trainLabels:
            pass
        trainLabels[key] = row[1]
    del trainLabels['Id']
    return trainLabels

# count occurrence of various classes
def countOfFiles(trainLabels):
    return dict(Counter(trainLabels.values()))

# half file count to separate training and testing evenly
def copyNFiles(fileCount, env):
    for keys in fileCount.keys():
        if fileCount[keys] > env * 3:
            fileCount[keys] = env * 3

    return fileCount

# get list of file names for training and testing data
def getFilesName(labels, fileCount):
    trainLabels = []
    validLabels = []
    testLabels = []
    tempFileCount = fileCount.copy()

    for keys in labels.keys():

        fileClass = labels[keys]
        if fileCount[fileClass] > (tempFileCount[fileClass] / 3) * 2 :
            trainLabels.append(keys)
            fileCount[fileClass] -= 1
        elif (fileCount[fileClass] <= (tempFileCount[fileClass] / 3) * 2) and (fileCount[fileClass] > tempFileCount[fileClass] / 3):
            testLabels.append(keys)
            fileCount[fileClass] -= 1
        elif (fileCount[fileClass] > 0) and (fileCount[fileClass] <= tempFileCount[fileClass] / 3):
            validLabels.append(keys)
            fileCount[fileClass] -= 1
        else:
            pass

    return trainLabels, validLabels, testLabels

# create train & test labels
def createLabelsCSV(labels, trainLabels, testLabels, validLabels):
    trainLabelsLoc = open(conf['train']['labels'], 'w+')
    testLabelsLoc = open(conf['test']['labels'], 'w+')
    validLabelsLoc = open(conf['valid']['labels'], 'w+')

    tr = csv.DictWriter(trainLabelsLoc, fieldnames=['Id','Class'])
    tr.writeheader()

    te = csv.DictWriter(testLabelsLoc, fieldnames=['Id','Class'])
    te.writeheader()

    tv = csv.DictWriter(validLabelsLoc, fieldnames=['Id','Class'])
    tv.writeheader()

    for value in trainLabels:
        entry = dict({'Id':value, 'Class':labels[value]})
        tr.writerow(entry)

    for value in testLabels:
        entry = dict({'Id':value, 'Class':labels[value]})
        te.writerow(entry)

    for value in validLabels:
        entry = dict({'Id':value, 'Class':labels[value]})
        tv.writerow(entry)

def makeDataFolders():
    if not os.path.exists(conf['train']['file_loc']):
        os.makedirs(conf['train']['file_loc'])

    if not os.path.exists(conf['test']['file_loc']):
        os.makedirs(conf['test']['file_loc'])

    if not os.path.exists(conf['valid']['file_loc']):
        os.makedirs(conf['valid']['file_loc'])

# copy files from the external hard disk to the local hard disk
def copyFilesOver(labels, env, bef1, bef2):
    for files in labels:
        asmPath = os.path.join(conf['script']['externalFiles'], files + ".asm")
        bytePath = os.path.join(conf['script']['externalFiles'], files + ".bytes")

        copyASMLocation = os.path.join(conf[env]['file_loc'], files + ".asm")
        copyByteLocation = os.path.join(conf[env]['file_loc'], files + ".bytes")

        befASMLocation = os.path.join(conf[bef1]['file_loc'], files + ".asm")
        befByteLocation = os.path.join(conf[bef1]['file_loc'], files + ".bytes")

        bef2ASMLocation = os.path.join(conf[bef2]['file_loc'], files + ".asm")
        bef2ByteLocation = os.path.join(conf[bef2]['file_loc'], files + ".bytes")


        if os.path.exists(befASMLocation) and os.path.exists(befByteLocation):
            shutil.move(befASMLocation,copyASMLocation)
            shutil.move(befByteLocation,copyByteLocation)
        elif os.path.exists(bef2ASMLocation) and os.path.exists(bef2ByteLocation):
            shutil.move(bef2ASMLocation,copyASMLocation)
            shutil.move(bef2ByteLocation,copyByteLocation)
        elif os.path.exists(copyASMLocation) and os.path.exists(copyByteLocation):
            pass
        else:
            shutil.copy(asmPath,copyASMLocation)
            shutil.copy(bytePath,copyByteLocation)


def checkForCommons(trainLabels, testLabels, validLabels):
    if set(trainLabels).intersection(set(testLabels)) == [] or set(testLabels).intersection(set(validLabels)) == []:
        print ">Common Files, Exiting."
        exit()

def main(env):
    classLabels = getClassLabels()
    fileCount = countOfFiles(classLabels)
    copyFileCount = copyNFiles(fileCount, int(env))

    trainLabels, validLabels, testLabels = getFilesName(classLabels, copyFileCount)

    print ">Training Data Files: " + str(len(trainLabels))
    print ">Valid Data Files: " + str(len(validLabels))
    print ">Testing Data Files: " + str(len(testLabels))
    createLabelsCSV(classLabels, trainLabels, testLabels, validLabels)

    checkForCommons(trainLabels,testLabels,validLabels)

    print ">Training, Valid & Testing Labels Created."
    makeDataFolders()
    print ">Training, Validation & Testing Data Folder Created."
    copyFilesOver(trainLabels,'train','test', 'valid')
    print ">Training Files Copied."
    copyFilesOver(validLabels,'valid','train', 'test')
    print ">Validation Files Copied."
    copyFilesOver(testLabels,'test','train', 'valid')
    print ">Testing Files Copied."

if __name__ == "__main__":
    main(sys.argv[1])
