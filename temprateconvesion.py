# program to use range function
def temp_to_celsius(x):
    celsius = (x-32) * 5/9
    return celsius

for x in range(0,101,10):  # range objected can accept three element range (start, stop, steps)
    print(x, temp_to_celsius(x))
