# A Load of MLarky
Written by Daniel Burns, Matthew Jones, and Alex Twilla

## Summary
For our COSC 307 final project, we wrote a small machine learning library in Python and C++ and 
tested our algorithms on various data, most notably stocks. The algorithms we 
wrote in this library are basic linear regression, k-nearest neighbor classification, 
and K-Means clustering. On top of this, there are comparisons in performace between our 
implementations and corresponding algorithms in the popular scikit Python library.

## Linear Regression
Our Python implementation of linear regression (linReg.py) is a class whose init function 
requires two one dimensional numpy arrays -- x and y training data. To produce the estimated 
line equation, call .fitData(). The learning rate (alpha) and number of epochs 
can be adjested as the user sees fit, but the error from the model can be quite 
sensitive to the learning rate. To obtain a prediction based on the created linear 
model, call .predict(xTest), where xTest is a 1D numpy array with test x points.

The C++ implementation (linReg.h) is nearly identical, except all instances of numpy arrays are 
instead vecotrs of floats, and there are addtional functions for acquiring data about 
the created linear model. More details can be found in the files mentioned above.

## K-Nearest Neighbor Classification
Our Python implementation of KNN (KNN.py) is a class whose init function requires a 2D 
numpy array of coordinates to serve as the independent variables and a 1D numpy array of 
dependent variables, i.e. classes. To classify a set of independent variables, call .classify(x)
where x is a 2D numpy array with dimensions that match those of the training data.

The C++ implementation (KNN.h) is almost identical to the Python implementation except all x 
arrays are instead vectors of vectors of floats. More details can be found in the files 
mentioned above.

## K-Means Clustering
The purpose of clustering is to determine potential center points of groups on a given set 
of data without necessarily knowing the boundaries of those groups or if distinct groups 
even exist.

The Python implementation of KMeans (KMeans.py) functions much like KNN, but there is no 
given classification. The constructor of this class takes a 2D numpy array of coordinates. 
The .cluster() method executes the KMeans algorithm and produces the estimated group centers.
The user can determine how many group centers to determine as well as the number of epochs 
to change the group centers.

The C++ implementation (KMeans.h) practically identical, except all instances of numpy arrays 
are replaced with a vector of some kind of number, as above.

## Demonstrations
stockDemo.py allows a user to input a stock ticker. It then pulls data from the Yahoo API, 
determines four parameters -- volatility by price, volatility by volume, slope from linear 
regression on price, and slope from linear regression on 10-day moving averages -- classifies 
it based on known data, and plots the given ticker with the tickers used to train our algorithm.

algoCompare.sh compared the runtime and results (percent error, group centers, etc.) of all 
of the algorithms from each implementation.

## Known Issues
Currently, decreasing data wreaks havoc on our linear regression algorithms. We believe that 
learning rate adjustment based on average slope may be a solution.

Our K-Means implementations may output bad group centers depending on what the group centers 
were randomly initialized to. While this is a problem inherent to the K-Means algorithm, we 
feel it is important for users to know that this is a possible outcome and simply requires 
additional runs (and perhaps a bit of good luck).