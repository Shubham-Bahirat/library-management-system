from datetime import datetime,timedelta
def card():
        try:
            with open("login_logout.txt","r") as bk:
                for line in bk:
                    data = line.split(",") 
                    if(len(data[0]) == 4): 
                        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("\t                 # LIBRARY CARD #                 ")
                        print("\t   +----------+                                   ")
                        print("\t   |          |  UNIQUE ID : "+data[0]             )
                        print("\t   |          |                                   ")
                        print("\t   |  PHOTO   |  NAME      : "+data[1]             )
                        print("\t   |          |                                   ")
                        print("\t   +----------+  ADDRESS   : "+data[2]              )
                        print("\t                                                  ")
                        print("\t  Sign of Librarian            Sign of Student    ")
                        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except:
            print("Error : Something Went Wrong ")
print(card())
date = datetime.now()
if(date == 12):
    print(date)
    
    
    