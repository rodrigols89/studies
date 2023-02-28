class Time
{
public:
    int hours;

    Time(int hours = 0); // Constructor prototype.
    Time operator+(const Time &t) const; // Method of type "Time", that's retorn a Time object.
    void showHours();
};
