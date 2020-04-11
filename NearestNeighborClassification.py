#Please put your code for Step 2 and Step 3 in this file.

"""
Name: Kennedy May
Collaboration:
Hours Spent: 2 hours
"""


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS

#this function takes no parameters and opens the data file and returns the
# 3 arrays of data
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

#this function takes 3 parameteres and normalizes (0-1) all the data so that 
#we can conpare them against each other
def normalizeData(glucose, hemoglobin, classification):
    glucose_scaled = []
    hemoglobin_scaled = []
    for g in glucose:
        glucose_scaled.append((g - 70)/(490-70))
    for h in hemoglobin:
        hemoglobin_scaled.append((h- 3.1)/(17.8-3.1))
    glucose_scaled = np.array(glucose_scaled)
    hemoglobin_scaled  = np.array(hemoglobin_scaled)
    return glucose_scaled, hemoglobin_scaled, classification
   
#this function takes 3 parameters and graphs them, depending on the
#classification makes the color of the dot, this function then returns the plot
def graphData(glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Glucose and Hemoglobin")
    plt.legend()
    return plt.show()

#this function takes no parameters but creates two random numbers both 
#being assigned newglucose and newhemoglobin, then returns this values
def createTestCase():
    newhemoglobin = random.random()
    newglucose = random.random()
    return newhemoglobin, newglucose

#this function takes 4 parameters and creates a distance array
#filled with the distances from the newglucose and newhemoglobin 
#from each of the glucose and hemoglobin values
def calculateDisatanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    distance = np.sqrt(((newhemoglobin-hemoglobin)**2)+(newglucose-glucose)**2)
    return distance

#this fucntion takes 5 parameters and 
def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    min_index = np.argmin(distance)
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification, nearest_class):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot([newhemoglobin], [newglucose], marker = 'o', markersize = 5, color = 'purple')
    #plt.plot(newhemoglobin[nearest_class==1],newglucose[nearest_class==1], maker = "o", makersize = 5, color = "black", label = "Class 1")
    #plt.plot(newhemoglobin[nearest_class==0],newglucose[nearest_class==0], maker = "o", makersize = 5, color = "red", label = "Class 2")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Glucose and Hemoglobin")
    plt.legend()
    plt.show()
    
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    zeros = 0
    ones = 0
    classMajority = 0
    sorted_indices = np.argsort(distance)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    for i in k_classifications:
        if i == 0:
            zeros = 1 + zeros
        if i == 1:
            ones = 1 + ones
    if ones > zeros:
        classMajority = 1.0
    else:
        classMajority = 0.0
    return k_classifications, classMajority


# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()

glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)

graphData(glucose, hemoglobin, classification)

newglucose, newhemoglobin = createTestCase()

distance = calculateDisatanceArray(newglucose, newhemoglobin, glucose, hemoglobin)

nearest_class = nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)

graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification, nearest_class)

k_classifications, classMajority = kNearestNeighborClassifier(15, newglucose, newhemoglobin, glucose, hemoglobin, classification)













