def outer():
    def inner():
        return "Hello,Core2Web"
    return inner
    print("Inner outer function")
if __name__=="__main__":
    result = outer()()
    print(result)