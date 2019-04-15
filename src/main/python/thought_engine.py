from opencog.atomspace import TruthValue, FloatValue
from opencog.type_constructors import *

ThoughtPool = None

def initialize_thought_pool():
    ThoughtPool = ConceptNode('thought pool')

class ThoughtEngine:
    def __init__(self, name, reflexivity = 0.5, pace = 0.5, dominance = 0.5):
        self.name = name
        self.repr = ConceptNode(name)
        self.repr.tv = TruthValue(1.0, 0.0)
        self.repr.set_value(PredicateNode('sti'), FloatValue(0.0))
        self.repr.set_value(PredicateNode('lti'), FloatValue(0.0))
        self.repr.set_value(PredicateNode('vlti'), FloatValue(1.0))
        self.repr.set_value(PredicateNode('thought stream'), ListLink([]))
        self.repr.set_value(PredicateNode('reflexivity'), FloatValue(reflexivity))
        self.repr.set_value(PredicateNode('pace'), FloatValue(pace))
        self.repr.set_value(PredicateNode('dominance'), FloatValue(dominance))
        alink = MemberLink(self.repr, ThoughtPool)
        active = EvaluationLink(PredicateNode('active'), self.repr)
        active_ctx = ContextLink(active, alink)
        active_ctx.tv = TruthValue(1.0, 1.0)
        inactive_ctx = ContextLink(NotLink(active), alink)
        inactive_ctx.tv = TruthValue(1.0, 0.0)

    def __str__(self):
        return 'ThoughtEngine[name: {}; repr: {}]'.format(self.name, str(self.repr))
