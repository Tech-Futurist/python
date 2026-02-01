######## code to make a file inside a folder

import os
# current_directory = os.getcwd()
# os.chdir("Harsh Narwariya")
# with open("Muskan","a") as f:
#     f.write("way to be the best version of me .")
#     os.path.join("Harsh Narwariya/","Muskan")

try:
    os.mkdir("Harsh Narwariya")
except Exception :
    os.chdir("Harsh Narwariya")
    with open("Physics Lover","a") as f:
        f.write("Physics is so amazing .")
        f.write("Diving into physics")
        f.write("\n")

        os.path.join("Harsh Narwariya","Physics Lover")
#
# os.chdir(current_directory)
# with open("To do list","r") as f:
#     os.path.join("Harsh Narwariya","To do list")

######################################################################






