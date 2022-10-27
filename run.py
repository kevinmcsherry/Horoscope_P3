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
global astro_sign
global want_reading

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
    age = (datetime.datetime.now() - dob)
    convertdays = int(age.days)
    exact_age_years = convertdays/365
    global age_years
    age_years = int(exact_age_years)


def calc_star_sign():
    """
    Function to determine the star sign of the user based
    on the date of birth entered
    """

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
    print(str(name) + ", you are " + str(age_years) + " years old \n"
          + "and " + "Your Astrological sign is : " + str(astro_sign))


def get_reading():
    """
    Function to ask the user if they would like
    thier horoscope for today
    """

    want_reading = str(input("Would you like your horoscope for today ? (Y/N): ")).lower().strip()
    try:
        if want_reading[0] == 'y':
            retrieve_today_reading()
        elif want_reading[0] == 'n':
            print("OK, GoodBye")
            exit()
        else:
            print('Invalid Input')
            return get_reading()
    except Exception as error:
        print("Please enter valid inputs 'y' or 'n'")
        print(error)
        return get_reading()


def retrieve_today_reading():
    """
    Function to retrieve and display 
    the correct horoscope reading
    """
    astro_sign = 'aries'
    if astro_sign == 'aries':
        get_reading = aries.acell('B2').value
        print(get_reading)
    elif astro_sign == 'taurus':
        get_reading = taurus.acell('B2').value
        print(get_reading)
    elif astro_sign == 'gemini':
        get_reading = gemini.acell('B2').value
        print(get_reading)
    elif astro_sign == 'cancer':
        get_reading = cancer.acell('B2').value
        print(get_reading)
    elif astro_sign == 'leo':
        get_reading = leo.acell('B2').value
        print(get_reading)
    elif astro_sign == 'virgo':
        get_reading = virgo.acell('B2').value
        print(get_reading)
    elif astro_sign == 'libra':
        get_reading = libra.acell('B2').value
        print(get_reading)
    elif astro_sign == 'scorpious':
        get_reading = scorpious.acell('B2').value
        print(get_reading)
    elif astro_sign == 'sagittarius':
        get_reading = sagittarius.acell('B2').value
        print(get_reading)
    elif astro_sign == 'capricorn':
        get_reading = capricorn.acell('B2').value
        print(get_reading)
    elif astro_sign == 'aquarius':
        get_reading = aquarius.acell('B2').value
        print(get_reading)
    elif astro_sign == 'pisces':
        get_reading = pisces.acell('B2').value
        print(get_reading)


calc_age()
calc_star_sign()
get_reading()

