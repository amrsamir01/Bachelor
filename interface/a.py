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
    print("the shortest path is:", find_shortest_path(graph, a, b))
    x.append(find_shortest_path(graph, a, b))
    w=input("find another path? ")

for j in range(len(x)-1):
    for c in range(1, len(x)-j):
        s = j + c
        for i in range(len(x[j])-1):
            if x[j][i] == x[s][i] and x[j][i+1] == x[s][i+1]:
                x[s].insert(i,"wait")
print(x)