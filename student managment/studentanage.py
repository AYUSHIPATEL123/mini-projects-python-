class Student():
    lst=[]
    def __init__(self,rollno, name, age, grade):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.grade = grade

    def accept(self,rollno,name,age,grade):
        ob=Student(rollno=rollno,name=name,age=age,grade=grade)
        self.lst.append(ob)
   
    def display(self,rn):
        print("Name : ",self.lst[rn].name)
        print("rollno : ",self.lst[rn].rollno)
        print("age : ",self.lst[rn].age)
        print("grade : ",self.lst[rn].grade)
        print()

    def search(self,rn):
        for i in range(self.lst.__len__()):
            if self.lst[i].rollno == rn:
                return i

    def delete(self,rn):
        ob=self.lst[self.search(rn)]
        self.lst.remove(ob)      

    def update(self,rn,no):
        i=self.search(rn) 
        self.lst[i].rollno = no

    def diplaylist(self):
        for i in range(self.lst.__len__()):
            self.display(self.search(self.lst[i].rollno))            

       
            