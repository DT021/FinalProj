#!/bin/bash

echo Starting to bash...

rm KNN/kError.txt

for K in {1..100..1}

do
	echo Running $K Nearest Neighbor...

	g++ -o ./KNN/KNN ./KNN/KNN.cpp

	cat Parameters/trainParams.txt Parameters/testParams.txt | ./KNN/KNN $K >> KNN/kError.txt

	python2 KNN/KNNTest.py $K >> KNN/kError.txt
done

unset K

echo Bashed...
