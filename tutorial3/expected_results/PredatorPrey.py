# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.8.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 2
CONSTANT_COUNT = 3
COMPUTED_CONSTANT_COUNT = 1
ALGEBRAIC_VARIABLE_COUNT = 0

VOI_INFO = {"name": "time", "units": "month", "component": "predator_prey_component"}

STATE_INFO = [
    {"name": "y_f", "units": "thousands_of_fish", "component": "predator_prey_component"},
    {"name": "y_s", "units": "number_of_sharks", "component": "predator_prey_component"}
]

CONSTANT_INFO = [
    {"name": "a", "units": "per_month", "component": "predator_prey_component"},
    {"name": "b", "units": "per_shark_month", "component": "predator_prey_component"},
    {"name": "d", "units": "per_1000fish_month", "component": "predator_prey_component"}
]

COMPUTED_CONSTANT_INFO = [
    {"name": "c", "units": "per_month", "component": "predator_prey_component"}
]

ALGEBRAIC_VARIABLE_INFO = [
]


def create_states_array():
    return [nan]*STATE_COUNT


def create_constants_array():
    return [nan]*CONSTANT_COUNT


def create_computed_constants_array():
    return [nan]*COMPUTED_CONSTANT_COUNT


def create_algebraic_variables_array():
    return [nan]*ALGEBRAIC_VARIABLE_COUNT


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 2.0
    states[1] = 1.0
    constants[0] = -0.8
    constants[1] = 0.3
    constants[2] = -0.6


def compute_computed_constants(voi, states, rates, constants, computed_constants, algebraic_variables):
    computed_constants[0] = constants[0]+2.0


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    rates[1] = constants[0]*states[1]+constants[1]*states[1]*states[0]
    rates[0] = computed_constants[0]*states[0]+constants[2]*states[1]*states[0]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    pass
