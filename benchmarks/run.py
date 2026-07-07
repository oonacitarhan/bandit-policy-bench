import sys,time,statistics,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from banditbench.features import *
durations=[]
for _ in range(5):
    start=time.perf_counter()
    compare([.2,.5,.8],3,100)
    durations.append(time.perf_counter()-start)
print(json.dumps({'workload':'compare([.2,.5,.8],3,100)','repetitions':len(durations),'median_seconds':statistics.median(durations),'min_seconds':min(durations)}))
