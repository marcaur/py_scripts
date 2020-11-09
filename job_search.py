#!/usr/bin/python3

import csv
import shutil
from tempfile import NamedTemporaryFile
"""
This will create a document that allows me to update my job search
The spreadsheet will have fields for:
-----------------------------------------------
company | date applied | email | company site |
-----------------------------------------------
"""
print("Lets add some jobs to our search.")


# need conditional statements for CRUD operations
# ask user if this is existing
# skip beginning and add new row to document

#dictionary contains our values
jobApplied = {} #Global variable

myFile = 'job_search.csv'

tempfile = NamedTemporaryFile(mode='w',delete=False)

fieldnames = ["Company", "Date Applied", "Website", "Email"]

# questions to ask the user
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


#create the csv document
#if this is new, run this part(Tip: change to functions for different tasks)
def newDocument():
    global csv_writer
    with open(myFile,"w+") as csv_file,tempfile:
        csv_reader = csv.DictReader(csv_file, fieldnames)
        csv_writer = csv.DictWriter(tempfile, fieldnames = fieldnames) #allows us to write to file. We pass csv file as argument
        #header names
        usrQuest()

def update_CSV():
    global csv_writer
    with open(myFile,'a+') as update_obj,tempfile:
        csv_reader = csv.DictReader(update_obj, fieldnames)
        csv_writer = csv.DictWriter(tempfile, fieldnames = fieldnames)
        usrQuest()

shutil.move(tempfile.name, myFile)
