
import cv2
import numpy as np
mywin = None
button = None
x = None
y = None


cv2.imshow('mywin',cv2.imread('media/lena.jpg',1))
def onmouse(button, x, y, flags, param):
  print(['x: ', x, ' y: ', y])

cv2.setMouseCallback('mywin', onmouse)
if cv2.waitKey(0)&0xff == 27:
  pass
cv2.destroyAllWindows()