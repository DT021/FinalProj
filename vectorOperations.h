#include <vector>
#include <iostream>

using namespace std;

typedef vector<float> fvec;

bool sameSize(fvec &op1, fvec &op2) {
	if (op1.size() != op2.size()) return false;
	return true;
}

void scalarMultiply(fvec &src, fvec &dest, float scalar) {
	//Multiply all values in a fvec by a given scalar.
	
	if (!sameSize(src, dest)) dest.resize(src.size());

	for (int i = 0; i < src.size(); i++) {
		dest[i] = src[i] * scalar;
	}
}

void multiply(fvec &op1, fvec &op2, fvec &dest) {
	// Multiply two vectors together and store results in dest.
	
	if (!sameSize(op1, op2)) {
		cout << "The two operands must be the same size.\n";
		return;
	}

	if (!sameSize(op1, dest)) dest.resize(dest.size());

	for (int i = 0; i < op1.size(); i++) {
		dest[i] = op1[i] * op2[i];
	}
}

void add(fvec &op1, fvec &op2, fvec &dest) {
	// Add the values of two vectors and store results in dest.

	if (!sameSize(op1, op2)) {
		cout << "The two operands must be the same size.\n";
		return;
	}

	if (!sameSize(op1, dest)) dest.resize(op1.size());
	
	for (int i = 0; i < op1.size(); i++) {
		dest[i] = op1[i] + op2[i];
	}
}

fvec add(fvec &op1, fvec &op2) {
	// Add two vectors and return a new vector.

	if (!sameSize(op1, op2)) {
		cout << "op1 and op2 must be the same size.\n";
		return fvec();
	}

	fvec sum;

	for (int i = 0; i < op1.size(); i++) {
		sum.push_back(op1[i] + op2[i]);
	}

	return sum;
}

float sum(fvec &op1) {
	// Return the sum of all elements in a vector.

	float sum = 0;

	for (int i = 0; i < op1.size(); i++) {
		sum += op1[i];
	}

	return sum;
}

float average(fvec &op1) {
	float op1Sum = sum(op1);

	return op1Sum / op1.size();
}

int main() {

}
