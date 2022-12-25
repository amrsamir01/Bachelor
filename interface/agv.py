import ast
import math
from tkinter import *

global xAxisEntry, yAxisEntry, startWallEntry, endWallEntry, startPathEntry, endPathEntry

def graph(x, y ,m):
    global graph 
    graph = {}
    for i in range(0, x+1,int(m)):
        for j in range(0, y+1,int(m)):
            graph[i,j]=([])
    for node in graph:
        for all in graph:
            if math.sqrt((node[0]-all[0])**2+(node[1]-all[1])**2)==float(m):
                connect_edges(node, all, graph)
    return graph

def connect_edges(node,all, graph):
    if node not in graph:
        pass
    elif all not in graph:
        pass
    else:
        graph[node].append(tuple(all))

def Wall(v1, v2):
    if v1 not in graph:
        pass
    elif v2 not in graph:
        pass
    else:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
    return graph

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

def dimensions():
    x = int(xAxisEntry.get())
    y = int(yAxisEntry.get())
    m = float(distanceEntry.get())
    print("Graph:", graph(x, y, m))

def AddWall():
    v1 = tuple(map(int, startWallEntry.get()))
    v2 = tuple(map(int, endWallEntry.get()))
    print("After adding the wall:", Wall(v1, v2))

def find():
    global x
    x = []
    start = tuple(map(int, startPathEntry.get()))
    end = tuple(map(int, endPathEntry.get()))
    print("the shortest path is:", find_shortest_path(graph, start, end))
    return x

def wait():
    for j in range(len(x)-1):
        for c in range(1, len(x)-j):
            s = j + c
            for i in range(len(x[j])-1):
                if x[j][i] == x[s][i] and x[j][i+1] == x[s][i+1]:
                    x[s].insert(i,"wait")
    print(x)

root = Tk()
root.title('Warehouse')
root.geometry('568x300')
bg=PhotoImage(file="C:/Users/amr01/OneDrive/Documents/GitHub/Bachelor/interface/warehouse.png")
my_label = Label(root, image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

Label1 = Label(root, text="Dimensions of the warehouse", bd=0, width=23).grid(padx=15, pady=5, row=1, column=1)

xAxisLabel = Label(root, text="x-axis", bd=0, width=15).grid(padx=15, pady=2, row=2, column=0)
xAxis = IntVar()
xAxisEntry = Entry(root, textvariable=xAxis, bd=0, width=20)
xAxisEntry.grid(padx=15, pady=2, row=2, column=1)

yAxisLabel = Label(root, text="y-axis", bd=0, width=15).grid(padx=15, pady=2, row=3, column=0)
yAxis = IntVar()
yAxisEntry = Entry(root, textvariable=yAxis,bd=0, width=20)
yAxisEntry.grid(padx=15, pady=2, row=3, column=1)

distanceLabel = Label(root, text="distance", bd=0, width=15).grid(padx=15, pady=2, row=4, column=0)
distance = IntVar()
distanceEntry = Entry(root, textvariable=distance,bd=0, width=20)
distanceEntry.grid(padx=15, pady=2, row=4, column=1)

Button(root, text='Graph', width=15, command=dimensions, bg="blue", bd=0).grid(padx=0, pady=2, row=4, column=3)

Label2 = Label(root, text="Do you want to add wall?", bd=0, width=20).grid(padx=15, pady=5, row=5, column=1)

startWallLabel = Label(root, text="start point", bd=0, width=15).grid(padx=15, pady=2, row=6, column=0)
startWall = IntVar()
startWallEntry = Entry(root, textvariable=startWall, bd=0, width=20)
startWallEntry.grid(padx=15, pady=2, row=6, column=1)

endWallLabel = Label(root, text="end point", bd=0, width=15).grid(padx=15, pady=2, row=7, column=0)
endWall = IntVar()
endWallEntry = Entry(root, textvariable=endWall,bd=0, width=20)
endWallEntry.grid(padx=15, pady=2, row=7, column=1)

Button(root, text='Add', width=15, command=AddWall, bg="green", bd=0).grid(padx=0, pady=2, row=7, column=3)

Label1 = Label(root, text="Find any path you want", bd=0, width=20).grid(padx=15, pady=2, row=8, column=1)

startPathLabel = Label(root, text="start point", bd=0, width=15).grid(padx=15, pady=5, row=9, column=0)
startPath = IntVar()
startPathEntry = Entry(root, textvariable=startPath, bd=0, width=20)
startPathEntry.grid(padx=15, pady=2, row=9, column=1)

endPathLabel = Label(root, text="end point", bd=0, width=15).grid(padx=15, pady=2, row=10, column=0)
endPath = IntVar()
endPathEntry = Entry(root, textvariable=endPath,bd=0, width=20)
endPathEntry.grid(padx=15, pady=2, row=10, column=1)

Button(root, text='Find', width=15, command=find, bg="green", bd=0).grid(padx=0, pady=2, row=10, column=3)

x.append(find())
print(x)

Button(root, text='View all robots', width=15, command=wait, bg="green", bd=0).grid(padx=0, pady=2, row=11, column=3)



root.mainloop()