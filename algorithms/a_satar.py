#Reference:
#https://www.pythonpool.com/a-star-algorithm-python/ 

import timeit

def A_Star_Algo(start, target):
    open_list = set([start])
    closed_list = set([])
    g = {} 
    parents = {}
    g[start] = 0
    parents[start] = start
    while len(open_list) > 0:
        neighbor_node = None
        #find the neighbor_node with the least f value
        for current_node in open_list: #loop over all the neighboring nodes of the open node
            if neighbor_node == None or g[current_node] + h(current_node) < g[neighbor_node] + h(neighbor_node): #cost function
                neighbor_node = current_node
        if neighbor_node == target or graph[neighbor_node] == None: #if we reach the target
            final_path(parents, start, neighbor_node)
        else: #if the neighbor node has g value less than the current node
            for (m, weight) in Get_Neighbor(neighbor_node):
                # if the current neighbor_node is not presentin both open_lst and closed_lst
                # add it to open_lst and note neighbor_node as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = neighbor_node
                    g[m] = g[neighbor_node] + weight
                elif g[m] > g[neighbor_node] + weight:
                  g[m] = g[neighbor_node] + weight
                  parents[m] = neighbor_node
                  if m in closed_list:
                    closed_list.remove(m)
                    open_list.add(m)
        if neighbor_node == None:
            return ('Path does not exist!')
        open_list.remove(neighbor_node)
        closed_list.add(neighbor_node)
    return None

def Get_Neighbor(current_node):
  return graph[current_node]

#Get all the choosed nodes and put it in an array called path
def final_path(parents, begin, neighbor_node):
    path = []
    while parents[neighbor_node] != neighbor_node:
        path.append(neighbor_node)
        neighbor_node = parents[neighbor_node]
    path.append(begin)
    path.reverse()
    print("Path found: ", path)
    return None 


if __name__ == "__main__":
    def h(n): #it is the cost of each node we have h(n) 
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
        }
        return H_dist[n]
    graph = {#Describe your graph here, each neighbor and their distance
        'A': [('B', 2), ('E', 3)],
        'B': [('A', 2), ('C', 1), ('G', 9)],
        'C': [('B', 1)],
        'D': [('E', 6), ('G', 1)],
        'E': [('A', 3), ('D', 6)],
        'G': [('B', 9), ('D', 1)]
    }
    starttime = timeit.default_timer()
    print("The start time is :",starttime)
    A_Star_Algo('A', 'G')
    print("The end time is :",timeit.default_timer())
    print("The time difference is :", timeit.default_timer() - starttime)