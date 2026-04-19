# AA of da Nerd Clusters :D
# This program is a password recognition system that allows
# students and staff to log in or out of the campus.
# It also includes admin controls and password recovery via LRN.

import datetime
from zoneinfo import ZoneInfo

# =========================
# DATA STORAGE (USING DICTIONARIES)
# =========================

# Lists for the Staff
slist = [
    {"name": "Guard, Frontman", "role": "Teacher/intern", "bday": "27011984", "password": "twunc"}
]

# Lists for the students
students = [
    {"name": "A", "role": "student/intern", "bday": "06102012", "password": "password",
     "grade": "8", "section": "Waling", "sectno": "204", "classno": "01"},
    {"name": "B", "role": "student/extern", "bday": "23042012", "password": "0123456",
     "grade": "8", "section": "Waling", "sectno": "204", "classno": "67"}
]

# Lists that store login and logout times
time_entered = {}
time_exited = {}

# Temporary variables used to store current user info
tname = "0"
trole = "0"
tbday = "0"
tgrade = "0"
tsect = "0"
idno = -1
secno = "0"
clsno = "0"
yn2 = "0"

# =========================
# TIME TRACKING FUNCTION
# =========================
def time_check(action, user_id):
    current_time = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p")
    if action == "enter":
        time_entered[user_id] = current_time
    elif action == "exit":
        time_exited[user_id] = current_time

# =========================
# PASSWORD AUTHENTICATION
# =========================
def pswd_enter():
    
    global yn2, tname, trole, tbday, tgrade, tsect, idno

    # Reset temporary variables
    tname = "0"
    trole = "0"
    tbday = "0"
    tgrade = "0"
    tsect = "0"
    idno = -1

    pawd = input("Please enter your password: ")

    # =========================
    # STUDENT PASSWORD CHECK
    # =========================
    for i, student in enumerate(students):
        if pawd == student["password"]:
            idno = i
            tname = student["name"]
            trole = student["role"]
            tbday = student["bday"]
            tgrade = student["grade"]
            tsect = student["section"]
            return "student"

    # =========================
    # STAFF PASSWORD CHECK
    # =========================
    for i, staff in enumerate(slist):
        if pawd == staff["password"]:
            idno = i
            tname = staff["name"]
            trole = staff["role"]

            # Staff/Admin menu
            yn1 = int(input("0 - Add a person \n1 - Remove a person \n2 - Manually enter \n3 - Check log in/log out time \nChoice: "))
            if yn1 == 0:
                sos = int(input("0 - Student \n1 - Staff \nChoice: "))
                nname = input("Enter the student/staff's name: ").title()
                npawd = input("Enter the student/staff's password: ")
                nbday = input("Enter the student/staff's birthday: ")
                nrole = input("Enter the student/staff's role: ").capitalize()
                if sos == 0:
                    ngrade = input("Enter grade: ")
                    nsect = input("Enter section name: ")
                    nsectno = input("Enter section number: ")
                    nclassno = input("Enter class number: ")
                    while nrole not in ["Student/extern", "Student/intern"]:
                        nrole = input("Enter your student's role again: ").capitalize()
                    students.append({
                        "name": nname, "role": nrole, "bday": nbday, "password": npawd,
                        "grade": ngrade, "section": nsect, "sectno": nsectno, "classno": nclassno
                    })
                else:
                    while nrole not in ["Teacher/extern", "Teacher/intern", "Custodian"]:
                        nrole = input("Enter your staff's role again: ").capitalize()
                    slist.append({"name": nname, "role": nrole, "bday": nbday, "password": npawd})
                return "staff"
            elif yn1 == 1:
                ridno = int(input("Enter the ID number of the student/staff you want to remove: "))
                sos2 = int(input("0 - Student \n1 - Staff\nChoice: "))
                if sos2 == 0 and 0 <= ridno < len(students):
                    removed = students.pop(ridno)
                    print(f"Removed student: {removed['name']}")
                elif sos2 == 1 and 0 <= ridno < len(slist):
                    removed = slist.pop(ridno)
                    print(f"Removed staff: {removed['name']}")
                return "staff"
            elif yn1 == 2:
                tname = input("Enter the name of the student: ").title()
                trole = input("Enter the role of the student: ").capitalize()
                tbday = input("Enter the birthday of the student: ")
                tidno = int(input("Enter the ID no. of the student: "))
                while True:
                    if 0 <= tidno < len(students) and tname == students[tidno]["name"] and \
                       trole == students[tidno]["role"] and tbday == students[tidno]["bday"]:
                        idno = tidno
                        return "staff"
                    else:
                        print("Incorrect details. Try again.")
                        tname = input("Enter the name of the student: ").title()
                        trole = input("Enter the role of the student: ").capitalize()
                        tbday = input("Enter the birthday of the student: ")
                        tidno = int(input("Enter the ID no. of the student: "))
            elif yn1 == 3:
                while True:
                    search = input("Enter the student's/staff's name to see their log in/log out time: ").title()
                    found = False
                    for i, student in enumerate(students):
                        if student["name"] == search:
                            print(f"Name: {student['name']} \nRole: {student['role']} \nBirthday: {student['bday']}"
                                  f"\nGrade and Section: {student['grade']} - {student['section']}"
                                  f"\nLogin time: {time_entered.get(i,'No login record')}")
                            found = True
                            break
                    for i, staff in enumerate(slist):
                        if staff["name"] == search:
                            print(f"Name: {staff['name']} \nRole: {staff['role']} \nBirthday: {staff['bday']}"
                                  f"\nLogin time: {time_entered.get(i,'No login record')}")
                            found = True
                            break
                    if not found:
                        print("Name not found.")
                    done = input("Do you NOT want to search another person? (Y/N): ").upper()
                    if done == "Y":
                        break
                return "staff"

    # =========================
    # INVALID PASSWORD
    # =========================
    print("The password you placed does not match any passwords in our database.")
    yn2 = input("Do you want to use your LRN? (Y/N): ").upper()
    return None

# =========================
# MAIN PROGRAM LOOP
# =========================
print("=====PASSWORD RECOGNITION SYSTEM=====")

while True:
    # Ask user if entering or exiting
    useract = input("Type 'enter' if you are entering or type 'exit' if you are exiting the campus: ").lower()

    # Ask for password
    result = pswd_enter()

    # If user wants LRN recovery
    if yn2 == "Y":
        while True:
            lrn_input = input("Enter your LRN: ")
            clsno = lrn_input[0:2]
            secno = lrn_input[2:5]
            tbday = lrn_input[5:13]

            # Search for student
            found = False
            for i, student in enumerate(students):
                if student["classno"] == clsno and student["sectno"] == secno and student["bday"] == tbday:
                    tname = student["name"]
                    trole = student["role"]
                    tgrade = student["grade"]
                    tsect = student["section"]
                    idno = i
                    found = True
                    print(f"Password recovered successfully for {tname}.")
                    break
            if found:
                break
            else:
                print("Invalid LRN. Try again.")

    # Authentication failed
    if idno == -1:
        print("Authentication failed. Please try again.\n")
        continue

    # Confirm identity
    yn3 = input(
        f"Is this you?: \n"
        f"Name: {tname} \n"
        f"Role: {trole} \n"
        f"Birthday: {tbday} \n"
        f"Grade and Section: {tgrade} - {tsect} \n"
        f"(Y/N): "
    ).upper()
    if yn3 == "N":
        print("Let's try again.\n")
        continue

    # Record time if correct
    if useract in ["enter", "exit"]:
        time_check(useract, idno)
        print("Time recorded successfully!\n")
    else:
        print("Invalid action. Please type 'enter' or 'exit'.\n")
        continue

    # Ask if user wants to restart
    yn4 = input("Do you want to start again? (Y/N): ").upper()
    if yn4 == "N":
        break

# =========================
# ATTENDANCE / LOGIN-LOGOUT TABLE
# =========================
print("\n===== CAMPUS LOGIN/LOGOUT RECORDS =====")
print(f"{'ID':<4}{'Name':<20}{'Role':<20}{'Login Time':<25}{'Logout Time':<25}")
print("-"*94)

# Show students
for i, student in enumerate(students):
    login = time_entered.get(i, "No record")
    logout = time_exited.get(i, "No record")
    print(f"{i:<4}{student['name']:<20}{student['role']:<20}{login:<25}{logout:<25}")

# Show staff
offset = len(students)  # Staff IDs after students
for i, staff in enumerate(slist):
    login = time_entered.get(i + offset, "No record")
    logout = time_exited.get(i + offset, "No record")
    print(f"{i + offset:<4}{staff['name']:<20}{staff['role']:<20}{login:<25}{logout:<25}")

print("\nSystem closed.")