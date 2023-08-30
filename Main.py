from Book_Info import Book
from BookMgt import BookSystem
if(__name__ == "__main__"):
    choice = 0
    cnt = 0
    mgt = BookSystem()
    while(cnt != 3):
        print('''
        \t\t+~~~~~~~~~~~~~~~~~~~~~~+
        \t\t| 1.Admin (Librarian)  |
        \t\t| 2.Student (Customer) |
        \t\t| 3.Exit               | 
        \t\t+~~~~~~~~~~~~~~~~~~~~~~+ 
 ''')
        try:
            cnt = int(input("Enter Your Choice :"))
            if(cnt >= 4):
                print('\n\t"',cnt,'is Invalid Choice Please Enter Valid Choice "')
        except:
            print("\nError : Please Enter Valid Data ")
        countA = 0
        if(cnt == 1):
            id = int(input("Enter Your Unique ID :"))
            
            with open("Userlogin.txt","r") as bk:  
                for line in bk:
                    data = line.split(",")    
                    if(data[0]  == str(id)):
                        countA = 2
                        print("\n\t ✔  Successfully Login  ")
                        print("\n   Welcome Mrs./ Mr.",data[1]+"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    if(countA == 0):
                        print("\n\t\t !!! The UNIQUE ID is Incorrect !!!")
                        break
        if(countA > 1 ):
            while(choice!=8):
                print('''
                \t+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
                \t| 1. Add New Book                   |
                \t| 2. Show All Book Details          |
                \t| 3. Show All Issue Book Details    | 
                \t| 4. Edit Book Details By Book ID   | 
                \t| 5. Delete Book Details By Book ID |
                \t| 6. Customer Details               |
                \t| 7. Fine Details                   |
                \t| 8. Log Out                        |
                \t+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
                ''')           
                try:
                    choice = int(input("Enter Your Choice :"))
                    if(choice >= 9):
                        print("\n\t!",choice,"is Invalid Choice Please Enter Valid Choice !")
                except:
                    print("\nError : Please Enter Valid Data ")
                cnt = 0
                if(choice == 1):
                    try:
                        bid = int(input("Enter Book ID to Add Books :"))   
                    except:
                        print("\nError : Please Enter Valid Data ")       
                             
                    with open("bookData.txt","r") as bk:
                        for line in bk:
                            data = line.split(",")
                            if(data[0] == str(bid)):
                                cnt += 1
                    if(cnt != 1):
                        bname = input("Enter Book Name :")
                        author = input("Enter Author Name :")
                        status = int(input("Ente Book Status :"))
                        b1 = Book(bid,bname,author,status)
                        mgt.AddBook(b1)  
                        print("\n\t ✔  Successfully Added Book  ")                 
                    else:
                        print("\n\t Book ID is Already Exist Please Enter 'Unique' Book ID ")
                            
                elif(choice == 2):
                    mgt.ShowAllBook()
            
        
                elif(choice == 3):
                    mgt.showIssueBook()

               
                elif(choice == 4):
                    try:
                        bid = int(input("Enter Book ID to Edit Book Details :"))
                        mgt.editById(bid)
                    except:
                        print("\nError : Please Enter Valid Data ")
                    
                elif(choice == 5):
                    try:
                        bid = int(input("Enter Book ID to Delete Book Details :"))
                        mgt. deleteById(bid)
                    except:
                        print("\nError : Please Enter Valid Data ")

                elif(choice==6):
                    mgt.Customerdetails()
                    
                elif(choice==7):
                    mgt.Show_fine_details()
                elif(choice==8):
                    s = "_______________________ Home Page "
                    print(s.ljust(90,"_"))
                    
        elif(cnt == 2):
            s = "_______________________ Login Page "
            print(s.ljust(90,"_"))
            cntt=0
            while(cntt != 3):
                print(''' 
                \t+~~~~~~~~~~~~~~~~~~~~~~~~~+
                \t| 1.Login                 |
                \t| 2.Registration          |
                \t| 3.Home Page             | 
                \t+~~~~~~~~~~~~~~~~~~~~~~~~~+''')
                try:
                    cntt = int(input("Enter Your Choice :"))
                    if(cntt >= 4):
                        print("\n\t!",cntt,"is Invalid Choice Please Enter Valid Choice !")
                    if(cntt == 1):
                        counnt_ = 0
                        id = int(input("Enter Your Unique ID :"))
                        with open("Userlogin.txt","r") as bk:  
                            for line in bk:
                                data = line.split(",")    
                                if(data[0]  == str(id)):
                                    print("\n\t ✔  Successfully Login  ")
                                    print("\n   Welcome Mrs./ Mr.",data[1],"In Our Library\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    mgt.login_logout(id)
                                    counnt_ +=1
                                    while(choice!=7):
                                        print('''
                        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
                        | 1. Show All Book Details           |
                        | 2. Issue Book By Book ID           |
                        | 3. My Issue Book Details           |
                        | 4. Submit Book By Book ID          |
                        | 5. Pay_Fine By Unique ID           |
                        | 6. My Library Card                 |
                        | 7. Log Out                         |
                        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+                                      
                                            ''')
                                        try:
                                            choice = int(input("Enter Your Choice :"))
                                            if(choice >= 8):
                                                print("\n\t!",choice,"is Invalid Choice Please Enter Valid Choice !")
                                        except:
                                            print("\nError : Please Enter Valid Data ")
                                        cnt = 0
                                                        
                                        if(choice == 1):
                                            mgt.ShowAllBook()
                                        
                                        elif(choice == 2):
                                            mgt.Issue_Return_Rule()
                                            uid = int(input("Enter Your Four Digit Unique ID :")) 
                                            count_5 = 0
                                            with open("login_logout.txt","r") as bk:
                                                for line in bk:
                                                    data = line.split(",")
                                                    if(data[0] == str(uid)):
                                                        name = data[1]
                                                        count_5 += 2  
                                                        count5 = 0
                                                        with open("pay_fine.txt","r") as bk:
                                                            for line in bk:
                                                                data = line.split(",")                    
                                                                if(data[0] == str(uid)): 
                                                                    count5 += 2 
                                                                    print("\n\tYour 'Fine' is Pending Please Pay Fine First ")
                                                                    break
                                                    
                                                            if(count5 == 0):
                                                                bid = int(input("Enter Book ID to Issue Book :")) 
                                                                mgt.issueBook(bid,name)
                                                if(count_5 == 0):
                                                   print('\n!! Invalid Unique ID !! If you forgot your Unique ID Check Here 👉 " 6. My Library Card " ') 

                                        elif(choice == 3):
                                            mgt.User_showIssueBook()

                                        elif(choice == 4):
                                            try:
                                                found = 0
                                                uid = int(input("Enter Your Four Digit Unique ID :"))
                                                with open("login_logout.txt","r") as bk:
                                                    for line in bk:
                                                        data = line.split(",")
                                                        if(data[0] == str(uid)): 
                                                            name = data[1]
                                                            found += 5
                                                            bid = int(input("Enter Book ID to Return Book :"))
                                                            mgt.returnBook(bid,uid,name)
                                                        if(found == 0):
                                                            print('\n!! Invalid Unique ID !! If you forgot your Unique ID Check Here 👉 " 6. My Library Card " ')
                                                            break  
                                            except:
                                                print("\nError : Please Enter Valid Data ")
                                        elif(choice == 5):
                                            try:
                                                valid = 0
                                                uid = int(input("Enter Your Unique ID to Pay Fine :"))
                                                with open("login_logout.txt","r") as bk:
                                                    for line in bk:
                                                        data = line.split(",")
                                                        if(data[0] == str(uid)):
                                                            valid += 5
                                                            mgt.Payfine(uid)
                                                        if(valid == 0 ):
                                                            print('\n!! Invalid Unique ID !! If you forgot your Unique ID Check Here 👉 " 6. My Library Card " ')  
                                                            break
                                            except:
                                                print("\nError : Please Enter Valid Data ")
                                        elif(choice == 6):                                          
                                           mgt.card()
                                        elif(choice == 7):                                          
                                            s = "_______________________ Login Page "
                                            print(s.ljust(90,"_"))
                    
                                                                    
                            if(counnt_ == 0):
                                print('\n!! Invalid Unique ID !! If you not registered with us please Check Here 👉 " 2.Registration " ')   

                    elif(cntt == 2):
                        mgt.Register()
                        cnt += 1 
                    elif(cntt == 3):                  
                        s = "_______________________ Home Page "
                        print(s.ljust(90,"_"))
                    
                except:
                    print("\nError : Please Enter Valid Data ")
        elif(cnt == 3):
            print(" ")
            print(" Thank You Visit Again ".center(90,"_"),"\n")