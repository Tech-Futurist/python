###### may be file descriptor is same as file handler.
# Is there any method in OS module to open a folder similar to file handling ?

# import os
# print(os.getcwd())
# import shutil
#
#
# # os.chdir("Hana")
# # src = os.getcwd()
# dest = os.path.join(os.getcwd(),"Hana")
# with open(os.path.join(os.getcwd(), "Martian.txt"), 'r') as f:
#     print(f.read())


# class Library:
#
#     def __init__(self, library_name):
#         self.lib_name = library_name
#
#
#     def make_directories(self):
#         os.mkdir("{}".format(self.lib_name))
#         os.chdir("{}".format(self.lib_name))
#         print(os.getcwd())
#
#     def Display_books(self):
#         try:
#             self.make_directories()
#             F1 = open("{}.txt".format(self.lib_name), "rt")
#             print(F1.read())
#             F1.close()
#         except Exception as e:
#             print("There is no book in library , first add few then come.")
#             print("Add books using Add_Books()")
#
#
#     def Add_Books(self):
#         os.chdir("{}".format(self.lib_name))
#         print(os.getcwd())
#         F1 = open("{}.txt".format(self.lib_name), "a")
#         # time = str(getdate())
#         proceed = "5"
#         while (proceed == "5"):
#             new_book = input()
#             F1.write("{} ".format(new_book))
#             F1.write("\n")
#             print("Do you wanna add more books ?")
#             choose = {"5": "Yes", "6": "No"}
#             for key, value in choose.items():
#                 print(f" press  {key} for {value}")
#             proceed = input()
#         F1.close()
#
#
# # l4 = Library("Muskan")
# l5 = Library("Hana")
# # l5.Add_Books()
# l5.Display_books()













