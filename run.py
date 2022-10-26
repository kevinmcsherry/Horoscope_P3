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
aries = SHEET.worksheet('Aries')
taurus = SHEET.worksheet('Taurus') 
gemini = SHEET.worksheet('Gemini')
cancer = SHEET.worksheet('Cancer')
leo = SHEET.worksheet('Leo')
virgo = SHEET.worksheet('Virgo')
libra = SHEET.worksheet('Libra')
scorpious = SHEET.worksheet('Scorpious')
sagittarius = SHEET.worksheet('Sagittarius')
capricorn = SHEET.worksheet('Capricorn')
aquarius = SHEET.worksheet('Aquarius')
pisces = SHEET.worksheet('Pisces')



tprint("Welcome  to", font="small")
#tprint("to your", font="small")
tprint("your  Daily", font="small")
tprint("Horoscope  page!", font="small")
#tprint("Page!\n", font="small")

name = input("Please Enter your Name:")
print("")
year = int(input("Please enter the year you were born: "))
print("")
month = int(input("Please enter the number of the month\n"
                 + "you were born. For example 3 = March: "))
print("")
day = int(input("Please enter the day you were born "))
dob = datetime.datetime(year,month,day)


def calc_age(dob):
    Age = (datetime.datetime.now() - dob)
    convertdays = int(Age.days)
    ExactAgeYears = convertdays/365
    global AgeYears
    AgeYears = int(ExactAgeYears)


def calc_star_sign(day, month):
    global astro_sign
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
    print("")
    print(str(name) + ", you are " + str(AgeYears) + " years old \n"
         + "and " + "Your Astrological sign is : " + str(astro_sign))


def get_today_reading():
    want_reading = str(input("Would you like your horoscope for today ? (Y/N): ")).lower().strip()
    try:
        if want_reading[0] == 'y':
            return True
            #add retrieve reading
        elif want_reading[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return get_today_reading()
    except Exception as error:
        print("Please enter valid inputs 'y' or 'n'")
        print(error)
        return get_today_reading()




def aries_horoscope():
    todays_scope = aries.acell('B2').value
    print(todays_scope)


def taurus_horoscope():
    todays_scope = taurus.acell('B2').value
    print(todays_scope)


def gemini_horoscope():
    todays_scope = gemini.acell('B2').value
    print(todays_scope)


def cancer_horoscope():
    todays_scope = cancer.acell('B2').value
    print(todays_scope)


def leo_horoscope():
    todays_scope = leo.acell('B2').value
    print(todays_scope)


def virgo_horoscope():
    todays_scope = virgo.acell('B2').value
    print(todays_scope)


def libra_horoscope():
    todays_scope = libra.acell('B2').value
    print(todays_scope)


def scorpious_horoscope():
    todays_scope = scorpious.acell('B2').value
    print(todays_scope)


def sagittarius_horoscope():
    todays_scope = sagittarius.acell('B2').value
    print(todays_scope)


def capricorn_horoscope():
    todays_scope = capricorn.acell('B2').value
    print(todays_scope)


def aquarius_horoscope():
    todays_scope = aquarius.acell('B2').value
    print(todays_scope)


def pisces_horoscope():
    todays_scope = pisces.acell('B2').value
    print(todays_scope)


calc_age(dob)
calc_star_sign(day, month)
get_today_reading()
