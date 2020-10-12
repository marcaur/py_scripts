#!/usr/bin/python3

import csv
"""
This will create a document that allows me to update my job search
The spreadsheet will have fields for:
-----------------------------------------------
company | date applied | email | company site |
-----------------------------------------------
"""
print("Lets add some jobs to our search.")


#need conditional statements for CRUD operations
#ask user if this is existing
# skip beginning and add new row to document

#dictionary contains our values
jobApplied = {} #Global variable


#create the csv document
#if this is new, run this part(Tip: change to functions for different tasks)
def newDocument():
    with open("job_search.csv","w+") as csv_file:
        fieldnames = ["Company", "Date Applied", "Website", "Email"]
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames) #allows us to write to file. We pass csv file as argument
        #header names

        #writes the first row of headers
        csv_writer.writeheader()
        # User Actions
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
            newDocument()



newDocument()
