import re
import getpass
import os
import sport_class
import sport_center_class
import sport_schedule_class
import coach_class
import rating_class
import student_schedule_class

class Student:
    student_id = ""
    student_name = ""
    student_password = ""
    student_weight = 0
    student_height = 0
    student_dob = ""
    student_phone = ""
    student_address = ""

    def __init__(self,student_id,student_name,student_password,student_weight,student_height,student_dob,student_phone,student_address):
        self.student_id = student_id
        self.student_name = student_name
        self.student_password = student_password
        self.student_height = student_height
        self.student_weight = student_weight
        self.student_dob = student_dob
        self.student_address = student_address
        self.student_phone = student_phone
    
    def file_format(self):
        return self.student_id + "#" + self.student_name + "#" + self.student_password + "#" + str(self.student_weight) + "#" + str(self.student_height) + "#" + self.student_dob + "#" + self.student_phone + "#" + self.student_address + "\n"

def read_all_registered_students():
    temp = []

    students_file = open("./student/credential.txt","r")
    list_of_students = students_file.readlines()
    students_file.close()

    for student in list_of_students:
        student_data = student.rstrip().split("#")
        temp.append(Student(student_data[0], student_data[1], student_data[2], int(student_data[3]), int(student_data[4]), student_data[5], student_data[6], student_data[7]))
    
    return temp

def register():
    os.system("cls")

    sports = sport_class.read_all_sports()
    sport_schedules = sport_schedule_class.read_all_sport_schedule()
    sport_centers = sport_center_class.read_all_sport_centers()

    student_id = ""
    student_name = ""
    student_password = ""
    student_weight = 0
    student_height = 0
    student_dob = ""
    student_phone = ""
    student_address = ""
    
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

    while (len(student_phone) < 12 or len(student_phone) > 13) or (not student_phone.startswith("+60") and not student_phone.startswith("60")):
        student_phone = input("Insert student's phone number [ starts with +60 or 60 with 12 or 13 digits] : ")
    
    while not student_address.endswith(" Street"):
        student_address = input("Insert student's address [must end with \" Street\"] : ")

    # Generate Student ID
    student_file = open("./student/credential.txt","r")
    student_id = "TP%.6d"%(len(student_file.readlines()) + 1)
    student_file.close()

    # Tampilkan sport yang ada
    student_schedule_class.register_new_student_sport_schedule(sports,sport_schedules,sport_centers,student_id)
    
    # Create object based on the information that the user have inputted
    student = Student(student_id,student_name,student_password,student_weight,student_height,student_dob,student_phone,student_address)

    # Insert all student information into credential.txt
    credentials = open("./student/credential.txt","a")
    credentials.write(student.file_format())
    credentials.close()

    # Display student id
    print("Your student ID is : %s"%(student_id))
    os.system("pause")
    

def get_all_student_coaches(coaches, sports, sport_schedules, sport_schedule_ids):
    temp = []
    coach_ids = []

    registered_coach_schedule_file = open("./coach/registered_coach_schedule.txt","r")
    coach_schedules = registered_coach_schedule_file.readlines()
    registered_coach_schedule_file.close()

    count = 1

    for sport_schedule_id in sport_schedule_ids:
        student_schedule = sport_schedule_class.search_schedule_by_id(sport_schedules, sport_schedule_id)
        for coach_schedule in coach_schedules:
            coach_schedule_data = coach_schedule.rstrip().split("#")
            if coach_schedule_data[1] == sport_schedule_id:
                coach = coach_class.search_coach_by_id(coaches,coach_schedule_data[0])
                sport = sport_class.search_sport_by_id(sports, coach.coach_sport_id)
                temp.append("%d. %s - %s - %s - %s - %s - %s"%(count,student_schedule.schedule_day,student_schedule.schedule_start_time,student_schedule.schedule_end_time,coach.coach_name,coach.coach_phone,sport.sport_name))
                coach_ids.append(coach.coach_id)
                count += 1
                break
    
    return temp, coach_ids

def get_all_student_ratings(student_id):
    temp = []
    ratings = rating_class.read_all_ratings()
    
    for rating in ratings:
        if rating.student_id == student_id:
            temp.append(rating)
    
    return temp

def registered_student_menu(student):

    sports = sport_class.read_all_sports()
    sport_schedules = sport_schedule_class.read_all_sport_schedule()
    sport_centers = sport_center_class.read_all_sport_centers()
    student_schedules, schedule_ids = student_schedule_class.get_all_student_sport_schedule(sports,sport_centers,sport_schedules,student.student_id)
    coaches = coach_class.read_all_coaches()
    student_ratings = get_all_student_ratings(student.student_id)

    choose = -1
    while choose != 4:
        os.system("cls")
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
                os.system("cls")
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
            sub = -1
            choose_coach = -1
            rating = -1
            rated = False

            student_coaches, coach_ids = get_all_student_coaches(coaches,sports,sport_schedules,schedule_ids)

            while sub != 2:
                rated = False
                print("Your coaches :")

                # print all coach here.
                for coach in student_coaches:
                    print(coach)

                print("")
                print("1. Give rating to coach")
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
                    try:
                        choose_coach = int(input("Choose coach [ 1 - %d ] : "%(len(coach_ids))))
                    except:
                        choose_coach = -1
                        continue

                    if choose_coach < 1 or choose_coach > len(coach_ids):
                        print("Invalid coach!")
                        continue

                    for student_rating in student_ratings:
                        if student_rating.coach_id == coach_ids[choose_coach - 1]:
                            print("You have given a rating to this coach before!")
                            rated = True

                    if rated:
                        continue

                    while rating < 1 or rating > 5:
                        try:
                            rating = int(input("Insert rating [ 1 - 5 ] : "))
                        except:
                            rating = -1
                            continue

                    student_ratings.append(rating_class.add(student.student_id,coach_ids[choose_coach - 1],rating))
                    print("Successfully give rating to coach!")

        elif choose == 3:
            sub = -1

            while sub != 4:
                print("Your sport schedule list:")

                for idx in range(len(student_schedules)):
                    print("\t" + str(idx + 1) + ". " + student_schedules[idx])

                print("")
                print("1. Register new sport schedule")
                print("2. Update sport schedule")
                print("3. Delete sport schedule")
                print("4. Exit")

                try:
                    sub = int(input("Choose [1 - 4] : "))
                except:
                    print("Wrong input")
                    sub = -1
                    continue

                if sub < 1 or sub > 4:
                    print("Invalid option given...")
                    continue
                
                if sub == 1:
                    student_schedules.append(student_schedule_class.register_new_student_sport_schedule(sports,sport_schedules,sport_centers,student.student_id))
                elif sub == 2 or sub == 3:
                    choice = -1
                    for idx in range(len(student_schedules)):
                        print("\t" + str(idx + 1) + ". " + student_schedules[idx])

                    try:
                        choice = int(input("\nChoose sport schedule [ 1 - %d ] : "%(len(student_schedules))))
                    except:
                        print("Wrong input")
                        choice = -1
                        continue

                    if choice < 1 or choice > len(student_schedules):
                        print("Invalid option")
                        continue

                    if sub == 2:
                        student_schedules.append(student_schedule_class.register_new_student_sport_schedule(sports,sport_schedules,sport_centers,student.student_id))

                    registered_student_sport_preference_file = open("./student/registered_student_sport.txt","r")
                    student_sport_schedules = registered_student_sport_preference_file.readlines()
                    registered_student_sport_preference_file.close()

                    registered_student_sport_preference_file = open("./student/registered_student_sport.txt","w")
                        
                    for student_sport_schedule in student_sport_schedules:
                        data = student_sport_schedule.rstrip().split("#")
                        if data[0] == student.student_id and data[1] == schedule_ids[choice - 1]:
                            continue
                        registered_student_sport_preference_file.write("%s#%s\n"%(data[0],data[1]))
                        
                    registered_student_sport_preference_file.close()
                    
                    schedule_ids.pop(choice - 1)
                    student_schedules.pop(choice - 1)


def login_as_student():
    # Input name and password
    os.system("cls")
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
            student = Student(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7])
            registered_student_menu(student)
            return
    
    print("Invalid Credential!")

def search_student_by_id(students, student_id):
    for student in students:
        if student_id == student.student_id:
            return student
    
    return None