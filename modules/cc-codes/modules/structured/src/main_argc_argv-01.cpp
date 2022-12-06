#include <iostream>
using namespace std;


int main(int argc, char ** argv)
{
    cout << "Program name: " << argv[0] << endl;

    // argc = 1 is when only run de program without arguments.
    // argv > 1 is when we pass arguments on the command line.
    if (argc > 1)
        cout << "arg: " << argv[1] << endl;

    return 0;
}
