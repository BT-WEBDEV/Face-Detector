#### Face Detector - Practice Project ####
### Case Use: Can Detect A Face or Multiple Faces From An Images 
### Modules Used - OpenCV ###


import cv2

# Face Cascade Object is the classifier for detecting faces from images
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Read The Image
img=cv2.imread("news.jpg")

#Convert to A Gray Scale to Help Detect Face
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detect the faces in the gray image
#Scale Factor is used to create the scale pyramid 
#Rescaling the input image can help resize a larger face towards a smaller one
#This makes it detectable for the algorithm and increases the chance of matching the face. 
#MinNeighbors - helps prevent false positives - increasing the number eliminates false positive, but can lost true positives as well. 
faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

#After Face Is Detected Output is an Array of Starting Point for Face: [X Coordinate Pixel, Y Coordinate Pixel, Width of Rectangle, Height of Rectangle]
#For Loop Iterates Through the Face Array
for x,y,w,h in faces:
    #Img Object Contains the Created Rectangle from Array - (GREEN COLOR CODE), RECTANGLE BORDER WIDTH
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)

#Image is Resized
resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()