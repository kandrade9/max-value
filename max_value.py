n = int(input("Number of elements: "))
while n < 1:
    print("Must have at least one element")
    n = int(input("Number of elements: "))

elements = []
for i in range(n):
    element = input(f"Element {i+1}: ")
    elements.append(int(element))
print(elements)


def max_value(element_list):
    """Returns maximum value within element_list"""
    maximum = 0
    for num in element_list:
        if num > maximum:
            maximum = num
    return "Maximum value is " + str(maximum)


result = max_value(elements)
print(result)









