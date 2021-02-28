import re
import getpass
import coach_class
import sport_class
import sport_schedule_class
import sort
import os
import rating_class
import coach_schedule_class
import student_class

class Admin:
    admin_id = ""
    admin_name = ""
    admin_password = ""

    def __init__(self,admin_id,admin_name,admin_password):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.admin_password = admin_password

    def file_format(self):
        return "%s#%s#%s\n"%(self.admin_id,self.admin_name,self.admin_password)
        
def admin_menu(admin):
    choose = -1
    
    students = student_class.read_all_registered_students()
    coaches = coach_class.read_all_coaches()
    sports = sport_class.read_all_sports()
    sport_schedules = sport_schedule_class.read_all_sport_schedule()
    sport_centers = sport_class.sport_center_class.read_all_sport_centers()
    ratings = rating_class.read_all_ratings()
    
    while choose != 5:
        os.system("cls")
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
            input("Invalid option given...")
            continue

        if choose == 1:
            # insert empty validation here
            sub = -1
            while sub != 7:
                os.system("cls")
                coach_class.view_coaches(coaches)
                
                print("")
                print("1. Order by name")
                print("2. Order by pay rate")
                print("3. Order by performance")
                print("4. Add coach")
                print("5. Search coach")
                print("6. Update coach")
                print("7. Exit")

                try:
                    sub = int(input("Choose [1 - 7] : "))
                except:
                    print("Wrong input")
                    sub = -1
                    continue

                if sub == 1:
                    sort.sort_by_coach_name(coaches)
                elif sub == 2:
                    sort.sort_by_coach_pay_rate(coaches)
                elif sub == 3:
                    sort.sort_by_coach_rating(coaches)
                elif sub == 4:
                    coaches.append(coach_class.register(sports,sport_schedules,sport_centers))
                elif sub == 5:
                    search_menu = -1
                    coach_id = ""
                    while search_menu != 3:
                        search_result = None
                        coach_id = ""
                        coach_rating = -1
                        os.system("cls")
                        print("1. Search coach by ID")
                        print("2. Search coach by Overall Performance")
                        print("3. Exit")
                        
                        try:
                            search_menu = int(input("Choose [1 - 3] : "))
                        except:
                            print("Wrong input")
                            search_menu = -1
                            continue

                        if search_menu < 1 or search_menu > 3:
                            print("Invalid option given...")
                            continue

                        search_results = []

                        if search_menu == 1:
                            # Masukin validasi kosong kalau misalnya belum ada coach yang terdaftar

                            while re.search("CO[0-9][0-9][0-9][0-9][0-9][0-9]",coach_id) == None:
                                coach_id = input("Insert coach id [ Starts with CO and followed by 6 digit ] : ")
                            
                            search_result = coach_class.search_coach_by_id(coaches,coach_id)

                            if search_result:
                                search_results.append(search_result)
                            
                        elif search_menu == 2:
                            # Cari coach berdasarkan performance
                            while coach_rating < 0.0 or coach_rating > 5.0:
                                try:
                                    coach_rating = float(input("Insert coach rating [ 0.0 - 5.0 ] : "))
                                except:
                                    coach_rating = -1
                                    print("Invalid coach rating")

                            search_results = coach_class.search_coaches_by_performance(coaches,coach_rating)

                        elif search_menu == 3:
                            break

                        if search_results:
                            for search_result in search_results:
                                print("Found coach with Coach ID %s"%(search_result.coach_id))
                                print("Coach name : %s"%(search_result.coach_name))
                                print("Coach pay rate : %f"%(search_result.coach_pay_rate))
                                print("Coach phone : %s"%(search_result.coach_phone))
                                print("Coach address : %s\n"%(search_result.coach_address))
                                coach_class.view_all_coach_sport_schedule(sports,sport_schedules,sport_centers,coach_id)
                                print("")
                        else:
                            print("Coach not found!")

                        os.system("pause")

                elif sub == 6:

                    update_menu = -1
                    
                    while update_menu != 4:
                        coach_id = ""

                        os.system("cls")

                        print("1. Update coach's pay rate")
                        print("2. Fire coach")
                        print("3. Add coach class")
                        print("4. Exit")

                        try:
                            update_menu = int(input("Choose [ 1 - 4 ] : "))
                        except:
                            print("Wrong input")
                            os.system("pause")
                            update_menu = -1
                            continue

                        if update_menu < 1 or update_menu > 4:
                            print("Invalid option given...")
                            os.system("pause")
                            continue
                        
                        if update_menu >= 1 and update_menu <= 3:
                            coach_class.view_coaches(coaches)

                            while re.search("CO[0-9][0-9][0-9][0-9][0-9][0-9]",coach_id) == None:
                                coach_id = input("Insert coach id [ Starts with CO and followed by 6 digit ] : ")

                            coach = coach_class.search_coach_by_id(coaches,coach_id)

                            if coach == None:
                                print("Coach not found")
                                os.system("pause")
                                continue

                            if update_menu in [coach_class.coach_option.UPDATE_OPTION, coach_class.coach_option.FIRE_OPTION]:
                                coach_class.update_or_fire_coach(coaches, coach, update_menu)
                                
                            elif update_menu == 3:
                                coach_schedule_class.register_coach_sport_schedule(sports,sport_schedules,sport_centers,coach_id)
                                
        elif choose == 2:
            sub = -1
            while sub != 4:
                sport_id = ""
                sport_fee = 0.0
                sport_class.view_all_sports(sports, sport_centers)
                print("\n1. Add sport")
                print("2. Search sport")
                print("3. Update sport")
                print("4. Exit")

                try:
                    sub = int(input("Choose [1 - 4] : "))
                except:
                    print("Wrong input")
                    sub = -1
                    os.system("pause")
                    continue

                if sub == 1:
                    sports.append(sport_class.add(sport_centers))
                elif sub == 2 or sub == 3:
                    while re.search("SP[0-9][0-9][0-9][0-9][0-9][0-9]",sport_id) == None:
                        sport_id = input("Insert sport id [ Starts with SP and followed by 6 digit ] : ")
                    
                    find_sport = sport_class.search_sport_by_id(sports,sport_id)

                    if find_sport == None:
                        print("Sport not found")
                        os.system("pause")
                        continue

                    if sub == 2:
                        print("Found sport with id %s"%(find_sport.sport_id))
                        print("Sport name : %s"%(find_sport.sport_name))
                        print("Sport fee : %f"%(find_sport.sport_fee))
                        print("Sport center id : %s"%(find_sport.sport_center_id))
                        os.system("pause")
                        continue
                    else:
                        while sport_fee <= 0.0:
                            try:
                                sport_fee = float(input("Insert sport fee [ value must more than 0.0 ] : "))
                            except:
                                print("Invalid fee!")
                                sport_fee = 0.0
                        
                        for idx in range(len(sports)):
                            if sports[idx].sport_id == find_sport.sport_id:
                                sports[idx].sport_fee = sport_fee
                                break

                        sport_file = open("./sport/sports.txt","w")

                        for sport in sports:
                            sport_file.write(sport.file_format())

                        sport_file.close()

        elif choose == 3:
            # register sport schedule
            sub = -1
            while sub != 3:
                sport_schedule_class.view_all_sport_schedule(sport_schedules,sports)
                print("1. Add sport schedule")
                print("2. Modify sport schedule")
                print("3. Exit")

                try:
                    sub = int(input("Choose [1 - 3] : "))
                except:
                    print("Wrong input")
                    sub = -1
                    continue

                if sub < 1 or sub > 3:
                    print("Invalid option...")
                    os.system("pause")
                    continue

                if sub == 1:
                    sport_schedules.append(sport_schedule_class.add(sports))
                elif sub == 2:
                    sport_schedule_class.update_sport_schedule(sport_schedules)

        elif choose == 4:
            sub = -1
            while sub != 2:
                # Print all student data
                count = 1
                for student in students:
                    print("%d. %s - %s - %d kg - %d cm - DOB : %s - %s - %s"%(count, student.student_id, student.student_name, student.student_weight, student.student_height, student.student_dob, student.student_phone, student.student_address))
                    count += 1

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
                    
                    student = student_class.search_student_by_id(students,student_id)
                    
                    if student != None:    
                        # Print all student information except for password
                        print("Student ID : %s"%(student.student_id))
                        print("Student Name : %s"%(student.student_name))
                        print("Student weight : %d"%(student.student_weight))
                        print("Student height : %d"%(student.student_height))
                        print("Student dob : %s"%(student.student_dob))
                        print("Student phone : %s"%(student.student_phone))
                        print("Student address : %s"%(student.student_address))
                    else:
                        print("Student not found")

                    os.system("pause")
                    

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