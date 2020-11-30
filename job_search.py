#!/usr/bin/python3

import csv
"""
This will create a document that allows me to update my job search
The spreadsheet will have fields for:
-----------------------------------------------
company | date applied | email | company site |
-----------------------------------------------
"""
jobApplied = {}

myFile = 'job_search.csv'

fieldnames = ["Company", "Date Applied", "Website", "Email"]

def usrQuest():
    while True:
        companyName = input("What is the name of the company ? :")
        dateApplied = input("When did you apply? : ")
        companySite = input("What is the company's website? : ")
        companyEmail = input("Email for company contact")

        #This sets key values for jobApplied dictionary
        jobApplied["Company"] = companyName
        jobApplied["Date Applied"] = dateApplied
        jobApplied["Website"] = companySite
        jobApplied["Email"] = companyEmail
        #Rows are stored as indexes.
        jobRow = {
            "Company": companyName,
            "Date Applied": dateApplied,
            "Website": companySite,
            "Email": companyEmail
            }

        csv_writer.writerow(jobRow)

        usrChoice = input("Do you want to add another? :")
        if usrChoice == 'y':
            continue
        elif usrChoice == 'n':
            break

def newDocument():
    global csv_writer
    with open(myFile,"w+") as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames)
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames) #allows us to write to file. We pass csv file as argument
        #header names
        usrQuest()

def update_CSV():
    global csv_writer
    with open(myFile,'a+',newline='') as update_obj:
        csv_writer = csv.DictWriter(update_obj, fieldnames = fieldnames)
        usrQuest()

print("Are you creating a new file updating an existing one?")

usr_choice = input("Enter 'N' for new document or 'U' to update existing")

if usr_choice == 'n':
    newDocument()
elif usr_choice == 'u':
    update_CSV()
