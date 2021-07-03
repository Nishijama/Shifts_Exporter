#a simple program that allows users to simply paste their shifts from
#excel/google-sheets/box-sheets and generate csv file to import into their
#calendar, it's pre-defined for shifts specific to my current needs

import re
import subprocess
import sys


YEAR = "2021"

#get input from the user
month = input("Please enter month in number format (e.g., '07' for June):\n")
shifts = input("Please paste your shifts:\n")

#remove whitespaces and split input into a list
shifts = re.sub('\\s+', ' ', shifts)
shifts_list = shifts.split(' ')

#pre-defined shifts for my current use
headers = "Subject, Start Date, Start Time, End Date, End Time, Description, Private\n"
start_times = ["6:30", "7:30", "6:30", "9:00", "10:00"]
end_times = ["15:00", "16:00", "17:00", "17:30", "18:30"]
subjects = ["Early 🌼", "Office 👔", "10h 👷", "Middle 🌻", "Late 🦉"]

f = open("shifts.csv", 'w')

#print output to the console and to the csv file at the same time
print(headers)
f.write(headers)

for day, shift in enumerate(shifts_list):
    description = shift
    date = str(day+1) + "." + month + "." + YEAR
    if shift == "Int-ES1":
        print(subjects[0] + ', ' + date +', ' + start_times[0] + ', ' + date + ', ' + end_times[0] + ', ' + description + ', ' + "TRUE\n")
        f.write(subjects[0] + ', ' + date +', ' + start_times[0] + ', ' + date + ', ' + end_times[0] + ', ' + description + ', ' + "TRUE\n")

    if shift == "Int-ES2":
        print(subjects[1] + ', ' + date +', ' + start_times[1] + ', ' + date + ', ' + end_times[1] + ', ' + description + ', ' + "TRUE\n")
        f.write(subjects[1] + ', ' + date +', ' + start_times[1] + ', ' + date + ', ' + end_times[1] + ', ' + description + ', ' + "TRUE\n")

    if shift == "IntES3":
        print(subjects[2] + ', ' + date +', ' + start_times[2] + ', ' + date + ', ' + end_times[2] + ', ' + description + ', ' + "TRUE\n")
        f.write(subjects[2] + ', ' + date +', ' + start_times[2] + ', ' + date + ', ' + end_times[2] + ', ' + description + ', ' + "TRUE\n")

    if shift == "MS":
        print(subjects[3] + ', ' + date +', ' + start_times[3] + ', ' + date + ', ' + end_times[3] + ', ' + description + ', ' + "TRUE\n")
        f.write(subjects[3] + ', ' + date +', ' + start_times[3] + ', ' + date + ', ' + end_times[3] + ', ' + description + ', ' + "TRUE\n")

    if shift == "Int-LS1":
        print(subjects[4] + ', ' + date +', ' + start_times[4] + ', ' + date + ', ' + end_times[4] + ', ' + description + ', ' + "TRUE\n")
        f.write(subjects[4] + ', ' + date +', ' + start_times[4] + ', ' + date + ', ' + end_times[4] + ', ' + description + ', ' + "TRUE\n")


print("Your shifts have been successfully saved to a CSV file. You can now import it to your calendar :)")
f.close()

#open the location where the file was saved
#this part of code is taken from stackoverflow and user Cas
def open_folder(path):
    if sys.platform == 'darwin':
        subprocess.check_call(['open', '--', path])
    elif sys.platform == 'linux2':
        subprocess.check_call(['gnome-open', '--', path])
    elif sys.platform == 'win32':
        subprocess.check_call(['explorer', path])

open_folder(path=".")  # open current directory
