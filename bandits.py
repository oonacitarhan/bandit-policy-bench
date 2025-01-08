"""Compare policies across reproducible independent seeded trials."""
import math,random,statistics

def run(probabilities,policy,seed=0,steps=2000,epsilon=.1):
    if not probabilities or any(not 0<=p<=1 for p in probabilities):
        raise ValueError('invalid arm probabilities')
    if policy not in ('epsilon','ucb') or steps<1 or not 0<=epsilon<=1:
        raise ValueError('invalid experiment configuration')
    choices,rewards=random.Random(seed),random.Random(seed+100000)
    counts=[0]*len(probabilities); sums=[0]*len(probabilities)
    regret=0.0
    for t in range(steps):
        if 0 in counts: arm=counts.index(0)
        elif policy=='epsilon' and choices.random()<epsilon: arm=choices.randrange(len(counts))
        else:
            values=[s/c for s,c in zip(sums,counts)]
            if policy=='ucb': values=[v+math.sqrt(2*math.log(t+1)/c) for v,c in zip(values,counts)]
            arm=max(range(len(values)),key=values.__getitem__)
        sums[arm] += rewards.random()<probabilities[arm]
        counts[arm] += 1
        regret += max(probabilities)-probabilities[arm]
    return {'reward':sum(sums),'pseudo_regret':regret,'counts':counts}

def benchmark(trials=20):
    results={}
    for policy in ('epsilon','ucb'):
        values=[run([.2,.5,.8],policy,seed=i)['pseudo_regret'] for i in range(trials)]
        results[policy]={'mean_pseudo_regret':statistics.mean(values),
                         'stddev':statistics.stdev(values) if trials>1 else 0}
    return results

def self_test():
    for policy in ('epsilon','ucb'):
        result=run([.2,.5,.8],policy,seed=7,steps=100)
        assert sum(result['counts'])==100 and 0<=result['reward']<=100
        assert result==run([.2,.5,.8],policy,seed=7,steps=100)
        assert run([1],policy,steps=10)['reward']==10
        assert run([.5,.5],policy,steps=10)['pseudo_regret']==0
    return benchmark()

if __name__=='__main__':
    print(self_test()); print('Self-tests passed')
