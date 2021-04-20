#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    name = ""
    studentNumber = ""
    grade = 0
    courses = []
    grades = []

    # properties should be listed first

    def __init__(self, name, studentNumber, grade): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade
    '''
    def __del__():
        pass
    '''
    def average(self):
        sum = 0
        for g in self.grades:
            sum += g

        return sum/len(self.grades)

    def getHonorRoll(self):
        s = self.grades
        s.sort(reverse=True)
        sum = 0
        for g in s[:5]:
            sum += g
        a = sum / 5
        return a >= 86

    def showCourses(self):
        print(course)

    def showGrade(self, i : int):
        print(self.courses[i] + ":" + self.grade[i])

    def getCourses(self, l):
        for i in l:
            self.courses.append(i)

    def getGrades(self, l):
        for i in l:
            self.grades.append(i)







def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()