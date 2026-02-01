# Observations:
#
# The dimension of the row of  𝑀  is the same as the dimension of  𝑣 . Otherwise, the inner product is not defined.
# The dimension of the result vector is the number of rows in  𝑀 , because we have the dot product for each row of  𝑀
"""
M = [[-1,0,1],[-2,-3,4],[1,5,6]]
v = [[1],[-3],[2]]
# first entry of u is dot product of first row of M and v.
u = [] # u = Mv
for i in range(3):
    u.append([])
    dot = 0
    for j in  range(3):
        dot = dot+( M[i][j]*v[j][0])
    u[i].append(dot)
print(u)

# output
# [[1], [15], [-2]] , this must be the correct way coz woh different rows ko represent kar raha hai. so list ke andar hi element hoga.

"""
"""
it's like sir's solution

M = [[-1,0,1],[-2,-3,4],[1,5,6]]
v = [[1],[-3],[2]]
# first entry of u is dot product of first row of M and v.
u = []  # u = Mv
for i in range(3):

    dot = 0
    for j in range(3):
        dot = dot + (M[i][j] * v[j][0])
    u.append(dot)
print(u)
# [1, 15, -2]

"""





