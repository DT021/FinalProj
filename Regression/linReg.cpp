#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

pair<float, float> linReg (vector<float> &x, vector<float> &y, float alpha=0.0000001, int epochs=10000) {
	float m = 0, b = 0;

	for (int i = 0; i < epochs; i++) {
		int elems = x.size();
		vector<int> yTest(elems), error(elems);

		for (int j = 0; j < elems; j++) {
			yTest[j] = m * x[j] + b;
		}

		float errorSum = 0, errorSumX = 0;

		for (int j = 0; j < elems; j++) {
			errorSum += yTest[j] - y[j];
			errorSumX += (yTest[j] - y[j]) * x[j];
		}

		m -= 2 * alpha * errorSumX / elems;
		b -= 2 * alpha * errorSum / elems;
	}

	return make_pair(m, b);
}

float calcR2 (vector<float> &y, vector<float> &yTest) {
	float ssReg = 0, ssTot = 0, R2, avg = 0;
	int n = y.size();

	for (int i = 0; i < n; i++) {
		avg += y[i];
	}

	avg /= n * 1.0;

	for (int i = 0; i < n; i++) {
		ssTot += pow(y[i] - yTest[i], 2);
		ssReg += pow(y[i] - avg, 2);
	}

	R2 = 1 - ssTot/ssReg;

	return R2;
}

int main() {
	vector<float> x, y, yTest;

	for (int i = 0; i < 100; i++) {
		x.push_back(i);
		y.push_back(i * i);
	}

	pair<float, float>line = linReg(x, y);
	printf("Slope: %f\nY Intercept: %f\n", line.first, line.second);

	for (int i = 0; i < 100; i++) {
		yTest.push_back(line.first * x[i] + line.second);
	}

	float R2 = calcR2(y, yTest);

	printf("R2: %f\n", R2);
}
