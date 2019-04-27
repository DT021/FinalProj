#!/bin/bash

echo Starting to bash...

#rm KNN/kError.txt
#rm KNN/KNNTiming.txt
rm KMeansClustering/KMCTiming.txt
g++ -std=c++11 -o ./KNN/KNN ./KNN/KNN.cpp
g++ -std=c++11 -o ./KMeansClustering/KMeansTest ./KMeansClustering/KMeansTest.cpp

for K in {1..100..1}

do
	echo Running $K Nearest Neighbor...

#	cat Parameters/trainParams.txt Parameters/testParams.txt | ./KNN/KNN $K >> KNN/kError.txt 2>> KNN/KNNTiming.txt

#	python3 KNN/KNNTest.py $K >> KNN/kError.txt


	./KMeansClustering/KMeansTest $K >> KMeansClustering/KMCTiming.txt

#	python3 KMeansClustering/KMeans.py $K >> KMeansClustering/KMCTiming.txt

	python3 KMeansClustering/KMeansTest.py $K >> KMeansClustering/KMCTiming.txt

done

unset K

echo Bashed...
