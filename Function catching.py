## create prime no. series using recursion. and then use caching method.
# try A.P. , G.P. and A.G.P series. for function catching.


####### try more function catching examples

'''
Just some extra things
# You can increase the recursion limit using sys module

import sys
# sys.setrecursionlimit(10**12)


# make main function
# ask user kitni value ko cache karna hai
# make function
# lru cache ko input main dena hai
'''

# factorial
# import time
# from functools import lru_cache,cache
# @cache
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * fact(n-1)
# start_time = time.time()
# print(fact(901))
# end_time = time.time()
# print(end_time-start_time)
#
# start_time = time.time()
# print(fact(904))
# end_time = time.time()
# print(end_time-start_time)
#
# start_time = time.time()
# print(fact(903))
# end_time = time.time()
# print(end_time-start_time)

######### checking whether the number is prime or not.
# prime no.s
# n = 6 # n is how many no. you wanna check.
# for j in range(n+1):
#     number = int(input())# which no. do you wanna check.
#     if number>1:
#         if number == 2:# if no. is equal to 2 then no doubt it is a prime number.
#             print("2 is a prime number.")
#         # if no. is greater than 1 and not equal to 2 so checking whether it is prime or not.
#         else:
#             #  go through all the elements in the loop or it will divide by all the numbers less than the given no. and greater than one until it will found the first no. which is divisible by this.
#             # and if still it is not divisible by the number than it will go to the else block means it's a prime number.
#             for i in range(2,number):
#                 if number%i == 0:
#                     print("It's not a prime number.")
#                     break
#             else:
#                 print(f"{number} is a prime number.")
#     # here if it is equal to one or less than one than not a prime number.
#     else:
#         print("It's not a prime number.")

##### prime number series*******

# print("Only give no. which are greater than 2")
# def prime_number(number):
#     for i in range(2 ,number+1):
#         for j in range(2, i+1):
#             if (i+1) % j == 0:
#                 pass
#             else:
#                 print(number)
#
#
# prime_number(17)
##### try to make a recursion function of this , but it will work example if 289 square of 17 so it will start checking from 2 to 17 until it got the first multiple
# so is there any way to not gone through 2 to 16 for 289 , coz same will happen for 49 it will check from 2  to 7 to get a first multiple.


import functools
import time
@functools.lru_cache(maxsize=6)
def prime_no(number):
   for i in range(2,number+1):
        if i==2:
            print(i , end=" ")
        else:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                print(i , end=" ")

a = time.time()
prime_no(20)
b = time.time()
c = b - a
print()
print(c)

a = time.time()
prime_no(200)
b = time.time()
c = b - a
print()
print(c)

a = time.time()
prime_no(2000)
b = time.time()
c = b - a
print()
print(c)

a = time.time()
prime_no(20000)
b = time.time()
c = b - a
print()
print(c)

a = time.time()
prime_no(200000)
b = time.time()
c = b - a
print()
print(c)
# 0.0 ,20 , 0.0
# 0.0010280609130859375 , 200 , 0.0
# 0.02592945098876953 , 2000 , 0.022104740142822266
# 1.4879951477050781 , 20000
# 139.17278718948364 , 200000

# why there is a difference in timing in running of the same function like same values. and time reduce hi nahi hua increase ho gaya lru_cache lagane ke baad bhi.
###### if caching is working only in case of recursion then like same thing ko store karna hai and in prime no. may be it's really not the case that's why prime no. is so unique.
# recursion is not possible in prime number. here we don't know konsa number work karega.
# 0.0 , 20
# 0.0 ,200
# 0.037750959396362305 ,2000
# 3.3752927780151367 ,20000
# 249.35942363739014 ,200000


