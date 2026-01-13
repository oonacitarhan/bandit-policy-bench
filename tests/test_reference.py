from banditbench.core import *

def self_test():
    for policy in ('epsilon','ucb'):
        result=run([.2,.5,.8],policy,seed=7,steps=100)
        assert sum(result['counts'])==100 and 0<=result['reward']<=100
        assert result==run([.2,.5,.8],policy,seed=7,steps=100)
        assert run([1],policy,steps=10)['reward']==10
        assert run([.5,.5],policy,steps=10)['pseudo_regret']==0
    return benchmark()

def test_original_reference_cases():
    self_test()
