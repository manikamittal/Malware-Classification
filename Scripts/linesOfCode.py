import os,sys
from config import conf
import csv

globalSectionDict = {}

# Calls the function countLines on all files of the directory
def getFile(dirName):
    for _, _, files in os.walk(dirName):
        for f in files:
            print f
            print countLines(os.path.join(dirName, f))


# Counts the number of lines in a file
def countLines(fileOpen):
    fileLines = fileOpen.readlines()
    return sum(1 for line in fileLines)


# Adds unique words with their counts to dictionary
def addToDictionary(dictionary, key):
    if dictionary.has_key(key):
        dictionary[key] += 1
    else:
        dictionary[key] = 1


# Counts unique sections
def countSections(fileName,env):
    sectionCountDict = {}
    fileAsmName = os.path.join(conf[env]['file_loc'],fileName)+ ".asm"
    fileAsmOpen = open(fileAsmName, "r")
    fileAsmOpen2 = open(fileAsmName, "r")
    fileByteName = os.path.join(conf[env]['file_loc'],fileName)+ ".bytes"
    fileByteOpen = open(fileByteName, "r")
    fileLines = fileAsmOpen2.readlines()

    testFeatures = []
    sabFeatures =[]
    assemblyFeature = []

    if env=="test" or env=="valid":
        fieldNamesLoc = conf['train']['feature_vector']
        wr = csv.reader(open(fieldNamesLoc,'r'))
        count = 0
        for line in wr:
            if count == 0:
                sabFeatures = line
                count +=1
            else:
                break
        assemblyFeaturesLoc = conf['script']['script_loc'] + "/Data/CSV Files/" + "trainFeature1.csv"
        wr = csv.reader(open(assemblyFeaturesLoc,'r'))
        count = 0
        for line in wr:
            if count == 0:
                assemblyFeature = line
                count +=1
            else:
                break
        testFeatures = set(sabFeatures).difference(set(assemblyFeature))

    for eachLine in fileLines:
        if ":" in eachLine:
            if (env=="test" or env=="valid") and eachLine.split(":")[0] in testFeatures:
                addToDictionary(sectionCountDict, eachLine.split(":")[0])
            elif env=="train":
                addToDictionary(sectionCountDict, eachLine.split(":")[0])

    sectionCountDict["LOC-asm"] = countLines(fileAsmOpen)
    sectionCountDict["fileSize-asm"] = os.path.getsize(fileAsmName)
    sectionCountDict["LOC-byte"] = countLines(fileByteOpen)
    sectionCountDict["fileSize-byte"] = os.path.getsize(fileByteName)
    globalSectionDict[fileName] = sectionCountDict


# Creates csv from a dictionary
def createCsvFromDict(env):
    countFeatureLoc = conf['script']['script_loc'] + "/Data/CSV Files/" + env + "Feature2.csv"
    fieldNames = set()

    for value in globalSectionDict.values():
        fieldNames.update(value.keys())
    fieldNames = ['ID'] + list(sorted(fieldNames))

    wr = csv.DictWriter(open(countFeatureLoc, 'w+'), fieldnames=fieldNames)
    wr.writeheader()

    for (key,value) in globalSectionDict.iteritems():
        countFeature = dict(zip(fieldNames, [0] * len(fieldNames)))
        countFeature.update({'ID': key})
        countFeature.update(value)
        wr.writerow(countFeature)

def main(env):
    csvReader = csv.DictReader(open(conf[env]['labels']), fieldnames=['Id','Class'])
    globalSectionDict.clear()
    print ">Executing Lines of Code - " + env
    for eachRow in csvReader:
        if eachRow['Id']=='Id':
            continue
        countSections(eachRow['Id'],env)
    createCsvFromDict(env)
    print ">Completed Lines of Code - " + env

if __name__ == "__main__":
    main(sys.argv[1])
