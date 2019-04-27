#!/bin/bash

echo Starting to bash...

echo 5th Nearest Neighbor...

g++ -o ./KNN/KNN ./KNN/KNN.cpp

cat Parameters/trainParams.txt Parameters/testParams.txt | ./KNN/KNN 5

#python2 KNN/KNNTest.py

echo Bashed...
