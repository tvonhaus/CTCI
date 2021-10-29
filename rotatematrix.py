def rotateMatrix(matrix):
    #layers = n/2 (4 and 5 -> 2 layers, 2 and 3 -> 1 layer)
    n = len(matrix)
    layers = n/2
    for layer in range(int(layers)):
        print('layer:',layer)
        first = layer
        last = n - layer - 1
        print('first:',first)
        print('last:',last)
        for i in range(first,last):
            offset = i - first
            top = matrix[first][i]; #save top
            
            #left -> top
            matrix[first][i] = matrix[last - offset][first]
            
            #bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            #right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            
            #top -> right
            matrix[i][last] = top
            
    return matrix


matrix = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
print(matrix)
rotateMatrix(matrix)
print(matrix)
# print(matrix)
# n = len(matrix)
# layers = n/2
# print(int(layers))
# for i in range(int(layers)):
#     print(i)
