from copy import deepcopy


T = [[1,2],[3,4]]
K = deepcopy(T)

K[0][0] = 100

print(K, T)

print(id(T))
print(id(K))

print(id(T[0]),id(T[1]))
print(id(K[0]),id(K[1]))

print(id(T[0][0]),id(T[0][1]))
print(id(K[0][0]),id(K[0][1]))
