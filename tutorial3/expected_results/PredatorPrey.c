/* The content of this file was generated using the C profile of libCellML 0.4.0. */

#include "PredatorPrey.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.4.0";
const char LIBCELLML_VERSION[] = "0.4.0";

const size_t STATE_COUNT = 2;
const size_t VARIABLE_COUNT = 4;

const VariableInfo VOI_INFO = {"time", "month", "predator_prey_component", VARIABLE_OF_INTEGRATION};

const VariableInfo STATE_INFO[] = {
    {"y_s", "number_of_sharks", "predator_prey_component", STATE},
    {"y_f", "thousands_of_fish", "predator_prey_component", STATE}
};

const VariableInfo VARIABLE_INFO[] = {
    {"c", "per_month", "predator_prey_component", COMPUTED_CONSTANT},
    {"a", "per_month", "predator_prey_component", CONSTANT},
    {"b", "per_shark_month", "predator_prey_component", CONSTANT},
    {"d", "per_1000fish_month", "predator_prey_component", CONSTANT}
};

double * createStatesArray()
{
    double *res = (double *) malloc(STATE_COUNT*sizeof(double));

    for (size_t i = 0; i < STATE_COUNT; ++i) {
        res[i] = NAN;
    }

    return res;
}

double * createVariablesArray()
{
    double *res = (double *) malloc(VARIABLE_COUNT*sizeof(double));

    for (size_t i = 0; i < VARIABLE_COUNT; ++i) {
        res[i] = NAN;
    }

    return res;
}

void deleteArray(double *array)
{
    free(array);
}

void initialiseVariables(double *states, double *rates, double *variables)
{
    variables[1] = -0.8;
    variables[2] = 0.3;
    variables[3] = -0.6;
    states[0] = 1.0;
    states[1] = 2.0;
}

void computeComputedConstants(double *variables)
{
    variables[0] = variables[1]+2.0;
}

void computeRates(double voi, double *states, double *rates, double *variables)
{
    rates[0] = variables[1]*states[0]+variables[2]*states[0]*states[1];
    rates[1] = variables[0]*states[1]+variables[3]*states[0]*states[1];
}

void computeVariables(double voi, double *states, double *rates, double *variables)
{
}
