from datetime import datetime,timedelta

with open("Userlogin.txt","r") as bk:
    for line in bk:
        data = line.split(",")
        if(data[0] == str()):
            name = data[1]
            with open("Userlogin.txt","r") as bk:
                    for line in bk:
                        data = line.split(",")
                        if(data[0]== str()):
                            name = data[1]
def returnBook(self,bid):
        try:
            allbook = []
            found = False
            with open("bookData.txt","r") as bk:
                for line in bk:
                    data = line.split(",")
                    if(data[0] == str(bid)):
                        data[3] = str(1)+"\n"
                        line = ",".join(data)

                        found = True
                    allbook.append(line)

                if(found):
                    with open("bookData.txt","w") as bk:
                        for book in allbook:
                            bk.write(book)
                else:
                    print("Record Not Found ")
            allbook = []
            found = False
            with open("issuebook.txt","r") as bk:
                for line in bk:
                    data = line.split(",")
                    if(data[0] == str(bid)):
                        issue_date = input("Enter Issue date in (DD-MM-YYYY) Format :")
                        issue_date = issue_date.split("-")
                        issue_date = datetime(int(issue_date[2]),int(issue_date[1]),int(issue_date[0]))
                        #print(issue_date)

                        submit_date = input("Enter Submit date in (DD-MM-YYYY) Format :")
                        submit_date = submit_date.split("-")
                        submit_date = datetime(int(submit_date[2]),int(submit_date[1]),int(submit_date[0]))
                        #print(submit_date)
                        days = (submit_date-issue_date).days
                        if(days < 1 ):
                            print("Please Enter Coorect Dates ")
                        print(days)
                        data[3] = str(1)+"\n"
                        
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
            print("File Does Not Exist")

def ShowAllBook(self):
        try:
            avlbook = []
            with open("bookData.txt","r") as bk:
                    for line in bk:
                        data = line.split(",")
                        if(data[3] == '1\n'):
                            line = ",".join(data)
                            avlbook.append(line)
                    with open("avlbook.txt","w") as bk:
                        for book in avlbook:
                            bk.write(book)
                    print("***** Library *****")
                    print(" __________________________________________________________________")
                    print("|  Book_ID  |    Book_Name         |    Author_Name       | Status |")
                    print("|__________________________________________________________________|")
                    with open("avlbook.txt","r") as bk:
                        for line in bk:
                            data = line.split(",")
                            print("|  ",data[0],"    |    ",data[1],"    |    ",data[2],"    |  ",data[3],end="|")

                            print("__________________________________________________________________|",)
                            
        except:
            print("*************************************** ")
                             
def retunBook(self,bid):
        try:
            allbook = []
            found = False
            with open("bookData.txt","r") as bk:
                for line in bk:
                    data = line.split(",")
                    if(data[0] == str(bid)):
                        data[3] = "1\n"
                        line = ",".join(data)

                        found = True
                    allbook.append(line)

                if(found):
                    with open("bookData.txt","w") as bk:
                        for book in allbook:
                            bk.write(book)
                else:
                    print("Record Not Found ")
            allbook = []
            found = False
            with open("issuebook.txt","r") as bk:
                for line in bk:
                    data = line.split(",")
                    if(data[0] != str(bid)):
                        print("Issue Book is Not Found")
                    else: 
                        with open("issuebook.txt","r") as bk:
                            for line in bk:
                                data = line.split(",")
                                issue_date = str(data[2])            
                                #issue_date = input("Enter Issue date in (DD-MM-YYYY) Format :")
                                issue_date = issue_date.split("-")
                                issue_date = datetime(int(issue_date[2]),int(issue_date[1]),int(issue_date[0]))
                                #print(issue_date)
                                submit_date = input("Enter Submit date in (DD-MM-YYYY) Format :")
                                submit_date = submit_date.split("-")
                                submit_date = datetime(int(submit_date[2]),int(submit_date[1]),int(submit_date[0]))
                    

                                days = (submit_date-issue_date).days
                                if(days <= 1 ):
                                    print("ERROR: Please Enter Coorect Dates ")                   
                                    print("       Submit Date is grater than Issue Date")

                                elif(days >=7):
                                    r = days - 7
                                    s = r * 15
                                    print(" " )
                                    print("+----------------------------------------+")
                                    print("|  Late Submitted Days :",r,'              |')    
                                    print('+                                        +')                      
                                    print("|  Your Total Fine : Rs.",s,'             |')   
                                    print('+----------------------------------------+')
                                
                                    data[3] = "1\n"  
                                        
                                    line = ",".join(data)

                                    found = True
                                allbook.append(line)

                                if(found):
                                    with open("issuebook.txt","w") as bk:
                                        for book in allbook:
                                            bk.write(book)
                                else:
                                    print("")
            
                          
        except FileNotFoundError:
            print("File Does Not Exist")

