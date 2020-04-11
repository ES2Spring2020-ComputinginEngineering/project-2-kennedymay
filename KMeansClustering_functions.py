#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random


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


def select(k):
    random_centroids = np.random.random((k, 2))
    return random_centroids


def assign(random_centroids, glucose, hemoglobin):
    s = random_centroids.shape[0]
    distances = np.zeros((s, (len(glucose))))
    assigned_centroids = np.zeros((len(glucose)))
    for i in range(s):
        h = random_centroids[i,0]
        g = random_centroids[i,1]
        distances[i] = np.sqrt(((h-hemoglobin)**2)+(g-glucose)**2)
    assigned_centroids = np.argmin(distances, axis = 0)
    return assigned_centroids, distances


def update(k, assigned_centroids, glucose, hemoglobin):
    updated_centroids = np.zeros((k,2))
    centroid_hemo = np.zeros((1))
    centroid_glu = np.zeros((1))
    for i in range(updated_centroids.shape[0]):
        centroid_hemo = np.mean(hemoglobin[assigned_centroids == i])
        centroid_glu = np.mean(glucose[assigned_centroids == i])
        updated_centroids[i] = np.append(centroid_hemo, centroid_glu) 
    return updated_centroids
    

def iterate(k, run_times):
    glucose, hemoglobin, classification = openckdfile()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
    updated_centroids = select(k)
    while run_times != 0:
        assigned_centroids, distances = assign(updated_centroids, glucose, hemoglobin)
        updated_centroids = update(k, assigned_centroids, glucose, hemoglobin)
        run_times = run_times - 1
    return assigned_centroids, updated_centroids, glucose, hemoglobin, classification


def graphingKMeans(glucose, hemoglobin, assigned_centroids, updated_centroids):
    plt.figure()
    for i in range(assigned_centroids.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assigned_centroids==i],glucose[assigned_centroids==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(updated_centroids[i, 0], updated_centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
    
def calculate_postives_negatives(classification, assigned_centroids):
    truepositives = 0
    falsepositives = 0
    truenegatives = 0
    falsenegatives = 0
    CKD = 0
    noCKD = 0 
    for i in range(158):
        if classification[i] == assigned_centroids[i] == 0:
            truepositives = truepositives + 1
            CKD = CKD + 1
        elif classification[i] == 1 and assigned_centroids[i] == 0:
            falsepositives = falsepositives + 1
            noCKD = noCKD + 1
        elif classification[i] == assigned_centroids[i] == 1:
            truenegatives = truenegatives + 1
            noCKD = noCKD + 1
        elif classification[i] == 0 and assigned_centroids[i] == 1:
            falsenegatives = falsenegatives + 1
            CKD = CKD + 1
    return truepositives, falsepositives, truenegatives, falsenegatives, CKD, noCKD

def calculate_percentages(truepositives, falsepositives, truenegatives, falsenegatives, CKD, noCKD):
    percentage_truepostives = "Percentage of True Positves:" + str((truepositives/CKD)*100) + "%"
    percentage_falsepositives = "Percentage of False Positives:" + str((falsepositives/noCKD)*100) + "%"
    percentage_truenegatives = "Percentage of True Negatives:" + str((truenegatives/noCKD)*100)+ "%"
    percentage_falsenegatives = "Percentage of False Negatives:" + str((falsenegatives/CKD)*100)+ "%"
    return percentage_truepostives, percentage_falsepositives, percentage_truenegatives, percentage_falsenegatives
    

