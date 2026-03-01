from banditbench.features import thompson,compare
def test_accounting():
    row=thompson([.1,.8],seed=3,steps=100)
    assert sum(row['counts'])==100 and 0<=row['reward']<=100
    assert row==thompson([.1,.8],seed=3,steps=100)
def test_deterministic_rewards():
    assert thompson([1],steps=10)['reward']==10
    assert thompson([.2,.2],steps=10)['pseudo_regret']==0
def test_summary():
    result=compare([.5,.5],3,50)
    assert len(result)==3 and all(x['standard_error']==0 for x in result.values())
def test_bad_trials():
    try:compare([.2,.8],1)
    except ValueError:return
    raise AssertionError('single trial accepted')
