import datetime
import sys
import os
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

while True:
    try:    
        year = int(input("Please enter the year you were born: "))
        print("")
        break
    except ValueError:
        print('This is not a number, please re-enter')
while True:
    try:
        month = int(input("Please enter the number of the month\n"
                + "you were born. For example 3 = March: "))     
        print("")
        break
    except ValueError:
        print('This is not a number, please re-enter')
    print("")
while True:
    try:
        day = int(input("Please enter the day you were born: "))
        print("")
        break
    except ValueError:
        print('This is not a number, please re-enter')

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


def calc_star_sign():
    """
    Function to determine the star sign of the user based
    on the date of birth entered
    """

    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    print("")
    return astro_sign       


def retrieve_today_reading():
    """
    Function to retrieve and display 
    the correct horoscope reading
    """
    user_astro_sign = calc_star_sign()

    print(name + ", " + "you are " + str(age_years) + " years old" 
          + " and your star sign is " + user_astro_sign)
    print("")

    if user_astro_sign == 'Aries':
        get_reading = aries.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Taurus':
        get_reading = taurus.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Gemini':
        get_reading = gemini.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Cancer':
        get_reading = cancer.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Leo':
        get_reading = leo.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Virgo':
        get_reading = virgo.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Libra':
        get_reading = libra.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Scorpious':
        get_reading = scorpious.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Sagittarius':
        get_reading = sagittarius.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Capricorn':
        get_reading = capricorn.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Aquarius':
        get_reading = aquarius.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")
    elif user_astro_sign == 'Pisces':
        get_reading = pisces.acell('B2').value
        print("Your Horoscope reading for Today is - " + get_reading)
        print("")


def get_another_reading():
    """
    Function to determine if the user would 
    like to restart the program and enter new details
    """
    want_reading = str(input("Type M for more readings or E to Exit M/E: ")).lower().strip()
    try:
        if want_reading[0] == 'e':
            print("OK, Goodbye")
            exit()
        elif want_reading[0] == 'm':
            want_tomorrow_reading = str(input("Would you like to know Tomorrows reading?  (Y/N:) ")).lower().strip()
            if want_tomorrow_reading[0] == 'y':
                tomorrow_reading()
            elif want_tomorrow_reading[0] == 'n':
                want_yesterday_reading = str(input("Would you like to know yesterdays reading?  (Y/N:) ")).lower().strip()
                if want_yesterday_reading[0] == 'y':
                    yesterday_reading()
                elif want_yesterday_reading[0] == 'n':
                    print("OK, Goodbye")
                    exit()
        else:
            print('Invalid Input')
            return get_another_reading()
    except Exception as error:
        print("Please enter valid inputs 'y' or 'n'")
        print(error)
        return get_another_reading()


def yesterday_reading():
    """
    Function to determine star sign and 
    correct reading from yesterday
    """

    user_astro_sign = calc_star_sign()

    if user_astro_sign == 'Aries':
        get_reading = aries.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Taurus':
        get_reading = taurus.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Gemini':
        get_reading = gemini.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Cancer':
        get_reading = cancer.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Leo':
        get_reading = leo.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Virgo':
        get_reading = virgo.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Libra':
        get_reading = libra.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Scorpious':
        get_reading = scorpious.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Sagittarius':
        get_reading = sagittarius.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Capricorn':
        get_reading = capricorn.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Aquarius':
        get_reading = aquarius.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")
    elif user_astro_sign == 'Pisces':
        get_reading = pisces.acell('D2').value
        print("Your Horoscope reading for Yesterday is - " + get_reading)
        print("")


def tomorrow_reading():
    """
    Function to determine star sign and
    correct reading from yesterday
    """  
    user_astro_sign = calc_star_sign()

    if user_astro_sign == 'Aries':
        get_reading = aries.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Taurus':
        get_reading = taurus.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Gemini':
        get_reading = gemini.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Cancer':
        get_reading = cancer.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Leo':
        get_reading = leo.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Virgo':
        get_reading = virgo.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Libra':
        get_reading = libra.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Scorpious':
        get_reading = scorpious.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Sagittarius':
        get_reading = sagittarius.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Capricorn':
        get_reading = capricorn.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Aquarius':
        get_reading = aquarius.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")
    elif user_astro_sign == 'Pisces':
        get_reading = pisces.acell('C2').value
        print("Your Horoscope reading for Tomorrow is - " + get_reading)
        print("")

    want_yesterday_reading = str(input("Would you like to know yesterdays reading?  (Y/N:) ")).lower().strip()
    if want_yesterday_reading[0] == 'y':
        yesterday_reading()
    else:
        start_again()


def start_again():
    """
    Function at the end of all horscope options
    allow the user to start again with new details
    """
    start_program_again = str(input("Would you like to start again? Y/N: ")).lower().strip()
    if start_program_again[0] == 'n':
        print("OK, Goodbye")
        exit()
    elif start_program_again[0] == 'y':
        os.execv(sys.executable, ['python3'] + sys.argv)


def main():
    """
    Run all program functions
    """
    calc_age()
    calc_star_sign()
    get_reading()
    get_another_reading()
    start_again()
   

main()
