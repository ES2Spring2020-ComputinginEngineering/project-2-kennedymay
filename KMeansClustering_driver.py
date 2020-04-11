#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions


glucose, hemoglobin, classification = kmc.openckdfile()

glucose, hemoglobin, classification = kmc.normalizeData(glucose, hemoglobin, classification)

assigned_centroids, updated_centroids, glucose, hemoglobin, classification = kmc.iterate(2, 50)

kmc.graphingKMeans(glucose, hemoglobin, assigned_centroids, updated_centroids)

truepositives, falsepositives, truenegatives, falsenegatives, CKD, noCKD = kmc.calculate_postives_negatives(classification, assigned_centroids)

percentage_truepostives, percentage_falsepositives, percentage_truenegatives, percentage_falsenegatives = kmc.calculate_percentages(truepositives, falsepositives, truenegatives, falsenegatives, CKD, noCKD)








