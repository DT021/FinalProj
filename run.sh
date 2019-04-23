#!/bin/bash

echo Starting to bash...

rm params.txt
rm irisTrain.txt
rm irisTest.txt

python2 Parameters/parMain.py

python2 irisPull.py

#./KNN/KNN < params.txt 3

echo 3rd Nearest Neighbor...

python2 KNN/KNNTest.py

g++ -o ./KNN/KNN ./KNN/KNN.cpp

cat irisTrain.txt irisTest.txt |./KNN/KNN 3

echo Bashed...
