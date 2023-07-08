#include <iostream>
#include <string>

int add(const int &x, const int &y);
int sub(const int &x, const int &y);
int mult(const int &x, const int &y);
float divFunc(const int &x, const int &y);

int main(int argc, char *argv[])
{
    int x = 5;
    int y = 10;
    int add_result = add(x, y);
    std::cout << "The sum between " << x << " and " << y << " is: " << add_result << "\n";

    int w = 5;
    int z = 10;
    int sub_result = sub(w, z);
    std::cout << "The subtraction between " << w << " and " << z << " is: " << sub_result << "\n";

    int r = 5;
    int s = 10;
    int mult_result = mult(r, s);
    std::cout << "The multiplication between " << r << " and " << s << " is: " << mult_result << "\n";

    float g = 5;
    float h = 10;
    float div_result = divFunc(g, h);
    std::cout << "The division between " << g << " and " << h << " is: " << div_result << "\n";

    return 0;
}

int add(const int &x, const int &y)
{
    int result;
    result = x + y;
    return result;
}

int sub(const int &x, const int &y)
{
    int result;
    result = x - y;
    return result;
}

int mult(const int &x, const int &y)
{
    int result;
    result = x * y;
    return result;
}

float divFunc(const int &x, const int &y)
{
    float div;
    div = static_cast<float>(x) / y;
    return div;
}
