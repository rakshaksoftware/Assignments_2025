import cv2
img = cv2.imread('hello/3-Cs-of-upgradcpp.png' ,0) #-1,0,1

imgcan = cv2.Canny(img,100,200)
imgblur = cv2.GaussianBlur(img, (5, 5), 0)
imgre = cv2.resize(img,(1000,1000))
imgro = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('image1',img)
cv2.imshow('image2',imgblur)
cv2.imshow('image3',imgro)
cv2.imshow('image4',imgre)
cv2.imshow('image5',imgcan)
cv2.waitKey(0)
cv2.destroyAllWindows()
