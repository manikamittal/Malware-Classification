import os

parentFolder = os.path.dirname(os.path.normpath(os.getcwd()))

conf = {
    'train': {
        'file_loc': os.path.join(parentFolder, "Data", "Training Data"),
        'feature_vector': os.path.join(parentFolder, "Data", "CSV Files", "trainFeatures.csv"),
        'labels': os.path.join(parentFolder, "Data", "CSV Files", "trainLabels.csv"),
        'copy_feature_vector': os.path.join(parentFolder,"Data","Feature Copy", "trainFeatures.csv")
    },
    'test': {
        'file_loc': os.path.join(parentFolder, "Data", "Testing Data"),
        'feature_vector': os.path.join(parentFolder, "Data", "CSV Files", "testFeatures.csv"),
        'labels': os.path.join(parentFolder, "Data", "CSV Files", "testLabels.csv")
    },
    'valid': {
        'file_loc': os.path.join(parentFolder, "Data", "Validation Data"),
        'feature_vector': os.path.join(parentFolder, "Data", "CSV Files", "validFeatures.csv"),
        'labels': os.path.join(parentFolder, "Data", "CSV Files", "validLabels.csv")
    },
    'script': {
        'script_loc': parentFolder,
        'labels': os.path.join(parentFolder,"Data", "CSV Files" , "allTrainLabels.csv"),
        'externalFiles' : os.path.normpath('/Volumes/TOSHIBA EXT/Machine Learning Project/train'),
    }
}

asmInstrSet = set(['mov','xchg','stc','clc','cmc','std','cld','sti','cli','push',
	'pushf','pusha','pop','popf','popa','cwd','cwde','in','out',
	'add','adc','sub','sbb','div','idiv','mul','imul','inc','dec',
	'cmp','sal','sar','rcl','rcr','rol','ror','neg','not','and',
	'or','xor','shl','shr','nop','lea','int','call','jmp',
	'je','jz','jp','ja','jb','jbe',
    'jnb','ret','jnz','jecxz',
	'jnp','jg','jge','jl','jle',
	'jo','jno','js','jns'])