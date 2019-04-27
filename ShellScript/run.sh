#!/bin/bash

echo Starting to bash...

#rm KNN/kError.txt
#rm KNN/KNNTiming.txt
rm KMeansClustering/KMCTiming.txt

for K in {1..100..1}

do
	echo Running $K Nearest Neighbor...

#	g++ -o ./KNN/KNN ./KNN/KNN.cpp

#	cat Parameters/trainParams.txt Parameters/testParams.txt | ./KNN/KNN $K >> KNN/kError.txt 2>> KNN/KNNTiming.txt

#	python2 KNN/KNNTest.py $K >> KNN/kError.txt

#	g++ -o ./KMeansClustering/KMeansTest ./KMeansClustering/KMeansTest.cpp

	./KMeansClustering/KMeansTest $K >> KMeansClustering/KMCTiming.txt

	python2 KMeansClustering/KMeans.py $K >> KMeansClustering/KMCTiming.txt

	python2 KMeansClustering/KMeansTest.py $K >> KMeansClustering/KMCTiming.txt

done

unset K

echo Bashed...
