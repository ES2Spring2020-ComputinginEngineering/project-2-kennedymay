This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).


Kennedy May Project 2


Instructions on running code.

NearestNeighborClassification.py:
To run this code the file simply just needs to be run. Once the file is run it should produce two graphs, the K-Nearest Neighbor Classifications and the Nearest Neighbor Classification. The first graph is without the test case and the second graph has the test case. This test case is classified in the key, by using Nearest Neighbor. 

KMeansClustering_Functions.py:
This file does not need to be run, it just contains the functions that will be used in the driver function. This function contains nine functions. This file will produce one graph displaying the data, each cluster is color coded a different color and has a key to say which centroid is which. It also calculates the percentages of true and false positives and negatives. 

KMeansClustering_Driver.py:
To run this code look for the letter k and the variable run_times. K is the number of centroids/cluster you want to be made and run_times is the amount of times you want the centroid array to be updated. Once this file is run the graph should be displayed and the percentages should be saved as variables and the values should be printed.  

K-Means Clustering Algorithm:

def openckdfile():
This function opens the file and allows us to read the data. It takes no parameters, but returns 3 arrays, the glucose, hemoglobin, and classification.

def normalizeData(glucose, hemoglobin, classification):
This function takes 3 arrays as parameters and returns the normalized values for these arrays. 

def select(k):
This function takes one parameter, and that parameter is the number of random centroids that will be made. This function returns an array of random centroid points

def assign(random_centroids, glucose, hemoglobin):
This function takes three parameters, the parameters are an array of centroids, and the glucose and hemoglobin data values. This function calculates the distance between each point and the each centroid and puts all those values into an array. Then another array is made that is filled with assignments of each data point to a certain centroid. These assignments are found by finding the shortest distance. The assignment array is returned.


def update(k, assigned_centroids, glucose, hemoglobin):
This function takes 4 parameters, k which is the number of centroids, assigned_centroids which is the array that is returned from the previous function, glucose and hemoglobin which are just data values. In this function the mean values in each centroid group are found and update the centroid points. These updated centroid points are returned.


def iterate(k, run_times):
This function takes 2 parameters, k which is the used in select and update, and run times which is the amount of times assign and update will be run. In this function all the previous functions are called. openckdfile(), normalizeData(), and select() are all called once and then the assigned_centroids() and updated_centroids() are run the amount of times that the function is sent. After all these functions are run, the assigned centroid array, the updated centroid array, the glucose and hemoglobin array, and the classification array are all returned.


def graphingMeans(glucose, hemoglobin, assigned_centroids, updated_centroids):
In this function a graph is produced. This graph shows the clusters and centroids that the data has. It does not return anything, void function


def calculate_positives_negatives(classification, assigned_centroids):
This function has two parameters, classification and assigned centroids. Classification were the reading given from the data file and assigned_centroids are the reading that were produced from the code. In this function the truepositves, truenegatives, falsepositives, falsenegatives, CKD and noCKD values are all calculated and then returned.  


def calculate_percentages(truepositives, falsepositives, truenegatives, falsenegatives, CKD, noCKD):
This function has 6 parameters. In this function it strictly turns the values that were produced in the previous function into percentages. It then returns these four percentages.

















