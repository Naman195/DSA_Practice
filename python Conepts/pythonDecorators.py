# def printer():
#     print("Welcome")
#     print("Welcome")


# def outer(printer):
#     def inner():
#         printer()
#         print("Welcome")
        
#     return inner
    

# inner = outer(printer)
# print(inner())


def decor1(func):
    def inner():
        return func().upper()
    
    return inner


def decor2(func):
    def inner():
        return func().split()
    
    return inner


@ decor2
@ decor1
def get_name():
    in1 = input("Enter your First Name: ")
    in2 = input("Enter your Last NAme: ")
    full_name = in1 + " " + in2
    return full_name


# get_name = decor2(decor1(get_name))
print(get_name())
