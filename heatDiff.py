# FSUID cjh17h
# Written by Cameron Heffelfinger on July 25th, 2019
# Program simulates heat distribution using a 2d matrix and plotting to a graph
# using pyplot

from numpy import *
import numpy as np
import matplotlib.pyplot as mp

'''
Temperature Formula
temp[i,j]= 1/4(oldTemp[i−1,j]+oldTemp[i+1,j]+oldTemp[i,j−1]+oldTemp[i,j+1])
'''


startingTemp = int(input("Enter the starting temperature:"))

# Initializes an array with startingTemp dimensions with zeroes plus the halo columns and rows surrounding it
oldArray = np.zeros((startingTemp+2)**2).reshape(startingTemp+2, startingTemp+2)

# Sets the left column values to startingTemp
for i in range(len(oldArray)):
    oldArray[i, 0] = startingTemp

newArray = np.zeros((startingTemp+2)**2).reshape(startingTemp+2, startingTemp+2)

# isnotequal bool and iteration will be used to determine when to stop the loop
# if the matrices are equal between two iterations, it terminates
# or if it hits iteration 3000
isnotequal = True
iteration = 0
while isnotequal == True:
    for i in range(len(newArray)):
        for j in range(len(newArray)):
            # I used try blocks to catch arrayindex out of bounds errors,
            # Whenever one of these occurs it simply replaces it with a zero
            # Also note: this is equivalent to the temperature formula given,
            # I simply calculate all of the 4 oldtemp parts of the equation individually
            # So I can make use of try blocks
            try:
                oldPart1 = oldArray[i-1, j]
            except IndexError:
                oldPart1 = 0
            try:
                oldPart2 = oldArray[i+1, j]
            except IndexError:
                oldPart2 = 0
            try:
                oldPart3 = oldArray[i, j-1]
            except IndexError:
                oldPart3 = 0
            try:
                oldPart4 = oldArray[i, j+1]
            except IndexError:
                oldPart4 = 0
            # Input our values into the temperature formula to get the temp of the cell
            newArray[i, j] = 1/4*(oldPart1 + oldPart2 + oldPart3 + oldPart4)

            # Note: index startingTemp + 1 is the last element in the array (the Halo Cells)
            # Ensuring that all the halo cells remain zero or if theyre the leftmost column,
            # then their value is starting temp
            if (i == 0 and j != 0) or (i == startingTemp+1 and j != 0):
                newArray[i, j] = 0
            elif (i == 0 and j == 0) or (i == startingTemp+1 and j == 0):
                newArray[i, j] = startingTemp
            elif j == 0:
                newArray[i, j] = startingTemp
            elif j == startingTemp+1:
                newArray[i, j] = 0

    oldArray = newArray
    newArray = np.zeros((startingTemp + 2) ** 2).reshape(startingTemp + 2, startingTemp + 2)
    iteration += 1
    if (oldArray == newArray).all() or iteration == 3000:
        isnotequal = False

# Here I will take a slice of the final array product without the halo cells included

finalArray = np.zeros(startingTemp**2).reshape(startingTemp, startingTemp)
for i in range(len(oldArray)):
    for j in range(len(oldArray)):
        if i != 0 and j != 0 and i != startingTemp+1 and j != startingTemp+1:
            finalArray[i-1][j-1] = oldArray[i][j]

# Now finalArray holds our finished data for the heat dispersion, time to plot it

#print("The old array\n", oldArray)

#print("The final array\n", finalArray)

#mp.plot(finalArray)

mp.imshow(finalArray, cmap='hot', interpolation='nearest')
mp.gca().invert_yaxis()
mp.show()








