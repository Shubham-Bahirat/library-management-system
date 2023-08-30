from Book_Info import Book

class BookSystem:

    def AddBook(self,b1):
        with open("bookData.txt","a") as bk:
            data = str(b1)
            bk.write(data)
            bk.write("\n")
    def ShowAllBook(self):
        try:
            with open("bookData.txt","r") as fp:
                data = fp.read()
                print("All Book in Our library : ")
                print("--------------------------- ")
                print(data)
        except FileNotFoundError:
            print("File Does Not Exist")

    def issueBook(self,bid):
        cnt = 0
        with open("bookData.txt","r") as bk:
                for line in bk:
                    data = line.split(",")
                    if(data[0] == str(bid)):
                        if(data[3] == '0\n'):
                            print(" Currently Book is Not Available Please Try Another Book ")
                        else:
                            cnt+=1
                            print(" Book is Available Please Enter Your Name to issue it ")
                        if(cnt != 0 ):
                            with open("issuebook.txt","a") as bk:
                                id = bid
                                name = input("Enter Your Name :")
                                date = input("Enter Date (DD/MM/YY) :")
                                status = '0'
                                bk.write(str(id)+",")
                                bk.write(name+",")
                                bk.write(date+",")
                                bk.write(status)
                                bk.write("\n")
                            '''with open("issuebook.txt","r") as bk:
                                data = bk.read()
                            print(data)''' 
                            try:
                                allbook = []
                                found = False
                                with open("bookData.txt","r") as bk:
                                    for line in bk:
                                        data = line.split(",")
                                        if(data[0] == str(id)):
                                            data[3] = str(0)+"\n"

                                            line = ",".join(data)

                                            found = True
                                        allbook.append(line)

                                    if(found):
                                        with open("bookData.txt","w") as bk:
                                            for book in allbook:
                                                bk.write(book)
                                    else:
                                        print("Record Not Found ")


                            except FileNotFoundError:
                                print("File does not exist")
                        
    def showIssueBook(self):
        with open("issuebook.txt","r") as bk:
            data = bk.read()
            print(data)                     
    def returnBook(self,bid):
        try:
            allbook = []
            found = False
            with open("bookData.txt","r") as bk:
                #Line by read
                for line in bk:
                    data = line.split(",")
                    if(data[0] == str(bid)):
                        data[3] = str(1)+"\n"
                        
                        line = ",".join(data)

                        found = True
                    allbook.append(line)

                if(found):
                    with open("bookData.txt","a") as bk:
                        for book in allbook:
                            bk.write(book)
                else:
                    print("Record Not Found ")


        except FileNotFoundError:
            print("File does not exist")

    def ShowAvlBook(self):
        avlbook = []
        with open("bookData.txt","r") as bk:
                for line in bk:
                    data = line.split(",")
                    if(data[3] == '1\n'):
                        line = ",".join(data)
                        avlbook.append(line)
                        print(line)
                with open("avlbook.txt","w") as bk:
                    for book in avlbook:
                        bk.write(book)
                with open("avlbook.txt","r") as bk:
                    d = bk.read()
                print("Available Books :")
                print("--------------------")
                print(d)