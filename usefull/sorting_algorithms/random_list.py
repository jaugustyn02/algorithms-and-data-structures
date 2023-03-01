from random import randint


def create_random_list(n, a, b):
    return [randint(a, b) for _ in range(n)]
    
    
def create_dense_list(n, a, b, k):
    A = [ randint(a, a+100)/1 for _ in range(k) ]
    B = [randint(a, b)/1 for _ in range(n-k) ]
    return A + B
    

if __name__ == "__main__":
    T = create_dense_list(1000, 1, 1000, 100)
    print(T)
