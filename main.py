import re
import getpass
import student_class
import admin_class
import os
    
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
            pass
        elif choose == 4:
            student_class.register()
    
main()