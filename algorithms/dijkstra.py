import sys
from heapq import heapify, heappush
import timeit


def dijkstra(graph, src, dest):
    node_data = NodeData()
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(len(graph)-1):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]: #to loop over the neighbors of the node
                if j not in visited: #bec if it is in the visited array we dont need to calc it's cost func
                    cost = node_data[temp]['cost'] + graph[temp][j] #cost = cost of the current node + the distance between the current node and the neighbor node 
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['predecessor'] = node_data[temp]['predecessor'] + list(temp)
                    heappush(min_heap, (node_data[j]['cost'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest distance: " + str(node_data[dest]['cost']))
    print("Shortest path: " + str(node_data[dest]['predecessor'] + list(dest)))

def NodeData():
    inf = sys.maxsize #initialize the cost of each node with an infinty value
    node_data = {'A':{'cost':inf, 'predecessor':[]}, #predecessor to get the path
    'B':{'cost':inf, 'predecessor':[]},
    'C':{'cost':inf, 'predecessor':[]},
    'D':{'cost':inf, 'predecessor':[]},
    'E':{'cost':inf, 'predecessor':[]},
    'F':{'cost':inf, 'predecessor':[]}
    }
    return node_data

if __name__ == "__main__":
    graph = {
        'A': {'B':2, 'C':4},
        'B': {'A':2, 'C':3, 'D':8},
        'C': {'A':4, 'B':3, 'E':5, 'D':2},
        'D': {'B':8, 'C':2, 'E':11, 'F':22},
        'E': {'C':5, 'D':11, 'F':1},
        'F': {'D':22, 'E':1}
    }
    starttime = timeit.default_timer()
    print("The start time is :",starttime)
    dijkstra(graph, 'A', 'F')
    print("The end time is :",timeit.default_timer())
    print("The time difference is :", timeit.default_timer() - starttime)
    

