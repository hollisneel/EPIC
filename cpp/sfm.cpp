#include <opencv2/opencv.hpp>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
using namespace cv;

int main(int argc, char** argv){
    cout << argv << endl;
    string address = "";
    ostringstream converter;
    int numberOfImages = 1080;
    int nrows = 540;
    int ncols = 960;



    cout << "before array" << endl;
    char *** finalArray = new char**[nrows];
    for(int i = 0; i < nrows;i++){
        finalArray[i]= new char*[ncols*3];
        for(int j = 0; j < ncols*3; j++){
            finalArray[i][j] = new char[numberOfImages];
        }
    }

    //cout << sizeof(finalArray) << endl << sizeof(finalArray[0]) << endl;

	cout << "after array" << endl;
    Mat image; 
	//image = imread(argv[1], IMREAD_COLOR);
    
    //cout << image.cols <<" " << image.rows << endl;
    //cout << image.step<< endl;
    cout << 0 << endl;
    
    
    for(int i = 1; i <= numberOfImages; i++){
    
        int ordinal = i;
        converter << ordinal;
        string temp = "";
        temp = converter.str();
        address = "./images2/" + temp + ".jpg"; //+ ordinal;
        converter.str(std::string());
        converter.clear();
        image = imread(address, IMREAD_COLOR);
        int depth = image.step/image.cols;

        for (int row = 0; row < (image.rows); row++){
            for (int col = 0; col < (image.cols); col++){
                for (int rgb = 0; rgb < depth; rgb ++ ){
                   //cout << "\n--------------------------\n" << "col: " << col << "\t row: " << row << endl;
                   //cout << "rgb: " << rgb << "\t image: " << i << endl;                
	               //cout << "pixel: " << image.at<uchar>(row,depth*col+rgb) << "\t depth: " << depth << endl;
                   //cout << i << " " <<row << " " <<col << endl;
                   finalArray[row][3*col+rgb][i] = image.at<uchar>(row,depth*col+rgb);
                   //finalArray[row][col+rgb][i] = image.at<uchar>(row,depth*col + rgb);
                   //if (rgb%depth == 0){
	                 //  image.at<uchar>(row,depth*col + rgb) = (char) 0; // Blue
	               //}
	               //if (rgb%depth == 1){
	                 //  image.at<uchar>(row,depth*col + rgb) = (char) 0;  // Green
	               //}
	               //if (rgb%depth == 2){
	                 //  image.at<uchar>(row,depth*col + rgb) = (char) 255; // Red
                    //}
                }
            }
        
        }
        // Created the 3D image with (row,col,image)
    }    
    
    Mat newImage;
    newImage = Mat(numberOfImages,ncols,CV_8UC3);

    /*for(int k = 0; k < numberOfImages; k ++){
        for(int i = 0; i <1080; i++){
            for(int j = 0; j< 1920*3; j++){
                //cout << k << endl << j;
                newImage.at<uchar>(i,j) = finalArray[i][j][k];
            }
        }
        namedWindow("Display Window", WINDOW_AUTOSIZE);
        imshow("Display Window", newImage);
        waitKey(0);

        imwrite("./out/test.jpg", newImage);
    }
*/
    //for(int k = 0; k < numberOfImages; k ++){
        for(int i = 0; i <numberOfImages; i++){
            for(int j = 0; j< ncols*3; j++){
                //cout << k << endl << j;
                newImage.at<uchar>(i,j) = finalArray[ncols/2][j][i];
            }
        }
        namedWindow("Display Window", WINDOW_AUTOSIZE);
        imshow("Display Window", newImage);
        waitKey(0);

        imwrite("./out/test.jpg", newImage);
    //}



    waitKey(0);

    return 0;

}

