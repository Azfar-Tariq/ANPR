import cv2
from matplotlib import pyplot as plt
import imutils
import easyocr
import numpy as np
from pandas import read_excel
# from PyQt5.QtWidgets import QMessageBox
# Read in image, grayscale and blur #

img = cv2.imread('image4.jpg')#COLOR_BGR2GRAY
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)         # convert single color code to different one
# plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))    # Reason for conversion : matplotlib expects RGB
# plt.show()


# Apply filter and find edges for localization #
# Filter -> remove noise
bfilter = cv2.bilateralFilter(gray,11,17,17)
edged = cv2.Canny(bfilter,30,200)   # edge detection : where is number plate?
# plt.imshow(cv2.cvtColor(edged,cv2.COLOR_BGR2RGB)) 
# plt.show()


# Find Contours and Apply Mask #
# contours detetction : detect where lines are and detecting polygon within those lines
# we will look for contour having four points like rectangle which will most likely will be a number plate
keypoints = cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    # second argument : how we want results, in this case we 
                                                                                    # have returned a tree. Tree will have different level of 
                                                                                    # shapes / contours returned.
                                                                                    # Third Argument : simply the returned results.
contours = imutils.grab_contours(keypoints)
contours = sorted(contours,key=cv2.contourArea,reverse=True)[:10]                  # sorting in descending order and getting top 10.

# iterate through returned contours and check if there are 4 keypoints in it or not? in other words whether it is a number plate or not?
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour,10,True)  # approxPolyDp method allows to approx. polygon from a contour
    if len(approx) == 4:
        location = approx
        break

# print(location)

# masking to isolate the number plate section
mask = np.zeros(gray.shape,np.uint8)                        # creating a blank mask of original grey image
new_image = cv2.drawContours(mask,[location],0,255,-1)      # drawing contours from location obtained in previous step
new_image = cv2.bitwise_and(img,img,mask=mask)              # paste masked image onto blank mask

# plt.imshow(cv2.cvtColor(new_image,cv2.COLOR_BGR2RGB))
# plt.show()

# crop the number plate from black section
(x,y) = np.where(mask==255)         # find every single section where image is not black
(x1,y1) = (np.min(x),np.min(y))
(x2,y2) = (np.max(x),np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]

# plt.imshow(cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB))
# plt.show()


# use easy ocr to to read text
reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)
print(result)

# from pandas import read_excel as rc
# reading numbers from excel file
df = read_excel('db.xlsx')

notFound = True

for i in df['numbers']:
    if i == result[0][-2]:    
        print('Let the vehicle in.')
        notFound = False
        break

if  notFound:    
    print('Vehicle not registered')


# render result #
text = result[0][-2]
font = cv2.FONT_HERSHEY_SIMPLEX
res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()