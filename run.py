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
tprint("your  Daily", font="small")
tprint("Horoscope  page!", font="small")


name = input("Please Enter your Name:")
print("")
year = int(input("Please enter the year you were born: "))
print("")
month = int(input("Please enter the number of the month\n"
            + "you were born. For example 3 = March: "))
print("")
day = int(input("Please enter the day you were born "))
dob = datetime.datetime(year, month, day)


def calc_age():
    """
    Function to determine and calculate the exact age from
    the user based on date of birth entered
    """
    Age = (datetime.datetime.now() - dob)
    convertdays = int(Age.days)
    ExactAgeYears = convertdays/365
    global AgeYears
    AgeYears = int(ExactAgeYears)


def calc_star_sign(day, month):
    """
    Function to determine the star sign of the user based
    on the date of birth entered
    """
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
    """
    Function to ask the user if they would like
    thier horoscope for today
    """
    want_reading = str(input("Would you like your horoscope for today ? (Y/N): ")).lower().strip()
    try:
        if want_reading[0] == 'y':
            return True
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
    """
    Function to determine and retrieve the cell value for Aries sign

    """
    todays_scope = aries.acell('B2').value
    print(todays_scope)


def taurus_horoscope():
    """
    Function to determine and retrieve the cell value for Taurus sign
    """
    todays_scope = taurus.acell('B2').value
    print(todays_scope)


def gemini_horoscope():
    """
    Function to determine and retrieve the cell value for Gemini sign
    """
    todays_scope = gemini.acell('B2').value
    print(todays_scope)


def cancer_horoscope():
    """
    Function to determine and retrieve the cell value for Cancer sign
    """
    todays_scope = cancer.acell('B2').value
    print(todays_scope)


def leo_horoscope():
    """
    Function to determine and retrieve the cell value for Leo sign
    """
    todays_scope = leo.acell('B2').value
    print(todays_scope)


def virgo_horoscope():
    """
    Function to determine and retrieve the cell value for Virgo sign
    """
    todays_scope = virgo.acell('B2').value
    print(todays_scope)


def libra_horoscope():
    """
    Function to determine and retrieve the cell value for Libra sign
    """
    todays_scope = libra.acell('B2').value
    print(todays_scope)


def scorpious_horoscope():
    """
    Function to determine and retrieve the cell value for Scorpious sign
    """
    todays_scope = scorpious.acell('B2').value
    print(todays_scope)


def sagittarius_horoscope():
    """
    Function to determine and retrieve the cell value for Sagittarius sign
    """
    todays_scope = sagittarius.acell('B2').value
    print(todays_scope)


def capricorn_horoscope():
    """
    Function to determine and retrieve the cell value for Capricorn sign
    """
    todays_scope = capricorn.acell('B2').value
    print(todays_scope)


def aquarius_horoscope():
    """
    Function to determine and retrieve the cell value for Aquarius sign
    """
    todays_scope = aquarius.acell('B2').value
    print(todays_scope)


def pisces_horoscope():
    """
    Function to determine and retrieve the cell value for Pisces sign
    """
    todays_scope = pisces.acell('B2').value
    print(todays_scope)


calc_age()
calc_star_sign(day, month)
get_today_reading()
