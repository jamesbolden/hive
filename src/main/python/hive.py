from opencog.atomspace import TruthValue, types
from opencog.type_constructors import *
from thought_engine import *
from global_space import *

initialize_global_space()
initialize_thought_pool()

introspective_search_engine = ThoughtEngine('introspective search', 1.0, 0.85, 0.375)
