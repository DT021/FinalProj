#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

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
