from opencog.atomspace import AtomSpace
from opencog.utilities import initialize_opencog

GlobalSpace = AtomSpace()

def initialize_global_space():
    initialize_opencog(GlobalSpace)
