import os
import csv
from datetime import datetime

__location__ = os.path.dirname(os.path.realpath(__file__))
inputDir = os.path.join(__location__, "input")
outputDir = os.path.join(__location__, "output.csv")

filesOut = [["Filename", "MTime", "ATime", "CTime", "Bytes"]]

for root, dirs, files in os.walk(inputDir):
	for filename in files:
		file = os.path.join(root, filename)
		
		
		
		mtime = str(datetime.fromtimestamp(os.path.getmtime(file)))
		ctime = str(datetime.fromtimestamp(os.path.getctime(file)))
		atime = str(datetime.fromtimestamp(os.path.getatime(file)))
		
		fileData = [filename, mtime, atime, ctime, str(os.path.getsize(file))]
		
		filesOut.append(fileData)
		
with open(outputDir, "wb") as f:
    writer = csv.writer(f)
    writer.writerows(filesOut)