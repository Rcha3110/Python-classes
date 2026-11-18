a = int(input("enter numberator"))
b = int(input("Enter denominator"))
try:
    c = a/b
    print("Result=",c)
except Exception as e:
    print("Division by zero is not possible")
print("Program terminated normally")

l = [12,12,34,56,7]
try:
    print(l[10])
except IndexError as e:
    print("Accesing list beyond its boundary")
print("Program terminated normally")