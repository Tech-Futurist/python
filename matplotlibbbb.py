### __version__ attribute is use to find the version of any module.

# import matplotlib

# print(matplotlib.__version__)
# u = [-3, -4]
# v = [-4, 3]
# uv1 = 0
# uv2 = 0
# uv3 = 0
# for i in range(len(u)):
#     uv1 = uv1 + u[i] * (-1 * v[i])
#     uv2 = uv2 + (-1 * u[i]) * v[i]
#     uv3 = uv3 + (-1 * u[i]) * (-1 * v[i])
#
# if uv1 and uv2 and uv3 == 0: # why it is not showing the print statement.
#     print("all the three different vectors are perpendicular to each other.")

from random import randrange
# print(randrange(-5,5))
rows = 4
columns = 5
M = []
N = []
for i in range(rows):
    M.append([])
    N.append([])
    for j in range(columns):
        M[i].append(randrange(-5,5))
        N[i].append(randrange(-5,5))
print(M)
print(N)





