import cv2
import numpy as np

src_img = cv2.imread("./test.png")

average_color = np.average(src_img, axis=0)

img_copy = np.copy(src_img)
img_copy[
    (img_copy[:, :, 0] > 50) | (img_copy[:, :, 1] < 150) | (img_copy[:, :, 2] < 150)
] = 0

if img_copy:
    print("Yellow")

cv2.imshow("Source image", src_img)
cv2.imshow("Average Color", img_copy)
cv2.waitKey(0)
