# graph.py
# A graph stored using an adjacency list
# Modified by:
# Note: Please write this yourself, not using an LLM.
from stack import Stack
from que import Queue


class Graph:
    def __init__(self):
        self._adjacency_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = set()
            
    def add_edge(self, from_, to, bidirectional=True):
        if from_ not in self._adjacency_list:
            self._adjacency_list[from_] = set()
        self._adjacency_list[from_].add(to)
        if bidirectional:
            if to not in self._adjacency_list:
                self._adjacency_list[to] = set()
            self._adjacency_list[to].add(from_)
        else:
            if to not in self._adjacency_list:
                self.add_vertex(to)
                
    def neighbors(self, vertex):
        assert vertex in self._adjacency_list, "Vertex not in graph"
        return self._adjacency_list[vertex]
    
    # Return whether or not *from_* exists in the graph,
    # and  *to* is one of its neighbors
    # Return True only if both criteria are true
    def edge_exists(self, from_, to):
        # YOUR CODE HERE
        pass
    
    # Work backwards to find a path from your dfs()
    # or bfs() goal using the explored dictionary as
    # the previous_map
    def _path_map_to_path(self, previous_map, goal):
        path = []
        current = goal
        while True:
            path.insert(0, current)
            previous = previous_map[current]
            if previous == current:
                break
            current = previous
        return path
    
    def dfs(self, start, goal):
        # explored keeps track of not only where we have been
        # but also how we got to it
        # explored[a] = b means we got to a from b
        # we market start as coming from start as a sentinel
        explored = {}
        explored[start] = start
        # frontier = ...
        # 1. Create your frontier with the right abstract data type
        # that we imported above
        # 2. Put start on it
        # 3. Loop while the frontier is not empty
        # 4. pop current off the frontier
        # 5. check if current is the goal and if it is, return the path to it
        # 6. Look through the neighbors of current, only visiting the ones that 
        # are not already explored
        # 7. Mark how you got to them and add them to the frontier
        # 8. Return None if you search through everything and never
        # find the goal
        # YOUR CODE HERE
    
    def bfs(self, start, goal):
        # Copy and paste your code from dfs() making the one 
        # important one-line change to it to make it bfs()
        # YOUR CODE HERE
        pass
    
    def print_explored(self, explored):
        for k, v in explored.items():
            print(f"{k} : {v}")
            
    def __str__(self):
        lines = []
        for v, neighbors in self._adjacency_list.items():
            n_str = ", ".join(str(x) for x in sorted(neighbors))
            lines.append(f"{v}: {n_str}")
        return "\n".join(lines)
    
    def __repr__(self):
        return f"Graph({self._adjacency_list})"
    