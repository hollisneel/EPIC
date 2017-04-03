from PIL import Image
import numpy
import cv2
import argparse
import os

class Scene:
    def __init__(self,imagePathDir):
        files = os.listdir(imagePathDir)
        finalArray = []
        for name in files:
            # final array is of format [image][row][col][rgb]
            finalArray.append(cv2.imread(imagePathDir+name))    

        self.numImages = len(files)
        self.nrows = len(finalArray[0])
        self.ncols = len(finalArray[0][0])
        self.depth = len(finalArray[0][0][0])

        self.slice = 0
        self.stackArray = finalArray



    def setSlice(self,rowHeight):

        ncols = self.ncols
        depth = self.depth
        numImages = self.numImages

        array = numpy.zeros((numImages,ncols,depth),dtype='uint8')

        for row in range(numImages):
            for col in range(ncols):
                for dep in range(depth):
                    array[row][col][dep] = self.stackArray[row][rowHeight][col][dep]

        self.slice = array

    def showSlice(self):
        if type(self.slice) != int:
            cv2.imshow("Image",self.slice) 
            cv2.waitKey()

    def showImage(self,imageNumber):
        img = numpy.zeros((self.nrows, self.ncols, self.depth),dtype='uint8')

        for row in range(self.nrows):
            for col in range(self.ncols):
                for depth in range(self.depth):
                    img[row][col][depth] = self.stackArray[imageNumber][row][col][depth]
        cv2.imshow("Image #"+str(imageNumber),img)
        cv2.waitKey() 

def showColor(filepath):
    z = open(filepath)
    raw = z.read()
    raw = raw.split("\n")
    raw = raw[0:len(raw)-1]
    raw2 = []
    for row in raw:
        raw2.append(row.split(" "))

    data = []
    for row in raw2:
        temp = []
        for col in row:
            if col == '':
                continue
            else :
                temp.append(float(col))
        data.append(temp)
    change = 970/(len(raw))

    mat = numpy.zeros((540,970,3),dtype='uint8')
 
    for row in range(540):
        count = 0
        idx = -1
        for col in range(970):
            
            if count%change == 0 and idx != len(raw)-1:
               idx += 1
            
            mat[row][col][0] = data[idx][3]
            mat[row][col][1] = data[idx][2]
            mat[row][col][2] = data[idx][1]
            count += 1
    cv2.imshow("Image",mat)
    cv2.waitKey()


