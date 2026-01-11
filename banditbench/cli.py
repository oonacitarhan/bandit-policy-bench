import argparse,json
from .features import compare
def main():
    parser=argparse.ArgumentParser(description='Seeded Bernoulli multi-armed bandit experiments')
    parser.add_argument('config');parser.add_argument('--trials',type=int,default=20);parser.add_argument('--steps',type=int,default=2000)
    args=parser.parse_args()
    try:
        with open(args.config) as f:config=json.load(f)
        print(json.dumps(compare(config['probabilities'],args.trials,args.steps),indent=2))
    except (ValueError,KeyError,OSError,TypeError) as error:parser.error(str(error))
