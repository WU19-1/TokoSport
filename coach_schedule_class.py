import sport_class
import coach_class
import sport_schedule_class
import sport_center_class
import os

class CoachSchedule:
    coach_id = ""
    schedule_id = ""

    def __init__(self,coach_id,schedule_id):
        self.coach_id = coach_id
        self.schedule_id = schedule_id
    
    def file_format(self):
        return "%s#%s\n"%(self.coach_id,self.schedule_id)

def register_coach_sport_schedule(sports,sport_schedules,sport_centers,coach_id):
    sport_choice = -1
    details, choices = sport_class.get_sports_detail(sports,sport_schedules,sport_centers)
    coach = coach_class.search_coach_by_id(coach_class.read_all_coaches(),coach_id)
    
    while sport_choice < 1 or sport_choice > len(choices):
        for detail in details:
            print(detail)
        
        try:
            sport_choice = int(input("Choose one of the sport [1 - %d] : "%(len(choices))))
        except:
            print("Wrong input")
            sport_choice = -1
            continue

        if sport_choice < 1 or sport_choice > len(choices):
            input("Invalid option given...")
            continue

        schedule = sport_schedule_class.search_schedule_by_id(sport_schedules,choices[sport_choice - 1])
        if coach != None and coach.coach_sport_id != schedule.sport_id:
            print("Invalid option")
            os.system("pause")
            sport_choice = -1

    coach_schedule = CoachSchedule(coach_id,choices[sport_choice - 1])

    register_coach_schedule_file = open("./coach/registered_coach_schedule.txt","a")
    register_coach_schedule_file.write(coach_schedule.file_format())
    register_coach_schedule_file.close()

    sport_id = sport_schedule_class.search_schedule_by_id(sport_schedules,choices[sport_choice - 1]).sport_id

    return sport_id

def view_all_coach_sport_schedule(sports,sport_schedules,sport_centers,coach_id):
    register_coach_schedule_file = open("./coach/registered_coach_schedule.txt","r")
    registered_coach_schedules = register_coach_schedule_file.readlines()

    print("Coach schedule : ")

    for registered_coach_schedule in registered_coach_schedules:
        data = registered_coach_schedule.rstrip().split("#")
        if data[0] == coach_id:
            schedule = sport_schedule_class.search_schedule_by_id(sport_schedules,data[1])
            sport = sport_class.search_sport_by_id(sports,schedule.sport_id)
            sport_center = sport_center_class.search_sport_center_by_id(sport_centers,sport.sport_center_id)
            print("\t%s - %s - %s - %s - %s - %s"%(sport.sport_name,schedule.schedule_day,schedule.schedule_start_time,schedule.schedule_end_time,sport_center.sport_center_name,sport_center.sport_center_address))
    
    register_coach_schedule_file.close()