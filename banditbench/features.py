import random,statistics,math
from .core import run

def thompson(probabilities,seed=0,steps=2000):
    if not probabilities or any(not 0<=p<=1 for p in probabilities) or steps<1:raise ValueError('invalid bandit configuration')
    policy=random.Random(seed);environment=random.Random(seed+100000)
    counts=[0]*len(probabilities);success=[0]*len(probabilities);regret=0
    for _ in range(steps):
        draws=[policy.betavariate(s+1,c-s+1) for s,c in zip(success,counts)]
        arm=max(range(len(draws)),key=draws.__getitem__)
        success[arm]+=environment.random()<probabilities[arm];counts[arm]+=1
        regret+=max(probabilities)-probabilities[arm]
    return {'reward':sum(success),'pseudo_regret':regret,'counts':counts}

def compare(probabilities,trials=20,steps=2000):
    if trials<2:raise ValueError('at least two trials required for uncertainty estimates')
    output={}
    for policy in ('epsilon','ucb','thompson'):
        rows=[thompson(probabilities,seed,steps) if policy=='thompson' else run(probabilities,policy,seed,steps) for seed in range(trials)]
        values=[row['pseudo_regret'] for row in rows];mean=statistics.mean(values)
        se=statistics.stdev(values)/math.sqrt(trials)
        output[policy]={'mean_pseudo_regret':mean,'standard_error':se,'normal_95_interval':[mean-1.96*se,mean+1.96*se],'mean_reward':statistics.mean(r['reward'] for r in rows),'trials':trials}
    return output
