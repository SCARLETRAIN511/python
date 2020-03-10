"""
def use_logging(func):
    def wrapper(*args,**kw):
        print("%s is running" % func.__name__)
        return func(*args,**kw)
    return wrapper

@use_logging
def bar():
    print("I am a bar")
"""
def use_logging2(level):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %d is running" % (func.__name__,level))
            return func(*args,**kw)
        return wrapper
    return decorator

@use_logging2(5)
def barN():
    print("barN is running")

if __name__ == "__main__":
    barN()

