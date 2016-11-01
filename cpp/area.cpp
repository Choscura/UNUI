#include <iostream>
using namespace std;
int main()
{
	float length, width, area;
	cout<< "enter length of rectangle: ";
	cin >> length;
	cout<< "enter width of rectangle: ";
	cin >> width;
	area = length*width;
	cout << "area of rectangle: " << area << endl;
	return 0;
}
