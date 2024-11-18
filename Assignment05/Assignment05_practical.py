from typing import List, Tuple
from collections import deque, defaultdict
import heapq

def construct_adjacency_matrix(edgelist, num_nodes, is_directed=False):
    adj_m = [[0] * num_nodes for _ in range(num_nodes)]
    
    for start, end in edgelist:
 
        adj_m[start-1][end-1] = 1
        
        if not is_directed:
            adj_m[end-1][start-1] =  1

    return adj_m


def construct_adjacency_matrix_weighted(edgelist, num_nodes, is_directed=False):
    
    adj_m = [[0] * num_nodes for _ in range(num_nodes)]
    
    for start, end, weight in edgelist:
        adj_m[start-1][end-1] = weight 
        
        if not is_directed:
            adj_m[end-1][start-1] = weight

    return adj_m


# ============ Q1 ============
def princeJourney(v, routes, home, target):
    
    def bfs_graph(adj_matrix, home, target):
        seen = []
        queue = deque([home])

        while queue:
            node = queue.popleft()
            print(node)
            seen.append(node)

            if node == target:
                return True

            for next in range(v):
                if adj_matrix[node][next] == 1 and next not in seen:
                    queue.append(next)


        return False
    
    if len(routes) == 0:
        return home == target

    adj_m = construct_adjacency_matrix(routes, v)
    return bfs_graph(adj_m, home-1, target-1)

# ============ Q2 ============
def constrainedNetwork(checkpoints: int, paths: int, network: list[Tuple[int, int, int]]): 

    def recursive_exploration(adj_matrix, node=0, past_weight=float('inf'), path_weight = 0):
        if node == len(adj_matrix)-1:
            return path_weight
        
        valid_paths = []
        for next_node in range(len(adj_matrix[node])):
            next_weight =  adj_matrix[node][next_node]
            if 0 < next_weight < past_weight:
                new_path_weight = path_weight + next_weight
                result = recursive_exploration(adj_matrix, node=next_node, past_weight=next_weight, path_weight=new_path_weight)
                if result != -1:
                    valid_paths.append(result)

        return min(valid_paths) if len(valid_paths) > 0 else -1

    adj_matrix = construct_adjacency_matrix_weighted(network, checkpoints)
    return recursive_exploration(adj_matrix)


# ============ Q3 ============
def MostFestiveExperience(n: int, highways: List[Tuple[int,int]], IsDiwali: List[int]):
    
    def count_connected_cities(node, visited, path_count = 0):
        visited[node] = True
        path_count += 1 if IsDiwali[node] == 1 else -1

        # print(f"Node: {node}, path_count: {path_count}")
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                child_path = count_connected_cities(neighbor, visited, path_count)
                path_count = max(path_count, child_path)
   

        return  path_count

    city_differences = []
    adj_matrix = construct_adjacency_matrix(highways, n) 

    for i in range(n):
        visited = [False] * n
        city_differences.append(count_connected_cities(i, visited))

    return city_differences

# ============ Q4 ============
def findDominion(dominion: List[List[int]]) -> int:

    # stack of nodes 
    # bfs removing all elements from the stack that are seen
    # each bfs call is one connected component

    def all_nodes(node):
        queue = deque([node])

        while queue:
            node = queue.popleft()
            visited[node] = True

            for neighbor in range(len(dominion)):
                if dominion[node][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)



    nodes = deque(list(range(len(dominion))))
    visited = [False] * len(nodes)
    num_dominions = 0
    while nodes:
        node = nodes.popleft()
        
        if not visited[node]:
            all_nodes(node)
            num_dominions += 1


    return num_dominions




# ============ Q5 ============
def Rangipur_Network(graph: List[List[int]]) -> bool:

    # check if graph is bipartite 

    # convert to adjacency dictionary where the key is the id and values are all nodes connected
    adj_dict = {index: value for index, value in enumerate(graph)}
    colors = [None] * len(adj_dict)

    def check_bipartite():

        visited = []
        queue = deque([0])
        colors[0] = 0
        while queue:

            node = queue.popleft()
            visited.append(node)
            current_color = colors[node]

            for neighbor in adj_dict[node]:
                if colors[neighbor] is None: 
                    colors[neighbor] = 1 if current_color == 0 else 0
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:
                    return False

        return True

    return check_bipartite()


# ============ Q6 ============
def manhattan_dist(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

def minCostConnectPoints(points: List[List[int]]) -> int:

    # Traveling salesman problem 
    # find minimum spanning tree
    # Using Prims algorithm

    heap = [(0, 0)]  
    total_cost = 0
    visited = []

    while len(visited) < len(points):
        min_cost, point = heapq.heappop(heap)
        if point in visited:
            continue

        visited.append(point)
        total_cost += min_cost

        for next_point in range(len(points)):
            # add new all new edges to consider
            if next_point not in visited:
                dist = manhattan_dist(points[point], points[next_point])
                heapq.heappush(heap, (dist, next_point))

    return total_cost

# ============ Q7 ============
def findCheapestLandTransport(n, routes, src, dst, K):
# Your implementation here
    
    adj_dict = defaultdict(list)
    for i, j, cost, _ in routes:        
        adj_dict[i].append((j,cost))

    # print(adj_dict)


    #djisktras shortest path algorithmn
    # priority queue holding information on distance, path length, and node value
    distances = [float('inf')] * n
    distances[src] = 0
    heap = [(0, 0, src)]
    while heap:
        dist, path, node = heapq.heappop(heap)
        # print(heap)
        # avoid going over K paths
        if path > K:
            continue

        for neighbor, weight in adj_dict[node]:
            cumultive_weight = dist + weight 
            if cumultive_weight < distances[neighbor]:
                distances[neighbor] = cumultive_weight
                heapq.heappush(heap, (cumultive_weight, path+1, neighbor))


    if distances[dst] != float('inf'):
        return distances[dst]
    else:
        return -1


# ============ Q8 ============
def influencer_network(n:int, connections:list[list[int]]) -> list[list[int]]:

    # flip direction keeping track of every neighbor that influences a node 
    adj_dict = defaultdict(list)
    for i, j in connections:        
        adj_dict[j].append(i)


    # perform bfs on reversed dict 
    # avoid computation on previously visited nodes
    # if influenced by 0 also influenced by every node inluencing 0 
    affected = {}
    def influenced_bfs(start):
        if start in affected:
            return affected[start]
        
        influenced_by = set()

        queue = deque([start])
        while queue:
            node = queue.popleft()

            for neighbor in adj_dict[node]:
                if neighbor not in influenced_by:
                    influenced_by.add(neighbor)
                    if neighbor in affected:
                        influenced_by.update(affected[neighbor])
                    else:
                        queue.append(neighbor)
                

        affected[start] = sorted(set(influenced_by))
        return affected[start]


    results = [influenced_bfs(i) for i in range(n)]
    return results


# ============ Q9 ============


def GraphInGokuldham(n: int, s: str) -> int:
    representatives = list(range(n*2))
    stack = []

    # find edges
    for j, char in enumerate(s):
        if char == '(':
            stack.append(j)
        elif char == ')':
            if stack:
                i = stack.pop()
                union(i, j, representatives)
                if stack:
                    last = stack[-1] + 1
                else:
                    last = 0

                union(last, j, representatives)
               
    print(representatives)
    for i in range(len(representatives)):
        find(i, representatives)

    unique_components = len(set(representatives))

    return unique_components







# ============ Q10 ============
def festiveWalkPath(n: int, streets: List[List[int]]) -> int:
    adj_dict = defaultdict(list)
    for i, j in streets:        
        adj_dict[j].append(i)
        adj_dict[i].append(j)



    def detect_cycle(node, parent, visited, path = []):
        path.append(node)
        visited[node] = True
        
        for neighbor in adj_dict[node]:
            if neighbor == parent:
                continue
            if visited[neighbor]:  
                if neighbor in path:
                    cycle_start_idx = path.index(neighbor)
                    return len(path[cycle_start_idx:]) 
            else:
                cycle_length = detect_cycle(neighbor, node, visited[:], path[:])
                if cycle_length != -1:
                    return cycle_length

        return -1


    min_path = float('inf')
    visited = [False] * n  
    for i in range(n):
        cycle_length = detect_cycle(i, -1, visited=visited, path=[]) 
        if cycle_length != -1:
            # print(cycle_length)
            min_path = min(min_path, cycle_length)


    return min_path if min_path != float('inf') else -1

        


# ============ Q11 ============
def countComponents(n: int, edges: list[list[int]]) -> int:
    representatives = list(range(n))
    for i,j in edges:
        union(i,j, representatives)
    
    return len(set(representatives))

def find(x, representatives):
    if x != representatives[x]:
        representatives[x] = find(representatives[x], representatives)
    return representatives[x]

def union(x,y, representatives):
    parent_x = find(x, representatives)
    parent_y = find(y, representatives)
    if parent_x != parent_y:
        representatives[parent_y] = parent_x
    