class SportCenter:
    sport_center_id = ""
    sport_center_name = ""
    sport_center_address = ""

    def __init__(self,sport_center_id,sport_center_name,sport_center_address):
        self.sport_center_id = sport_center_id
        self.sport_center_name = sport_center_name
        self.sport_center_address = sport_center_address
    
def read_all_sport_centers():
    sport_centers_file = open("./sport_center/sport_centers.txt","r")
    sport_centers = sport_centers_file.readlines()
    sport_centers_file.close()

    temp = []
    for sport_center in sport_centers:
        sport_center_data = sport_center.rstrip().split("#")
        temp.append(SportCenter(sport_center_data[0],sport_center_data[1],sport_center_data[2]))
    
    return temp

def search_sport_center_by_id(sport_centers,sport_center_id):
    for sport_center in sport_centers:
        if sport_center.sport_center_id == sport_center_id:
            return sport_center
    return None