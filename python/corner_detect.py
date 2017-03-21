from PIL import Image
import numpy
import cv2
import argparse
import os


def keypoints(image_path,final_image_dir,tag1):

    img = cv2.imread(image_path,0)

    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector_create()

    # find and draw the keypoints
    kp = fast.detect(img,None)
    img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))

    # Print all default params
    print "Threshold: ", fast.getThreshold()
    print "nonmaxSuppression: ", fast.getNonmaxSuppression()
    print "neighborhood: ", fast.getType()
    print "Total Keypoints with nonmaxSuppression: ", len(kp)

    #cv2.imwrite(final_image_dir+str(tag1)+"Sfast_true.png",img2)

    # Disable nonmaxSuppression
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img,None)

    print "Total Keypoints without nonmaxSuppression: ", len(kp)
    img3 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
    #cv2.imwrite(final_image_dir+str(tag1)+"Ufast_false.png",img3)

    
    bool_array = numpy.zeros((len(img),len(img[0])),dtype=bool)

    for pt in kp:
        bool_array[int(pt.pt[1])][int(pt.pt[0])] = True
    
    return (bool_array,img2) # return keypoint location in bool array




def bool_reduce(bool_array,n):

    width  = len(bool_array[0])
    height = len(bool_array)

    new_width  = width/n
    new_height = height/n

    new_array = numpy.zeros((new_height,new_width),dtype='uint8')
    
    for row in range(new_height):
        for col in range(new_width):

            for k in range(n):
                for l in range(n):
                    if bool_array[row*n+k][col*n+l]:
                        new_array[row][col] = 255
    return new_array




def stack(arrayList,row):

    height = len(arrayList)
    width  = len(arrayList[0][0])

    final_array = []    

    for arr in arrayList:
        final_array.append(arr[row])
        
    return final_array
    
def show(array):
    img = numpy.matrix(array,dtype='uint8')
    Image.fromarray(img).show()
    return




if __name__=="__main__" and 0:
    # read in file names
    files = os.listdir("/home/hollis/dev/EPIC/images/")
    key_points = []
    images = []
    for tag1 in range(len(files)):

        path = "/home/hollis/dev/EPIC/images" + str(tag1)+"/"
        os.mkdir(str(tag1)) 
        keypoint_return = keypoints(files, path, tag1)

        key_points.append(keypoint_return[0]) # stores the keypoint of image tag
        images.append(keypoint_return[1])     # stores the image
