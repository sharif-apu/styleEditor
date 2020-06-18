import cv2 
import numpy as np 

bgRoot = "BG/"
maskRoot = "MK/"
imRoot = "image/"

bgPath = bgRoot + "b9.png"
mkPath = maskRoot + "m8.jpg"

bg = cv2.imread(bgPath)
mk = cv2.imread(mkPath)

bg = cv2.resize(bg, (960, 960))
mkResize = cv2.resize(mk, (960, 960)) 
print (bg.shape, mk.shape) 
mkIverted = 255- mkResize
cv2.imwrite("t12.png", mkIverted)

blendMask = cv2.addWeighted(bg, .6, mkIverted, 1, 0)

cv2.imwrite("blendedMaks1.5.png", blendMask)


