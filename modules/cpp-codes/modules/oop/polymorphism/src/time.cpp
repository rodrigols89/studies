#include <iostream>
#include "time.h"

Time::Time(int hours)
{
    this->hours = hours;
};

// Method of type "Time", that's retorn a Time object.
Time Time::operator+(const Time & t) const
{
    Time time_obj;
    time_obj.hours = this->hours + t.hours;

    return time_obj;
}

void Time::showHours()
{
    std::cout << "Object hours is: " << this->hours << "\n";
}
