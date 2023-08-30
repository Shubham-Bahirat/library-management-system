from Book_Info import Book
from datetime import datetime,timedelta

class BookSystem:
    def AddBook(self,b1):                   # Add Book In " bookData.txt " File
        with open("bookData.txt","a") as bk:
            data = str(b1)
            bk.write(data)
            bk.write("\n")
    def ShowAllBook(self):                   # Display All Availeble Book Details 
        try:
            cnt = 1
            print(" ")
            s = " All Books 📚 in our Library "
            print(s.center(90,"-"))
            print("                                                                                        ")
            print("     ___________________________________________________________________________________________")
            print("    | Sr.No. |  Book_ID  |    Book_Name                |    Author_Name              |  Status  |")
            print("    |________|___________|_____________________________|_____________________________|__________|")
            with open("bookData.txt","r") as bk:
                    for line in bk:
                        data = line.split(",")
                        if(data[3] == '1\n'):      
                            length = len(data[1]) 
                            length_1 = len(data[2])
                            result = 25 - length
                            result_1 = 25 - length_1
                            with open("Spaces.txt","r") as bk:
                                for line in bk:
                                    data2 = line.split(",")
               
                            print("    |  ",cnt,"   |    "+data[0]+"    |    "+data[1]+data2[result]+data[2]+data2[result_1]+data[3],end="")
                            
                            print("    +--------+-----------+-----------------------------+-----------------------------+----------|")
                            cnt +=1                            
        except:
            print("Error : Something Went Wrong ")
                    
    def issueBook(self,bid,name):     
        try:            # Issue Book By Book ID 
            cnt = 0
            count8= 0        # Read First For Checking Book Is Availeble OR  Not
            with open("bookData.txt","r") as bk:
                    for line in bk:
                        data = line.split(",")
                        if(data[0] == str(bid)):
                            count8 +=1
                            if(data[3] == '0\n'):
                                print("\n\tBook is Not Available Book is Already Issued ")
                            else:
                                cnt+=1 
                            if(cnt != 0 ):

                                with open("issuebook.txt","a") as bk:
                                    id = bid
                                    issue_date = input("Enter Issue date in (DD-MM-YYYY) Format : ") 
                                    issuedate = issue_date
                                    issue_date = issue_date.split("-")
                                    issue_date = datetime(int(issue_date[2]),int(issue_date[1]),int(issue_date[0]))                    
                                    status = '0\n'
                                    bk.write(str(id)+",")
                                    bk.write(name+",")
                                    bk.write(str(issuedate)+",")
                                    bk.write(status)
                                    print("\n\t  ✔  Successfully Issue Book ID",bid)   

                    #  Change The Book Status "1" To "0" In " bookData.txt " File                                                                                                      
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
                    if(count8 == 0):
                        print("\n\t Book ID is Not Present in our library  ")

        except ValueError:
            print("\n   !! Invalid Date !! Please Enter Valid Date ")
    def showIssueBook(self):
        try:                    # Display Issue Book Details 
            count = 1
            s = " Issue Book Details "
            print(s.center(90,"-"))  
            print("     _____________________________________________________________________________________")
            print("    |  Sr.No. |  Book_ID  |    Student_Name             |  Date_of_Issue_Book  |  Status  |")
            print("    |_________|___________|_____________________________|______________________|__________|")
            with open("issuebook.txt","r") as bk:
                for line in bk:
                    data = line.split(",")
                    if(data[3] == '0\n'):
                        length = len(data[1]) 
                        result = 25 - length
                        with open("Spaces.txt","r") as bk:
                            for line in bk:
                                data2 = line.split(",")
 
                        print("    |   ",count,"   |   "+data[0]+"     |    "+data[1]+data2[result]+data[2]+"        |    "+data[3],end="")                                   
                        print("    +---------+-----------+-----------------------------+----------------------+----------|")
                        count += 1                                               
        except:
            print("ERROR: Issue Book Details Not Found ")
        
    def User_showIssueBook(self):
        try:  
             # Display Issue Book Details 
            not_found = 0
            with open("login_logout.txt","r") as bk:
                for line in bk:
                    data = line.split(",")
                    if(len(data[0]) == 4):
                        name = data[1]  
                        count = 1
                        s = " Issue Book Details "
                        print(s.center(90,"-"))  
                        print("     _____________________________________________________________________________________")
                        print("    |  Sr.No. |  Book_ID  |    Student_Name             |  Date_of_Issue_Book  |  Status  |")
                        print("    |_________|___________|_____________________________|______________________|__________|")
                        with open("issuebook.txt","r") as bk:
                            for line in bk:
                                data_U = line.split(",")
                                if(data_U[1] == name):
                                    not_found += 2
                                    length = len(data_U[1]) 
                                    result = 25 - length
                                    with open("Spaces.txt","r") as bk:
                                        for line in bk:
                                            data2 = line.split(",")
                                            print("    |   ",count,"   |   "+data_U[0]+"     |    "+data_U[1]+data2[result]+data_U[2]+"        |    "+data_U[3],end="")                                   
                                            print("    +---------+-----------+-----------------------------+----------------------+----------|")
                                            count += 1  
                if(not_found == 0):
                    print("\n\t\t\tIssue Book Details Not Found ")  

                                                                               
        except:
            print("ERROR: Issue Book Details Not Found ")
                                                    
    def returnBook(self,bid,uid,name):
        try: 
            count = 0         # Submitting Book By Book ID 
            allbook = []
            found = False
            with open("issuebook.txt","r") as bk:
                for line in bk:
                    data = line.split(",")
                    if(data[0] == str(bid)):
                        count +=2
                        issue_date = str(data[2])                              
                        issue_date = issue_date.split("-")
                        issue_date = datetime(int(issue_date[2]),int(issue_date[1]),int(issue_date[0]))
                        submit_date = input("Enter Submit date in (DD-MM-YYYY) Format :")
                        submit_date = submit_date.split("-")
                        submit_date = datetime(int(submit_date[2]),int(submit_date[1]),int(submit_date[0]))                      
                        days = (submit_date-issue_date).days
                        if(days < 0 ):
                            print("\n   ERROR : Please Enter Coorect Dates Check Submit Date ")                   
                        elif(days <= 8 ):
                            print("\n\t ✔  Successfully Submited Book ID","\n\n\t  Thanks for the Early Submission") 
             # Delete Issue Book Details of Submited Book From issuebook.txt " File   
                        if(days >=1):
                            allbook = []
                            found = False
                            with open("issuebook.txt","r") as bk:
                                for line in bk:
                                    data = line.split(",")
                                    if(data[0] == str(bid)):
                                        found = True
                                    else:
                                        allbook.append(line)

                                if(found):
                                    with open("issuebook.txt","w") as bk:
                                        for book in allbook:
                                            bk.write(book)
                                else:
                                    print("Record Not Found ")
 
          #  Change The Submited Book Status "0" To "1" In " bookData.txt " File                   
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
                    # If Total Days are grater than equal to 9 then Inserting Total Days And Fine In " pay_fine.txt " File
                            if(days >=9):
                                result = days - 8 
                                fine = result * 15                             
                                with open("pay_fine.txt","a") as bk:   
                                    unique_id = uid
                                    total_days = result                              
                                    tfine = fine
                                    bk.write(str(unique_id)+",")
                                    bk.write(name+",")
                                    bk.write(str(total_days)+",")
                                    bk.write(str(tfine))
                                    bk.write("\n")
                           
                        if(days >=9): 
                            print("\n\t ✔  Successfully Submited Book ID",bid,"\n\n\t  Please Pay Fine For Late Submission More Details Check 'Pay_fine' Option ")
                                                                          
                       
            if(count == 0):
                print("\nError : Book ID Not Found ")

        except ValueError:
            print("\n   !! Invalid Date !! Please Enter Valid Date ")

    def editById(self,bid):
        try:
            count1 = 0
            count_6 = 0
            with open("issuebook.txt","r") as bk:
                for line in bk:     # Edit The Book Details By Book ID  
                    data = line.split(",")
                    if(data[0] == str(bid)):  
                        count_6 += 5
                        print("\n   You Cannot Edit This Book Because Book is Issued ")  
                    if(count_6 == 0):                     
                        allbook = []
                        found = False
                        with open("bookData.txt","r") as bk:
                            for line in bk:
                                data = line.split(",")
                                if(data[0] == str(bid)):
                                    count1 += 2
                                    ans = input("Do you want to Change Book ID (y/n) :")
                                    if(ans.lower() == 'y'):
                                        data[0] = input("Enter New Book ID :")
                                        print("\n\t  ✔  Successfully Updated Book ID \n")
                                    ans = input("Do you want to Change Book Name (y/n) :")
                                    if(ans.lower() == 'y'):
                                        data[1] = input("Enter New Name :")
                                        print("\n\t  ✔  Successfully Updated Book Name \n")

                                    ans = input("Do you want to Change Author Name (y/n) :")
                                    if(ans.lower() == 'y'):
                                        data[2] = input("Enter New Name :")
                                        print("\n\t  ✔  Successfully Updated Author Name \n")
                                    line = ",".join(data)

                                    found = True
                                allbook.append(line)

                            if(found):
                                with open("bookData.txt","w") as bk:
                                    for book in allbook:
                                        bk.write(book)
                            else:
                                print("Record Not Found")
                        if(count1 == 0):
                            print("\n   Error : Book ID Not Found")
        except FileNotFoundError:
            print("File Does Not Exist")

    def deleteById(self,bid):
        try:                # Delete Particular Book Details
            count2 = 0
            count_2 = 0
            with open("issuebook.txt","r") as bk:
                for line in bk:     
                    data = line.split(",")
                    if(data[0] == str(bid)): 
                        count_2 += 5 
                        print("\n   You Cannot Delete This Book Because Book is Issued  ")  
                    if(count_2 == 0):           
                        allbook = []
                        found = False
                        with open("bookData.txt","r") as bk:
                            for line in bk:
                                data = line.split(",")
                                if(data[0] == str(bid)):
                                    count2 += 2
                                    found = True
                                else:
                                    allbook.append(line)

                            if(found):
                                with open("bookData.txt","w") as bk:
                                    for book in allbook:
                                        bk.write(book)

                                print("\n\t  ✔  Successfully Deleted Book ID",bid)
                            else:
                                print("Record Not Found")
                        if(count2 == 0):
                            print("\n   Error : Book ID Not Found")
        except FileNotFoundError:
            print("File Does Not Exist")

    def Payfine(self,uid):
        try:                # Pay Fine By User Unique ID 
            count3 = 0
            with open("pay_fine.txt","r") as bk:
                    for line in bk:
                        data = line.split(",")                    
                        if(data[0] == str(uid)): 
                            count3 += 2                      
                            print("\n\t Hello Mrs. / Mr.",data[1],"\n\t_____________________________________")                 
                            print("\n\t Late Submitted Days   : Days.",data[2])
                            print("\t Late Submission Fine  : "+"₹.",float(data[3])+000.0)
                            if(int(data[2]) >= 60 ):
                            
                                print("\t Submiting Book After\n\t 60 Day Penalty Amount : ₹. 1000.0 \n\t_____________________________________\n\t Your Total Fine      :  "+"₹.",float(data[3])+1000.00)
                                print("\t_____________________________________")
                                print("\n\tNOTE : You have broken the Rules. You have to pay the Penalty of Rs.1000 and fine \n")
                        if(data[0] == str(uid)):
                            pay = input("\nAre you Paying This Fine (y/n) :")
                            if(pay.lower() == 'y'):
                                allbook = []
                                found = False
                                with open("pay_fine.txt","r") as bk:
                                    for line in bk:
                                        data = line.split(",")
                                        if(data[0] == str(uid)):
                                            found = True
                                        else:
                                            allbook.append(line)

                                    if(found):
                                        with open("pay_fine.txt","w") as bk:
                                            for book in allbook:
                                                bk.write(book) 
                                        print("\n\t  ✔  Successfully Paid ")
                                  
                            else:
                                print("\n   Please Pay Earlier Otherwise We Will Not Allow You to Issue Another Book ")  
            if(count3 == 0):
                print("\n\t    !!! Your Fine Details Not Found  !!!")  
        except FileNotFoundError:
            print("Issue Details Not Found")
    def Register(self):
        try:                # Registration of New User 
            cnt = 1299
            with open("Userlogin.txt","r") as bk:
                for line in bk:
                    data = line.split(",") 
                    if(data[0] == str(cnt)):
                        cnt = int(cnt) + 11
            with open("Userlogin.txt","a") as bk: 
                name = input("Enter Your Name { First_Name & Last_Name } : ")
                dob = input("Enter Your Date of Birth { DD-MM-YYYY } : ")
                mobile_no = int(input("Enter Your Mobile Number : "))
                add = input("Enter Your Address { City - Pune,Mumbai } : ")
                bk.write(str(cnt)+",")
                bk.write(str(name)+",")
                bk.write(str(dob)+",")
                bk.write(str(mobile_no)+",")
                bk.write(str(add))
                bk.write("\n")                                                     
                print("\n               ✔                    ")
                print(" Registration Completed Successfully  \n")
                print('"',cnt,'"',"This Is Your Unique ID Please Remember This For Login Purpose "+"\n  ````")
                cnt += 1 
        except:
            print("Error : Please Enter Valid Data ")
    
    def Customerdetails(self):
        try:
            cnt = 1
            print(" ")
            s = "Customer_Details "
            print(s.center(90,"-"))   
            print("     ________________________________________________________________________________________________________________")
            print("    | Sr.No. |  Unique_ID  |    Student_Name             |  Date of Birth   |  Mobile No    |    Address             |")
            print("    |________|_____________|_____________________________|__________________|_______________|________________________|")
            with open("Userlogin.txt","r") as bk:
                for line in bk:
                    data = line.split(",") 
                    if(data[0] == str(1299)):   
                        pass
                    else:   
                        length = len(data[1]) 
                        result = 25 - length
                        with open("Spaces.txt","r") as bk:
                            for line in bk:
                                data2 = line.split(",")                      
                        print("    |  ",cnt,"   |    "+data[0]+"     |    "+data[1]+data2[result]+data[2]+"    |  "+data[3]+"   |    "+data[4],end="")
                        print("    +--------+-------------+-----------------------------+------------------+---------------+------------------------|")
                        cnt +=1  
                                   
        except:
            print("Error : Something Went Wrong ")
    def Show_fine_details(self):                   # Display All Availeble Book Details 
        try:
            cnt = 1
            print(" ")
            s = "  Fine_Datails  "
            print(s.center(90,"-"))   
            print("     ________________________________________________________________________________________________")
            print("    | Sr.No. |  Unique_ID  |    Student_Name             |  Late_Submited_Days  |  Total_Fine in ₹.  |")
            print("    |________|_____________|_____________________________|______________________|____________________|")
            with open("pay_fine.txt","r") as bk:
                    for line in bk:
                        data = line.split(",")
                        if(int(data[2]) >= 61 ):
                            data[3] = (int(data[3]) + 1000)
                        length = len(data[1]) 
                        length_1 = len(data[2])
                        result = 25 - length
                        result_1 = 18 - (length_1+5)
                        with open("Spaces.txt","r") as bk:
                            for line in bk:
                                data2 = line.split(",")                                   
                        print("    |  ",cnt,"   |    "+data[0]+"     |    "+data[1]+data2[result]+data[2]+" Days"+data2[result_1]+"₹.",float(data[3]),end="\n")
                        print("    +--------+-------------+-----------------------------+----------------------+--------------------|")
                        cnt +=1                 
        except:
            print("Error : Something Went Wrong ")

    def Issue_Return_Rule(self):
        try:
            print(" ")
            print(" ________________________________________________________________________________________")
            print("|                               # Issue / Return Rules #                                 |")
            print("+--------+---------------------+-------------------------+----------------+--------------+")
            print("| Sr.No. | Member's Category   |  Limit Of Issue Book    | Issuing Period | Fine Per Day |")
            print('+--------+---------------------+-------------------------+----------------+--------------+')
            print("| 1      | Students            |  10 Books In Months     |     8 Days     |     15.Rs    |")
            print('+--------+---------------------+-------------------------+----------------+--------------+')                                  
            print("|                                                                                        |")
            print('|   1. A Fine Of 15.Rupees per day per Book will be Charged for Late submting of Book.   |')
            print("|                                                                                        |")   
            print('|   2. After sixty days the book will be accepted but you will have to pay the           |') 
            print("|      Fine till that date and the penalty of Rs.1000.                                   |")                             
            print("|________________________________________________________________________________________|")
            print("\n   #   Please Read the above terms and conditions carefully Before Issuing the Book    #\n ")
        except:
            print("Error : Something Went Wrong ")

    def login_logout(self,id):
        try:                    # Store Currently Login User Details 
            with open("Userlogin.txt","r") as bk:
                for line in bk:
                    data = line.split(",") 
                    if(data[0] == str(id)):
                        with open("login_logout.txt","w") as bk:            
                            bk.write(str(data[0])+",")
                            bk.write(str(data[1])+",")
                            bk.write(str(data[2])+",")
                            bk.write(str(data[3])+",")
                            bk.write(str(data[4]))
                            bk.write("\n") 
    
        except:
            print("Error : Something Went Wrong ")

    def card(self):
        try:
            with open("login_logout.txt","r") as bk:
                for line in bk:
                    data = line.split(",") 
                    if(len(data[0]) == 4):
                        print("\n") 
                        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("\t                 # LIBRARY CARD #                 ")
                        print("\t   +----------+                                   ")
                        print("\t   |          |  Unique ID : "+data[0]             )
                        print("\t   |          |  Name      : "+data[1]            )
                        print("\t   |  PHOTO   |  DoB       : "+data[2]             )
                        print("\t   |          |  Mobile No : "+data[3]                 )
                        print("\t   +----------+  Address   : "+data[4]              )
                        print("\t                                                  ")
                        print("\t  Sign of Librarian            Sign of Student    ")
                        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except:
            print("Error : Something Went Wrong ")


