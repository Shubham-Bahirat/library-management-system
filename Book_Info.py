class Book:
    def __init__(self,bid,bname='learn python',author='Programmer',status=1):
        self.bid = bid
        self.bname = bname  # This is a Constructor 
        self.author = author
        self.status = status
    
    def __str__(self):
        data = str(self.bid)+","+self.bname+","+self.author+","+str(self.status)
        return data
    
if(__name__ == "__main__"):
    for m in range(5):
        b1 = Book(221,'learn C++','Scott Meyers',1)
        print(b1)
