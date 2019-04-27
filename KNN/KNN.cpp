/***********************************************************
 *
 *	C++ Implementation of K Nth Nearest Neighbor 
 *
 ***********************************************************/

#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>

using namespace std;

// Calculates euclidean distance between two points based on parameters
float getDistance(vector<float> staticPoint, vector<float> movingPoint){

        float dist = 0;
        for(unsigned int i = 0; i < staticPoint.size(); i++){
                dist += (movingPoint[i]-staticPoint[i])*(movingPoint[i]-staticPoint[i]);
        }
        dist = sqrt(dist);

        return dist;
}

// Define class for KNN
class KNNClassifier{
	public:
	
	int k;
	vector< vector<float> > xTrain;
	vector<string> yTrain;
	set<string> classifications;

	KNNClassifier(vector< vector<float> > xTrain, vector<string> yTrain, int k);
	void getClassifications();
	void addData(vector< vector<float> > newX, vector<string> newY);
	void clearData(vector< vector<float> > newX = {}, vector<string> newY = {});
	vector<string> classify(vector< vector<float> > testX);
	void print();
};

// Constructor
KNNClassifier::KNNClassifier(vector< vector<float> > xTrain, vector<string> yTrain, int k){
	
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
void KNNClassifier::addData(vector< vector<float> > newX, vector<string> newY){
	
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
void KNNClassifier::clearData(vector< vector<float> > newX, vector<string> newY){
	
	xTrain.clear();
	yTrain.clear();
	xTrain = newX;
	yTrain = newY;
	classifications.clear();
	getClassifications();
	
	return;
}

// Classify each point in the test data set via distance function and return vector of classification strings
vector<string> KNNClassifier::classify(vector< vector<float> > testX){
	
	vector<string> classes;

	// The distances from the current test point are stored in a multimap so that finding the lowest five distances is a breeze
	multimap<float, string> distances;
	map<string, float> votes;

	// Calculate all point distances of training data to test data for EACH test data point
	for(unsigned int i = 0; i < testX.size(); i++){
		
		distances.clear();
		votes.clear();

		for(unsigned int j = 0; j < xTrain.size(); j++){
			float dist = getDistance(testX[i], xTrain[j]);
			distances.insert(pair<float, string>(dist, yTrain[j]));
		}
	
		multimap<float, string>::iterator mmit = distances.begin();
		int counter = 0;

		// Count the classification votes from each of the five closest distanced training points
		while(counter < k){
			votes[mmit->second]++;
			mmit++;
			counter++;
		}

		map<string, float>::iterator mit = votes.begin();
		map<string, float>::iterator winner;
		int max = 0;
		while(mit != votes.end()){
			if(mit->second > max){
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
vector<string> trainInit(vector< vector<float> > &xTrain, vector<string> &yTrain, vector< vector<float> > &xTest){
	
	float param1, param2, param3, param4;
	vector<float> paramVec;
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


// Main implementation
int main(int argc, char *argv[]){


	int k = atoi(argv[1]);

	vector< vector<float> > xTrain;
	vector<string> yTrain;

	vector< vector<float> > xTest;

	vector<string> trues;

	// Keep true classifications from test data for comparison
	trues = trainInit(xTrain, yTrain, xTest);

	// Allocate memory
	KNNClassifier* KNNptr = new KNNClassifier(xTrain, yTrain, k);

	vector<string> classes = KNNptr->classify(xTest);


	// Compute percent error
	float errCount = 0;

	for(unsigned int i = 0; i < classes.size(); i++){
		if(classes[i] != trues[i]){
			errCount = errCount + 1;
		}
	}
	float errPercent = (errCount/classes.size())*100;
	cout << "C++ Percent Error: " << errPercent << endl;

	// Clean memory
	delete KNNptr;	

	return 0;
}
