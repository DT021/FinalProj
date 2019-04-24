#!/bin/bash

echo Starting to bash...

#python2 Parameters/parMain.py

#python2 irisPull.py

#./KNN/KNN < params.txt 3

echo 5th Nearest Neighbor...

#python2 KNN/KNNTest.py

python2 studentPull.py

python2 Parameters/studentMain.py

g++ -o ./KNN/KNN ./KNN/KNN.cpp

cat Parameters/train.txt studentParams.txt | ./KNN/KNN 5

python2 KNN/studentKNNTest.py

echo Bashed...
