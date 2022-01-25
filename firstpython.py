from sympy import Matrix

mx = Matrix(([1,3,-2,0,2,0,0],[2,6,-5,-2,4,-3,0],[0,0,5,10,0,15,0],[2,6,0,8,4,18,0]))
print (mx.rref())

print("adding test")
