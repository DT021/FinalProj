#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>

using namespace std;

double getDistance(vector<double> staticPoint, vector<double> movingPoint){

        double dist = 0;
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
	vector< vector<double> > xTrain;
	vector<string> yTrain;
	set<string> classifications;

	void _init_(vector< vector<double> > xTrain, vector<string> yTrain, int k);
	void getClassifications();
	void addData(vector< vector<double> > newX, vector<string> newY);
	void clearData(vector< vector<double> > newX = {}, vector<string> newY = {});
	vector<string> classify(vector< vector<double> > testX);
	void print();
};

void KNNClassifier::_init_(vector< vector<double> > xTrain, vector<string> yTrain, int k){
	
	this->xTrain = xTrain;
	this->yTrain = yTrain;
	this->k = k;
	getClassifications();

	return;
}

void KNNClassifier::getClassifications(){
	
	for(unsigned int i = 0; i < yTrain.size(); i++){
		if(classifications.find(yTrain[i]) == classifications.end()){
			classifications.insert(yTrain[i]);
		}
	}
	return;
}

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

void KNNClassifier::clearData(vector< vector<double> > newX, vector<string> newY){
	
	xTrain.clear();
	yTrain.clear();
	xTrain = newX;
	yTrain = newY;
	classifications.clear();
	getClassifications();
	
	return;
}

vector<string> KNNClassifier::classify(vector< vector<double> > testX){
	
	vector<string> classes;

	multimap<double, string> distances;
	map<string, double> votes;
	for(unsigned int i = 0; i < testX.size(); i++){
		
		distances.clear();
		votes.clear();

		for(unsigned int j = 0; j < xTrain.size(); j++){
			double dist = getDistance(testX[i], xTrain[j]);
			distances.insert(pair<double, string>(dist, yTrain[j]));
		}
	
		multimap<double, string>::iterator mmit = distances.begin();
		int counter = 0;

		// TEST
//		while(mmit != distances.end()){
//			cout << mmit->first << " " << mmit->second << endl;
//			mmit++;
//		}
//		cout << endl;
//		mmit = distances.begin();

		while(counter < k){
			votes[mmit->second]++;
			mmit++;
			counter++;
		}

		map<string, double>::iterator mit = votes.begin();
		map<string, double>::iterator winner;
		int max = 0;
		while(mit != votes.end()){
			if(mit->second > max){
				winner = mit;	
			}
			mit++;
		}
		
		classes.push_back(winner->first);

	}
	
	return classes;
}

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

int main(int argc, char *argv[]){

	KNNClassifier* KNNptr = new KNNClassifier;

	int k = atoi(argv[1]);

	vector< vector<double> > xTrain;
	vector<string> yTrain;
	
	// This must be altered with more params
//	double parameter = 0;
//	vector<double> paramVec;
//	string classification = "";
//	while(cin >> parameter >> classification){
//		paramVec.push_back(parameter);
//		xTrain.push_back(paramVec);
//		yTrain.push_back(classification);
//		paramVec.clear();
//	}

	vector< vector<double> > xTest;

	vector<string> trues;

	trues = trainInit(xTrain, yTrain, xTest);

	KNNptr->_init_(xTrain, yTrain, k);

//	KNNptr->print();

//	vector< vector<double> > xTest = {{0.00},{0.01},{0.02},{0.03},{0.04},{0.05},{0.06},{0.07},{0.08},{0.09},{0.10}};

	vector<string> classes = KNNptr->classify(xTest);

/*
	cout << "True Classifications: " << endl;
	cout << "[";
	
	for(unsigned int i = 0; i < trues.size(); i++){
		cout << trues[i];
		if(i != trues.size()-1){
			cout << " ";	
		}	
	}
	cout << "]" << endl;

	cout << "Our C++ Predictions: " << endl;
	cout << "[";

	for(unsigned int i = 0; i < classes.size(); i++){
		cout << classes[i];
		if(i != classes.size()-1){
			cout << " ";
		}
	}
	cout << "]" << endl;
*/
	double errCount = 0;

	for(unsigned int i = 0; i < classes.size(); i++){
		if(classes[i] != trues[i]){
			errCount = errCount + 1;
		}
	}
	double errPercent = (errCount/classes.size())*100;
	cout << "C++ Percent Error: " << errPercent << endl;

/*
	vector< vector<double> > xTrain = {{1,2,3,3},{1,4,3,5},{29,15,19,12},{89,69,54,73},{76,100,99,80}};
	vector <string> yTrain = {"Good","Good","Okay","Bad","Bad"};
	
	vector< vector<double> > newX = {{1,1,1,1},{30,30,30,30},{100,100,100,100}};
	vector<string> newY = {"Good","Okay","Bad"};

	int k = 3;

	KNNptr->_init_(xTrain, yTrain, k);

	KNNptr->print();

	KNNptr->addData(newX, newY);

	KNNptr->print();

//	KNNptr->clearData(newX, newY);

//	KNNptr->print();

//	KNNptr->clearData();

//	KNNptr->print();

	vector< vector<double> > xTest = {{0,0,0,0},{200,200,200,200}};

	vector<string> classes = KNNptr->classify(xTest);

	for(unsigned int i = 0; i < classes.size(); i++){
		cout << classes[i] << endl;
	}
	cout << endl;

*/
	delete KNNptr;	

	return 0;
}
