# AA of da Nerd Clusters :D
# This program is a password recognition system that allows
# students and staff to log in or out of the campus.
# It also includes admin controls and password recovery via LRN.

import datetime
from zoneinfo import ZoneInfo

# =========================
# DATA STORAGE (USING DICTIONARIES)
# =========================

slist = [
    {"id": 1000, "name": "Guard, Frontman", "role": "teacher/intern", "bday": "27011984", "password": "twunc"}
]

students = [
    {"id": 0, "name": "A", "role": "student/intern", "bday": "06102012", "password": "password",
     "grade": "8", "section": "Waling", "sectno": "204", "classno": "01"},
    {"id": 1, "name": "B", "role": "student/extern", "bday": "23042012", "password": "0123456",
     "grade": "8", "section": "Waling", "sectno": "204", "classno": "67"}
]

time_entered = {}
time_exited = {}

inside_status = {}  # True = inside, False = outside

# temp vars
tname = ""
trole = ""
tbday = ""
tgrade = ""
tsect = ""
idno = -1
yn2 = "N"
idno = -1
yn2 = "N"

# =========================
# UNIVERSAL SAFE INPUT
# =========================

def safe_input(prompt, type_=str, allowed=None, length=None, numeric=False):
    while True:
        try:
            val = input(prompt).strip()

            if val == "":
                raise ValueError("Input cannot be empty.")

            if type_ == int:
                val = int(val)

            if numeric and not val.isdigit():
                raise ValueError("Must be numbers only.")

            if length and len(val) != length:
                raise ValueError(f"Must be exactly {length} characters.")

            if allowed and str(val).lower() not in allowed:
                raise ValueError("Invalid choice.")

            return val

        except Exception as e:
            print(f"Error: {e}")

# =========================
# TIME TRACKING FUNCTION
# =========================
def time_check(action, user_id):
    if user_id == -1:
        return False  # invalid user safeguard

    current_time = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p")

    # Ensure user has a status
    if user_id not in inside_status:
        inside_status[user_id] = False

    # =========================
    # ENTER VALIDATION
    # =========================
    if action == "enter":
        if inside_status[user_id] == True:
            print("⚠️ Warning: You are already inside the campus. Entry denied.\n")
            return False

        time_entered.setdefault(user_id, []).append(current_time)
        inside_status[user_id] = True
        return True

    # =========================
    # EXIT VALIDATION
    # =========================
    elif action == "exit":
        if not inside_status[user_id]:
            print("⚠️ Warning: No entry record found. Cannot exit.\n")
            return False

        if user_id not in time_exited:
            time_exited[user_id] = []
        time_exited[user_id].append(current_time)

        inside_status[user_id] = False
        return True

# =========================
# PASSWORD AUTHENTICATION
# =========================
def pswd_enter():
    global yn2, tname, trole, tbday, tgrade, tsect, idno

    tname = trole = tbday = tgrade = tsect = "0"
    idno = -1
    yn2 = "N"

    pawd = safe_input("Please enter your password: ")

    # =========================
    # STUDENT PASSWORD CHECK
    # =========================
    for s in students:
        if pawd == s["password"]:
            idno = s["id"]
            tname, trole, tbday = s["name"], s["role"], s["bday"]
            tgrade, tsect = s["grade"], s["section"]
            return "student"

    # =========================
    # STAFF PASSWORD CHECK
    # =========================
    for s in slist:
        if pawd == s["password"]:
            idno = s["id"]
            tname, trole, tbday = s["name"], s["role"], s["bday"]

            yn1 = safe_input(
                "0 - Add a person \n1 - Remove a person \n2 - Manually enter \n3 - Check log in/log out time \n4 - Exit Admin Menu\nChoice: ",
                int
            )

            # =========================
            # ADD PERSON
            # =========================
            if yn1 == 0:
                sos = safe_input("0 - Student \n1 - Staff \nChoice: ", int)

                nname = safe_input("Enter the student/staff's name: ").title()
                npawd = safe_input("Enter the student/staff's password: ")
                nbday = safe_input("Enter the student/staff's birthday: ", numeric=True, length=8)
                nrole = safe_input("Enter the student/staff's role: ").lower()

                if sos == 0:
                    if nrole not in ["student/intern", "student/extern"]:
                        print("Error: Invalid student role.")
                        return "staff"

                    ngrade = safe_input("Enter grade: ", numeric=True)
                    nsect = safe_input("Enter section name: ")
                    nsectno = safe_input("Enter section number: ")
                    nclassno = safe_input("Enter class number: ")

                    new_id = max([x["id"] for x in students] + [0]) + 1

                    students.append({
                        "id": new_id, "name": nname, "role": nrole,
                        "bday": nbday, "password": npawd,
                        "grade": ngrade, "section": nsect,
                        "sectno": nsectno, "classno": nclassno
                    })

                elif sos == 1:
                    if nrole not in ["teacher/intern", "teacher/extern", "custodian"]:
                        print("Error: Invalid staff role.")
                        return "staff"

                    new_id = max([x["id"] for x in slist] + [999]) + 1

                    slist.append({
                        "id": new_id, "name": nname,
                        "role": nrole, "bday": nbday, "password": npawd
                    })

                print("User added successfully!")
                return "staff"

            # =========================
            # REMOVE PERSON
            # =========================
            elif yn1 == 1:
                rid = safe_input("Enter ID: ", int)
                sos2 = safe_input("0 - Student \n1 - Staff\nChoice: ", int)

                if sos2 == 0:
                    before = len(students)
                    students[:] = [x for x in students if x["id"] != rid]
                    print("Removed." if len(students) < before else "ID not found.")
                else:
                    before = len(slist)
                    slist[:] = [x for x in slist if x["id"] != rid]
                    print("Removed." if len(slist) < before else "ID not found.")

                return "staff"

            # =========================
            # MANUAL ENTRY 
            # =========================
            elif yn1 == 2:
                while True:
                    tname = safe_input("Enter the name of the student: ").title()
                    trole = safe_input("Enter the role of the student: ").lower()
                    tbday = safe_input("Enter the birthday of the student: ", numeric=True, length=8)
                    tidno = safe_input("Enter the ID no. of the student: ", int)

                    for st in students:
                        if st["id"] == tidno and st["name"] == tname and \
                           st["role"] == trole and st["bday"] == tbday:
                            idno = tidno
                            print("Manual entry successful.")
                            return "staff"

                    print("Incorrect details. Try again.")

            # =========================
            # VIEW LOGS
            # =========================
            elif yn1 == 3:
                while True:
                    search = safe_input("Enter name: ").title()
                    found = False

                    for st in students + slist:
                        if st["name"] == search:
                            uid = st["id"]
                            print(f"\nName: {st['name']}")
                            print(f"Role: {st['role']}")
                            print(f"Login: {time_entered.get(uid) or 'No record'}")
                            print(f"Logout: {time_exited.get(uid) or 'No record'}")
                            found = True

                    if not found:
                        print("Name not found.")

                    stop = safe_input("Stop searching? (Y/N): ", allowed=["y","n"]).upper()

                    if stop == "Y":
                        break  

                print("Noted!")
                return "staff"   
                
            elif yn1 == 4:
                print("Noted!")
                return "staff"
            
            else:
                print("Invalid admin choice.")
                return "staff"

    # =========================
    # INVALID PASSWORD
    # =========================
    # ========================= 
    print("The password you placed does not match any passwords in our database.")

    yn2 = safe_input("Do you want to use your LRN? (Y/N): ", allowed=["y","n"]).upper()

    # =========================
    # LRN RECOVERY  
    # =========================
    if yn2 == "Y":
        while True:
            lrn_input = safe_input("Enter your LRN: ")

            if len(lrn_input) != 13:
                print("Invalid LRN length. Must be 13 digits.")
                continue

            clsno = lrn_input[0:2]
            secno = lrn_input[2:5]
            bday = lrn_input[5:13]

            for student in students:
                if (student["classno"] == clsno and
                    student["sectno"] == secno and
                    student["bday"] == bday):

                    idno = student["id"]
                    tname = student["name"]
                    trole = student["role"]
                    tbday = student["bday"]
                    tgrade = student["grade"]
                    tsect = student["section"]

                    print("LRN recovery successful!")
                    return "student"

            print("Invalid LRN. Try again.")
# =========================
# MAIN PROGRAM LOOP
# =========================
print("=====PASSWORD RECOGNITION SYSTEM=====")

while True:

    # =========================
    # STEP 1: ACTION (ENTER / EXIT)
    # =========================
    useract = safe_input(
        "Type 'enter' if you are entering or type 'exit' if you are exiting the campus: ",
        allowed=["enter", "exit"]
    )

    # =========================
    # STEP 2: AUTHENTICATION
    # =========================
    result = pswd_enter()

    # =========================
    # HANDLE EXIT FIRST
    # =========================
    if useract == "exit":
        success = time_check("exit", idno)

        if success:
            print("Exit recorded successfully!\n")
            print("Goodbye. You are exiting the campus.")
        else:
            print("Exit not recorded.\n")

        continue

    if result is None:
        print("Authentication failed. Please try again.\n")
        continue

    # =========================
    # STEP 3: HANDLE MANUAL MODE
    # =========================
    if result == "manual":
        print("Manual entry completed. Returning to main menu.\n")
        continue

    # =========================
    # STEP 4: CONFIRM ONLY REAL USERS
    # =========================
    if result in ["student", "staff"]:

        confirm = safe_input(
            f"\nIs this you?\n"
            f"Name: {tname}\n"
            f"Role: {trole}\n"
            f"Birthday: {tbday}\n"
            + (f"Grade and Section: {tgrade} - {tsect}\n" if "student" in trole else "")
            + "(Y/N): ",
            allowed=["y", "n"]
        ).upper()
    
        if confirm == "N":
            print("Identity rejected. No time recorded.\n")
            continue
    
        # ONLY runs if YES
        success = time_check(useract, idno)

        if success:
            print("Time recorded successfully!\n")
        else:
            print("Time not recorded.\n")
            continue
    
        # =========================
        # STEP 6: RESTART OPTION
        # =========================
        
        again = safe_input("Do you want to start again? (Y/N): ", allowed=["y", "n"]).upper()
        if again == "N":
            break


# =========================
# FINAL TABLE
# =========================
print("\n===== CAMPUS LOGIN/LOGOUT RECORDS =====")
print(f"{'ID':<6}{'Name':<20}{'Role':<20}{'Entry Time':<25}{'Exit Time':<25}")
print("-"*100)

for s in students + slist:
    uid = s["id"]
    name = s["name"]
    role = s["role"]

    enters = time_entered.get(uid, [])
    exits = time_exited.get(uid, [])

    max_len = max(len(enters), len(exits))

    if max_len == 0:
        print(f"{uid:<6}{name:<20}{role:<20}{'No record':<25}{'No record':<25}")
        continue

    for i in range(max_len):
        enter_time = enters[i] if i < len(enters) else "—"
        exit_time = exits[i] if i < len(exits) else "—"

        print(f"{uid:<6}{name:<20}{role:<20}{enter_time:<25}{exit_time:<25}")
