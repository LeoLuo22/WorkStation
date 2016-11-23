#include<iostream>

using namespace std;

int NumberOf1(unsigned int n) {
	int number = 0;
	while (n) {
		if (n % 10 == 1)
			number += 1;
		n = n / 10;
	}
	return number;
}
int Numberof1Between1AndN(unsigned int n) {
	int number = 0;
	for (unsigned int i = 1; i <= n; ++i) {
		number += NumberOf1(i);
	}
	return number;
}


int main() {
	cout << Numberof1Between1AndN(11) << endl;
	system("pause");
	return 0;
}