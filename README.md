# Radon Barcode - Content Based Image Retrieval Course Project

## Overview
The generation of a barcode to represent images has many practical applications, both in image representation as well as search queries based on an image. A Radon barcode is a type of barcode designed to represent the contents of an image in a simplified yet comprehensive form. This barcode can then be used to conduct searches based on an image, finding images that have been found to produce similar barcodes. The use of a barcode to conduct the search over other commonly used alternatives, such as those that look for commonly occurring shapes in the content of an image, can be advantageous due to the speed at which barcodes can be searched. 

This program was designed to work with a dataset of 28 x 28-pixel jpg images displaying numbers from 0 to 9. The algorithm is to search the dataset to locate the most similar image (excluding itself). The accuracy of the program search function can then be tested through verifying if the resultant image displays the same number as the original search term.

Currently the program only functions with the MNIST_DS dataset included.

## How to Run
To use the program you must first install numpy and openCV python libraries. Extract and place files from MNIST_DS.zip in same folder as Radon.py. Run Radon.py
