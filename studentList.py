"""
    Joy Lyka Buangjug
    7:30-9:00AM
    14092
    Student List
    --------------------
    1. Add Student
    2. Find Student
    3. Delete Student
    4. Update Student
    5. Display All Student
    0. Quit/End
    ---------------------
    Enter Option(0..5):
    * Provide functionality for each option
    * use 'student.txt' as filename 
    * store the structure of the student dictionary(key-value pair )
    
    student = {
        'idno':'0001',
        'lastname':'durano',
        'firstname':'dennis',
        'course':'bscpe',
        'level':'4',
    }
"""
from os import system,path

filename:str = "student.txt"

def addStudent()->None: 
    system("cls")
    if path.exists(filename):
        student:dict = {
            'idno': input("Enter ID number: "),
            'lastname': input("Enter last name: "),
            'firstname': input("Enter first name: "),
            'course': input("Enter course: "),
            'level': input("Enter year level: ")
        }
        with open(filename, 'a') as file: #used 'a' for append mode, 'with' statement for properly closing the file
            file.write(','.join(student.values()) + '\n') #writing the data as comma separated string (getting from student:dict values())
            print("Student data written to file successfully.")
    else:
        print(f"Unable to write to file/{filename} not exists...")

def findStudent()->None:
    system("cls")
    if path.exists(filename):
        idno = input("Enter ID Number of student to find: ")
        found:bool = False
        file = open(filename)
        for student in file:
            fields:list = student.split(',')
            if fields[0] == idno:
                print(f"Student ID {idno} is found!")
                found = True
                break
        if not found:
            print(f"Student ID {idno} is not found!")
        file.close()
    else:
        print(f"Unable to find/{filename} not exists...")

def deleteStudent()->None:
    system("cls")
    if path.exists(filename):
        idno = input("Enter ID Number of student to delete: ")
        found:bool = False
        temp_data:list = list() #temoporary store the data of those student data that doesnt match 
        file = open(filename)
        for student in file:
            fields:list = student.split(',')
            if fields[0] == idno:
                found = True
            else:
                temp_data.append(student) #adding the students that doesn't match to the one that's been deleted (idno)
        if found:
            with open(filename, 'w') as file: #used 'w' to write and 'with' statement to make sure the file is closed properly
                for student in temp_data:
                    file.write(student) #rewriting the file student data without the deleted student
                print(f"Student ID {idno} data deleted successfully.")
        else: 
            print(f"Student ID {idno} not found! There's nothing to delete...")
        file.close()
    else:
        print(f"Unable to delete/{filename} not exists...")
       
def updateStudent()->None:
    system("cls")
    if path.exists(filename):
        idno = input("Enter ID Number of student to update: ")
        found:bool = False
        temp_data:list = list()
        file = open(filename)
        for student in file:
            fields:list = student.strip().split(',') #strip() -> remove leading and trailing whitespaces (spaces, tabs, newlines)
            if fields[0] == idno:
                found = True
                fields[1] = input("Enter New Last Name: ")
                fields[2] = input("Enter New First Name: ")
                fields[3] = input("Enter New Course: ")
                fields[4] = input("Enter New Level: ")
            temp_data.append(','.join(fields) + '\n') #adding the updated or unchanged student data (comma separated string)   
        if found:
            with open(filename, 'w') as file: 
                file.writelines(temp_data) #rewriting the udated data back to the file
            print(f"Student ID {idno} information updated successfully.")
        else: 
            print(f"Student ID {idno} not found! There's nothing to update...")
    else:
        print(f"Unable to update/{filename} not exists...")
    
def displayAllStudent()->None:
    system("cls")
    if path.exists(filename):
        print("Displaying All Student Data:")
        file = open(filename)
        for student in file:
            fields:list = student.split(",")
            print("IDNO      :",format(fields[0]))
            print("LASTNAME  :",format(fields[1]))
            print("FIRSTNAME :",format(fields[2]))
            print("COURSE    :",format(fields[3]))
            print("LEVEL     :",format(fields[4]))
            print()
        file.close()
    else: print(f"{filename} not found!")

def end()->None:
    print("Program End...")
    
def displayMenu()->None:
    system("cls")
    menu:list = [
        "Student List",
        "--------------------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All Student",
        "0. Quit/End",
        "---------------------"
    ]
    [print(list) for list in menu]

def main()->None:
    option:int = -1
    menuItems:dict = {
        1:addStudent,
        2:findStudent,
        3:deleteStudent,
        4:updateStudent,
        5:displayAllStudent,
        0:end,
    }
    while option != 0:
        try:
            displayMenu()
            option = int(input("Enter Option(0..5):"))
            menuItems.get(option)()
        except:
            print("Please enter only from 0 to 5")
        input("Press any key to continue...")

if __name__ == "__main__":
    main()