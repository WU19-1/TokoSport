class Rating:
    rating_id = ""
    coach_id = ""
    student_id = ""
    rating = 0

    def __init__(self,rating_id,student_id,coach_id,rating):
        self.rating_id = rating_id
        self.student_id = student_id
        self.coach_id = coach_id
        self.rating = rating

    def file_format(self):
        return "%s#%s#%s#%d\n"%(self.rating_id,self.student_id,self.coach_id,self.rating)


def add(student_id,coach_id,rating):
    # cari tahu seberapa banyak rating yang sudah dikasi untuk menentukan idnya
    rating_file = open("./rating/rating.txt","r")
    count = len(rating_file.readlines()) + 1
    rating_file.close()
    rating_id = "RA%.6d"%(count)
    
    rating = Rating(rating_id,student_id,coach_id,rating)

    rating_file = open("./rating/rating.txt","a")
    rating_file.write(rating.file_format())
    rating_file.close()
    
