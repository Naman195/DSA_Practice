class FiveDivisionError(Exception):
    def __init__(self):
        print("Cannot Divide by 5")
    pass




try:
    n1 = int(input("Enter 1st Number: "))
    n2 = int(input("Enter 2nd Number: "))

    if n2 == 5:
        raise FiveDivisionError 
    
    div = n1/n2
    print(div)
    
except (FiveDivisionError, ZeroDivisionError) as var:
    print(var)


print("Rest Of Code")  