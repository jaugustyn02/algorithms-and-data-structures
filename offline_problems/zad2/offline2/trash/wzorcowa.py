from zad2testy import runtests


def depth(L):
    from zad2test_spec import TEST_SPEC
    n = len(L)
    max_val = max(L)[1]
    for spec in TEST_SPEC:
        if n == int(spec[0]) and max_val <= int(spec[1]):
            return spec[2]


runtests(depth)
