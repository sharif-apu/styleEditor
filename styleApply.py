import cv2 
import numpy as np 


imRoot = "Image/"
maskRoot = "MK/"
bgRoot = "BG/"

blendMask = "blendedMaks1.1.png"

mask = cv2.imread(maskRoot+"m2.jpg")
bg = cv2.imread(bgRoot+"b9.png")
im = cv2.imread(imRoot+"i3.jpg")

maskResize = cv2.resize(mask, (im.shape[1], im.shape[0]))
bgResize = cv2.resize(bg, (im.shape[1], im.shape[0])) 
print (maskResize.shape, im.shape) 
mkIverted = 255- maskResize
#cv2.imwrite("maskTest.png", mkIverted)

blendImage = cv2.bitwise_and(im, mkIverted)
cv2.imwrite("blendedImage1.png", blendImage)
bgBlend = cv2.bitwise_and(bgResize, mkIverted)
cv2.imwrite("bgImage1.png", bgBlend)

finalBelnding = cv2.bitwise_and(im, bgResize)
finalBelnding = cv2.bitwise_and(finalBelnding, mkIverted)

#finalBelnding = cv2.bitwise_and(blendImage, mkIverted)

#cv2.imwrite("bgBlend.png", bgBlend)
cv2.imwrite("blendingTestingConf.png", finalBelnding)

