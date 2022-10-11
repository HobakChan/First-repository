
# class Student:
#     def __init__(self, deptNo, name, dept):
#         self.deptNo = deptNo
#         self.name = name
#         self.dept = dept

#     def print_info(self):
#         print("\tdeptNo: ", self.deptNo)
#         print("\tname: ", self.name)
#         print("\tdept: ", self.dept)

# def set_student():
#     deptNo = input("학번: ")
#     name = input("이름: ")
#     dept = input("학과: ")
#     student = Student(deptNo, name, dept)
#     return student

# def print_student(student_list):
#     for student in student_list:
#         student.print_info()

# def delete_student(student_list, name):
#     for i, student in enumerate(student_list):
#         if student.name == name:
#             del student_list[i]

# def find_student(student_list, name):
#     for i, student in enumerate(student_list):
#         if student.name == name:
#             student_list[i].print_info()

# def print_menu():
#     print("1. 학생 입력")
#     print("2. 학생 출력")
#     print("3. 학생 삭제")
#     print("4. 학생 검색")
#     print("5. 종료")
#     menu = input("메뉴선택: ")
#     return int(menu)
# def run():
#     student_list = []
#     student_list.append(Student("20220503","홍길동","matrials"))
#     student_list.append(Student("20220504","박찬호","matrials"))
#     student_list.append(Student("20220505","임꺽정","computer"))    
#     while 1:
#         menu = print_menu()
#         if menu == 1:
#             student = set_student()
#             student_list.append(student)
#         elif menu == 2:
#             print_student(student_list)
#         elif menu == 3:
#             name = input("Name to delete: ")
#             delete_student(student_list, name)
#         elif menu == 4:
#             name = input("Name to find: ")
#             find_student(student_list, name)
#         elif menu == 5:
#             break
# if __name__ == "__main__":
#     run()



# class Dept:
#     def __init__(self, deptNo, name):
#         self.deptNo = deptNo
#         self.name = name
#     def __str__(self):
#         result = "("+str(self.deptNo) + " " + self.name+ ")"
#         return result
       
# class Student:
#     def __init__(self, studentNo, name, dept):
#         self.studentNo = studentNo
#         self.name = name
#         self.dept = dept
#     def __str__(self):
#         result = "("+str(self.studentNo) + " "
#         result += self.name + " " + self.dept.name + ")"
#         return result
    
# studentList = []
# deptList = []

# def prepareData():
#     global deptList, studentList
#     matrials = Dept(100,"신소재")
#     mechanics = Dept(200,"기계공학과")
#     deptList= [matrials, mechanics]
#     studentList = []
#     studentList.append(Student(101,"신철수",matrials))
#     studentList.append(Student(102,"신정철",matrials))
#     studentList.append(Student(201,"기대승",mechanics))
#     studentList.append(Student(202,"기정은",mechanics))
    
# def main():
#     prepareData()
#     print("="*10,"All Departments List")
#     for dept in deptList:
#         print(dept)
#     print("="*10,"All Students List")
#     for student in studentList:
#         print(student)
# main()

# def set_student():
#     deptNo = input("학번: ")
#     name = input("이름: ")
#     dept = input("학과: ")
#     student = Student(deptNo, name, dept)
#     return student

# class Contact:
#     def __init__(self, name, phone_number, e_mail, addr):
#         self.name = name
#         self.phone_number = phone_number
#         self.e_mail = e_mail
#         self.addr = addr

#     def print_info(self):
#         print("Name: ", self.name)
#         print("\tPhone Number: ", self.phone_number)
#         print("\tE-mail: ", self.e_mail)
#         print("\tAddress: ", self.addr)

# def set_contact():
#     name = input("Name: ")
#     phone_number = input("Phone Number: ")
#     e_mail = input("E-mail: ")
#     addr = input("Address: ")
#     contact = Contact(name, phone_number, e_mail, addr)
#     return contact

# def print_contact(contact_list):
#     for contact in contact_list:
#         contact.print_info()

# def delete_contact(contact_list, name):
#     for i, contact in enumerate(contact_list):
#         if contact.name == name:
#             del contact_list[i]

# def find_contact(contact_list, name):
#     for i, contact in enumerate(contact_list):
#         if contact.name == name:
#             contact_list[i].print_info()

# def print_menu():
#     print("1. 연락처 입력")
#     print("2. 연락처 출력")
#     print("3. 연락처 삭제")
#     print("4. 연락처 검색")
#     print("5. 종료")
#     menu = input("메뉴선택: ")
#     return int(menu)

# def run():
#     contact_list = []
#     contact_list.append(Contact("jjh","010-111-1112","jjh@jjh.com","강화군"))
#     contact_list.append(Contact("ktr","010-222-2222","ktr@ktr.com","의성군"))
#     contact_list.append(Contact("lya","010-222-2222","lya@ktr.com","안성군"))    
#     while 1:
#         menu = print_menu()
#         if menu == 1:
#             contact = set_contact()
#             contact_list.append(contact)
#         elif menu == 2:
#             print_contact(contact_list)
#         elif menu == 3:
#             name = input("Name to delete: ")
#             delete_contact(contact_list, name)
#         elif menu == 4:
#             name = input("Name to find: ")
#             find_contact(contact_list, name)
#         elif menu == 5:
#             break
# if __name__ == "__main__":
#     run()

# class Bird:
#     def __init__(self):
#         self.flying = True  
#     def birdsong(self):
#         print("새소리")    

# class Sparrow(Bird):
#     def birdsong(self):
#         print("짹짹")    

# class Chicken(Bird):
#     def __init__(self):
#         self.flying = False
#     def birdsong(self):
#         print("꼬끼오")   
 
# my_sparrow = Sparrow()
# my_chicken = Chicken()  
# my_sparrow.birdsong()
# my_chicken.birdsong() 

# class Shape:
#     def __init__(self):
#         self.x=int(input('x=? '))
#         self.y=int(input('y=? '))
#     def disp(self):
#         pass

# class Circle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.r=int(input('r=? '))
#     def disp(self):
#         print('원',self.x,self.y,self.r)

# class Rect(Shape):
#     def __init__(self):
#         super().__init__()
#         self.w=int(input('w=? '))
#         self.h=int(input('h=? '))
#     def disp(self):
#         print('사각형',self.x,self.y,self.w,self.h)

# def main():
#     li=list()
#     menu='1.사각형, 2.원 3.조회 4.종료'
#     while True:
#         s=input(menu)
#         if s=='1':
#             li.append(Rect())
#         elif s=='2':
#             li.append(Circle())
#         elif s=='3':
#             for i in li:
#                 i.disp()
#         elif s=='4':
#             break
#         else:
#             print('잘못입력하셨습니다.')
# main()

# class Student:
#     def __init__(self, deptNo, name, dept):
#         self.deptNo = deptNo
#         self.name = name
#         self.dept = dept

#     def print_info(self):
#         print("\tdeptNo: ", self.deptNo)
#         print("\tname: ", self.name)
#         print("\tdept: ", self.dept)

# def set_student():
#     deptNo = input("학번: ")
#     name = input("이름: ")
#     dept = input("학과: ")
#     student = Student(deptNo, name, dept)
#     return student

# def print_student(student_list):
#     for student in student_list:
#         student.print_info()

# def delete_student(student_list, name):
#     for i, student in enumerate(student_list):
#         if student.name == name:
#             del student_list[i]

# def find_student(student_list, name):
#     for i, student in enumerate(student_list):
#         if student.name == name:
#             student_list[i].print_info()

# def print_menu():
#     print("1. 학생 입력")
#     print("2. 학생 출력")
#     print("3. 학생 삭제")
#     print("4. 학생 검색")
#     print("5. 종료")
#     menu = input("메뉴선택: ")
#     return int(menu)
# def run():
#     student_list = []
#     student_list.append(Student("20220503","홍길동","matrials"))
#     student_list.append(Student("20220504","박찬호","matrials"))
#     student_list.append(Student("20220505","임꺽정","computer"))    
#     while 1:
#         menu = print_menu()
#         if menu == 1:
#             student = set_student()
#             student_list.append(student)
#         elif menu == 2:
#             print_student(student_list)
#         elif menu == 3:
#             name = input("Name to delete: ")
#             delete_student(student_list, name)
#         elif menu == 4:
#             name = input("Name to find: ")
#             find_student(student_list, name)
#         elif menu == 5:
#             break
# if __name__ == "__main__":
#     run()


# class Student:
#     def __init__(self, deptNo, name, dept):
#         self.deptNo = deptNo
#         self.name = name
#         self.dept = dept
#     def __str__(self):
#         result = "("+str(self.deptNo) + " "
#         result += self.name + " " + self.dept + ")"
#         return result

# def set_student():
#     deptNo = input("학번: ")
#     name = input("이름: ")
#     dept = input("학과: ")
#     student = Student(deptNo, name, dept)
#     return student

# a = set_student().split()
# print(a)

# matList = []
# comList = []
# class Dept:
#     def __init__(self, deptNo, name):
#         self.deptNo = deptNo
#         self.name = name
#     def __str__(self):
#         result = "("+str(self.deptNo) + " " + self.name+ ")"
#         return result
       
# class Student:
#     def __init__(self, studentNo, name, dept):
#         self.studentNo = studentNo
#         self.name = name
#         self.dept = dept
#     def __str__(self):
#         result = "("+str(self.studentNo) + " "
#         result += self.name + " " + self.dept.name + ")"
#         return result


# studentList = []
# deptList = []

# def prepareData():
#     global deptList, studentList
#     matrials = Dept(100,"신소재",["홍길동","임꺽정","박찬호"])
#     mechanics = Dept(200,"기계공학과",["전도일","고뭉치"])
#     deptList= [matrials, mechanics]
#     # studentList = []
#     # studentList.append(Student(101,"신철수",matrials))
#     # studentList.append(Student(102,"신정철",matrials))
#     # studentList.append(Student(201,"기대승",mechanics))
#     # studentList.append(Student(202,"기정은",mechanics))
    
# def main():
#     prepareData()
#     print("="*10,"All Departments List")
#     for dept in deptList:
#         print(dept)
#     print("="*10,"All Students List")
#     for student in studentList:
#         print(student)
# main()

class Dept:
    def __init__(self, deptNo, name, students):
        self.deptNo = deptNo
        self.name = name
        self.students = students
    def __str__(self):
        result = "("+str(self.deptNo) + " " + self.name+ ")"
        return result
       
class Student:
    def __init__(self, studentNo, name):
        self.studentNo = studentNo
        self.name = name
    def __str__(self):
        result = "("+str(self.studentNo) + " "
        result += self.name + ")"
        return result
    
studentList = []
deptList = []

def prepareData():
    global deptList, studentList
    matrials = Dept(100,"신소재", [101, 102])
    mechanics = Dept(200,"기계공학과", [201, 202])
    deptList= [matrials, mechanics]
    studentList = []
    studentList.append(Student(101,"신철수"))
    studentList.append(Student(102,"신정철"))
    studentList.append(Student(201,"기대승"))
    studentList.append(Student(202,"기정은"))
    
def main():
    prepareData()
    print("="*10,"All Departments List")
    for dept in deptList:
        print(dept)
    print("="*10,"All Students List")
    for student in studentList:
        print(student)
main()


class Dept:
    def __init__(self, deptNo, name):
        self.deptNo = deptNo
        self.name = name
    def __str__(self):
        result = "("+str(self.deptNo) + " " + self.name+ ")"
        return result
       
class Student:
    def __init__(self, studentNo, name, dept):
        self.studentNo = studentNo
        self.name = name
        self.dept = dept
    def __str__(self):
        result = "("+str(self.studentNo) + " "
        result += self.name + " " + self.dept.name + ")"
        return result
    
studentList = []
deptList = []

def prepareData():
    global deptList, studentList
    matrials = Dept(100,"신소재")
    mechanics = Dept(200,"기계공학과")
    deptList= [matrials, mechanics]
    studentList = []
    studentList.append(Student(101,"신철수",matrials))
    studentList.append(Student(102,"신정철",matrials))
    studentList.append(Student(201,"기대승",mechanics))
    studentList.append(Student(202,"기정은",mechanics))
    
def main():
    prepareData()
    print("="*10,"All Departments List")
    for dept in deptList:
        print(dept)
    print("="*10,"All Students List")
    for student in studentList:
        print(student)
main()
