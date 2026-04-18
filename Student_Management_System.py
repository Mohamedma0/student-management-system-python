from abc import ABCMeta,abstractmethod

class Person(metaclass = ABCMeta):
    def __init__(self,name,age):
        self.name =name
        self.age =age
    @abstractmethod    
    def describe(self):
        pass

class Student(Person) :
    def __init__(self,name,age,grades):
        super().__init__(name,age)
        self.__grades=grades
    def describe(self):
        print('I am a student')
    def add_grade(self,new_grade):
        if not (0 <= new_grade <= 100):
            return print ('invaild grade')
        self.__grades.append(new_grade)
    @property
    def grades(self):
        return self.__grades     
    def average (self):
        total=0
        for num in self.grades:
            total+=num
        return total/len(self.__grades)       



class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display_salary(self):
        return self.salary
    def describe(self):
        print('I am a teacher')    


students = []


while True :
    print(' choose 1 to add student')
    print(' choose 2 to show student')
    print(' choose 3 to add grade')
    print(' choose 4 to show top students')

    print(' choose q to quit')
    choice = input ("Enter a choice :")

    if choice =='1':
        name =input('enter name :')
        age = int(input('enter age :'))
        s = Student(name,age,[])
        students.append(s)
        print ("student added")
    elif choice =='2':
        for i,s in enumerate(students):
            print (f' the name is {s.name} and the age is {s.age} and the grades is {s.grades}')


    elif choice =='3'  :
        for i,s in enumerate(students):
            print (i, s.name)

        index = int(input('choose a student index')) 
        grade = int (input('Enter grade :'))    
        students[index].add_grade(grade)

    elif choice == '4':
        if not students:
            print('No students')
             
        else:
            top = students[0]
            for s in students:
                if (s.average() > top.average()):
                    top = s
            print ('top student:')        
            print (f'name:{top.name}')
            print (f'Average{top.average()}')

    elif choice =='q':
        break
