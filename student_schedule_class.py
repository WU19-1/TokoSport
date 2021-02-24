import sport_schedule_class
import sport_class
import sport_center_class

class StudentSchedule:
    schedule_id = ""
    student_id = ""

    def __init__(self,student_id,schedule_id):
        self.schedule_id = schedule_id
        self.student_id = student_id

    def file_format(self):
        return "%s#%s\n"%(self.student_id,self.schedule_id)

def get_all_student_sport_schedule(sports,sport_centers,sport_schedules,student_id):
    details = []
    choices = []
    
    registered_student_sport_preference_file = open("./student/registered_student_sport.txt","r")
    student_sport_schedules = registered_student_sport_preference_file.readlines()
    registered_student_sport_preference_file.close()

    for student_sport_schedule in student_sport_schedules:
        data = student_sport_schedule.rstrip().split("#")
        if student_id == data[0]:
            schedule = sport_schedule_class.search_schedule_by_id(sport_schedules,data[1])
            sport = sport_class.search_sport_by_id(sports,schedule.sport_id)
            sport_center = sport_center_class.search_sport_center_by_id(sport_centers,sport.sport_center_id)
            details.append(sport.sport_name + " - " + schedule.schedule_day + " - " + schedule.schedule_start_time + " - " + schedule.schedule_end_time + " - " + sport_center.sport_center_name + " - " + sport_center.sport_center_address)
            choices.append(schedule.sport_schedule_id)

    return details,choices

def register_new_student_sport_schedule(sports,sport_schedules,sport_centers,student_id):
    sport_choice = -1
    details, choices = sport_class.get_sports_detail(sports,sport_schedules,sport_centers)
    
    while sport_choice < 1 or sport_choice > len(choices):
        for detail in details:
            print(detail)
        
        try:
            sport_choice = int(input("Choose one of the sport [ 1 - %d ] : "%(len(choices))))
        except:
            print("Wrong input")
            sport_choice = -1
            continue

        if sport_choice < 1 or sport_choice > len(choices):
            input("Invalid option given...")
            continue

    student_schedule = StudentSchedule(student_id,choices[sport_choice - 1])

    registered_student_sport_preference_file = open("./student/registered_student_sport.txt","a")
    registered_student_sport_preference_file.write(student_schedule.file_format())
    registered_student_sport_preference_file.close()

    data = details[sport_choice - 1][3:]
    data = data.split(" - ")
    return data[0] + " - " + data[2] + " - " + data[3] + " - " + data[4] + " - " + data[5] + " - " + data[6]