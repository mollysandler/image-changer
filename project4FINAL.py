#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:09:20 2021

@author: mollysandler
"""
#takes name of file being read
inputFile = input('please enter the name of the file you want to use: ')
#takes name of file being printed on 
outputFile = input('please enter an output file name: ')
#appends everything to output file
open(outputFile, 'a')

command = input('please enter one of the following commands: negate, high contrast, grayscale, remove <color> where <color> is "red", "green", or "blue:" ') 

#defines function that makes it negative DONE
def negate_image(inputFile, outputFile):
    line = 0
    #splits text file into four separate rows - top three lines and all the pixels 
    for row in file1:
        each = row.split()
        newImage = " "
        #writes first three rows as they are in the original file (are a PPM necesessity)
        if line < 3:
            file2.write(row)
            line = line + 1
        else:
            #writes value of remaning rows subtracted from 255 to get the negative
            for i in range(len(each)):
                #changes value 
                each[i] = abs(int(each[i]) - 255)
                #adds each value to the current string 
                newImage = newImage + str(each[i]) + " "
                #writes it in the file
            file2.write(newImage)
    
#defines function that makes it high contrast DONE
def high_contrast_image(inputFile, outputFile):
    line = 0
    #splits text file into four separate rows - top three lines and all the pixels 
    for row in file1:
        each = row.split()
        newImage = " "
        #writes first three rows as they are in the original file (are a PPM necesessity)
        if line < 3:
            file2.write(row)
            line = line + 1
        else:
            #writes value of remaning rows as either 255 or 0 depending on their current value 
            for i in range(len(each)):
                #changes values 
                if int(each[i]) > 127:
                    each[i] = 255                        
                else:
                    each[i] = 0
                    #adds each value to the current string
                newImage = newImage + str(each[i]) + " "
                #writes it on the file
            file2.write(newImage)
    
#defines function that makes it grayscale DONE
def gray_scale_image(inputFile, outputFile):
    line = 0
    #splits text file into four separate rows - top three lines and all the pixels 
    for row in file1:
        each = row.split()
        newImage = " "
        #writes first three rows as they are in the original file (are a PPM necesessity)
        if line < 3:
            file2.write(row)
            line = line + 1
        else:
            #writes value of remaning rows as the average of each triplet of pixels to get a grayscale iamge
            i = 0
            while i < len(each):
                #gets total of each RGB value in each pixel
                total = []
                total.extend((int(each[i]), int(each[i + 1]), int(each[i + 2])))
                #finds average of list total 
                avg = int(sum(total) / len(total))
                each[i] = avg
                #prints average three times as all of the values
                newImage = newImage + str(each[i]) + " "
                each[i + 1] = avg
                newImage = newImage + str(each[i + 1]) + " "
                each[i + 2] = avg
                newImage = newImage + str(each[i + 2]) + " "
                #moves on to the next triplet of values
                i = i + 3
                #writes it in the file
            file2.write(newImage)

#defines function that removes every red pixel DONE
def remove_red_image(inputFile, outputFile): #first in triplet
    line = 0    
    #splits text file into four separate rows - top three lines and all the pixels 
    for row in file1:
        each = row.split()
        newImage = " "
        #writes first three rows as they are in the original file (are a PPM necesessity)
        if line < 3:
            file2.write(row)
            line = line + 1
        else:
            #writes value of remaning rows as their current value, with the first of each triplet being a 0 
            i = 0
            while i < len(each):
                #makes first value zero (red value in RGB)
                each[i] = 0
                #keeps rest of values the same 
                newImage = newImage + str(each[i]) + " "
                each[i + 1] = each[i + 1]
                newImage = newImage + str(each[i + 1]) + " "
                each[i + 2] = each[i + 2]
                newImage = newImage + str(each[i + 2]) + " "
                #moves on to the next triplet
                i = i + 3
               #writes it in the files 
            file2.write(newImage)

    
#defines function that removes every green pixel
def remove_green_image(inputFile, outputFile): #second in triplet
    line = 0
    #splits text file into four separate rows - top three lines and all the pixels 
    for row in file1:
        each = row.split()
        newImage = " "
        #writes first three rows as they are in the original file (are a PPM necesessity)
        if line < 3:
            file2.write(row)
            line = line + 1
        else:
            #writes value of remaning rows as their current value, with the second of each triplet being a 0 
            i = 0
            while i < len(each):
                #keeps first value the same
                each[i] = each[i]
                #makes second value zero 
                newImage = newImage + str(each[i]) + " "
                each[i + 1] = 0
                newImage = newImage + str(each[i + 1]) + " "
                #keeps third value the same
                each[i + 2] = each[i + 2]
                newImage = newImage + str(each[i + 2]) + " "
                #moves on to the next triplet
                i = i + 3
                #writes it in the file
            file2.write(newImage)

#defines function that removes every blue pixel DONE
def remove_blue_image(inputFile, outputFile): #third in triplet
    line = 0
    #splits text file into four separate rows - top three lines and all the pixels 
    for row in file1:
        each = row.split()
        newImage = " "
        #writes first three rows as they are in the original file (are a PPM necesessity)
        if line < 3:
            file2.write(row)
            line = line + 1
        else:
            #writes value of remaning rows as their current value, with the third of each triplet being a 0 
            i = 0
            while i < len(each):
                #keeps first two values the same
                each[i] = each[i]
                newImage = newImage + str(each[i]) + " "
                each[i + 1] = each[i + 1]
                newImage = newImage + str(each[i + 1]) + " "
                #makes third value zero
                each[i + 2] = 0
                newImage = newImage + str(each[i + 2]) + " "
                i = i + 3
                #writes it on the file
            file2.write(newImage)  
                
#opens files
file1 = open(inputFile, "r")
file2 = open(outputFile, "w")

#calls function per each command given by the user 
if "negate" in command:
    negate_image(inputFile, outputFile)
elif "contrast" in command:
    high_contrast_image(inputFile, outputFile)
elif "gray" in command:
    gray_scale_image(inputFile, outputFile)
elif "red" in command:
    remove_red_image(inputFile, outputFile)
elif "green" in command:
    remove_green_image(inputFile, outputFile)
elif "blue" in command:
    remove_blue_image(inputFile, outputFile)

#closes files
file1.close()
file2.close()
