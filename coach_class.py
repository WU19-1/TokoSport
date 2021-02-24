import re
import os
import sport_class
import sport_center_class
import sport_schedule_class
import math
import rating_class
import coach_schedule_class
import coach_option

class Coach:
    coach_id = ""
    coach_name = ""
    coach_pay_rate = 0.0
    coach_phone = ""
    coach_address = ""
    coach_sport_id = ""
    coach_rating = 0.0

    def __init__(self,coach_id,coach_name,coach_pay_rate,coach_phone,coach_address,coach_sport_id,coach_rating):
        self.coach_id = coach_id
        self.coach_name = coach_name
        self.coach_pay_rate = coach_pay_rate
        self.coach_phone = coach_phone
        self.coach_address = coach_address
        self.coach_sport_id = coach_sport_id
        self.coach_rating = coach_rating

    def file_format(self):
        return "%s#%s#%.2f#%s#%s#%s#%.2f\n"%(self.coach_id,self.coach_name,self.coach_pay_rate,self.coach_phone,self.coach_address,self.coach_sport_id,self.coach_rating)

# def register_coach_sport_schedule(sports,sport_schedules,sport_centers,coach_id):
#     sport_choice = -1
#     details, choices = sport_class.get_sports_detail(sports,sport_schedules,sport_centers)
#     coach = search_coach_by_id(read_all_coaches(),coach_id)
    
#     while sport_choice < 1 or sport_choice > len(choices):
#         for detail in details:
#             print(detail)
        
#         try:
#             sport_choice = int(input("Choose one of the sport [1 - %d] : "%(len(choices))))
#         except:
#             print("Wrong input")
#             sport_choice = -1
#             continue

#         if sport_choice < 1 or sport_choice > len(choices):
#             input("Invalid option given...")
#             continue

#         schedule = sport_schedule_class.search_schedule_by_id(sport_schedules,choices[sport_choice - 1])
#         if coach != None and coach.coach_sport_id != schedule.sport_id:
#             print("Invalid option")
#             os.system("pause")
#             sport_choice = -1

#     register_coach_schedule_file = open("./coach/registered_coach_schedule.txt","a")
#     register_coach_schedule_file.write("%s#%s\n"%(coach_id,choices[sport_choice - 1]))
#     register_coach_schedule_file.close()

#     sport_id = sport_schedule_class.search_schedule_by_id(sport_schedules,choices[sport_choice - 1]).sport_id

#     return sport_id

# def view_all_coach_sport_schedule(sports,sport_schedules,sport_centers,coach_id):
#     register_coach_schedule_file = open("./coach/registered_coach_schedule.txt","r")
#     registered_coach_schedules = register_coach_schedule_file.readlines()

#     print("Coach schedule : ")

#     for registered_coach_schedule in registered_coach_schedules:
#         data = registered_coach_schedule.rstrip().split("#")
#         if data[0] == coach_id:
#             schedule = sport_schedule_class.search_schedule_by_id(sport_schedules,data[1])
#             sport = sport_class.search_sport_by_id(sports,schedule.sport_id)
#             sport_center = sport_center_class.search_sport_center_by_id(sport_centers,sport.sport_center_id)
#             print("\t%s - %s - %s - %s - %s - %s"%(sport.sport_name,schedule.schedule_day,schedule.schedule_start_time,schedule.schedule_end_time,sport_center.sport_center_name,sport_center.sport_center_address))
    
#     register_coach_schedule_file.close()

def register(sports,sport_schedules,sport_centers):
    os.system("cls")
    coach_id = ""
    coach_name = ""
    coach_pay_rate = 0.0
    coach_phone = ""
    coach_address = ""
    coach_sport_id = ""
    
    # coach name validation need 3 to 50 characters
    while len(coach_name) < 3 or len(coach_name) > 50:
        coach_name = input("Insert coach name [ 3 to 50 characters ] : ")

    while coach_pay_rate < 100.0 or coach_pay_rate > 500.0:
        try:
            coach_pay_rate = float(input("Insert coach pay rate [ value must be between 100 to 500 RM ] : "))
        except:
            print("Invalid pay rate!")
            coach_pay_rate = 0.0

    while (len(coach_phone) < 12 or len(coach_phone) > 13) or (not coach_phone.startswith("+60") and not coach_phone.startswith("60")):
        coach_phone = input("Insert coach's phone number [ starts with +60 or 60 with 12 or 13 digits] : ")
    
    while not coach_address.endswith(" Street"):
        coach_address = input("Insert coach's address [must end with \" Street\"] : ")

    # Generate coach id
    coaches_file = open("./coach/coaches.txt","r")
    coach_id = "CO%.6d"%(len(coaches_file.readlines()) + 1)
    coaches_file.close()

    coach_sport_id = coach_schedule_class.register_coach_sport_schedule(sports,sport_schedules,sport_centers,coach_id)

    coach = Coach(coach_id,coach_name,coach_pay_rate,coach_phone,coach_address,coach_sport_id,0)

    coaches_file = open("./coach/coaches.txt","a")
    coaches_file.write(coach.file_format())
    coaches_file.close()

    return coach

def read_all_coaches():
    coaches_file = open("./coach/coaches.txt","r")
    list_of_coaches = coaches_file.readlines()
    coaches_file.close()

    ratings = rating_class.read_all_ratings()
    
    temp = []
    for coach in list_of_coaches:
        coach_data = coach.rstrip().split("#")
        rating = rating_class.get_performance(ratings, coach_data[0])
        temp.append(Coach(coach_data[0],coach_data[1],float(coach_data[2]),coach_data[3],coach_data[4],coach_data[5],rating))
    
    return temp

def search_coach_by_id(coaches,coach_id):
    for coach in coaches:
        if coach.coach_id == coach_id:
            return coach
    return None

def search_coaches_by_performance(coaches, performance):
    temp = []
    for coach in coaches:
        if coach.coach_rating == performance:
            temp.append(coach)

    return temp

def update_or_fire_coach(coaches, coach_obj, option):
    if option == coach_option.UPDATE_OPTION:
        coach_pay_rate = -1.0
        while coach_pay_rate <= 0.0:
            try:
                coach_pay_rate = float(input("Insert coach pay rate [ value must more than 0.0 ] : "))
            except:
                print("Invalid pay rate!")
                coach_pay_rate = -1.0
        
        for idx in range(len(coaches)):
            if coaches[idx].coach_id == coach_obj.coach_id:
                coaches[idx].coach_pay_rate = coach_pay_rate
                break
    elif option == coach_option.FIRE_OPTION:
        for idx in range(len(coaches)):
            if coaches[idx].coach_id == coach_obj.coach_id:
                coaches.pop(idx)
                break

    coach_file = open("./coach/coaches.txt","w")

    for coach in coaches:
        coach_file.write(coach.file_format())

    coach_file.close()

def view_coaches(coaches, ratings):
    count = 1
    for coach in coaches:
        print(str(count) + ". " + coach.coach_id + " - " + coach.coach_name + " - " + str(coach.coach_pay_rate) + " - " + coach.coach_phone + " - " + coach.coach_address + " - " + str(coach.coach_rating))
        count += 1