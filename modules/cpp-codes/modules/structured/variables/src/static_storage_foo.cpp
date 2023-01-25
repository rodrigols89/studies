#include <iostream>
#include "extern_foo.h"

int sizeVar = 1000; // External, visible on other files.
static int index;   // Internal, visible only in the current file.

int main()
{
    printSize();

    return 0;
}
