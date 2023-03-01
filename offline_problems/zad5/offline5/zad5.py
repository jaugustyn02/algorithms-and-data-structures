# Jan Augustyn
# Algorytm zachłanny polega na:
#   Liniowym przejściu po liście T i dodawaniu kolejnych "plam" do Kolejki Pioretytowej.
#   Jednocześnie kontrolowany jest aktualny zasięg cysterny i gdy jest on równy 0, następuje dotankowanie
#   pojazdu ropą o największej objętości, z dotychczas napotkanych plam (największym piorytecie w kolejce).
#   A miejsce pobrania plamy (indeks) zostaje zapisane w tablicy wynikowej, która przed zwróceniem zostaje posortowana.
# n - len(T)
# m - liczba plam ropy
# Złożoność czasowa: O(nlogm) { nlogn - dla m rzędu n }
# Złożoność pamięciowa: O(m)  { n - dla m rzędu n }

from zad5testy import runtests
from queue import PriorityQueue


def plan(T):
    pqueue = PriorityQueue()
    result = [0]
    tank_range = T[0]-1
    for i in range(1, len(T)-1):
        if T[i] > 0:
            pqueue.put((-T[i], i))
        if tank_range == 0:
            oil_stain = pqueue.get()
            tank_range -= oil_stain[0]
            result.append(oil_stain[1])
        tank_range -= 1
    return sorted(result)
# end


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
