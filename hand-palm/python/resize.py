import os
import os
import sys
import cv2


directoryName = "train-neg"
filePath = os.path.abspath(directoryName)
filePathWithSlash = filePath + "/"
for counter, filename in enumerate(os.listdir(directoryName)):
    try:
		filenameWithPath = os.path.join(filePathWithSlash, filename)
		img = cv2.imread(filenameWithPath)

		height, width = img.shape[:2]
		max_height = 100
		max_width = 100

		# only shrink if img is bigger than required
		if max_height < height or max_width < width:
		# get scaling factor
			scaling_factor = max_height / float(height)
			if max_width/float(width) < scaling_factor:
				scaling_factor = max_width / float(width)
			# resize image
			img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
			cv2.imwrite(filenameWithPath,img)
    except Exception as e:
		print e
#cv2.imshow("Shrinked image", img)
#cv2.imwrite('/mnt/c/Users/phuon/Repos/Github/phuongdv/ml-data/hand-palm/train-pos-case-1/IMG_158.jpg',img)


