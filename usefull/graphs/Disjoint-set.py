class DisjointSet:
    class Set:
        def __init__(self, ind):
            self.index = ind
            self.rank = 0
            self.parent = self
        # end init
    # end class

    def __init__(self, V=0):
        self.V = V
        self.vertices = [self.Set(i) for i in range(V)]
    # end init

    def clear(self):
        self.vertices = [self.Set(i) for i in range(self.V)]
    # end def

    def find(self, x):
        if x != x.parent:
            x.parent = self.find(x.parent)
        return x.parent
    # end def

    def union(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)

    def print(self):
        for i, v in enumerate(self.vertices):
            print(i, v.parent.index, sep="->", end="  ")
    # end def
# end class


def main():
    ds = DisjointSet(10)
    ds.print()
# end main


if __name__ == "__main__":
    main()
# end if
