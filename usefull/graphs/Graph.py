from random import randint
from math import inf


class UndirectedGraph:
    def __init__(self, ver=10, den=2, wg=False, conn=True):  # density lvl 0-5
        self.V = ver
        self.E = 0
        self.density_lvl = max(min(den, 5), 0)
        self.weights = wg
        self.adjacency_list = [[] for _ in range(ver)]
        if not self.weights:
            self.adjacency_matrix = [[0 for _ in range(ver)] for _ in range(ver)]
        else:
            self.weight_max = 10
            self.weight_min = 0
            self.adjacency_matrix = [[inf for _ in range(ver)] for _ in range(ver)]
        self.edges_list = []
        self.connectivity = conn
        self.generate_edges()
    # end def

    def generate_edges(self):
        den = self.density_lvl
        if den == 0: return
        V = self.V
        a1 = V-1
        a5 = V*(V-1)//2
        r = (a5 - a1)/4
        E_left = int((den-1)*r)
        self.E = a1 + E_left
        if self.connectivity:
            self.generate_st()
        else:
            E_left = self.E
        while E_left:
            i = randint(0, V-2)
            j = randint(i+1, V-1)
            if self.add_edge(i, j):
                E_left -= 1
        for row in self.adjacency_list:
            row.sort()
        if not self.weights:
            self.edges_list.sort()
        # end def

    def generate_st(self):
        if self.V == 0: return
        visited = [0]
        unvisited = [i for i in range(1, self.V)]
        for _ in range(self.V-1):
            i = randint(0, len(visited)-1)
            j = randint(0, len(unvisited)-1)
            a, b = visited[i], unvisited[j]
            self.add_edge(a, b)
            visited.append(b)
            unvisited.pop(j)

    def add_edge(self, i, j):
        if (not self.weights and self.adjacency_matrix[i][j])\
                or (self.weights and self.adjacency_matrix[i][j] != inf):
            return False
        if not self.weights:
            self.adjacency_matrix[i][j] = 1
            self.adjacency_matrix[j][i] = 1
            self.adjacency_list[i].append(j)
            self.adjacency_list[j].append(i)
            self.edges_list.append((i, j))
        else:
            w = randint(self.weight_min, self.weight_max)
            self.adjacency_matrix[i][j] = w
            self.adjacency_matrix[j][i] = w
            self.adjacency_list[i].append((j, w))
            self.adjacency_list[j].append((i, w))
            self.edges_list.append((i, j, w))
        return True

    def print(self, forms='l', no_path='-'):
        # print adjacency list
        if 'l' in forms:
            print("Adjacency list:")
            for i, row in enumerate(self.adjacency_list):
                print(i, row)
            print()
        # print adjacency matrix
        if 'm' in forms:
            print("Adjacency matrix:")
            print('', end='\t')
            for i in range(self.V):
                print(i, end='\t')
            print()
            for i, row in enumerate(self.adjacency_matrix):
                print(i, end='\t')
                for x in row:
                    if x != inf: print(x, end='\t')
                    else: print(no_path, end='\t')
                print()
            print()
        if 'e' in forms:
            print("Edges list:")
            for i in range(self.E-1):
                print(self.edges_list[i], end=", ")
                if (i+1) % 10 == 0: print()
            print(self.edges_list[-1])
# end class


if __name__ == "__main__":
    G = UndirectedGraph(1000, den=3)
    # G.print_graph('lem')
    # G.print_graph('l')
    # G.print_graph('e')
