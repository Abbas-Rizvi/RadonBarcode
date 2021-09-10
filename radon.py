# imports
import cv2
import os
import numpy as np


# ------------------  Barcode Generation  ----------------------------------
def generateBarcode(img):
    # Creates several projections of image
    # Converts each projection to binary based on value of row
    # Creates one barcode representing results from each projection conversion

    # create lists to store barcode and projection matrices
    RBC = []
    projections = []

    # Project at angles 0, 45, 90, 135
    for angle in range(0, 180, 45):
        projections.append(rotateImage(img, angle))  # Add rotated img to projection list

    for proj in projections:  # For each projection in projection list

        sum = 0 # initialize sum

        for row in proj:    # for each row in the projection
            for val in row:  # for each value in the row
                sum += val  # add value to sum

        th = sum / 28   # divide sum by number of row

        # for each row in the projection matrix
        for row in proj:

            rowSum = 0  # Initialize sum

            # sum all values in row
            for val in row:
                rowSum += val

            # check if row has sum greater than threshold
            if rowSum >= th:
                RBC.append(1)  # add a 1 to barcode
            else:
                RBC.append(0)  # add a 0 to barcode

    return RBC  # return completed barcode


# --------------------  Image Search  ------------------------------------
def searchImage(searchCode, database):
    # Searches through list of barcodes to find index of most similar barcode
    # Displays the original and result to user
    # Determines if search was successful

    bestMatch = -1

    # loops through all barcodes in database and identifies closest match to searched through comparing values at index
    for code in range(len(barcodes)):  # For each barcode in list of barcodes
        match = 0

        for index in range(len(barcodes[code])):  # For each index of the barcode

            # Check if value at index is same between both codes
            if barcodes[code][index] == searchCode[index]:
                match += 1  # Increment match

        # If barcode has best match and is not 100% match (itself)
        if match >= bestMatch and match != len(barcodes[code]):
            bestMatch = match  # assign match as best
            similar = code  # save index of code

    # save location of original and found images
    original = cv2.imread(testImg, cv2.IMREAD_GRAYSCALE)
    result = cv2.imread(database[similar], cv2.IMREAD_GRAYSCALE)

    cv2.imshow("Result", np.hstack((original, result)))  # Displays images side by side
    cv2.waitKey(0)  # delay for user input

    # Check if original and found images are in same directory
    # Used in determining success rate
    if os.path.dirname(database[similar]) == os.path.dirname(testImg):
        return 1    # if true return 1
    else:
        return 0    # if false return 0


# -------------------   Image Rotation  --------------------------------
def rotateImage(image, angle):
    # Converts image to Greyscale, Matrix form
    # Rotates image by desired angle

    imgMat = cv2.imread(image, cv2.IMREAD_GRAYSCALE)  # Converts image to Grayscale, Matrix Form
    rows, cols = imgMat.shape  # Set rows and cols = to rows and cols of img matrix

    # Create rotation transformation matrix about centre, rotating by desired angle
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)

    # Apply transformation matrix to img
    rotated = cv2.warpAffine(imgMat, M, (cols, rows))

    # Return img in matrix form after rotation
    return rotated


# --------------------  Main   ----------------------------------------

# Creates list of all files in search database
path = "MNIST_DS/"
dirs = os.listdir(path)

allFiles = []

for folder in dirs:
    subFolder = path + folder
    for file in os.listdir(subFolder):
        allFiles.append(subFolder + '/' + file)

# generate a barcode for each file
barcodes = []
for i in range(len(allFiles)):  # For each file
    barcodes.append(generateBarcode(allFiles[i]))  # add the generated barcode to list of barcodes

success = 0  # Initialize success

# For each image in file list
for testImg in allFiles:
    testCode = generateBarcode(testImg)  # generate barcode for image

    success += searchImage(testCode, allFiles)  # Search barcode, increment success if search is correct

print("success rate: ", success, "%")  # output success rate
