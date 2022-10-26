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


tprint("Welcome  to", font="small")
#tprint("to your", font="small")
tprint("your  Daily", font="small")
tprint("Horoscope  page!", font="small")
#tprint("Page!\n", font="small")

name = input("Please Enter your Name:")
year = int(input(" Please enter the year you were born: "))
month = int(input(" Please enter the number of the month you were born. For example 3 = March: "))
day = int(input(" Please enter the day you were born "))
dob = datetime.datetime(year,month,day)


def calc_age(dob):
    Age = (datetime.datetime.now() - dob)
    convertdays = int(Age.days)
    ExactAgeYears = convertdays/365
    global AgeYears
    AgeYears = int(ExactAgeYears)


def calc_star_sign(day, month):
    if month == 12:
	    astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 1:
	    astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 2:
	    astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 3:
	    astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 4:
	    astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 5:
	    astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 6:
	    astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 7:
	    astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 9:
	    astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 10:
	    astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 11:
	    astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
    print(str(name) + ", you are " + str(AgeYears) + " years old " + "and " + "Your Astrological sign is : " + str(astro_sign))


calc_age(dob)
calc_star_sign(day, month)



#aries = SHEET.worksheet('Aries')

#data = aries.get_all_values()

#print(data)