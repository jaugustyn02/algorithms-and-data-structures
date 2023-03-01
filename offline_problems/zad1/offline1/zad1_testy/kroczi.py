# Jakub Kroczek
# Ten algorytm sortowania w głównej mierze opiera się na sortowaniu Bubble-Sort i Merge-sort,
# dla k=1 zrobiłem zmodyfikowanego Bubble-Sort, a wygląda to tak, że idziemy po tablicy
# jeden raz (dla k>1 później tłumaczę dlaczego 1 raz przechodzę) i jak zamienię dwa kolejne elementy miejscami to będą
# posortowane i nie muszę już sprawdzać czy ten drugi element jest większy od kolejnego, bo jest już posortowany, więc
# przeskakuję o dwie pozycje
# dla 1<k<=log(n) w pierwszym przejściu liczę "n" i sortuję od razu Bubble sortem. Następnie sprawdzam czy k<=log(n),
# jeżeli zał. jest spełnione to jest to Bubble-Sort wiedząc że lista jest k-chaotyczna można wydedukować,
# że przejdzimy po tablicy k razy, gdyż w jednej iteracji dany element zmienia położenie o conajmniej jedną
# pozycję w kierunku miejsca, gdzie będzie się znajdowało na posortowanej pozycji. Lecz dałem tam, że główna pętla
# przejdzie k-1 razy, gdyż przy wyliczaniu "n" już jest +1 iterację głównej pętli sortowane
# dla k>log(n) jest to Merge-Sort
# Złożoność czasowa:
# k = Θ(1) => n
# k = Θ(log n) => n*log(n)
# k = Θ(n) => n*log(n)

from zad1testy import Node, runtests


def SortH(p, k):
    # tu prosze wpisac wlasna implementacje
    first = p
    if k == 1:
        pom = first
        pop = pom
        while pom.next != None:
            if pom.val > pom.next.val:
                tmp = pom.next
                pom.next = pom.next.next
                tmp.next = pom
                if tmp.next == first:
                    first = tmp
                    pop = tmp
                    continue
                pop.next = tmp
                pop = pop.next.next
                pom = pom.next
            else:
                pop = pom
                pom = pom.next
    else:
        n = 1
        pom = first
        pop = pom
        while pom.next != None:
            n += 1
            if pom.val > pom.next.val:
                tmp = pom.next
                pom.next = pom.next.next
                tmp.next = pom
                if tmp.next == first:
                    first = tmp
                    pop = tmp
                    continue
                pop.next = tmp
                pop = pop.next
            else:
                pop = pom
                pom = pom.next
        # z def. logartmu log(n)=k, to 2**k=n
        if n >= 2**k:
            for _ in range(k-1):
                pom = first
                pop = pom
                while pom.next != None:
                    if pom.val > pom.next.val:
                        tmp = pom.next
                        pom.next = pom.next.next
                        tmp.next = pom
                        if tmp.next == first:
                            first = tmp
                            pop = tmp
                            continue
                        pop.next = tmp
                        pop = pop.next
                    else:
                        pop = pom
                        pom = pom.next
        else:
            # Jak to w Merge-Sort scalanie dwóch posortowanych list
            def scal_dwie_listy(a, b):
                if a.val <= b.val:
                    result = a
                    a = a.next
                else:
                    result = b
                    b = b.next
                pom = result
                while a != None and b != None:
                    if a.val <= b.val:
                        pom.next = a
                        a = a.next
                        pom = pom.next
                    else:
                        pom.next = b
                        b = b.next
                        pom = pom.next
                if a != None:
                    pom.next = a
                if b != None:
                    pom.next = b
                return result

            # szukanie środkowego elementu poprzez dwa wskaźniki które idą z predkością s=2i, w=i, gdy "s" dojdzie
            # do końca to "w" będzie w połowie
            def stworz_sr(pocz):
                s = pocz
                w = pocz
                while (s.next != None and s.next.next != None):
                    s = s.next.next
                    w = w.next
                return w
            # tworzenie 2 list potem z tych dwóch po kolejne dwie z każdej z tych dwóch list itd.
            # są one tworzone poprzez rozłączenie jednej listy w dwie listy itd., które potem będą scalane
            # w funkcji scal_dwie_listy()
            def merge_sort(t):
                if t == None or t.next == None:
                    return t
                sr = stworz_sr(t)
                sr_n = sr.next
                sr.next = None
                l = merge_sort(t)
                r = merge_sort(sr_n)
                posortowana = scal_dwie_listy(l, r)
                return posortowana
            first = merge_sort(first)
    return first
    pass


runtests( SortH ) 
