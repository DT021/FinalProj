#!/bin/bash

echo Starting to bash...

#rm params.txt
#rm irisTrain.txt
#rm irisTest.txt

#python2 Parameters/parMain.py

#python2 irisPull.py

#./KNN/KNN < params.txt 3

echo 5th Nearest Neighbor...

#python2 KNN/KNNTest.py

g++ -o ./KNN/KNN ./KNN/KNN.cpp

cat Parameters/train.txt Parameters/test.txt | ./KNN/KNN 5

python2 KNN/KNNTest.py

echo Bashed...
