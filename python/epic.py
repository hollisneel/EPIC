from PIL import Image
import numpy
import cv2
import argparse
import os

class Scene:
    def __init__(self,imagePathDir):
        files = os.listdir(imagePathDir)
        finalArray = []
        # Assume num of files starts at 1
        for i in range(1,len(files)+1):
            # final array is of format [image][row][col][rgb]
            finalArray.append(cv2.imread(imagePathDir+str(i)+".jpg"))    

        self.numImages = len(files)
        self.nrows     = len(finalArray[0])
        self.ncols     = len(finalArray[0][0])
        self.depth     = len(finalArray[0][0][0])
        self.image     = 0
        self.slice     = 0
        self.stackArray= finalArray
        self.boolArray = []
        self.boolSlice = 0


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

    def setImage(self,imageNumber):
        img = numpy.zeros((self.nrows, self.ncols, self.depth),dtype='uint8')

        for row in range(self.nrows):
            for col in range(self.ncols):
                for depth in range(self.depth):
                    img[row][col][depth] = self.stackArray[imageNumber][row][col][depth]
        self.image = img
    

    def showImage(self):
        cv2.imshow("Image",self.image)
        cv2.waitKey()

    def saveSlice(self,name):
        cv2.imwrite(self.slice)

    def cornerDetect(self,r):
        fast = cv2.FastFeatureDetector()
        final = []
        for image in range(self.numImages):
            bArray = numpy.zeros((self.nrows,self.ncols,self.depth),dtype='uint8')

            self.setImage(image)
            kp = fast.detect(self.image,None)   
            for pt in kp:
                for x_change in range(-r,r):
                    for y_change in range(-r,r):
                        bArray[int(pt.pt[1])+y_change][int(pt.pt[0])+x_change][0] = 255
                        bArray[int(pt.pt[1])+y_change][int(pt.pt[0])+x_change][1] = 255
                        bArray[int(pt.pt[1])+y_change][int(pt.pt[0])+x_change][2] = 255
            final.append(bArray)
        self.boolArray = final

    def featureSlice(self,rowHeight):
        ncols = self.ncols
        depth = self.depth
        numImages = self.numImages

        array = numpy.zeros((numImages,ncols,depth),dtype='uint8')

        for row in range(numImages):
            for col in range(ncols):
                for dep in range(depth):
                    array[row][col][dep] = self.boolArray[row][rowHeight][col][dep]

        self.featureSlice = array

        





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


