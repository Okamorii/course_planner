import sys

class Teacher:
    def __init__(self, name, position, total_hours, weekly_hours):
        self.name: str = name
        self.assigned_hours: int = 0
        self.total_hours: int = total_hours
        self.weekly_hours: int = weekly_hours
        self.position: str = position

    def add_hours(self, hours):
        if self.assigned_hours + hours <= self.total_hours:
            if self.assigned_hours + hours <= self.weekly_hours:
                self.assigned_hours += hours
                print('Hours added.') 
            else: print('The Teacher already has too much hours this week. ')
        else: 
            print('The Teacher already has too much hours. ')
        return self.assigned_hours

class Course:
    def __init__(self, name, year, promotion, semester, LC_hours, IC_hours, EX_hours, PW_hours):
        self.name: str = name
        self.year: str = year #the student year L1 L2 etc..
        self.promotion: str = promotion # [CE, GE, PE, CS]
        self.LC_hours: int = LC_hours
        self.IC_hours: int = IC_hours
        self.EX_hours: int = EX_hours
        self.PW_hours: int = PW_hours





def get_hours_input():
    while True:
        try:
            hours: int = int(input('How Much Hours: ').strip())
            if hours >= 0: return hours
            else: print('The Value must be a positive integer witout unit, ex: "20" for a 20 hours service.')
        except:
            TypeError
            print('Please enter a valid number.')

def get_course_input(courses: list[Course]) -> Course:
    while True:
        try:
            course_name: str = input('Name of the Course: ').strip().upper()
            for course in courses:
                if course.name.upper() == course_name: 
                    return course
            else: 
                print("This Course doesn't exist.")
        except:
            Exception
            print('Please enter a valid name.')


def main():
    my_teacher: object = Teacher("Maxime", "Local", 380, 20)
    courses: list = [Course("AOM_1", "L1",["CE", "PE", "GE", "CS"], 1, 12, 0, 12, 0),Course("AOM_2", "L1",["CE", "PE", "GE"], 1, 15, 0, 15, 0)]
    
    course: object = get_course_input(courses)  
    hours: object = get_hours_input()
    print(f'{my_teacher.name} has {my_teacher.assigned_hours} to {course.name}')


        

if __name__ == "__main__":
    main()