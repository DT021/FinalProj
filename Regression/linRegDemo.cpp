/*
The purpose of this program is to use the linReg file to gather predictions 
on the most recent six months of the Walmart test data for comparison with 
the Python and scikit models.
*/

#include <iostream>
#include <fstream>
#include <vector>
#include "linReg.cpp"

int main() {
	vector<float> rawX, rawY;
	vector<float> sixMoX, sixMoY;
	ifstream rawData;
	float day, price;

	rawData.open("test-data");

	while (rawData >> day >> price) {
		rawX.push_back(day);
		rawY.push_back(price);
	}

	rawData.close();

	for (int i = rawX.size() - 180; i < rawX.size(); i++) {
		sixMoX.push_back(rawX[i]);
		sixMoY.push_back(rawY[i]);
	}

	pair<float, float> line = linReg(sixMoX, sixMoY);

	ofstream newData;
	newData.open("cpp-reg-data.txt");

	for (int i = 0; i < sixMoX.size(); i++) {
		newData << sixMoX[i] << " " << 
			(line.first * sixMoX[i]) + line.second << endl;
	}

	newData.close();
}