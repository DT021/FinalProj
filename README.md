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

The C++ implementation (KMeans.h) is practically identical, except all instances of numpy arrays
are replaced with a vector of some kind of number, as above.

## Demonstrations
stockDemo.py allows a user to input a stock ticker. It then pulls data from the Yahoo API, 
determines four parameters -- volatility by price, volatility by volume, slope from linear 
regression on price, and slope from linear regression on 10-day moving averages -- classifies 
it based on known data, and plots the given ticker with the tickers used to train our algorithm.

run.sh compares the runtime and results (percent error, group centers, etc.) of all
of the algorithms from each implementation and pipes them to various txt files to be plotted and analyzed.

Our analysis of timing and error for the elements of our library (KNN, K Means Clustering, Linear Regression)
can all be found in the Statistics folder as PNG images.

## Known Issues
Currently, decreasing data wreaks havoc on our linear regression algorithms. We believe that 
learning rate adjustment based on average slope may be a solution.

Our K-Means implementations may output bad group centers depending on what the group centers 
were randomly initialized to. While this is a problem inherent to the K-Means algorithm, we 
feel it is important for users to know that this is a possible outcome and simply requires 
additional runs (and perhaps a bit of good luck).

In the stocksData.py demonstration, it may be difficult to spot the user's point among the 
rest of the data, but we assure you that it is there.

## Useful Commands
Note: run all programs from the root directory with appropriate relative paths
Note: most programs and scripts are used for setup and are presented here in the order to be
run for a new ground-up data set analysis; some stock ticker pulling commands have been omitted
for brevity.

### Setup Commands:

python3 Setup/iterData.py 
	This command pulls specified stock data from the S&P 500 list of tickers into CSV files.

python3 Parameters/collectData.py
	This command parses all CSV files and computes parameters that are written to a params.txt file
	in the Parameters folder.

python3 Parameters/split.py
	This command performs a 70/30 split of the params.txt data into training and testing files
	trainParams.txt and testParams.txt in the Parameters folder.

### Demo/Analysis:

python3 stockDemo.py
	This command prompts the user to input a ticker for analysis and plotting against all of the
	training data pre-loaded into our repo databank by the setup code.

./ShellScript/run.sh
	This bash script performs timing and accuracy analysis of KNN as well as timing analysis of 
	K Means Clustering for each implementation over a range of K 1:100 and then writes the 
	data to a series of files to be plotted by our python plotting scripts

python3 KNN/KNNErrorGraph.py
	This command plots the KNN accuracy error over the K range for each implementation

python KNN/KNNTiming.py
	This command plots the KNN timing over the K range for each implementation
