import cv2
file = 'cat.jpg'
img = cv2.imread(file, 1)
cv2.imshow('WOW AMAZING', img)
cv2.waitKey(0)
cv2.destroyAllWindows
