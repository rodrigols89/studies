#include "diamond_problem_electric.h"
#include "diamond_problem_gasoline.h"

class Hybrid : public Electric, public Gasoline
{
public:
    Hybrid();
};
