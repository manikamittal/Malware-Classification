import os, sys
import csv
import time
from config import conf, asmInstrSet

# counts the number of occurrences of assembly instructions & {'??','00'} in .bytes
def countInstructions(env):
    timeStart = time.time()
    print ">Assembly Features Calculation for - " + str(env)
    reader = csv.DictReader(open(conf[env]['labels']), fieldnames=['Id','Class'])
    instrFeatureLoc = os.path.join(conf['script']['script_loc'], "Data", "CSV Files", env + "Feature1.csv")

    fieldNames = ['ID','Class'] + list(asmInstrSet) + ['00', '??']
    wr = csv.DictWriter(open(instrFeatureLoc, 'w+'), fieldnames=fieldNames)
    wr.writeheader()

    for value in reader:
        if value['Id'] == 'Id':
            continue
        pathASM = os.path.join(conf[env]['file_loc'],value['Id'] + ".asm")
        pathByte = os.path.join(conf[env]['file_loc'],value['Id'] + ".bytes")
        instrFeature = dict(zip(asmInstrSet, [0] * len(asmInstrSet)))
        instrFeature.update({'ID': value['Id'], '00': 0, '??': 0, 'Class':value['Class']})
        for line in open(pathASM, 'r'):
            if ';' not in line:
                for key in asmInstrSet:
                    if key in line:
                        instrFeature[key] += 1
        for line in open(pathByte, 'r'):
            instrFeature['00'] += line.count('00')
            instrFeature['??'] += line.count('??')

        wr.writerow(instrFeature)

    timeStop = time.time()
    print ">Time Elapsed : " + str(timeStop - timeStart)
    print ">Assembly Features Calculated for - " + str(env)
