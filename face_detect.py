import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))

# try to add a emoji to a existing face
s_img = cv2.imread("tear.png")
s_height, s_width, s_channels = s_img.shape
# s_img = cv2.resize(s_img, (0,0), fx=0.2, fy=0.2) 
l_img = image
# x_offset=y_offset=50
# l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
# cv2.imshow("Faces found", l_img)

# Draw a rectangle around the faces
resized = False
for (x, y, w, h) in faces:
    # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    resize_ratio = round(w*10/(10.0*s_width), 2)
    # print "width " + str(w)
    if not resized:
    	s_img = cv2.resize(s_img, (0,0), fx= resize_ratio, fy= resize_ratio) 
    	resized = True
    x_offset = x
    y_offset = y
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
cv2.imwrite("result-emoji.jpg", image)
cv2.imshow("Faces found", image)
cv2.waitKey(0)
