#University System Display infomation of
#Classes: Person (parent), and subclasses Student, Lecturer, Staff.
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")
        
        # Allows updating email
    def update_email(self, new_email):
        print(f"Updating email for {self.name} from {self.email} to {new_email}")
        self.email = new_email
        print("Email updated successfully.")
        
 #Subclass for Student
class Student(Person):
    def __init__(self, name, age, email, student_id, major, enrollment_year):
        super().__init__(name, age,email)
        self.student_id = student_id
        self.major = major
        self.courses_enrolled = []
        self.GPA = 0.0  # Default GPA
        self.enrollment = enrollment_year
        
      
    #Stydent enroll for course  
    def enroll_course(self, course_name):
        if course_name not in self.courses_enrolled:
            self.courses_enrolled.append(course_name)
            print(f"{self.name} enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")
            
    #Student drop course    
    def drop_course(self, course_name):
    
        if course_name in self.courses_enrolled:
            self.courses_enrolled.remove(course_name)
            print(f"{self.name} dropped {course_name}.")
        else:
            print(f"{course_name} not found in {self.name}'s enrolled courses.")
        
    #Student update GPA    
    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        print(f"{self.name}'s GPA updated to {self.gpa}.")


    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Enrollment Year: {self.enrollment}")
        print(f"Major: {self.major},")
        print(f"Courses Enrolled: {', '.join(self.courses_enrolled) if self.courses_enrolled else 'None'}, GPA: {self.GPA:.2f}")
      
# Subclass for Lecturer  
class Lecturer(Person):
    def __init__(self, name, age,email, staff_id, department):
        super().__init__(name, age, email)
        self.staff_id = staff_id
        self.department = department
        self.courses_taught = []
        
    #Lecturer assign course
    def assign_course(self, course_name):
        if course_name not in self.courses_taught:
            self.courses_taught.append(course_name)
            print(f"{self.name} assigned to teach {course_name}.")
        else:
            print(f"{self.name} is already assigned to {course_name}.")

    #Lecturer remove course
    def remove_course(self, course_name):
        if course_name in self.courses_taught:
            self.courses_taught.remove(course_name)
            print(f"{self.name} no longer assigned to {course_name}.")
        else:
            print(f"{course_name} not found in {self.name}'s assigned courses.")
        
    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Department: {self.department}")
        print(f"Courses Taught: {', '.join(self.courses_taught) if self.courses_taught else 'None'}")
        
#Subclass for Staff
class Staff(Person):
    def __init__(self, name, age, email, staff_id, department, role):
        super().__init__(name, age, email)
        self.staff_id = staff_id
        self.department = department
        self.role = role
        
        #Task of the staff member
    def perform_task(self, task_description):
        print(f"{self.role} {self.name} {task_description}")
        
    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}, Department: {self.department}, Role: {self.role}")
        
# Create instances of each class
student = Student("Naluyinda Moureen Renitah",21,"naluyinda@gmail.com",2300714122,"BSSE",2023,)
lecturer = Lecturer("Mukiibi Rodgers",55,"mukiibi@gmail.com","SI44552","Networks") 
staff = Staff("Kasibante John",45,"kasibante@gmail.com","SI44552","Administration","Registrar")

# Displaying information
print("University System Information:\n")
student.display_info()

print("\n")

lecturer.display_info()
print("\n")

staff.display_info()

print("\n")
# Demonstrating functionality
student.enroll_course("Data Structures")
student.enroll_course("Algorithms")
student.enroll_course("Database Systems")
student.drop_course("Algorithms")
student.update_gpa(3.8)
student.update_email("nalumoureen@gmail.com")

print("\n") 

lecturer.assign_course("Data Structures")
lecturer.assign_course("Algorithms")
lecturer.remove_course("Algorithms")

print("\n") 

staff.perform_task("Manages student records")

print("\n")

# Displaying updated information
student.display_info()

print("\n")

lecturer.display_info()
print("\n")

staff.display_info()