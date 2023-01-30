#include <iostream>

int main()
{
	float x = 5.6;

	std::cout << "'x' value is " << x << ", Primitive data type is: " << typeid(x).name() << "\n";
	return 0;
}
