import ast
import math

def connect_edges(node,all):
    if node not in graph:
        pass
    elif all not in graph:
        pass
    else:
        graph[node].append(tuple(all))

def Wall(v1,v2):
    if v1 not in graph:
        pass
    elif v2 not in graph:
        pass
    else:
        a=tuple(v1)
        b=tuple(v2)
        graph[v1].remove(b)
        graph[v2].remove(a)

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return None
        paths = []
        for node in graph[start]:
            node1=tuple(node)
            if node1 not in path:
                newpaths = find_all_paths(graph, node1, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        node1=tuple(node)
        if node1 not in path:
            newpath = find_shortest_path(graph, node1, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

print("put the dimension of x axis:")
x=int(input())
print("put the dimension of y axis:")
y=int(input())
print("put the distance between each node:")
m=float(input())

graph = {}

for i in range(0, x+1,int(m)):
    for j in range(0, y+1,int(m)):
        graph[i,j]=([])

for node in graph:
    for all in graph:
        if math.sqrt((node[0]-all[0])**2+(node[1]-all[1])**2)==m:
            connect_edges(node, all)

print("Do you want to add a wall?")
q=input()
if(q=='yes' or q=='Yes'):
    a = ast.literal_eval(input('start point of the wall: '))
    b = ast.literal_eval(input('end point of the wall: '))
    Wall(a,b)

x = []
w=input("find the path? ")
while(w=='yes' or w=='Yes'):
    a = ast.literal_eval(input('start point: '))
    b = ast.literal_eval(input('end point: '))
    print("all paths are:", find_all_paths(graph, a, b))
    print()
    print("the shortest path is:", find_shortest_path(graph, a, b))
    print("the shortest path is:", shortest_path(graph, a, b))
    
    x.append(find_shortest_path(graph, a, b))
    w=input("find another path? ")

for j in range(len(x)-1):
    for c in range(1, len(x)-j):
        s = j + c
        for i in range(len(x[j])-1):
            if x[j][i] == x[s][i] and x[j][i+1] == x[s][i+1]:
                x[s].insert(i,"wait")
count = 1
for i in x:
    print("Robot", count, "Final Path:", i)
    count = count+1