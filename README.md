SmartGate: A Multi-Factor Login System for Campus Security
	SmartGate is a Python-based campus access monitoring system designed to improve security within the Philippine Science High School CALABARZON Campus in Batangas City. It replaces traditional logbooks and gate passes with a structured digital system that monitors and verifies the entry and exit of students, staff, and visitors, ensuring individual safety.

	The system uses multi-factor authentication, combining password verification and LRN-based recovery along with admin controls to ensure that only authorized personnel can access the campus’s facilities.

Notice: This project is not affiliated with any official institute or external system and is exclusively an academic project. All features and assets were created for educational purposes.

Objectives:
Track campus entry and exit accurately
Strengthen authorization and identity verification
Provide password recovery options
Have detailed activity logs
Enhance overall campus security

Features:
Password Authentication
LRN-Based REcovery
Time Monitoring
Admin controls
Activity Logs
Role-based system

Purpose:
	The project addresses the issue of inconsistent and insufficient campus logging systems. By programming access records and implementing verification layers, SmartGate aims to 
Improve campus safety
Prevent unsafe entry
Ensure accurate monitoring on the campus
Support admin decision-making

Requirements:
	Programming Language: Python
	Libraries: Standard Python Library, datetime

How It Works:
	How to run the program
Install Python on the device
Open the folder containing the program file
Run the script using a terminal or command prompt

Program Interaction Flow:
System asks for the action (Enter/Exit)
Enter if entering the campus
Exit if leaving the campus
The user is asked to provide their password
If correct, the system proceeds to the identity verification
If incorrect, the system offers a recovery option using LRN
The identity verification requires the confirmation of the following:
Full name
Birthday
Role (Student/Staff)
Grade Level (if applicable)
Section or class details (for students)
Once the user is verified, the system records the following:
User identity
Entry/Exit Status
Exact timestamp of the transaction
After completing the process, the system returns to the main menu for the next user.

Keywords for test cases:
Students:
Names: “A”, “B”
Roles: “student/intern”, “student/extern.”
Birthdays: “06102012”,”23042012”
Passwords: “password”,”012345.6.”
Grade Levels: “8”, “8”
Sections: “Waling”, “Waling”
Section numbers: “204”, “204”
Class Numbers: “01”, “67”

Staff:
	Names: “Guard”, “Frontman”
Roles: “teacher/intern.”
Birthdays: “27011984”
Passwords: “twunc”







Legend: I = Input. O = Output. # for comments

Sample Input and Output

O: Type 'enter' if you are entering or type 'exit' if you are exiting the campus: 
I: enter
O: Please enter your password:
I: twunc #This password accesses the admin controls

O:
—Admin Controls—
0 - Add a person 
1 - Remove a person 
2 - Manually enter 
3 - Chelogin ilogoutut time 
Choice:

I: 3
O: Enter the student's/staff's name to see their login/logout time:
I: A

O: 
Name: A 
Role: student/intern 
Birthday: 06102012 
Grade and Section: 8 - Waling
Login time: No login record found
Do you NOT want to search for another person? (Y/N):

I: Y

Team Members:
	Aquino, Yuri
	Fajilan, Joaquin
	Balondo, Gabby
	Macasaet, Athens
	Batecan, Xie

Acknowledgements:
	This project was developed as part of Computer Science 2 under the guidance of Ms. Marbecel Florida at the Philippine Science High School CALABARZON Campus in Batangas City.

License:
	This project is for educational purposes only.

