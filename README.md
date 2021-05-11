# Radon Barcode - Content Based Image Retrieval

## Introduction
The generation of a barcode to represent images has many practical applications, both in image representation as well as search queries based on an image. A Radon barcode is a type of barcode designed to represent the contents of an image in a simplified yet comprehensive form. This barcode can then be used to conduct searches based on an image, finding images that have been found to produce similar barcodes. The use of a barcode to conduct the search over other commonly used alternatives, such as those that look for commonly occurring shapes in the content of an image, can be advantageous due to the speed at which barcodes can be searched. 

This program was designed to work with a dataset of 28 x 28-pixel jpg images displaying numbers from 0 to 9. The algorithm is to search the dataset to locate the most similar image (excluding itself). The accuracy of the program search function can then be tested through verifying if the resultant image displays the same number as the original search term.

## Background
Content-Based Image Retrieval (CBIR) is the search of an image dataset based on certain content. CBIR can be difficult due to the amount and density of data found in images. To resolve this issue, a method must be created to represent the images in a simple yet comprehensive way.
Barcodes are a method of displaying binarized data, allowing machines to decode and interpret the encoded information. This method of displaying information is very useful in practical applications due to its simplicity and versatility. Due to the simplification of data, it can become easier and more efficient to search for similar codes among a dataset. 

This same approach of displaying data can be applied to images, however it can be difficult to represent the vast amount of information stored in images in a barcode due to the compaction of data that is required. This requires an approach to locate patterns between similar results and translate these findings into barcodes which are searchable. Here Radon projections can be used, representing the image from multiple angles allows for the creation of a more complete representation in a barcode, and similarities in images are easier to find due to an increased likelihood that similar images will also be similar from other angles. This can help filter through possible coincidences which may occur between image barcodes that may happen to be similar. Increasing the number of projections 
Program Structure and Algorithms

The Radon Barcode program was created using two main algorithms/functions, a barcode creation function, and a search function. The program first creates a list of the locations of all images in the current dataset. It then applies the barcode generation function to each image in the dataset, creating a list of all the barcodes in the dataset. When an image is searched, its barcode is first generated then it is sent to the search function which finds the most similar barcode. The location of this found barcode is then located using the list of all images and this corresponding image is outputted.

## 1.	Barcode Generation Algorithm
### Functionality
The Barcode creation algorithm is a key component to this project. It is responsible for binarizing the image content through the discovery of distinct patterns or trends that can be found between images. Representing these patterns found in groups of images is essential to the query of images.

The barcode generation algorithm uses the OpenCV python library as a crucial aspect in its functionality. OpenCV was chosen over alternative imaging libraries such as Pillow due to its versatility and application in Artificial Intelligence programs. While these more advanced functions were not used, the use of OpenCV can allow for future modifications to the program with minimal change to the core aspects. For the function of the Barcode generation, the OpenCV library was only used to convert the image file into a matrix and convert to black and white. Greyscale conversion was conducted to normalize images across the dataset and future datasets in addition to placing only a single brightness value in the image matrix. This allows for simple and effective iteration through each row in the image.

### Explanation
The function receives an image file as input and uses the OpenCV python library to convert to a greyscale matrix, where each pixel is represented by its brightness value ranging from 0 to 255. This image is again used to create several additional representations through 45-degree rotations, producing four matrices containing different representations of the image contents from the angles 0°, 45°, 90° and 135°. Upon producing the projections, a threshold value unique to each matrix which is used in the binarization process is then calculated through finding the average value of a row in the matrix. Using the threshold value, for each matrix, the rows are summed and compared against the threshold for that matrix. If the row is found to have a greater value than the threshold, it is represented by a 1 which is appended to a barcode list. If the value is found to be less than the threshold, it is represented by a 0 which is appended to the barcode list. This process is repeated for each row in each projection until every row is represented in the barcode. This barcode is then returned by the function in the form of a list to be used in search functions.

### Big O Analysis
The barcode generation algorithm has a big O complexity of O(n). Although there is a nested loop, the program does not exceed a complexity greater than the original image matrix. Since each pixel value is iterated once, the complexity remains O(n).

The implication of this complexity is that the barcode generation scales linearly with the image size. This means that if the barcode was to be generated for a larger image,  the difference in time would be linearly proportionate to the size increase/decrease. 

## 2. Search Algorithm
### Functionality
The algorithm with the largest impact on the effectiveness of the Content-Based Image Retrieval is the Search algorithm. The Search algorithm is tasked with finding the most similar image from the dataset through an association evaluation of each image in the dataset. The accuracy of the Search algorithm directly impacts the accuracy of the results and therefore the practical uses of the program. 

The Search algorithm for this application uses the hamming distance as its main driver. Hamming distance is defined as the number of positions at which the values of two codes differ. When applied to comparing barcodes, the Search algorithm will function through checking between the barcode inputted when the search was called, and each barcode stored in the barcode database. After finding the hamming distance between each of the barcodes, the barcode with the minimum hamming distance will be selected as the best match.

### Explanation
The Search algorithm requires a barcode corresponding to an image, generated using the generateBarcode() algorithm. The algorithm then creates a variable to store the best match. After defining a location for the best match, the algorithm then iterates through each barcode held in the database by their index. A match variable is created to score the individual performance of the specific barcode. Each induvial value in the barcode is then iterated through. The value held in the database barcode and is checked against the value of the barcode being queried and If both values at the index are equivalent, the match variable is incremented by one. After all index values in the barcodes have been compared, the value of match is checked against the previously defined best match to check if the current barcode is the most similar to the queried. If it is a better match, the value for the best match is changed to the greater value and the index at which the barcode is stored at (within the list of all barcodes) is saved.

After analyzing all barcodes in the database, finding the most similar match and saving the index of the best match, the algorithm then displays and checks whether or not the found image was correct (the same number as the original). The image display is done through horizontally stacking images and outputting using the imshow() function from the OpenCV library. Determining whether the found image was correct is done through verifying whether both files originated from the same directory. The file path of the found image can be located through looking up the index of the best match in the list of all files. Since the barcodes for the database were generated using the list of all files, the indices are aligned allowing for the location of the file path corresponding to the best match. The OS python library can then be used on both file paths to find the directory in which the file exists. If both files originate from the same directory, the function returns a value of one to the user, representing a correct match. If the files do not originate from the same directory the function returns a zero, representing an incorrect match.

### Big O Analysis
The Search algorithm has a big O complexity of O(nm). This is due to the need for the algorithm to firstly traverse all the barcodes, held in the list m, then iterate through each digit in the barcodes of length n. This nested for loop structure means the maximum number of operations is n*m.

Since the Search function is dependent on both the size of the barcode n, and size of the list m. This complexity becomes more relevant when searching through larger datasets or through larger images. An increase in either or both of these elements could significantly increase the number of operations conducted by the program. This primarily is relevant in the database size, as in larger scale applications the database will likely be significantly larger and thus more of a limiting factor than the image size. 

## Program Effectiveness
To test the effectiveness and accuracy of the Content-Based Image Recovery, a dataset containing images of numbers ranging from 0 to 9 was used. The numbers were categorized in separate directories and each directory contained 10 images, producing a total of 100 images in the dataset. The program effectiveness is determined through finding the number of times which the program can find a similar image within the same folder as the original.

After running the program, the accuracy was found to be 53%. This accuracy is somewhat low however it demonstrates that the program is working correctly, as it is 141% greater than the expected accuracy of the search had it been conducted at random.

## Future Improvements
Although the Content-Based Image Retrieval program functions as expected, there are many improvements which can be made to increase the accuracy of the search results. It is important to note that although these alterations may increase the accuracy of image retrieval, they may not be desirable in applications due to the increase in complexity which may be added through their implementation.

##Optimized Projection Generation
One of the simplest changes which can be made to increase the accuracy is increasing the number of projections. For the purpose of this project, only four projections were taken at the angles 0, 45, 90 and 135 degrees. While using only four projections does reduce the complexity of the program, increasing the number of projections or changing the projection angles to provide a more comprehensive representation of the image may improve the search results. 

This approach was tested, using projections taken at angles 0, 30, 60, 90, 120 and 150 degrees, and the program was found to have a 62% accuracy, a 15.6% increase over the use of four projections. Interestingly, the program accuracy did not increase drastically when tested with the number of projections being increased further, meaning that more experimentation and calculation needs to be done to maximize the efficiency.

### Improved Search algorithm
The Search algorithm is likely the most crucial component in the image retrieval application. For the main program, the search functioned through the use of a hamming 
distance formula. The hamming distance scores searched codes based on how many digits are equivalent to the original code. This approach is very simplistic and allows for easy comparison of binary strings such as the barcodes being compared, however it has shortcomings in that it disregards any association that may exist outside of the specific index being compared at. This can lead to some results being favoured over another which more closely resembles the original code.

A possible solution to this limitation is changing the way this scoring process is conducted using an alternative formula. One possible example of this implementation is scoring neighboring bits, so if the bits at the index differ, the formula can check for equivalence in the adjacent bits and provide a lesser score. This approach can help identify results which may have some alignment, however extensive testing needs to be conducted to find an adequate score and if this approach can increase the search accuracy.

## Conclusion
The Content-Based Image Retrieval using Radon barcodes has proven to be an effective solution to searching based on image contents. Through the creation of four projections and generation of a barcode, images can be expressed relatively accurately, drastically reducing the complexity of a search on an image. Using the barcode, searches can be conducted very simply through a hamming distance calculation and similar images can be found at a fairly good rate at 53%
