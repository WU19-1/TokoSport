import os
import re
import sport_schedule_class
import sport_center_class

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
        return "%s#%s#%.2f#%s\n"%(self.sport_id,self.sport_name,self.sport_fee,self.sport_center_id)

def print_sport_classes(sports):
    count = 1
    for sport in sports:
        print("%d. %s"%(count,sport.rstrip()))
        count += 1

def add(sport_centers):
    os.system("cls")
    sport_id = ""
    sport_name = ""
    sport_fee = 0.0
    sport_center_id = ""

    # while re.search("SP[0-9][0-9][0-9][0-9][0-9][0-9]",sport_id) == None:
    #     sport_id = input("Insert sport id [ Starts with SP and followed by 6 digit ] : ")
    
    list_of_sports_file = open("./sport/list_of_sports.txt")
    list_of_sports = list_of_sports_file.readlines()
    list_of_sports_file.close()

    sport_choice = -1

    # sport name validation need 3 to 50 characters
    while sport_choice < 1 or sport_choice > len(list_of_sports):
        print_sport_classes(list_of_sports)
        try:
            sport_choice = int(input("Choose a sport [ 1 - %d ] : "%(len(list_of_sports))))
        except:
            sport_choice = -1
            print("Invalid input")
    
    sport_name = list_of_sports[sport_choice - 1].rstrip()

    while sport_fee <= 0.0:
        try:
            sport_fee = float(input("Insert sport pay rate [ value must more than 0.0 ] : "))
        except:
            print("Invalid pay rate!")
            sport_fee = 0.0
    
    sport_center_choice = -1

    while sport_center_choice < 1 or sport_center_choice > len(sport_centers):
        count = 1
        for sport_center in sport_centers:
            print("%d. %s - %s"%(count,sport_center.sport_center_name,sport_center.sport_center_address))
            count += 1
        
        try:
            sport_center_choice = int(input("Choose a sport center [ 1 - %d ] "%(len(sport_centers))))
        except:
            sport_center_choice = -1
            print("Invalid option")
            os.system("pause")
    
    sport_center_id = sport_centers[sport_center_choice - 1].sport_center_id
    
    sport_file = open("./sport/sports.txt","r")
    sport_id = "SP%.6d"%(len(sport_file.readlines()) + 1)
    sport_file.close()

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

def view_all_sports(sports,sport_centers):
    count = 1
    for sport in sports:
        sport_center = sport_center_class.search_sport_center_by_id(sport_centers, sport.sport_center_id)
        print("%d. %s - %s - %.2f - %s - %s"%(count, sport.sport_id, sport.sport_name, sport.sport_fee, sport_center.sport_center_name, sport_center.sport_center_address))
        count += 1

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