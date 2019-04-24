#include <fstream>
#include "kMeans.cpp"

using namespace std;

int main() {

	vector< vector<float> > irisData;
	float p1, p2, p3, groupThrowAway;
	int point = 0;
	ifstream iris;
	iris.open("../irisTrain.txt");

	while (iris >> p1 >> p2 >> p3 >> groupThrowAway) {
		irisData.push_back(vector<float>());
		irisData[point].push_back(p1);
		irisData[point].push_back(p2);
		irisData[point].push_back(p3);

		point++;
	}

	iris.close();

	/*for (int i = 0; i < irisData.size(); i++) {

		for (int j = 0; j < irisData[i].size(); j++) {
			cout << irisData[i][j] << " ";
		}
		cout << endl;
	}

	cin.get();*/

	KMeansCluster<vector<vector<float> > > irisCluster(irisData);
	irisCluster.cluster(3, 100);
	irisCluster.printGroupCenters();
	cin.get();
}