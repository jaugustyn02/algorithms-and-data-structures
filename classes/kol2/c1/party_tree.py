from random import randint


class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []
        self.f = -1
        self.g = -1
# end


def create_party_tree(emp_n=100, emp_max=None, fun_min=0, fun_max=100, parent=None):
    if emp_max is None:
        emp_max = max(3, int(emp_n**0.5))
    boss = Employee(randint(fun_min, fun_max))
    rand_emp(boss, emp_n-1, emp_max, fun_min, fun_max)
    return boss
# end


def rand_emp(parent, emp_n, e_max, f_min, f_max):
    if emp_n > 0:
        new_emp_n = randint(0, min(e_max, emp_n))
        emp_n -= new_emp_n
        for _ in range(new_emp_n):
            new_emp = Employee(randint(f_min, f_max))
            parent.emp.append(new_emp)

        if new_emp_n > 0:
            while emp_n > 0:  # usprawnić żeby losowało tylko z puli pracowników których liczba pracowników jest < maksymalnej liczby dozwolonych pracownikóœ
                emp_ind = randint(0, new_emp_n-1)
                # emp_len = len(parent.emp[emp_ind].emp)
                # if emp_len < e_max:
                available_emp = randint(0, min(e_max, emp_n))
                rand_emp(parent.emp[emp_ind], available_emp, e_max, f_min, f_max)
                emp_n -= available_emp
# end


def print_party_tree(parent, margin=""):
    if len(parent.emp) > 0:
        print(margin + "{} ({}):".format(parent.fun, len(parent.emp)), sep="")
    else:
        print(margin, parent.fun, sep="")
    for emp in parent.emp:
        print_party_tree(emp, margin+"\t")
# end


if __name__ == "__main__":
    boss = create_party_tree(100, 10, 0, 100)
    print_party_tree(boss)
# end
