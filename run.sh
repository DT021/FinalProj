#!/bin/bash

echo Starting to bash...

rm params.txt

python2 Parameters/parMain.py

./KNN/KNN < params.txt 3

echo Bashed...
