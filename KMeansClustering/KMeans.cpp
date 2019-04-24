#include <cstdlib>
#include <vector>
#include <iostream>
#include <time.h>
#include "../vectorOperations.h"

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
};

template <typename T>
KMeansCluster<T>::KMeansCluster(T testData) {
	this->data = testData;
	this->dimensions = data[0].size();
	this->groups.resize(data.size());

	srand(time(NULL));
}

template <typename T>
void KMeansCluster<T>::cluster(int numgroups, int epochs) {

	this->groupCenters.resize(0);

	for (int i = 0; i < this->groupCenters.size(); i++) {
		this->groupCenters.push_back(vector<float>());

		for (int j = 0; j < this->groupCenters[0].size(); j++) {
			this->groupCenters[i].push_back(rand() % 100 / 100);
		}
	}

	for (int epoch = 0; epoch < epochs; epoch++) {

	}
}

int main() {
	vector<vector<int> > testData;

	for (int i = 0; i < 5; i++) {
		testData.push_back(vector<int>());

		for (int j = 0; j < 3; j++)
			testData[i].push_back(j);
	}

	KMeansCluster<vector<vector<int> > > test(testData);
	test.cluster(3, 100);
}