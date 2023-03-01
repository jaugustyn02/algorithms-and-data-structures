from zad4testy import runtests


def select_buildings(T,p):
    def prawy(a):
        nonlocal T
        return T[a][2]

    tab_indeksow = [i for i in range(len(T))]
    tab_indeksow.sort(key=prawy)
    z=[[0 for i in range(p+1)]for j in range(len(T))]
    F=[[0 for i in range(p+1)]for j in range(len(T))]
    indeks = tab_indeksow[0]
    for b in range(T[indeks][3],p+1):
        F[0][b]=T[indeks][0]*(T[indeks][2]-T[indeks][1])
        z[0][b]=T[indeks][2]
    for b in range(p+1):
        for i in range(1,len(T)):
            F[i][b]=F[i-1][b]
            z[i][b]=z[i-1][b]
            indeks = tab_indeksow[i]
            if b>=T[indeks][3]:
                k=0
                for j in range(i-1,-1,-1):
                    if z[j][b-T[indeks][3]]<T[indeks][1]:
                        k = F[j][b - T[indeks][3]]
                        break
                k+=(T[indeks][2] - T[indeks][1]) * T[indeks][0]
                a=F[i][b]
                if k>a:
                    z[i][b]=T[indeks][2]
                    F[i][b]=k

    w=len(T)-1
    k=p
    s=F[w][k]
    tab_wynikowa=[]
    while s>0:
        value = F[w][k]
        while w >= 0 and value == F[w][k]:
            w-=1
        w+=1
        indeks = tab_indeksow[w]
        tab_wynikowa.append(indeks)
        s-=(T[indeks][2]-T[indeks][1])*T[indeks][0]
        k-=T[indeks][3]
        a=T[indeks][1]
        w -= 1
        while w>=0 and z[w][k] >= a:
            w-=1

    return tab_wynikowa


runtests( select_buildings )


# if __name__ == '__main__':
#     T= [(7, 11, 28, 23), (6, 1, 18, 91), (3, 1, 88, 35), (4, 1, 2, 3), (3, 6, 7, 75), (3, 21, 76, 95), (2, 1, 71, 3), (3, 9, 12, 11), (3, 6, 8, 7), (2, 13, 14, 75), (3, 6, 56, 43), (4, 1, 17, 99), (3, 1, 37, 95), (4, 1, 68, 35), (3, 1, 14, 51), (3, 1, 28, 7), (4, 16, 23, 39), (3, 29, 50, 63), (2, 1, 11, 35), (3, 1, 10, 27), (3, 26, 37, 27), (2, 11, 23, 51), (3, 1, 21, 7), (3, 19, 20, 91), (2, 1, 65, 59), (3, 3, 6, 67), (3, 56, 59, 71), (2, 7, 26, 51), (3, 78, 97, 27), (4, 35, 49, 55), (3, 2, 57, 23), (3, 9, 25, 99), (4, 32, 87, 99), (3, 93, 191, 35), (2, 48, 74, 43), (3, 23, 50, 35), (2, 44, 46, 35), (3, 23, 31, 99), (4, 1, 16, 79), (3, 21, 63, 75), (4, 48, 66, 55), (3, 59, 105, 87), (4, 1, 47, 59), (3, 1, 16, 43), (2, 18, 22, 63), (3, 61, 63, 95), (3, 92, 151, 71), (4, 85, 110, 59), (3, 72, 86, 7), (4, 45, 46, 75), (3, 60, 65, 63), (3, 97, 107, 43), (3, 78, 105, 99), (3, 1, 100, 7), (3, 56, 60, 31), (4, 37, 44, 95), (3, 1, 66, 3), (3, 57, 59, 11), (3, 54, 64, 19), (3, 61, 77, 3), (4, 60, 63, 19), (3, 51, 61, 39), (2, 24, 58, 11), (3, 67, 68, 23), (2, 74, 84, 79), (3, 107, 116, 63), (3, 24, 49, 19), (2, 75, 76, 87), (3, 14, 72, 59), (2, 57, 92, 63), (3, 88, 151, 91), (3, 83, 148, 91), (3, 22, 61, 43), (4, 35, 65, 39), (3, 40, 42, 87), (3, 135, 165, 79), (3, 74, 106, 39), (3, 85, 108, 91), (3, 1, 91, 87), (4, 41, 85, 47), (3, 116, 131, 71), (2, 133, 159, 15), (3, 80, 85, 67), (3, 145, 208, 39), (3, 46, 52, 59), (4, 43, 66, 91), (3, 18, 61, 23), (2, 89, 95, 39), (3, 114, 153, 31), (3, 65, 91, 99), (2, 1, 50, 35), (3, 107, 126, 51), (4, 62, 104, 91), (3, 89, 128, 83), (2, 12, 13, 67), (3, 109, 138, 15), (3, 100, 111, 51), (4, 65, 78, 67), (3, 126, 152, 83), (2, 117, 164, 87)]
#
#     a=(3, 1, 17, 19)
#     b=(2, 9, 10, 11)
#     p=500
#     tab=[]
#
#
#
#     print(select_buildings(T,p,tab))


