#include <opencv2/opencv.hpp>
#include <iostream>
#include <fstream>

using namespace std;
using namespace cv;

int main(int argc, char** argv){
    cout << argv << endl;

	Mat image; 
	image = imread(argv[1], IMREAD_COLOR);
    
    cout << image.cols <<" " << image.rows << endl;
    cout << image.step<< endl;

    for (int row = 0; row < image.rows; row ++){
        for (int col = 0; col < image.cols; col++){
            for (int rgb = 0; rgb < image.step/image.cols; rgb ++ ){ 
                image.at<uchar>(row,(image.step/image.cols)*col + rgb) = (char) 255;
            }
        }
    }    

    namedWindow("Display Window", WINDOW_AUTOSIZE);
    imshow("Display Window", image);

    waitKey(0);

    return 0;

}

