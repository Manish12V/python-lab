n=[3,5,7]
def double(lst):
    for x in lst:
        x*=2
        print(x)
        return lst
    print(double(n))
            