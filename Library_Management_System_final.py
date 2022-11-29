from datetime import datetime
from datetime import timedelta




class library :
    master_dict = {1:{'identification_no':1 ,'rack_number':1 ,'title':'Harry Porter - 1' ,'author':'Charles' ,'subject_category':'Fiction' ,'publication_date':'12-10-2010' },
                   2:{'identification_no':2 ,'rack_number':1 ,'title':'Harry Porter - 2' ,'author':'Darwin' ,'subject_category':'Non-Fiction' ,'publication_date':'15-12-2012'},
                   3:{'identification_no':3 ,'rack_number':1 ,'title':'Harry Porter - 2' ,'author':'Darwin' ,'subject_category':'Non-Fiction' ,'publication_date':'15-12-2012'},
                   4:{'identification_no':4 ,'rack_number':2 ,'title':'Harry Porter - 3' ,'author':'Sharukh Khan' ,'subject_category':'Comedy' ,'publication_date':'18-06-2014'},
                   5:{'identification_no':5 ,'rack_number':2 ,'title':'Harry Porter - 1' ,'author':'Charles' ,'subject_category':'Fiction' ,'publication_date':'12-10-2010' }}
    master_dict_1 = {1:{'identification_no':1 ,'rack_number':1 ,'title':'Harry Porter - 1' ,'author':'Charles' ,'subject_category':'Fiction' ,'publication_date':'12-10-2010' },
                   2:{'identification_no':2 ,'rack_number':1 ,'title':'Harry Porter - 2' ,'author':'Darwin' ,'subject_category':'Non-Fiction' ,'publication_date':'15-12-2012'},
                   3:{'identification_no':3 ,'rack_number':1 ,'title':'Harry Porter - 2' ,'author':'Darwin' ,'subject_category':'Non-Fiction' ,'publication_date':'15-12-2012'},
                   4:{'identification_no':4 ,'rack_number':2 ,'title':'Harry Porter - 3' ,'author':'Sharukh Khan' ,'subject_category':'Comedy' ,'publication_date':'18-06-2014'},
                   5:{'identification_no':5 ,'rack_number':2 ,'title':'Harry Porter - 1' ,'author':'Charles' ,'subject_category':'Fiction' ,'publication_date':'12-10-2010' }}
 
    @classmethod
    def add_book(self):
        identification_no  = 6
        while(True):
            
            rack_number = int(input('Please input the rack number in which you want to place the book: \n'))
            title = input('Please enter the title of the book : \n')
            author = input('Please enter the author of the book : \n')
            subject_category = input('Please enter the subject category of the book : \n')
            publication_date = input('Please enter the publication date of the book : \n')
            nested_dict = {'identification_no':identification_no,'rack_number':rack_number,'title':title,'author':author,'subject_category':subject_category,'publication_date':publication_date}
            library.master_dict[identification_no]=nested_dict
            library.master_dict_1[identification_no]=nested_dict
            identification_no+=1
            n=input('Do you want to add another book or not (yes/no) : \n')
            if n=='yes' :
                continue
            else :
                break
            
    @classmethod
    def search_by(self,option,string):
        n=0
        for i in library.master_dict :
            if library.master_dict[i][option]==string:
                print ('Found!! --> ', library.master_dict[i],'\n')
                n+=1
        if n==0:
            print ('Not Found!! \n')
            
    @classmethod
    def check_copies(self,name,author):
        n=0
        for i in library.master_dict:
            if library.master_dict[i]['title']==name and library.master_dict[i]['author']==author:
                n+=1
        return ('The total number of copies of this book = ', n, '\n')
    issued_book_data = {}
    all_issues = {}
    p=1
    @classmethod
    def check_out(self,name,author,issuer):
        y=0
        for i in library.issued_book_data :
            if library.issued_book_data[i]["Issuer's Name"]==issuer:
                y+=1
        if y<5 :

            copies_dict = {}
            for i in library.master_dict_1.copy():
                if library.master_dict_1[i]['title']==name and library.master_dict_1[i]['author']==author:
                    copies_dict[i] = library.master_dict_1.pop(i)
            if copies_dict == {}:
                print("Currently all the copies of this book has been issued, but you can reserve the copy in advance. \n")
                z = input("If you want to reserve a copy of this book then type YES : \n")
                if z=='YES' :
                    library.reserve_copy(name,author)
        
            if copies_dict != {}:
                    print ('These are the available copies of this book --> ', copies_dict, '\n')
            n = int(input('Please enter the ID Number of the book that you want to reserve : \n'))
        
            now = datetime.now()
            dt = now.strftime("%d-%m-%Y %H:%M:%S")
            dt1= now.strftime("%Y-%m-%d %H:%M:%S")
            self.dt2 = now.strftime("%d-%m-%Y %H:%M:%S")
            date,time = dt.split()
            date1,time1 = dt1.split()
            Begindatestring = date1
            Begindate = datetime.strptime(Begindatestring, "%Y-%m-%d")
            enddate = str(Begindate + timedelta(days=10))
            return_date,mis = enddate.split()
            library.issued_book_data[n] = {"title":library.master_dict[n]['title'],"author":library.master_dict[n]['author'], "Serial Number":library.p, "Issuer's Name":issuer,'Issuing Date':date,'Time':time ,'Returning Date':return_date}
            library.all_issues[n] = {"title":library.master_dict[n]['title'],"author":library.master_dict[n]['author'], "Serial Number":library.p, "Issuer's Name":issuer,'Issuing Date':date,'Time':time ,'Returning Date':return_date}
            print ('Congratulations, Your book has been issued. Please keeep in mind that you have to reissue this book after 10 days otherwise 10rs fine will be imposed per day afterwards till you reissue it again. The details of the issue are as follows -->', library.issued_book_data[n], '\n') 
            library.p+=1
        else :
            print("You have exceeded the limit for issuing books. Kindly return a book to issue a new book. \n")

    reserve_dict = {}

    @classmethod
    def reserve_copy(self,name,author):
        copies_dict = {}
        for i in library.master_dict_1:
            if library.master_dict_1[i]['title']==name and library.master_dict_1[i]['author']==author:
                copies_dict[i] = library.master_dict_1[i]
            
        if copies_dict == {}:

            lst1 = []
            lst2 = []
            for i in library.issued_book_data:
                if library.issued_book_data[i]['title']==name and library.issued_book_data[i]['author']==author :
                    t=library.issued_book_data[i]['Time']
                    lst2.append(t)
            
                    d2=library.issued_book_data[i]['Issuing Date']
                    lst1.append(d2[::-1])
            latest_arrival = min(lst1)[::-1]
            latest_time = min(lst2)
            for i in library.issued_book_data :
                if library.issued_book_data[i]['Issuing Date']==latest_arrival and library.issued_book_data[i]['Time']==latest_time  :
                    issuer = input('Please enter your name : \n')
                    library.reserve_dict[i] = {"Book ID Number":i,"title":name, "author":author, "Issuer's Name":issuer}
                    print("Congratulations, You have successfully reserved the latest expiring issue of that book. Your 10 days issuing period will start once the previous issuer returns the book. You will be notified once the book is returned by the previous owner \n")

    @classmethod
    def return_book(self,name,author,issuer):
        g=0
        for i in library.issued_book_data.copy() :
            if library.issued_book_data[i]['title']==name and library.issued_book_data[i]['author']==author and library.issued_book_data[i]["Issuer's Name"]==issuer:
                library.master_dict_1[i] = library.issued_book_data.pop(i)
                now = datetime.now()
                dt = now.strftime("%d-%m-%Y %H:%M:%S")
                date,time = dt.split()
                library.all_issues[i]['Time of returning'] = time
                library.all_issues[i]['Date of returning'] = date
                print("You have successfully returned the selected book \n")
                g+=1
            if g==0:
                print("Sorry You have not issued this book !! \n")
    @staticmethod
    def notify_return() :
        while True :
            now = datetime.now()
            nowf=now.strftime("%d-%m-%Y %H:%M:%S")
            
            
            for i in library.issued_book_data :
                if nowf == library.dt2 and (i in library.reserve_dict.keys()):
                    print("The book having Title : ", library.master_dict[i]['title'],"and Author : ", library.master_dict[i]['author'], "is now available for issuing. Kindly issue the copy reserved by you. \n")
    fine_accounts = {}
    @staticmethod
    def impose_fine() :
        for i in library.all_issues :
            d1= library.all_issues[i]['Issuing Date']
            d2 = library.all_issues[i]['Date of returning']
            d1 = datetime.strptime(d1, "%d-%m-%Y")
            d2 = datetime.strptime(d2, "%d-%m-%Y")
            name = library.all_issues[i]["Issuer's Name"]
            delta = d2 - d1
            diff = delta.days
            if diff > 10 :
                library.fine_accounts[name] = (diff-10)*10
                
print("-------------------------------Welcome to our BITS Library Management System-------------------------------\n")
while(True):
   
    print("1) Add a book \n")
    print("2) Search a book in the database \n")
    print("3) Check Out a book \n") # further we also have the option of reserving a book
    
    print("4) Return a Book \n")
    print("5) Quit \n")
    print("-----------------------------------------------------------------------------------------------------")
    #library.notify_return() after completing everything it came to my mind that such an infinite loop will not let the commands written below to execute thats why i couldnt correct it at the end moment
    #library.impose_fine() some error was coming in this thats why i wasnt able to include this but pls consider looking the source code once i have worked very hard to get all the logics
    n = int(input("Please enter your choice from the above mentioned options : \n"))
    if n == 1 :
        library.add_book()
        print ("Your book was successfully added \n")
    elif n==2 :
        option = input("Please input the mode of searching : \n")
        string = input("Please input the literal by which book has to be searched : \n")
        library.search_by(option,string)
    elif n == 3 :
        name = input("Please input the title of the book : \n")
        author = input("Please input the author of the book : \n")
        issuer = input("Please enter your name : \n")
        library.check_out(name,author,issuer)
    elif n==4 :
        name = input("Please input the title of the book : \n")
        author = input("Please input the author of the book : \n")
        issuer = input("Please enter your name : \n")
        library.return_book(name,author,issuer)
    elif n==5 :
        break
    
        

    
    
        
    
    
        
    
        
        
        
                            
                      
            
        
        
        
        
        








                      
    
