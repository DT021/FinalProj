#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

pair<float, float> linReg (vector<float> &x, vector<float> &y, float alpha=0.0000001, int epochs=10000) {
		/* Return the slope and y intercept of the regression line formed based on 
		   the given data. */

		float m = 0, b = 0;

		for (int i = 0; i < epochs; i++) {
				int elems = x.size();
				vector<int> yTest(elems), error(elems);

				// Make predictions based on the current slope and y intercept.
				for (int j = 0; j < elems; j++) {
						yTest[j] = m * x[j] + b;
				}

				float errorSum = 0, errorSumX = 0;

				// Compare results to actual data and form the sum components of the 
				// gradient of the mean squared error function.
				for (int j = 0; j < elems; j++) {
						errorSum += yTest[j] - y[j];
						errorSumX += (yTest[j] - y[j]) * x[j];
				}

				// Adjust parameters based on the gradient value and the learning
				// rate, alpha.
				m -= 2 * alpha * errorSumX / elems;
				b -= 2 * alpha * errorSum / elems;
		}

		return make_pair(m, b);
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

int main() {
		vector<float> x, y, yTest;

		// Test algorith on y = x^2 over [0, 99].
		for (int i = 0; i < 100; i++) {
				x.push_back(i);
				y.push_back(i * i);
		}

		pair<float, float>line = linReg(x, y);

		for (int i = 0; i < 100; i++) {
				yTest.push_back(line.first * x[i] + line.second);
		}

		float R2 = calcR2(y, yTest), avg = calcAvg(y);

		printf("Slope: %f\nY Intercept: %f\n", line.first, line.second);
		printf("R2: %f AVG:%f\n", R2, avg);
}
