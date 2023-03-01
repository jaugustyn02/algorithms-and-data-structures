import time
import os
from zad2test_spec import ALLOWED_TIME, TEST_SPEC

MY_seed = 42
MY_a = 134775813
MY_c = 1
MY_modulus = 2 ** 32


def MY_random():
    global MY_seed, MY_a, MY_c, MY_modulus
    MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
    return MY_seed


def gentest(n, maxint, hint):
    time.sleep(0.5)
    arg = [[MY_random() % maxint, MY_random() % maxint] for _ in range(n)]
    for i in range(n):
        while arg[i][0] == arg[i][1]:
            arg[i][0] = MY_random() % maxint
            arg[i][1] = MY_random() % maxint

        if arg[i][0] > arg[i][1]:
            tmp = arg[i][0]
            arg[i][0] = arg[i][1]
            arg[i][1] = tmp

    return [arg]


def runtests(f):
    global MY_seed
    INITIAL_seed = MY_seed = int(input("Seed: "))
    TESTS = []
    for spec in TEST_SPEC:
        newtest = {}
        arg = gentest(*spec)
        newtest["n"] = spec[0]
        newtest["maxint"] = spec[1]
        newtest["hint"] = f(*arg)
        TESTS.append(newtest)
    save_spec(TESTS, INITIAL_seed)


def save_spec(tests, seed):
    direct = "SPECS"
    path = os.path.join(os.path.dirname(__file__), direct)
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as error:
        print("Directory '%s' can not be created" % direct)
    # sprawdzić czy plik już nie istnieje !!!
    file = open("{}/test_spec{}.py".format(direct, seed), "w")
    file.write("SEED = {}\n\n".format(seed))
    file.write("ALLOWED_TIME = {}\n\n".format(ALLOWED_TIME))
    file.write("TEST_SPEC = [\n")
    for spec in tests:
        file.write("    ({}, {}, {}),\n".format(spec["n"], spec["maxint"], spec["hint"]))
    file.write("]\n")
    file.close()
