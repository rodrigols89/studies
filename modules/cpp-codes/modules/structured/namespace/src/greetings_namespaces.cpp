#include <iostream>
using namespace std;

namespace morning
{
    void greetings()
    {
        cout << "Good Morning!"
             << "\n";
    }
}

namespace afternoon
{
    void greetings()
    {
        cout << "Good Afternoon!"
             << "\n";
    }
}

namespace night
{
    void greetings()
    {
        cout << "Good night!"
             << "\n";
    }
}

int main()
{
    morning::greetings();
    afternoon::greetings();
    night::greetings();

    return 0;
}
