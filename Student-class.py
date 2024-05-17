# This is a main module for Student-class.py
# Student-class.py
# CSC-121
# Christian Mcfadden

"""
Student-class.py ----|
                      | - StudentInfo.csv
                      | - function.py
                      | - student.py
                      |
                      |-----------------Output-(Reports)----|
                                                            |
                                                            |----------stu_accounts.txt
                                                            |----------student_accounts.csv
"""

from function import *

def main():
    while True:
        option = menu()
        if option == 1:
            student_registry = read_content()
            write_report(student_registry)
            #main()
        
        elif option == 2:
            student_registry = read_content()
            student_registry = add_record(student_registry)
            write_report(student_registry)
            #main()

        elif option == 3:
            student_registry = read_content()
            student_registry = delete_record(student_registry)
            write_report(student_registry)
            #main()

        elif option == 4:
            student_registry = read_content()
            search_lname(student_registry)
            #main()

        elif option == 5:
            student_registry = read_content()
            search_id(student_registry)
            #main()

        elif option == 6:
            print('Program has ended!')
            break
            #main()

        else:
            print("Invalid response")
            print('Program will restart')
            #main()
    
if __name__ == "__main__":
    main()