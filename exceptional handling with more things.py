##### EOL means basically syntax error like in strings  forgetting the end quotes or parenthesis or square brackets in print statement or lists.
##### EOF means End of file error occur when we use the inbuilt functions like input() or read() in file handling and interpreter read the data incorrectly.

#########  EOF error related thing.
# BaseException class is the base class of the Exception class which in turn inherits the EOFError class.
#
# 2. EOFError is not an error technically, but it is an exception. When the in-built functions such as the input() function or read() function return a string that is empty without reading any data, then the EOFError exception is raised.
#
# 3. This exception is raised when our program is trying to obtain something and do modifications to it, but when it fails to read any data and returns a string that is empty, the EOFError exception is raised.

## you willl know other kind of errors by the time , so just go with the flow for a while. Just complete it.

# a = int(input())
# print(a)
# # had just give the blank space as input in integer input
#********** ValueError: invalid literal for int() with base 10:*********

"""try:
    #Run this code
except Exception as error:
    #Execute this code when there is an exception
else:
    #No Exception. Run this code
Note: An else will only run in the case where no exception occurs."""

"""
when all four keywords use simultaneously
try:
    #Run this code
except Exception as error:
    #Execute this code when there is an exception
else:
   #No Exception. Run this code
finally:
   #Always run this code
"""