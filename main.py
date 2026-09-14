import json
import sys

from graph import graph
from simulate import simulate

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3: 
        print("wrong number of arguments")
        quit()
    path = sys.argv[1]
    f = open(path)
    sim = False
    if len(sys.argv) == 3 and sys.argv[2].lower() == "sim":
            sim = True
    
    records = [json.loads(line) for line in f if line.strip()]
    f.close()

    t = [r["t"] for r in records]
    x = [r["pose"]["x"] for r in records]
    y = [r["pose"]["y"] for r in records]
    theta = [r["pose"]["theta"] for r in records]
    if sim:
        simulate(x,y,t,theta)
    else:
        graph(x,y,t,theta)

if __name__ == "__main__":
    main()