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
        if from_ in self._adjacency_list:
            if to in self._adjacency_list[from_]:
                return True
        return False
    
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
        explored = {}
        explored[start] = start

        frontier = Stack()
        frontier.push(start)

        # USE is_empty (NO parentheses)
        while not frontier.is_empty:
            current = frontier.pop()

            if current == goal:
                return self._path_map_to_path(explored, goal)

            for neighbor in self.neighbors(current):
                if neighbor not in explored:
                    explored[neighbor] = current
                    frontier.push(neighbor)

        return None
    
    def bfs(self, start, goal):
        explored = {}
        explored[start] = start

        frontier = Queue()
        frontier.push(start)

        # USE is_empty (NO parentheses)
        while not frontier.is_empty:
            current = frontier.pop()

            if current == goal:
                return self._path_map_to_path(explored, goal)

            for neighbor in self.neighbors(current):
                if neighbor not in explored:
                    explored[neighbor] = current
                    frontier.push(neighbor)

        return None
    
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
