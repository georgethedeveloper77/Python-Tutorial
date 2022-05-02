# Calculator
# first = input("first no: ")
# second = input("second no: ")
# sum = int(first) + int(second)
# print("Sum: ",sum)
print('Input only numbers or float')
first = input("first: ")  # float(input("first: "))
second = input("second: ")
sum = float(first) + float(second)
print("Your Sum is: " + str(sum))


def fun():
    return [i for i in range(0, 3, 3)]
print(fun())

def funs():
    return 55 + int(55.55)
print(funs())
