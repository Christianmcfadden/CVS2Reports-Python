# this is a class for student for final_mcfaddec.py
# student.py
# CSC- 121
# Christian Mcfadden

class Student:
    def __init__(self, id, first, last):
        self.id = id
        self.first = first
        self.last = last
        self.login = self.set_login()
        self.email = self.set_email()
        self.active = True

    def set_login(self):
        # first 5 of last name and and last 3 of student id 
        # if last name is less then 5 add all of it (len())
        lname = self.last[:5].lower()
        student_id = str(self.id)[-3:]
        login = lname + student_id
        return login

    def set_email(self):
        # uses login and adds it to '@student.faytech.edu'
        email = self.login + '@student.faytech.edu'
        return email
    
    def set_active(self):
        self.active = True
        
    def __repr__(self):
        #repr should return a string that refrences values refrenced in all the attributes
        return f"Student(id={self.id}, first={self.first}, last={self.last}, login={self.login}, email={self.email}, active={self.active})"



        

    
    
    
