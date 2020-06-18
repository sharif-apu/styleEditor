import cv2 
import numpy as np 
import glob
from pathlib import Path
from etaprogress.progress import ProgressBar
from colorama import Fore, Style

def imageList(path, multiDir = False, imageExtension =['*.jpg', '*.png', '*.jpeg', '*.tif', '*.bmp']):
    #types = () # the tuple of file types
    imageList = []
    for ext in imageExtension:

        if multiDir == True:
            imageList.extend(glob.glob(path+"*/"+ext))
        else:
            imageList.extend(glob.glob(path+ext))
        
        imageList
    return imageList


def createDir(path):
    # Create a directory to save processed samples
    Path(path).mkdir(parents=True, exist_ok=True)
    return True 

def styleEditor(imList, maskList, bgList, targetRoot, invertedEditor = False ):

    if invertedEditor == False:
        invertedEditorCounter = 1
    else:
        invertedEditorCounter = 2

    imList = imageList(imRoot)
    maskList = imageList(maskRoot)
    bgList = imageList(bgRoot)
    counter = 0
    bar = ProgressBar(len(imList) * len(maskList) * len(bgList) * invertedEditorCounter, max_width=int(10))
    for i in imList:
        for m in maskList:
            for b in bgList:

                mask = cv2.imread(m)
                bg = cv2.imread(b)
                im = cv2.imread(i)

                # Resizing Images
                maskResize = cv2.resize(mask, (im.shape[1], im.shape[0]))
                bgResize = cv2.resize(bg, (im.shape[1], im.shape[0])) 

                # Making Mask
                mkIverted = 255- maskResize
                
                # Alpha Blending
                blendImage = cv2.bitwise_and(im, mkIverted)
                bgBlend = cv2.bitwise_and(bgResize, maskResize)
                finalBelnding = cv2.bitwise_or(bgBlend.copy(), blendImage.copy())
                counter += 1
                # Exporting Image
                cv2.imwrite(targetRoot + "styleImage_" + str(counter) + ".png", finalBelnding)

                if invertedEditor == True:
                    # Inverted Blending
                    invertedBelnding = cv2.bitwise_and(im, bgResize)
                    invertedBelnding = cv2.bitwise_and(invertedBelnding, mkIverted)
                    counter += 1

                    # Exporting Image
                    cv2.imwrite(targetRoot + "invertedStyleImage_" + str(counter) + ".png", invertedBelnding)
                    
                # Logger
                if counter % 2 == 0:
                    bar.numerator = counter
                    print(Fore.CYAN + "Processd |", bar,Fore.CYAN, end='\r')
                
           
        
    print ("\nImage edited {}".format(counter))

if __name__ == "__main__":
    
    imRoot = "SM/"
    maskRoot = "MK/"
    bgRoot = "BG/"
    targetRoot = "edited/"

    createDir(targetRoot)

    print(Fore.YELLOW + "Applying style...")      
    
    styleEditor(imRoot, maskRoot, bgRoot, targetRoot, False)
    