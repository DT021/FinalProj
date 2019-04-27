#!/bin/bash

echo Starting to bash...

echo Please input K value greater than 0...

read K

echo $K Nearest Neighbor...



g++ -o ./KNN/KNN ./KNN/KNN.cpp

cat Parameters/trainParams.txt Parameters/testParams.txt | ./KNN/KNN $K

python2 KNN/KNNTest.py $K

unset K

echo Bashed...
