def adjacentElementsProduct(inputArray):
    
    max_product = inputArray[0] * inputArray[1]

    for i in range(1, len(inputArray) - 1):
        produto = inputArray[i] * inputArray[i + 1]
        if produto > max_product:
            max_product = produto

    return max_product

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
print(adjacentElementsProduct([1, 2, 3, 4]))
print(adjacentElementsProduct([-1, -2, -3, -4]))