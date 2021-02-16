import os
import re
import sport_schedule_class
import sport_center_class

SPORT_CLASSES = ["Swimming", "Badminton", "Football", "Archery", "Gymnastics", "Volleyball", "Basketball", "Cricket", "Tennis", "Table Tennis"]

class Sport:
    sport_id = ""
    sport_name = ""
    sport_fee = 0.0
    sport_center_id = ""

    def __init__(self,sport_id,sport_name,sport_fee,sport_center_id):
        self.sport_id = sport_id
        self.sport_name = sport_name
        self.sport_fee = sport_fee
        self.sport_center_id = sport_center_id

    def file_format(self):
        return self.sport_id + "#" + self.sport_name + "#" + str(self.sport_fee) + "#" + self.sport_center_id + "\n"

def print_sport_classes(sports):
    count = 1
    for sport in sports:
        print("%d. %s - %s"%(count,sport.sport_id,sport.sport_name))
        count += 1

def add():
    os.system("cls")
    sport_id = ""
    sport_name = ""
    sport_fee = 0.0
    sport_center_id = ""

    while re.search("SP[0-9][0-9][0-9][0-9][0-9][0-9]",sport_id) == None:
        sport_id = input("Insert sport id [ Starts with SP and followed by 6 digit ] : ")
    
    # sport name validation need 3 to 50 characters
    while sport_name not in sport_classes:
        print_sport_classes()
        sport_name = input("Insert sport name : ")

    while sport_fee <= 0.0:
        try:
            sport_fee = float(input("Insert sport pay rate [ value must more than 0.0 ] : "))
        except:
            print("Invalid pay rate!")
            sport_fee = 0.0
    
    while re.search("SC[0-9][0-9][0-9][0-9][0-9][0-9]",sport_center_id) == None:
        sport_center_id = input("Insert sport center id [ Starts with SP and followed by 6 digit ] : ")
    

    sport = Sport(sport_id,sport_name,sport_fee,sport_center_id)

    sport_file = open("./sport/sports.txt","a")
    sport_file.write(sport.file_format())
    sport_file.close()

    return sport

def read_all_sports():
    sport_file = open("./sport/sports.txt","r")
    list_of_sports = sport_file.readlines()

    temp = []
    for sport in list_of_sports:
        sport_data = sport.rstrip().split("#")
        temp.append(Sport(sport_data[0],sport_data[1],float(sport_data[2]),sport_data[3]))
    
    return temp

def view_all_sports(sports):
    for sport in sports:
        print(sport.sport_id + " - " + sport.sport_name + " - " + str(sport.sport_fee) + " - " + sport.sport_center_id)

def get_sports_detail(sports,sport_schedules,sport_centers):
    choices = []
    details = []
    count = 1
    for i in range(len(sports)):
        sport_center = sport_center_class.search_sport_center_by_id(sport_centers,sports[i].sport_center_id)
        
        sport_schedule = sport_schedule_class.find_all_sport_schedules(sport_schedules,sports[i].sport_id)
        if sport_schedule != []:
            for data in sport_schedule:
                details.append(str(count) + ". " + sports[i].sport_name + " - " + str(sports[i].sport_fee) + " - " + data.schedule_day + " - " + data.schedule_start_time + " - " + data.schedule_end_time + " - " + sport_center.sport_center_name + " - " + sport_center.sport_center_address)
                choices.append(data.sport_schedule_id)
                count += 1

    return details,choices


def search_sport_by_id(sports,sport_id):
    for sport in sports:
        if sport.sport_id == sport_id:
            return sport
    return None