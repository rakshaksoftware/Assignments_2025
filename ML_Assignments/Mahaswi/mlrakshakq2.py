import cv2
image=CV2.imread(path)
(h, w)=image.shape[:2]
angle=30
center=(w//2,h//2)
scale=1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
scaled_img=cv2.resize(image,(w*2,h*2))
flippedhori_img=cvr.flip(image,1)
cv2.imshow(rotated_image)
cv2.imshow(scaled_img)
cv2.imshow(flippedhori_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
