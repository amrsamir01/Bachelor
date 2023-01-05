def findWaitingTime(x, n, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = x[i - 1][1] + wt[i - 1]

def findavgTime(x, n):
    wt = [0] * n
    findWaitingTime(x, n, wt)
    print("\n AGV    Start Time    Waiting", "Time")
    total_wt = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        print(" ", x[i][0], "\t", x[i][1], "\t\t", wt[i])
    print("\nAverage waiting time = %.5f "%(total_wt /n))
 
def priorityScheduling(x, n):
    x = sorted(x, key = lambda x:x[3], reverse = True)
    print(x)
    print("Order in which AGV gets executed")
    for i in x:
        print(i, end = " ")
    findavgTime(x, n)

if __name__ =="__main__":
    x = [[1, 10, 1],
            [2, 5, 0],
            [3, 8, 1]]
    n = len(x)
    priorityScheduling(x, n)