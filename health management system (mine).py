# Health management software
print(" What you wanna do log or retreive , press 1 for log and 2 for retreive ? \n")
def client_name():
    a = {"3":" Rohan" , "4": "Harry" ,"5" :"Hammad"}
    print(" choose from given client list" , a)
    key1 = input()
    name1 = a[key1]
    stuff = {"6": "Exercise", "7": " Diet"}
    print("Okay so for {} , but what you wanna do ,  choose and press that number {},\n ".format(name1, stuff))
    key2 = input()
    name2 = stuff[key2]
    file_name = "{}_{} file".format(name1, name2)
    return file_name

def getdate():
    import datetime
    return datetime.datetime.now()
try:
    b = int(input())
    access = client_name()
    if b==1:
        F1 = open("{}.txt".format(access) , "a")
        time = str(getdate())
        info = input()
        F1.write("{} ,{}".format([time],info))
        F1.write("\n")
        F1.close()

    elif b == 2:
        F2 = open("{}.txt".format(access) , "rt")
        print(F2.read())
        F2.close()
except Exception as e:
    print("Invalid input !!!! ")