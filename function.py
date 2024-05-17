# This is a function module for final_mcfaddec that contains all the functions needed to work correctly
# function.py
# CSC-121
# Christian Mcfadden

from student import Student
import csv

def menu():
    print("--------------Menu-----------------------------------")
    print("1) Read Student Info and Create Class Objects/Instances")
    print("2) Add a New Student Record")
    print("3) Delete a Student Record (set to inactive)")
    print("4) Search for Student by Last Name")
    print("5) Search for Student by Id")
    print("6) Exit")
    print("")
    print("---------------------------------------------------------")
    print('')
    while True:
        try:
            option = int(input("Please choose one of the options above (1-6): "))
            print('------------------------------------------------')
            if 1 <= option <= 6:
                return option
            else:
                print("Invalid option! Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a valid option.")

def read_content():
    student_registry = []
    #reads student.csv row by row and creates a list in a list to store the info
    data = []
    with open('Studentinfo.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
                # Add each row to a list but create an instance
            if row[0].lower() != 'last Name':
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                temp.append(row[2])
                data.append(temp)
        data.pop(0)
        for i in data:
            student1 = Student(i[2], i[1], i[0])
            student_registry.append(student1)
            
    return student_registry


def write_report(student_registry):
    print('------------------------------------------------')
    print('CSV and text Reports Created')
    print('------------------------------------------------')
    print('')
    print(student_registry)
    #moved print iteration of instances here.
    for i in student_registry:
        print(i)
    try:
        # this function also needs to send info to a text file and to a csv file  
        with open('student_accounts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'First', 'Last', 'Login', 'Email', 'Active'])
            for i in student_registry:
                writer.writerow([i.id, i.first, i.last, i.login, i.email, i.active])
        with open('stu_accounts.txt', 'w') as txt_file:
            txt_file.write('             Student Login Information\n')
            txt_file.write('{}       {}    {}       {}             {}                      {}\n'.format('Last', 'First', 'ID Num', 'Login', 'Email', 'Active'))
            for j in student_registry:
                txt_file.write('{}       {}    {}    {}    {}       {}\n'.format(j.last, j.first, j.id, j.login, j.email, j.active))          
    except IOError:
        print('An error occurred while writing reports.')

def add_record(student_registry):
    while True:
        try:
            #add list to list of data 
            search = int(input('What is the Student ID: '))
            for i in student_registry:
                if int(i.id) == search:
                    print('Student ID is already in Registry')
                    print('Try Again. Please!')
                    break
                    #add_record(student_registry)
            else:
                first = input('What is the first name: ')
                last = input('What is the last name: ')
                student2 = Student(str(search), first, last)
                student_registry.append(student2)
                print('Record Added to Registry')
                return student_registry
        except ValueError:
            print('Invalid input! Please enter a valid Student ID.')

def delete_record(student_registry):
    try:
        # ask for id and search for student then set active() to false 
        search = int(input('What is the Student ID: '))
        for i in student_registry:
            if int(i.id) == search:
                # setting user.set_active() == false
                i.active = False
                print(f'User with the id : {i.id} has been deactivated')
                print()
                return student_registry   
        print('Student ID is NOT in Registry')
        print('Try Again. Please!')
        delete_record(student_registry) 
    except ValueError:
        print('Invalid input! Please enter a valid Student ID.')
    
def search_lname(student_registry):
    try:
        #search list for last name
        search = input("What is the Student's last name: ")
        for i in student_registry:
            if i.last.lower() == search.lower():
                print(i)
                print()
                return
        print('Student ID is NOT in Registry')
        print('Try Again. Please!')
        #search_lname(student_registry)
    except:
        print('An error occurred while searching by last name.')
        print()

def search_id(student_registry):
    try:
        #search list for id
        search = int(input('What is the Student ID: '))
        for i in student_registry:
            if int(i.id) == search:
                print(i)
                print()
                return
        print('Student ID is NOT in Registry')
        print('Try Again. Please!')
        #search_id(student_registry)
        print()
    except ValueError:
        print('Invalid input! Please enter a valid Student ID.')