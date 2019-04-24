#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <cmath>
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
void KMeansCluster<T>::cluster(int numgroups, int epochs) {

	// Reset groupCenters and initialize to random points.
	this->groupCenters.resize(0);

	for (int i = 0; i < this->groupCenters.size(); i++) {
		this->groupCenters.push_back(vector<float>());

		for (int j = 0; j < this->groupCenters[0].size(); j++) {
			this->groupCenters[i].push_back(rand() % 100 / 100);
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

		for (int group = 0; group < groupCenters.size(); group++) {
			float numInGroup = 0;
			vector<float> pointSums(data[0].size(), 0); 

			for (int i = 0; i < groups.size(); i++) {

				if (groups[i] == group) {
					numInGroup++;

					for (int j = 0; j < data[i].size(); j++) {
						pointSums[i] += data[i][j];
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

		for (int j = 0; j < groupCenters[i].size(); i++) {
			cout << groupCenters[i][j] << "/";
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

/*int main() {
	vector<vector<int> > testData;

	for (int i = 0; i < 5; i++) {
		testData.push_back(vector<int>());

		for (int j = 0; j < 3; j++)
			testData[i].push_back(j);
	}

	KMeansCluster<vector<vector<int> > > test(testData);
	test.cluster(3, 100);
}*/