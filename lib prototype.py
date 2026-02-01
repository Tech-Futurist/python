#### it has a record with time but not complete (second one)

######## there is only one way to add a book that is by using the add method , in other way repitation is occuring.
######### try to make something which will directly prompt to the add section if library is empty  and display command is use to show.

###### arrange the books in alphabetical order.

###### total books
######## available books = total - lend books , after showing the number it will
# show who has owned the lend books , it will also show after how many days you will get the book.
########## lend books - file
##### return books - file

######## you have to connect lend file and the return file to the main file i.e.
# the available books such that you can delete or return the file and simultaneouly
# the action will perform on the available books thing


def getdate():
    import datetime
    return datetime.datetime.now()

class Library:

    def __init__(self, library_name):
        self.lib_name = library_name

    # print("Which library do you wanna go")
    # lib_name = input()
    # print("What do you wanna do ?")
    # bucket_list = {"1":" book list" , "2":"Lending the book", "3":"Returning the book","4": "For donating the book"}
    # for keys, values in bucket_list.items():
    #     print(f"press {keys} for {values}")


    def Display_books(self):
        try:
            F1 = open("{}.txt".format(self.lib_name), "rt")
            print(F1.read())
            F1.close()
        except Exception as e:
            print("There is no book in library , first add few then come.")
            print("Add books using Add_Books()")



    # @decorators.func
    def Add_Books(self):
        F1 = open("{}.txt".format(self.lib_name), "a")
        time = str(getdate())
        proceed = "5"
        while(proceed =="5"):
            new_book = input()
            F1.write("{} ,{}".format([time],new_book))
            F1.write("\n")
            print("Do you wanna add more books ?")
            choose = {"5": "Yes", "6": "No"}
            for key, value in choose.items():
                print(f" press  {key} for {value}")
            proceed = input()
        F1.close()


    def Lend(self):
       print("Tell me your name and the book you wanna borrow.")
       ####### try to take input in one go but with complete name means including space too.
       name  = input()
       book = input()
       customer_info = {name:book}
       print(customer_info)


        # if book in content:
        #     content.remove(book)
        #     print(content)
        # else:
        #     print("Sorry not availalbe , please come in few days.")

        # print(content1)
        #
        #
        # print(content1[2])
        # content1.pop(2)
        # print((content1))
    def Available_books(self):
        import os

        with open("{}.txt".format(self.lib_name), "r") as F1:
            print(F1.read())
            with open("Avail_bookss.txt", "w") as output:
                # iterate all lines from file
                book = input()

                for line in (F1.readlines()):
                    # if book matches then don't write it
                    if line.strip("\n") != book:
                        output.write(line)

                    # if book matches then don't write it put space in that place
                    # if line.strip("\n") == book:
                    #     output.write("")

    #
    #     # replace file with original name
        os.rename('Avail_bookss.txt', 'Avail2.txt')
        # with open("{}.txt".format(self.lib_name), "r") as F1:
        #         print(F1.read())
        #         with open("Avail_books.txt","w") as F2:
        #              book = input("So which book do you want to borrow .")
        #              for line in F1:
        #                 if line.strip("\n") != book:
        #                    F2.write(line)
        #                    F2.close()
        #                 F1.close()
                # with open("Avail_books.txt","r") as F2:
                #     print(F2.read())
                #     F2.close()



        # F1 = open("{}.txt".format(self.lib_name), "rt")
        # new_file = F1.readlines()
        #
        # F2 = open("Avail_books.txt","a")
        # for i in new_file:
        #     F2.write("{}".format(i,end=""))
        # #     F2.write("\n")
        # #     print(F2.read())
        # F2.close()
        # F2 = open("Avail_books.txt","rt")
        # print(F2.read())
        # F2.close()

    # @decorators.func

    # @decorators.func
    def Return_book(self):
        ## it will add the book to the to the
        pass
    # help = input()
    # if help == "1":
    #  Display_books()
    # elif help =="2":
    #     Lend()
    # elif help == "3":
    #    Return_book()
    # elif help == "4":
    #     Add_Books()


# l1 = Library("Martian")
l2 = Library("Cool_Mileva")
# l2.Lend()
# l2.Add_Books()
# l2.Display_books()
l2.Available_books()



