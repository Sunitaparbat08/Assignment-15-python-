def outer():
    def inner():
        return "This is the inner function"
    return inner
if __name__=="__main__":
    retobj = outer()
    retinner =retobj()
    print(retinner)
