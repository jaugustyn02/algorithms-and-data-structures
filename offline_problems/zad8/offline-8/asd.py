from zad8testy import runtests
import math


class Node:
    def __init__(self, value):
        self.parent=self
        self.value=value
        self.rank=0

def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return False
    if x.rank>y.rank:
        y.parent=x
        x.rank += y.rank+1
    else:
        x.parent=y
        y.rank += x.rank+1
    return True

def highway(A):
    V = len(A)
    E = V*(V-1)//2
    G=[]
    for i in range(V-1):
        for j in range(i+1,V):
            x1=A[i][0]
            x2=A[j][0]
            y1=A[i][1]
            y2=A[j][1]

            czas=math.ceil(math.sqrt((x1-x2)**2+(y1-y2)**2))
            G.append((i,j,czas))
    tab=[]
    for i in range(V):
        tab.append(Node(i))

    G.sort(key=lambda x: x[2])
    ostateczna=math.inf
    for i in range(E-V+2):
        min_waga = G[i][2]
        if G[i+V-2][2]-min_waga >= ostateczna: continue
        union(tab[G[i][0]], tab[G[i][1]])
        n = 1
        flag = True
        for j in range(i+1, E):
            if union(tab[G[j][0]], tab[G[j][1]]):
                roznica = G[j][2] - min_waga
                n += 1
                if roznica >= ostateczna:
                    flag = False
                    break
                if n == V-1: break

        if flag:
            if n < V-1: return ostateczna
            ostateczna=roznica

        for x in tab:
            x.parent=x
            x.rank=0
    return ostateczna

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )