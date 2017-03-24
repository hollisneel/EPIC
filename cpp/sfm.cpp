#include <opencv2/opencv.hpp>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
using namespace cv;

int main(int argc, char** argv){

    // Unsure as to purpose
    string address = "";
    ostringstream converter;

    // Define the properties of the image set we are using
    int numberOfImages = 1080;
    int nrows = 540;
    int ncols = 960;
    int depth = 3;
    
    int ordinal;
    
    String verbose = argv[1];
    bool v = false;

    if(verbose == "-v"){
        cout << "Verbose ON" << endl;
        v = true;
    }
    else v = false;
    
    if(v) cout << "before array" << endl;
    
    // Create an empty 3D array of dimension (rows,col,image)
    char *** finalArray = new char**[nrows]; 
    for(int i = 0; i < nrows;i++){
        finalArray[i]= new char*[ncols*3];
        for(int j = 0; j < ncols*3; j++){
            finalArray[i][j] = new char[numberOfImages];
        }
    }

    // Prints the size of the final array
    if(v){ 
        cout << sizeof(finalArray) << endl << sizeof(finalArray[0]) << endl;
	    cout << "after array" << endl;
    }

    // Create image object
    Mat image;
   
    // Read in the directory images2
    for(int i = 1; i <= numberOfImages; i++){

        // goes from 1-#images
        ordinal = i;

        // Unsure about the purpose of this code
        converter << ordinal;
        string temp = "";
        temp = converter.str();

        // Creates the address of the image we are reading in.
        address = "./images2/" + temp + ".jpg";

        // Clears the converter?
        converter.str(std::string());
        converter.clear();

        // Reads the image and determines the bit depth
        image = imread(address, IMREAD_COLOR);
        depth = image.step/image.cols;

        for (int row = 0; row < (image.rows); row++){
            for (int col = 0; col < (image.cols); col++){
                for (int rgb = 0; rgb < depth; rgb ++ ){

                    // Prints out information about each image
                    if(v){
                        cout << "\n--------------------------\n" << "col: " << col << "\t row: " << row << endl;
                        cout << "rgb: " << rgb << "\t image: " << i << endl;                
	                    cout << "pixel: " << image.at<uchar>(row,depth*col+rgb) << "\t depth: " << depth << endl;
                        cout << i << " " <<row << " " <<col << endl;
                    }        
                    // Reads in the image to the final array
                    finalArray[row][3*col+rgb][i] = image.at<uchar>(row,depth*col+rgb);
                }
            }
        }
        
    }
        // Created the 3D image with (row,col,image)    
   

    // Now we will do things to the image set.
 
    // Create a new image matrix object
    Mat newImage; 
    newImage = Mat(numberOfImages,ncols,CV_8UC3);

        
    for(int i = 0; i <numberOfImages; i++){
        for(int j = 0; j< ncols*3; j++){
            // Prints the current row col.
            if(v) cout << i <<" " << j << endl;

            // place the slice of the 3D final array into an image.
            newImage.at<uchar>(i,j) = finalArray[ncols/2][j][i];
        }
    }
    
    // Display the image
    namedWindow("Display Window", WINDOW_AUTOSIZE);
    imshow("Display Window", newImage);
    waitKey(0);

    // Write the image
    //mwrite("./out/test.jpg", newImage);
    
    /*
    for(int i = 0; i < nrows;i++){
        finalArray[i]= new char*[ncols*3];
        for(int j = 0; j < ncols*3; j++){
            for(int im = 0; im < numberOfImages;im++){
                delete(finalArray[i][j][im]);
            }
        }
    }

    for(int i = 0; i < nrows;i++){
        for(int j = 0; j < ncols*3; j++){
            delete(finalArray[i][j]);
        }
    }
 
    for(int i = 0; i < nrows;i++){
        delete(finalArray[i]);
    }

    delete(finalArray); 
    */
    return 0;

}

