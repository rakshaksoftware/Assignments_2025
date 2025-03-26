import cv2
image=cv2.imreadread(path, cv2.IMREAD_GRAYSCALE)
median = cv2.medianBlur(image, 5)
image=median
edges=cv2.Canny(image, 50, 150)
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
