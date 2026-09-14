import json
import sys
import matplotlib.pyplot as plt
def graph(x, y, t, theta):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes[0][0].plot(t, x)
    axes[0][0].set_ylabel("x / lateral")
    axes[0][0].set_xlabel("time")
    axes[0][0].grid(True)
    axes[1][0].plot(t, y)
    axes[1][0].set_ylabel("y / linear")
    axes[1][0].set_xlabel("time")
    axes[1][0].grid(True)
    axes[0][1].plot(t, theta)
    axes[0][1].set_ylabel("theta")
    axes[0][1].set_xlabel("time")
    axes[0][1].grid(True)
    axes[1][1].plot(x, y)
    axes[1][1].set_xlabel("x")
    axes[1][1].set_ylabel("y")
    axes[1][1].grid(True)
    axes[1][1].set_aspect("equal")

    fig.suptitle("Pose")
    plt.tight_layout()
    plt.show()

def sim(x, y, t, theta):
    pass
    # to be implemented

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
        sim(x,y,t,theta)
    else:
        graph(x,y,t,theta)

if __name__ == "__main__":
    main()