import glob,os
from config import conf
import subprocess
from assemblyFeatures import countInstructions
from linesOfCode import main
from combineCSV import combineCSV
from featureSelection import selectFeatures

env = ['train','valid','test']
if __name__ == "__main__":
    for field in env:
        featureVectorLoc = conf[field]['feature_vector']
        csvDirectory = os.path.dirname(featureVectorLoc)
        for name in glob.glob(csvDirectory + "/" + field + "Feature*.csv"):
            os.remove(name)

        countInstructions(field)
        main(field)
        combineCSV(field)
        if field == 'train':
            selectFeatures()

    subprocess.call("python classifications.py ", shell=True)