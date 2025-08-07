from studentanage import Student
lst=[]
obj=Student(0,'',0,0)
# obj.accept(1,'a',1,1)
# obj.accept(2,'b',2,2)
# obj.accept(3,"c",3,6)
# # obj.display(1)

# obj.delete(2)
# # rn=obj.search(1)
# # obj.display(rn)
# obj.update(1,4)
# obj.diplaylist()

print("__________Start The Program___________\n")
while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("select operation : ")
    opt=input("\n1. Enter New Student\n2. Display All Students\n3. Search A Student\n4. Update A Student\n5. Delete A Student and Q to quit \n selcet the option number : ")
    if opt == '1':
        name=input("name : ")
        rollno=int(input("roll no :"))
        age=int(input("age : "))
        grade=int(input("grade : "))
        obj.accept(rollno,name,age,grade)
    elif opt == '2':
        obj.diplaylist()
    elif opt == '3':
        rollno=int(input("roll no to search :"))
        i=obj.search(rollno)
        obj.display(i)
    elif opt == '4':
        rollno=int(input("roll no to update :"))
        no=int(input("new roll no : "))
        obj.update(rollno,no)
    elif opt == '5':
        rollno=int(input("roll no to delete :"))    
        obj.delete(rollno)
    elif opt == 'Q':
        quit()