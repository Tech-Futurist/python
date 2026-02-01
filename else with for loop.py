# use of else with for loop


# it is use when we are dealing with long programs and to reduce the error or to make program more readable or elegant
# like we can also use flags in our loops to avoid error , flags means more and more print statement.

# case 1:-
##### Normal loop so it will go to the else statement.
# lis = ["Mileva","Martian","Physics","Idiot"]
#
# for i in lis:
#     print(i)
# else:
#     print("loop was run successfully.")

# case 2:-
#### break condition but checking element and it was found so it won't go into the else block.
#******************** we are finding something and got it so it won't go to the else block.*******************
lis2 = ["roti","chawal","shakes","paratha"]
for j in lis2:
    print(j)
    if j == "shakes":
        break
else:
    print("coz of some error the loop was stopped suddenly.")

# # case 3 :-
# #### break statement hai but check karne wali hai item ko so else main jaayega
#**************** we are searching something and hadn't find so here it will go to the else loop.******************
# lis2 = ["roti","chawal","shakes","paratha"]
# for j in lis2:
#     if j == "Chocolates":
#         break
#
# else:
#     print("your item was not found")