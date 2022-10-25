import datetime
import gspread
from google.oauth2.service_account import Credentials
from art import tprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Horoscope_P3')


tprint("Welcome" + "  " + "to" + "  " + "your" + "  " + "Daily")
tprint("HOROSCOPE" + "   " + "Page")

name = input("Please Enter your Name:")


def calc_age():
    Year = int(input(" Please enter the year you were born "))
    Month = int(input(" Please enter the number of the month you were born.  For example 3 = March "))
    Day = int(input(" Please enter the day you were born "))
    DOB = datetime.datetime(Year,Month,Day)
    Age = (datetime.datetime.now() - DOB)
    convertdays = int(Age.days)
    ExactAgeYears = convertdays/365
    AgeYears = int(ExactAgeYears)
    print("You are" + str(AgeYears) + " years old")


calc_age()


aries = SHEET.worksheet('Aries')

data = aries.get_all_values()

print(data)