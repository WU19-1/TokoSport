import re
import getpass

class Student:
    student_id = ""
    student_name = ""
    student_password = ""
    student_weight = 0
    student_height = 0
    student_dob = ""

    def __init__(self,student_id,student_name,student_password,student_weight,student_height,student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_password = student_password
        self.student_height = student_height
        self.student_weight = student_weight
        self.student_dob = student_dob
    
    def file_format(self):
        return self.student_id + "#" + self.student_name + "#" + self.student_password + "#" + str(self.student_weight) + "#" + str(self.student_height) + "#" + self.student_dob + "\n"

def register():
    print("Menu register")
    student_id = ""
    student_name = ""
    student_password = ""
    student_weight = 0
    student_height = 0
    student_dob = ""
    
    # Student ID validation based on APU Student ID
    while re.search("TP[0-9][0-9][0-9][0-9][0-9][0-9]",student_id) == None:
        student_id = input("Insert student id [ Starts with TP and followed by 6 digit ] : ")
    
    # Student name validation need 3 to 50 characters
    while len(student_name) < 3 or len(student_name) > 50:
        student_name = input("Insert student name [ 3 to 50 characters ] : ")

    # Student password minimal of 8 characters
    while len(student_password) < 8:
        student_password = getpass.getpass("Insert student password [ minimal 8 characters ] : ")

    while student_weight == 0:
        try:
            student_weight = int(input("Insert your weight [ cannot be zero | in kilograms ] : "))
        except:
            student_weight = 0
    
    while student_height == 0:
        try:
            student_height = int(input("Insert your height [ cannot be zero | in centimeters ] : "))
        except:
            student_height = 0

    while re.search("[0-9][0-9] - [0-9][0-9] - [0-9][0-9][0-9][0-9]",student_dob) == None:
        student_dob = input("Insert student's date of birth [ with format \"dd - mm - yyyy\" ] : ")

    # Create object based on the information that the user have inputted
    student = Student(student_id,student_name,student_password,student_weight,student_height,student_dob)

    # Insert all student information into credential.txt
    credentials = open("./student/credential.txt","a")
    credentials.write(student.file_format())
    credentials.close()

def registered_student_menu(student):
    choose = -1
    while choose != 4:
        print("Welcome " + student.student_id + " - " + student.student_name)
        print("1. View self record")
        print("2. View coach")
        print("3. View schedule")
        print("4. Exit")

        try:
            choose = int(input("Choose [1 - 4] : "))
        except:
            print("Wrong input")
            choose = -1
            continue

        if choose < 1 or choose > 4:
            print("Invalid option given...")
            continue

        if choose == 1:
            sub = -1
            while sub != 2:
                print("My self record")
                print("Name :",student.student_name)
                print("Weight :",student.student_weight,"kg(s)")
                print("Height :",student.student_height,"cm(s)")
                print("1. Update self record")
                print("2. Exit")

                try:
                    sub = int(input("Choose [1 - 2] : "))
                except:
                    print("Wrong input")
                    sub = -1
                    continue

                if sub < 1 or sub > 2:
                    print("Invalid option given...")
                    continue

                if sub == 1:
                    student_weight = 0
                    student_height = 0

                    while student_weight == 0:
                        try:
                            student_weight = int(input("Insert your weight [ cannot be zero | in kilograms ] : "))
                        except:
                            student_weight = 0
                
                    while student_height == 0:
                        try:
                            student_height = int(input("Insert your height [ cannot be zero | in centimeters ] : "))
                        except:
                            student_height = 0
                    
                    student.student_height = student_height
                    student.student_weight = student_weight

                    credentials = open("./student/credential.txt","r")
                    list_of_credentials = credentials.readlines()
                    credentials.close()

                    for idx in range(len(list_of_credentials)):
                        temp = list_of_credentials[idx].rstrip().split("#")
                        if temp[0] == student.student_id:
                            list_of_credentials[idx] = student.file_format()

                    credentials = open("./student/credential.txt","w")
                    
                    for data in list_of_credentials:
                        credentials.write(data)

                    credentials.close()


        elif choose == 2:
            pass
        elif choose == 3:
            pass

def login_as_student():
    # Input name and password
    student_id = ""
    student_password = ""

    while re.search("TP[0-9][0-9][0-9][0-9][0-9][0-9]",student_id) == None:
        student_id = input("Insert student id [ Starts with TP and followed by 6 digit ] : ")

    while len(student_password) < 8:
        student_password = getpass.getpass("Insert student password [ minimal 8 characters ] : ")
    
    # Read credential.txt from folder student
    credentials = open("./student/credential.txt","r")
    list_of_credentials = credentials.readlines()
    credentials.close()

    for info in list_of_credentials:
        # Split the data with pound sign
        temp = info.rstrip().split("#")

        # If the credential match the credential in credential.txt then we redirect the user
        # to student menu
        if temp[0] == student_id and temp[2] == student_password:
            print("Login successful!")
            student = Student(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5])
            registered_student_menu(student)
            return
    
    print("Invalid Credential!")