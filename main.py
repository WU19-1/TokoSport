import re
import getpass
import student_class
import admin_class
import coach_class
import sport_class
import sport_schedule_class
import os
import rating_class
import sport_center_class
    
def main():
    choose = -1
    while choose != 5:
        os.system("cls")
        print("1. Login as Admin")
        print("2. Login as Student")
        print("3. Login as Guest")
        print("4. Register")
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
            admin_class.login_as_admin()
        elif choose == 2:
            student_class.login_as_student()
        elif choose == 3:
            
            sports = sport_class.read_all_sports()
            sport_schedules = sport_schedule_class.read_all_sport_schedule()
            coaches = coach_class.read_all_coaches()
            sport_centers = sport_center_class.read_all_sport_centers()

            sub = -1
            
            while sub != 3:
                os.system("cls")
                print("1. View all sport")
                print("2. View all sport schedule")
                print("3. Exit")

                try:
                    sub = int(input("Choose [1 - 3] : "))
                except:
                    print("Wrong input")
                    sub = -1
                    continue

                if sub < 1 or sub > 3:
                    print("Invalid option given...")
                    continue

                if sub == 1:
                    sport_class.view_all_sports(sports,sport_centers)
                elif sub == 2:
                    sport_schedule_class.view_all_sport_schedule(sport_schedules,sports)

                os.system("pause")

        elif choose == 4:
            student_class.register()

if __name__ == "__main__":
    main()