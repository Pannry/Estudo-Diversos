def mf(a):
    if a == 0:
        return 0
    elif a >= 1:
        print(rec(a))
        return mf(a-1)

def rec(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a >= 2:
        return rec(a - 1) + rec(a - 2)


mf(20)
