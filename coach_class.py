import re

class Coach:
    coach_id = ""
    coach_name = ""
    coach_pay_rate = 0.0
    coach_speciality = ""

    def __init__(self,coach_id,coach_name,coach_pay_rate,coach_speciality):
        self.coach_id = coach_id
        self.coach_name = coach_name
        self.coach_pay_rate = coach_pay_rate
        self.coach_speciality = coach_speciality

    def file_format(self):
        return self.coach_id + "#" + self.coach_name + "#" + str(self.coach_pay_rate) + "#" + self.coach_speciality + "\n"

def register():
    coach_id = ""
    coach_name = ""
    coach_pay_rate = 0.0
    coach_speciality = ""

    while re.search("CO[0-9][0-9][0-9][0-9][0-9][0-9]",coach_id) == None:
        coach_id = input("Insert coach id [ Starts with CO and followed by 6 digit ] : ")
    
    # coach name validation need 3 to 50 characters
    while len(coach_name) < 3 or len(coach_name) > 50:
        coach_name = input("Insert coach name [ 3 to 50 characters ] : ")

    while coach_pay_rate <= 0.0:
        try:
            coach_pay_rate = float(input("Insert coach pay rate [ value must more than 0.0 ] : "))
        except:
            print("Invalid pay rate!")
            coach_pay_rate = 0.0
    
    while coach_speciality == "":
        coach_speciality = input("Insert coach speciality [ seperated by comma ] : ")

    coach = Coach(coach_id,coach_name,coach_pay_rate,coach_speciality)

    coaches = open("./coach/coaches.txt","a")
    coaches.write(coach.file_format())
    coaches.close()

    return coach

def read_all_coaches():
    coaches = open("./coach/coaches.txt","r")
    list_of_coaches = coaches.readlines()
    coaches.close()
    
    temp = []
    for coach in list_of_coaches:
        coach_data = coach.rstrip().split("#")
        temp.append(Coach(coach_data[0],coach_data[1],float(coach_data[2]),coach_data[3]))
    
    return temp