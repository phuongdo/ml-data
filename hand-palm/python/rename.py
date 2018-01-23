import os
import os
import sys

directoryName = "train-pos"
filePath = os.path.abspath(directoryName)
filePathWithSlash = filePath + "/"
for counter, filename in enumerate(os.listdir(directoryName)):
  filenameWithPath = os.path.join(filePathWithSlash, filename)
  os.rename(filenameWithPath, filenameWithPath.replace(filename,"IMG_" + str(counter+1).zfill(5) + ".jpg" ))
  
