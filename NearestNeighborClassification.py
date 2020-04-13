#Please put your code for Step 2 and Step 3 in this file.



"""
Name: Kennedy May
Collaboration: none, office hours w/ Jenn
Hours Spent: 2 hours
"""

#IMPORT STATEMENTS
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



#this fucntion takes 5 parameters and classfies the newglucose and 
#newhemoglobin to either class 1 or 0 depending on which point it is closer to
#and then returns that value
def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    min_index = np.argmin(distance)
    nearest_class = classification[min_index]
    return nearest_class



#This function takes 6 paramters and returns nothing. This function 
#graphs all the points of hemoglobin and glucose and the new point created
#with the nearest_class shown in key
def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification, nearest_class):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot([newhemoglobin], [newglucose], marker = 'o', markersize = 5, color = 'purple', label = "Class " + str(nearest_class))
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Glucose and Hemoglobin w/Test Case")
    plt.legend()
    plt.show()
    
    
#this function takes 6 parameters, it takes k which is the number of points
#the newhemoglobin and newglucose are being compared to, 
#it returns the classficiations of each of the points that newhemoglobin 
#and newglucose are compared to and finds the majority within
#the kclassifications array and returns that value
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    sorted_indices = np.argsort(distance)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    classMajority = np.median(k_classifications)
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

print("Class from K-Nearest Neighbor: " + str(k_classifications))
print("Class from Nearest Neighbor: " + str(nearest_class) )













