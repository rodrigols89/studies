#include <iostream>
using namespace std;

namespace ns
{
    // A Class in a namespace
    class geek
    {
    public:
        void display()
        {
            cout << "ns::geek::display()" << endl;
            ;
        }
    };
}

int main()
{
    // Creating Object of geek Class
    ns::geek obj;
    obj.display();

    return 0;
}
