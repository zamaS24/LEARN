import numpy as np 
import os


#_______________ Basics
a = np.array([1,2,3,4,5])   #creating a numpy array

print(a)
print(a.shape)  #size of the array, here it's (5,)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)

print(a[0]) 
a[0] = 10
print(a[0])

b = a * np.array([0,1,0,0,1]) #B will be an array a(ij) * arr(ij)
print(b)

#_____________ Array vs Lists
a = np.array([1,2,3])
a = np.sqrt(a)
print(a)

#_____________ Dot Product
# It is also an Instance method
dot = 0
a1 = np.array([1,2,3])
a2 = np.array([1,3,6])
l1 = [1,2,3]
l2 = [4,5,6]
for i in range(len(l1)): 
    dot += l1[i] * l2[i]
print(dot)

dot = np.dot(a1,a2) #produit cartesien
print(dot)

# Nd arrays 
a = np.array([[1,2,3],[1,2,3],[1,3,4]])
print(f"Shape: {a.shape}")
a[0][0] = 99
print(a[0][0])

print(a.T)              # Transpose
print(np.linalg.inv(a)) # Inverse, matrice should be square
print(np.linalg.det(a)) # Determinant of a
print(np.diag(a))       # Diagonal matrix return is array
print(np.diag(np.diag(a))) # Diagonal on array, returns matrix, of diagonal and other elements are zero


#_____________ Slicing, indexing, Boolean indexing
if os.name == 'nt':  # for Windows
    os.system('cls')

a = np.array([
    [1,2,3,4],
    [9,1,5,6]
])
print("a: \n", a)
print("\na[0][2]=", a[0][1])

s = a[0:1, 1:3]           # Slicing , just imagine it 
b = a[-1,-2]            # Negative indexex, last row, second last column
print(s)

bool_idx = a > 2
print(bool_idx)

a = np.array([1,2,3,4,5])
b = [2,3,4]
print(a[b])     # It will return an array of the values of the index

even = np.argwhere(a%2==0).flatten() 
# flatten() :converting a multi-dimensional array into a one-dimensional array
# argwhere: returns the indices of the elements in an array that satisfy a certain condition.


#_____________ Reshaping     

if os.name == 'nt':  # for Windows
    os.system('cls')

a = np.arange(1,7)
print(a)
print(a.shape)
b = a.reshape((2,3))        # rearranger les elements du tableau selon le reshape
a = np.arange(1,7)
print(a)
print(a.shape)

b = a[np.newaxis, :]        # add an extra dimension to the array, in columns or rows
print(b)
print(b.shape)
c = b[np.newaxis, :]
print(c)
print(c.shape)

#_____________ Concatenation     

if os.name == 'nt':  # for Windows
    os.system('cls')

a = np.array([[1,2], [3,4]])
print("\na",a)
b = np.array([[5,6]])
c = np.concatenate((a,b))                   #Concatention
print("\nc",c)
d = np.concatenate((a,b.T), axis = 1)       #concatenation en colonne
print("\nd",d)

array = np.array([1,2,3,4])
matrix = np.array([[1,2,3,4]])
matrixT = matrix.T

print("\narray",array)
print("\narrayT", array.T)      #An array is always an array. 
print("\nmatrix",matrix)
print("\nmatrixT",matrixT)  

a = np.array([1,2,3,4])
b = np.array([1,3,4,5])

c = np.hstack((a,b))            # H stack and vstack
d = np.vstack((a,b))


print(c)
print(d)

# ____________ Broadcasting
if os.name == 'nt':  # for Windows
    os.system('cls')

x = np.array([[1,2,3],[1,4,5],[5,6,7]])
y = np.array([1,0,1])

sum = y + x                     #Broadcasting, the addittion will be made to all the arrays of the matrix, without rewritng the [1,0,1] 3 times
print("\nsum",sum)

# ____________ Functions and axis (Data sience)
if os.name == 'nt':  # for Windows
    os.system('cls')

a = np.array(
    [
     [1,2,3,4,5,6,7,8,9,10  ],
     [1,4,5,6,7,8,9,10,11,12]
    ]
)
print(a)
print(a.sum())          #Sum of all elements
print(a.sum(axis=0))    #Sum along the rows
print(a.sum(axis=1))    #Sum along the columns
# axis is used to specify the dimension or dimensions along which an operation should be applied.

#                       .mean(axis=)
#                       .var() la variance
#                       .std() ecart type standard deviation
#                       .min()
#                       .max()
print(a.mean())
print(a.mean(axis=0))
print(np.std(a, axis = None))


#_______________ DATA TYPES

x = np.array([1.0,2.0], dtype = np.float32)
print(a.dtype)

#_______________ COPYING
# np uses referenced objects
b = a.copy() #To actually cope the a object

#______________ Generating arrays and random numbers
a = np.zeros((2,3))         #np.zeros()
print(a)

a = np.ones((2,3))          #np.ones()
print(b)

a = np.full((2,3), 5.0)    #np.full()
print(c)

a = np.eye(3)              #np.eye() diagonale a 1 autre zero
print(d)

a = np.arange(20)          #np.arange()

a = np.linspace(0,10,5)     #np.linspace() create equally spaced arrays
print(a)

a = np.random.random((3,2))     # 0-1
print(a)

a = np.random.randn(1000)       # Normale, Gaussiene
print(a)

a = np.random.randint(3,10,size=(3,3)) #random.randint()
points = np.random.uniform(0,1, size=(2,10)) # real values instead of int values
print(a)


#_______________ Linear Algebra (PCA, and ML) (ACP, AA) and solving linear systems
if os.name == 'nt':  # for Windows
    os.system('cls')

a = np.array([[1,2],[3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)    #Valeurs propres

print("eigenvalues",eigenvalues)
print("eigenvectors",eigenvectors)

# evec * eval = A * eval
b = eigenvectors[:,0] * eigenvalues[0]
print("b", b)

c = a @ eigenvectors[:,0]

print(np.allclose(b,c))     # Don't use if (b == c)

print(np.array([1,2,3,4,5]) @ np.array([2,4,5,6,7]))


# Solving linear system
"""
    x1 + x2 = 2200
    1.5x1 + 4.0 x2 = 5050
    Solution:
    A.x = B         / x = (x1,x2).T, A = (1.0 1.0) ,b = (2200,5050).T
                                         (1.5 4.0)
    Ax=B <=> x = A^-1.B
"""
A = np.array([[1.0 ,1.0],
               [1.5, 4.0]])

B = np.array([2200,5050])
print(B)
X = np.linalg.inv(A).dot(B)
print(X)

#_____ Better way to do it: 
x = np.linalg.solve(A,B)
print(x)

#_______________ Load CSV
# data = np.loadtxt('spambase.csv',delimiter=",", dtype=np.float32)
# data = np.genfromtxt('spambase.csv', delimiter=",", dtype=np.float32)
# print(data)




















































