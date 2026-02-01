### check the last version of code
from random import randrange
#
# #
# # your solution is here
## 1st way of doing it.
rows = 4
columns = 5
A = []
B = []
C = []
for i in range(rows):
    A.append([])
    B.append([])
    for j in range(columns):
        a, b = randrange(-5, 5), randrange(-5, 5)
        A[i].append(a)
        B[i].append(b)
       # same as above code
        # A[i].append(randrange(-5,5))
        # B[i].append(randrange(-5,5))

for k in range(rows):

    C.append([])
    for l in range(columns):
        C[k].append((3*A[k][l])-(2*B[k][l]))
print("Matrix A is ", A)
print("Matrix B is ", B)
print("Matrix C is ", C)

### by making seperate matrix for 3A and -2B
# threeA = []
# minustwoB = []
# for i in range(rows):
#     threeA.append([])
#     minustwoB.append([])
#     for j in range(columns):
#         threeA[i].append(3 * A[i][j])
#         minustwoB[i].append(-2 * B[i][j])
# for k in range(rows):
#
#     C.append([])
#     for l in range(columns):
#         C[k].append((threeA[k][l]+minustwoB[k][l]))
# print("Matrix A is ")
# for l1 in A:
#     print(l1)

######### more efficient code
rows = 4
columns = 5
A = []
B = []
C = []
for i in range(rows):
    A.append([])
    B.append([])
    C.append([])
    for j in range(columns):
        a,b = randrange(-5,5),randrange(-5,5)
        A[i].append(a) # same as left side code, A[i].append(randrange(-5,5))
#         # same as left side code, B[i].append(randrange(-5,5))
        B[i].append(b)
        C[i].append((3*a+(-2)*b))
print("Matrix A is ",A)
print("Matrix B is ",B)
print("Matrix C is ",C)