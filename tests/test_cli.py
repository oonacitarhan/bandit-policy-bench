import subprocess,sys
def test_help():
    result=subprocess.run([sys.executable,'-m','banditbench','--help'],text=True,capture_output=True)
    assert result.returncode==0 and 'usage:' in result.stdout
def test_cli_rejects_unknown_argument():
    result=subprocess.run([sys.executable,'-m','banditbench','--unknown-option'],text=True,capture_output=True)
    assert result.returncode!=0

def test_documented_workflow():
    import json
    result=subprocess.run([sys.executable,'-m','banditbench',*['examples/bernoulli.json','--trials','3','--steps','100']],text=True,capture_output=True)
    assert result.returncode==0, result.stderr
    data=json.loads(result.stdout)
    assert set(data)=={'epsilon','ucb','thompson'} and all(row['trials']==3 for row in data.values())
