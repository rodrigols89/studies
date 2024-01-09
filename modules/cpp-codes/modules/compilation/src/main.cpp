#include <iostream>        // Header inclusion
#include "external_code.h" // File inclusion

// Macro definition
#define SQUARE(x) ((x) * (x))

// Conditional compilation
#ifdef DEBUG
#define LOG(message) std::cout << "Debug: " << message << std::endl;
#else
#define LOG(message)
#endif

// Assertion
#define CHECK_CONDITION(condition)                                 \
    if (!(condition))                                              \
    {                                                              \
        std::cerr << "Assertion failed: " #condition << std::endl; \
        exit(EXIT_FAILURE);                                        \
    }

int main()
{
    // Macro expansion
    int result = SQUARE(5);

    // Conditional compilation
    LOG("This is a debug message.");

    // Tokenization
    int i = 10;
    int j = i + 20;

    // Line continuation
    int sum = i +
              j;

    // Character set conversion
    char specialChar = '\x41';

    // Assertion handling
    CHECK_CONDITION(i < 100);

    std::cout << "Result: " << result << std::endl;

    return 0;
}
