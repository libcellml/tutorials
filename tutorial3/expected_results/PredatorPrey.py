# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.4.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 2
VARIABLE_COUNT = 4


class VariableType(Enum):
    VARIABLE_OF_INTEGRATION = 0
    STATE = 1
    CONSTANT = 2
    COMPUTED_CONSTANT = 3
    ALGEBRAIC = 4


VOI_INFO = {"name": "time", "units": "month", "component": "predator_prey_component", "type": VariableType.VARIABLE_OF_INTEGRATION}

STATE_INFO = [
    {"name": "y_f", "units": "thousands_of_fish", "component": "predator_prey_component", "type": VariableType.STATE},
    {"name": "y_s", "units": "number_of_sharks", "component": "predator_prey_component", "type": VariableType.STATE}
]

VARIABLE_INFO = [
    {"name": "a", "units": "per_month", "component": "predator_prey_component", "type": VariableType.CONSTANT},
    {"name": "c", "units": "per_month", "component": "predator_prey_component", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "b", "units": "per_shark_month", "component": "predator_prey_component", "type": VariableType.CONSTANT},
    {"name": "d", "units": "per_1000fish_month", "component": "predator_prey_component", "type": VariableType.CONSTANT}
]


def create_states_array():
    return [nan]*STATE_COUNT


def create_variables_array():
    return [nan]*VARIABLE_COUNT


def initialise_variables(states, rates, variables):
    variables[0] = -0.8
    variables[2] = 0.3
    variables[3] = -0.6
    states[0] = 2.0
    states[1] = 1.0


def compute_computed_constants(variables):
    variables[1] = variables[0]+2.0


def compute_rates(voi, states, rates, variables):
    rates[1] = variables[0]*states[1]+variables[2]*states[1]*states[0]
    rates[0] = variables[1]*states[0]+variables[3]*states[1]*states[0]


def compute_variables(voi, states, rates, variables):
    pass
