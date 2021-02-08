import re
import getpass
import coach_class

class Admin:
    admin_id = ""
    admin_name = ""
    admin_password = ""

    def __init__(self,admin_id,admin_name,admin_password):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.admin_password = admin_password

    def file_format(self):
        return self.admin_id + "#" + self.admin_name + "#" + self.admin_password + "\n"

def read_all_registered_student():
    students = open("./student/credential.txt","r")
    list_of_students = students.readlines()
    students.close()
    return list_of_students

def admin_menu(admin):
    choose = -1
    
    students = read_all_registered_student()
    coaches = coach_class.read_all_coaches()
    
    while choose != 5:
        print("Welcome " + admin.admin_id + " - " + admin.admin_name)
        print("1. View all coach")
        print("2. View all sport")
        print("3. View all sport schedule")
        print("4. View all registered student")
        print("5. Exit")

        try:
            choose = int(input("Choose [1 - 5] : "))
        except:
            print("Wrong input")
            choose = -1
            continue

        if choose < 1 or choose > 5:
            print("Invalid option given...")
            continue

        if choose == 1:
            # insert empty validation here

            sub = -1

            while sub != 7:
                for coach in coaches:
                    print(coach.coach_id + " - " + coach.coach_name + " - " + str(coach.coach_pay_rate) + " - " + coach.coach_speciality.replace(",",", "))
                
                print("")
                print("1. Order by name")
                print("2. Order by pay rate")
                print("3. Order by performance")
                print("4. Add coach")
                print("5. Search Coach")
                print("6. Update sport")
                print("7. Exit")

                try:
                    sub = int(input("Choose [1 - 7] : "))
                except:
                    print("Wrong input")
                    sub = -1
                    continue

                if sub == 1:
                    pass
                elif sub == 2:
                    pass
                elif sub == 3:
                    pass
                elif sub == 4:
                    coaches.append(coach_class.register())
                elif sub == 5:
                    pass
                elif sub == 6:
                    pass
                    

        elif choose == 2:
            pass
        elif choose == 3:
            pass
        elif choose == 4:
            sub = -1
            while sub != 2:
                # Print all student data
                for student in students:
                    temp = student.rstrip().split("#")
                    print(temp[0] + " - " + temp[1])

                print("1. Search student by ID")
                print("2. Exit")

                try:
                    sub = int(input("Choose [1 - 2] : "))
                except:
                    print("Wrong input")
                    sub = -1
                    continue

                if sub == 1:
                    # search by id
                    student_id = ""
                    
                    if len(students) == 0:
                        print("THERE IS NO REGISTERED STUDENT YET!")
                        continue

                    while re.search("TP[0-9][0-9][0-9][0-9][0-9][0-9]",student_id) == None:
                        student_id = input("Insert student id [ Starts with TP and followed by 6 digit ] : ")
                    
                    found = False

                    for student in students:
                        temp = student.rstrip().split("#")
                        if temp[0] == student_id:
                            # Print all student information except for password
                            print("Student ID :",temp[0])
                            print("Name :",temp[1])
                            print("Weight :",temp[3],"kg(s)")
                            print("Height :",temp[4],"cm(s)")
                            print("DOB :",temp[5])
                            found = True
                    
                    if not found:
                        print("Invalid student ID")

                    input()
                    
                    
                    
                


def login_as_admin():
    # Input name and password
    admin_id = ""
    admin_password = ""

    while re.search("AD[0-9][0-9][0-9][0-9][0-9][0-9]",admin_id) == None:
        admin_id = input("Insert admin id [ Starts with AD and followed by 6 digit ] : ")

    while len(admin_password) < 8:
        admin_password = getpass.getpass("Insert admin password [ minimal 8 characters ] : ")
    
    # Read credential.txt from folder admin
    credentials = open("./admin/credential.txt","r")
    list_of_credentials = credentials.readlines()
    credentials.close()

    for info in list_of_credentials:
        # Split the data with pound sign
        temp = info.rstrip().split("#")

        # If the credential match the credential in credential.txt then we redirect the user
        # to admin menu
        if temp[0] == admin_id and temp[2] == admin_password:
            print("Login successful!")
            admin = Admin(temp[0],temp[1],temp[2])
            admin_menu(admin)
            return
    
    print("Invalid Credential!")