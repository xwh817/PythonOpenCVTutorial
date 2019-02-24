# pylint: disable=no-member
import cv2 as cv

print("--------- Python OpenCV Tutorial ---------")
src = cv.imread("./images/image_1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)

cv.destroyAllWindows()