#include "time.h"

int main()
{
    Time obj1{10};
    Time obj2{20};
    Time obj3;

    obj3 = obj1 + (obj2);
    obj3.showHours();

    return 0;
}
