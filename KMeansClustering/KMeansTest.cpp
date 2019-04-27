#include <fstream>
#include "KMeans.cpp"
#include <limits>
#include <chrono>
#include <cstdio>

using namespace std;

int main(int argc, char *argv[]){

	vector< vector<float> > irisData;
	float p1, p2, p3, groupThrowAway;
	int point = 0;
	ifstream iris;
	iris.open("Iris/irisTrain.txt");

	while (iris >> p1 >> p2 >> p3 >> groupThrowAway) {
		irisData.push_back(vector<float>());
		irisData[point].push_back(p1);
		irisData[point].push_back(p2);

		point++;
	}

	iris.close();

	/*for (int i = 0; i < irisData.size(); i++) {

		for (int j = 0; j < irisData[i].size(); j++) {
			cout << irisData[i][j] << " ";
		}
		cout << endl;
	}*/

	int k = atoi(argv[1]);

	KMeansCluster<vector<vector<float> > > irisCluster(irisData);

	// Perform cluster and timing
	auto start = chrono::high_resolution_clock::now();
	
	irisCluster.cluster(k, 100);

	auto stop = chrono::high_resolution_clock::now();
	auto duration = chrono::duration_cast<chrono::microseconds>(stop-start);
	unsigned long long duration_microseconds = duration.count();
	
	printf("%i %llu ", k, duration_microseconds);

}
