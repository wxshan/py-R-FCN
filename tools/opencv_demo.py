import cv2

img = cv2.imread("/home/lxz/wxshan/py-R-FCN/data/demo/000001.jpg")

cv2.rectangle(img, (0,0), (500,500), (255, 0, 0), 5)

cv2.imshow('dd',img)
cv2.waitKey()