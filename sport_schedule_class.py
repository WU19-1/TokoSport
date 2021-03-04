import re
import sport_class
import os
import sport_time


class SportSchedule:
    sport_schedule_id = ""
    sport_id = ""
    schedule_start_time = ""
    schedule_end_time = ""
    schedule_day = ""

    def __init__(self,sport_schedule_id,sport_id,schedule_start_time,schedule_end_time,schedule_day):
        self.sport_schedule_id = sport_schedule_id
        self.sport_id = sport_id
        self.schedule_start_time = schedule_start_time
        self.schedule_end_time = schedule_end_time
        self.schedule_day = schedule_day
        
    def file_format(self):
        return self.sport_schedule_id + "#" + self.sport_id + "#" + self.schedule_start_time + "#" + self.schedule_end_time + "#" + self.schedule_day + "\n"


def print_time():
    for idx in range(len(sport_time.START_TIME)):
        print("%d. %s - %s"%(idx + 1,sport_time.START_TIME[idx],sport_time.END_TIME[idx]))

def add(sports):
    sport_schedule_id = ""
    sport_id = ""
    schedule_start_time = ""
    schedule_end_time = ""
    schedule_day = ""

    # while re.search("SS[0-9][0-9][0-9][0-9][0-9][0-9]",sport_schedule_id) == None:
    #     sport_schedule_id = input("Insert sport schedule id [ Starts with SS and followed by 6 digit ] : ")

    sport_choice = -1

    while sport_choice < 1 or sport_choice > len(sports):
        sport_class.print_sport_classes(sports)
        try:
            sport_choice = int(input("Choose sport [ 1 - %d ] : "%(len(sports))))
        except:
            sport_choice = -1
            print("Invalid option")
            continue

    sport_id = sports[sport_choice - 1].sport_id

    choice = -1

    while choice < 1 or choice > 6:
        print_time()
        try:
            choice = int(input("Insert start time [ choose between 1 to 6 ] : "))
        except:
            choice = -1
    
    schedule_start_time = sport_time.START_TIME[choice - 1]
    schedule_end_time = sport_time.END_TIME[choice - 1]

    while schedule_day not in sport_time.DAY:
        schedule_day = input("Insert day [ choose between Sunday to Saturday ] : ")
    
    sport_schedule_file = open("./sport_schedule/sport_schedule.txt","r")
    sport_schedule_id = "SS%.6d"%(len(sport_schedule_file.readlines()) + 1)
    sport_schedule_file.close()

    sport_schedule = SportSchedule(sport_schedule_id,sport_id,schedule_start_time,schedule_end_time,schedule_day)
    
    sport_schedule_file = open("./sport_schedule/sport_schedule.txt","a")
    sport_schedule_file.write(sport_schedule.file_format())
    sport_schedule_file.close()

    return sport_schedule

    
def read_all_sport_schedule():
    sport_schedule_file = open("./sport_schedule/sport_schedule.txt","r")
    list_of_sport_schedules = sport_schedule_file.readlines()
    sport_schedule_file.close()

    temp = []
    for sport_schedule in list_of_sport_schedules:
        sport_schedule_data = sport_schedule.rstrip().split("#")
        temp.append(SportSchedule(sport_schedule_data[0],sport_schedule_data[1],sport_schedule_data[2],sport_schedule_data[3],sport_schedule_data[4]))
    
    return temp

def view_all_sport_schedule(sport_schedules,sports):
    for sport_schedule in sport_schedules:
        sport = sport_class.search_sport_by_id(sports,sport_schedule.sport_id)
        print(sport_schedule.sport_schedule_id + " - " + sport.sport_name + " - " + sport_schedule.schedule_start_time + " - " + sport_schedule.schedule_end_time + " - " + sport_schedule.schedule_day)

def search_schedule_by_id(sport_schedules,sport_schedule_id):
    for data in sport_schedules:
        if data.sport_schedule_id == sport_schedule_id:
            return data
    return None

def update_sport_schedule(sport_schedules):
    sport_schedule_id = ""
    schedule_start_time = ""
    schedule_end_time = ""
    schedule_day = ""

    while re.search("SS[0-9][0-9][0-9][0-9][0-9][0-9]",sport_schedule_id) == None or search_schedule_by_id(sport_schedules,sport_schedule_id) == None:
        sport_schedule_id = input("Insert sport schedule id [ Starts with SS and followed by 6 digit ] : ")

    choice = -1

    while choice < 1 or choice > 6:
        print_time()
        try:
            choice = int(input("Insert start time [ choose between 1 to 6 ] : "))
            if choice < 1 or choice > 6:
                continue
        except:
            choice = -1
    
    schedule_start_time = sport_time.START_TIME[choice - 1]
    schedule_end_time = sport_time.END_TIME[choice - 1]

    while schedule_day not in sport_time.DAY:
        schedule_day = input("Insert day [ choose between Sunday to Saturday ] : ")

    for idx in range(len(sport_schedules)):
        if sport_schedules[idx].sport_schedule_id == sport_schedule_id:
            sport_schedules[idx].schedule_start_time = schedule_start_time
            sport_schedules[idx].schedule_end_time = schedule_end_time
            sport_schedules[idx].schedule_day = schedule_day
            break
    
    sport_schedule_file = open("./sport_schedule/sport_schedule.txt","w")
    
    for sport_schedule in sport_schedules:
        sport_schedule_file.write(sport_schedule.file_format())

    sport_schedule_file.close()

def find_all_sport_schedules(sport_schedules,sport_id):
    temp = []
    for data in sport_schedules:
        if data.sport_id == sport_id:
            temp.append(data)
    return temp
    