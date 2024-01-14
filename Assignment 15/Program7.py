def outer():
    def inner1(a,b):
        print("in inner1")
        return a-b
    def inner2(obj):
        print("in inner2")
        print(obj)
        return inner2
    retinner1 = inner1(10,4)
    retinner2 = inner2(retinner1)
    return retinner2
if __name__=="__main__":
    retobj = outer()
    print(retobj)