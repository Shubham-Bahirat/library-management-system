try:
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
                            length = len(data_U[1]) 
                            result = 25 - length
                            with open("Spaces.txt","r") as bk:
                                for line in bk:
                                    data2 = line.split(",")
                                    print("    |   ",count,"   |   "+data_U[0]+"     |    "+data_U[1]+data2[result]+data_U[2]+"        |    "+data_U[3],end="")                                   
                                    print("    +---------+-----------+-----------------------------+----------------------+----------|")
                                    count += 1   
                                 
                                       
                        #print(data)  
                        
except IndexError:
    print("INDEX")