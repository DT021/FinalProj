// MLarky.h Header File for all C++ Algorithm Implementations; K Means Cluster, K Nearest Neighbor, Linear Regression

#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <cmath>
#include <time.h>
#include <cstdio>
#include <string>
#include <set>
#include <math.h>
#include <limits>
#include <chrono>

// K Means Cluster Algorithm; C++ Implementation

using namespace std;

template <typename T>
class KMeansCluster {

	T data;
	int dimensions;
	vector<vector<float> > groupCenters;
	vector<int> groups;

	public:
		KMeansCluster(T data);
		void cluster(int numGroups, int epochs);
		void printGroupCenters();
		void printGroups();
};

template <typename T>
KMeansCluster<T>::KMeansCluster(T testData) {
	this->data = testData;
	this->dimensions = data[0].size();
	this->groups.resize(data.size());

	srand(time(NULL));
}

template <typename T>
void KMeansCluster<T>::cluster(int numGroups, int epochs) {

	// Reset groupCenters and initialize to random points.
	this->groupCenters.resize(0);

	for (int i = 0; i < numGroups; i++) {
		this->groupCenters.push_back(vector<float>());

		for (int j = 0; j < this->data[0].size(); j++) {
			this->groupCenters[i].push_back(rand() % 5);
		}
	}

	for (int epoch = 0; epoch < epochs; epoch++) {

		// Determine which group each point is closest to.
		for (int point = 0; point < data.size(); point++) {
			multimap<float, int> centerDistances;
			
			// Determine distance from each group.
			for (int i = 0; i < groupCenters.size(); i++) {
				float centerDistance = 0;

				for (int j = 0; j < groupCenters[i].size(); j++) {
					centerDistance += pow((data[point][j] - groupCenters[i][j]), 2);
				}

				centerDistance = sqrt(centerDistance);
				centerDistances.insert(make_pair(centerDistance, i));
			}

			groups[point] = centerDistances.begin()->second;
		}

		// For each group, determine how many points belong to it, and sum all 
		// vectors in that group.
		for (int group = 0; group < groupCenters.size(); group++) {
			float numInGroup = 0;
			vector<float> pointSums(data[0].size(), 0); 

			for (int i = 0; i < groups.size(); i++) {

				if (groups[i] == group) {
					numInGroup++;

					for (int j = 0; j < data[i].size(); j++) {
						pointSums[j] += data[i][j];
					}
				}
			}


			// Set group center to the average of all points currently in group.
			for (int i = 0; i < groupCenters[group].size(); i++) {

				if (numInGroup) {
					groupCenters[group][i] = pointSums[i] / numInGroup;
				}
			}
		}	
	}
}

template <typename T>
void KMeansCluster<T>::printGroupCenters() {

	for (int i = 0; i < groupCenters.size(); i++) {

		for (int j = 0; j < groupCenters[i].size(); j++) {
			cout << groupCenters[i][j] << " ";
		}
		cout << endl;
	}
}

template <typename T>
void KMeansCluster<T>::printGroups() {
	for (int i = 0; i < groups.size(); i++) {
		cout << groups[i] << endl;
	}
}


// K Nth Nearest Neighbor Algorithm; C++ Implementation 

// Calculates euclidean distance between two points based on parameters
double getDistance(vector<double> staticPoint, vector<double> movingPoint){

        double dist = 0;
        for(unsigned int i = 0; i < staticPoint.size(); i++){
		dist += pow(movingPoint[i]-staticPoint[i], 2);
	}
        dist = sqrt(dist);

        return dist;
}

// Define class for KNN
class KNNClassifier{
	public:
	
	int k;
	vector< vector<double> > xTrain;
	vector<string> yTrain;
	set<string> classifications;

	KNNClassifier(vector< vector<double> > xTrain, vector<string> yTrain, int k);
	void getClassifications();
	void addData(vector< vector<double> > newX, vector<string> newY);
	void clearData(vector< vector<double> > newX = {}, vector<string> newY = {});
	vector<string> classify(vector< vector<double> > testX);
	void print();
};

// Constructor
KNNClassifier::KNNClassifier(vector< vector<double> > xTrain, vector<string> yTrain, int k){
	
	this->xTrain = xTrain;
	this->yTrain = yTrain;
	this->k = k;
	getClassifications();
}

// Rip all of the classification tags from the training data set and store them
void KNNClassifier::getClassifications(){
	
	for(unsigned int i = 0; i < yTrain.size(); i++){
		if(classifications.find(yTrain[i]) == classifications.end()){
			classifications.insert(yTrain[i]);
		}
	}
	return;
}

// Add new data sets for training
void KNNClassifier::addData(vector< vector<double> > newX, vector<string> newY){
	
	for(unsigned int i = 0; i < newX.size(); i++){
		xTrain.push_back(newX[i]);
	}

	for(unsigned int j = 0; j < newY.size(); j++){
		yTrain.push_back(newY[j]);
	}

	getClassifications();

	return;
}

// Clear all current training data vectors
void KNNClassifier::clearData(vector< vector<double> > newX, vector<string> newY){
	
	xTrain.clear();
	yTrain.clear();
	xTrain = newX;
	yTrain = newY;
	classifications.clear();
	getClassifications();
	
	return;
}

// Classify each point in the test data set via distance function and return vector of classification strings
vector<string> KNNClassifier::classify(vector< vector<double> > testX){
	
	vector<string> classes;

	// The distances from the current test point are stored in a multimap so that finding the lowest five distances is a breeze
	multimap<double, string> distances;
	map<string, double> votes;

	// Calculate all point distances of training data to test data for EACH test data point
	for(unsigned int i = 0; i < testX.size(); i++){
		
		distances.clear();
		votes.clear();

		for(unsigned int j = 0; j < xTrain.size(); j++){
			double dist = getDistance(testX[i], xTrain[j]);
			distances.insert(pair<double, string>(dist, yTrain[j]));
		}
	
		multimap<double, string>::iterator mmit = distances.begin();
		int counter = 0;

		// Count the classification votes from each of the five closest distanced training points
		while(counter < k){
			votes[mmit->second]++;
			mmit++;
			counter++;
		}

		map<string, double>::iterator mit = votes.begin();
		map<string, double>::iterator winner;
		int max = 0;
		while(mit != votes.end()){
			if(mit->second >= max){
				winner = mit;	
			}
			mit++;
		}
		
		// Update the classification for a certain test point index
		classes.push_back(winner->first);

	}
	
	return classes;
}

// Print everything to ease in debugging
void KNNClassifier::print(){
	
	cout << "Printing xTrain:\n";
	for(unsigned int rows = 0; rows < xTrain.size(); rows++){
		for(unsigned int cols = 0; cols < xTrain[0].size(); cols++){
			cout << xTrain[rows][cols] << " ";
		}
		cout << endl;
	}
	cout << endl;

	cout << "Printing yTrain:\n";
	for(unsigned int i = 0; i < yTrain.size(); i++){
		cout << yTrain[i] << endl;
	}
	cout << endl;

	cout << "Printing Classifications:\n";
	set<string>::iterator sit = classifications.begin();
	while(sit != classifications.end()){
		cout << *sit << endl;
		sit++;
	}
	cout << endl;

	return;
}

// Initialize the training data and rip the true classifications from the test data and return as a vector of strings
vector<string> trainInit(vector< vector<double> > &xTrain, vector<string> &yTrain, vector< vector<double> > &xTest){
	
	double param1, param2, param3, param4;
	vector<double> paramVec;
	string classification;
	while(cin >> param1 >> param2 >> param3 >> param4 >> classification){

		if(param1 == 777){
			break;
		}

		paramVec.push_back(param1);
		paramVec.push_back(param2);
		paramVec.push_back(param3);
		xTrain.push_back(paramVec);
		yTrain.push_back(classification);
		paramVec.clear();
	}

	vector<string> trues;

	paramVec.clear();
	while(cin >> param1 >> param2 >> param3 >> param4 >> classification){
		paramVec.push_back(param1);
		paramVec.push_back(param2);
		paramVec.push_back(param3);
		xTest.push_back(paramVec);
		paramVec.clear();
		trues.push_back(classification);
	}

	return trues;
}



// Linear Regression Algorithm; C++ Implementation

class LinearRegression {
	vector<float> xTrain, yTrain;
	float slope, yInter;

	public:
		LinearRegression(vector<float> &xTrain, vector<float> &yTrain);
		void fitData(float alpha, int epochs);
		float getSlope();
		vector<float> predict(vector<float> &xTest);
		void addData(vector<float> &newX, vector<float> &newY);
		void resetData(vector<float> &newX, vector<float> &newY);
};

LinearRegression::LinearRegression(vector<float> &xTrain, vector<float> &yTrain) {
	this->xTrain = xTrain;
	this->yTrain = yTrain;
}

void LinearRegression::fitData(float alpha, int epochs) {
		/* Return the slope and y intercept of the regression line formed based on 
		   the given data. */

		slope = 0;
		yInter = 0;

		int elems = xTrain.size();
		vector<int> yTest(elems), error(elems);

		for (int i = 0; i < epochs; i++) {

				// Make predictions based on the current slope and y intercept.
				for (int j = 0; j < elems; j++) {
						yTest[j] = slope * xTrain[j] + yInter;
				}

				float errorSum = 0, errorSumX = 0;

				// Compare results to actual data and form the sum components of the 
				// gradient of the mean squared error function.
				for (int j = 0; j < elems; j++) {
						errorSum += yTest[j] - yTrain[j];
						errorSumX += (yTest[j] - yTrain[j]) * xTrain[j];
				}

				// Adjust parameters based on the gradient value and the learning
				// rate, alpha.
				slope -= 2 * alpha * errorSumX / elems;
				yInter -= 2 * alpha * errorSum / elems;
		}
}

float LinearRegression::getSlope() {
	return this->slope;
}

void LinearRegression::addData(vector<float> &newX, vector<float> &newY) {
	// Concatenate given vectors to xTrain and yTrain.

	this->xTrain.insert(xTrain.end(), newX.begin(), newX.end());
	this->yTrain.insert(yTrain.end(), newY.begin(), newY.end());
}

void LinearRegression::resetData(vector<float> &newX, vector<float> &newY) {
	// Replace xTrain and yTrain with given vectors.

	this->xTrain = newX;
	this->yTrain = newY;
}

float calcR2 (vector<float> &y, vector<float> &yTest) {
		/* Calculate the R-squared value for a given set of predictions.*/

		float ssRes = 0, ssTot = 0, R2, avg = 0;
		int n = y.size();

		for (int i = 0; i < n; i++) {
				avg += y[i];
		}

		avg /= n;

		// Compute the residual sum of squares and the total sum of squares.
		for (int i = 0; i < n; i++) {
				ssRes += pow(y[i] - yTest[i], 2);
				ssTot += pow(y[i] - avg, 2);
		}

		R2 = 1 - ssRes/ssTot;

		return R2;
}

float calcAvg (vector<float> &y) {
	int n = y.size();
	float avg = 0;

	for (int i = 0; i < n; i++) {
		avg += y[i];
	}

	avg /= n;
	
	return avg;
}
