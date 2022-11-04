# Horoscope_P3  

The Horoscope_P3 project delivers a useable and intuitive program that prompts and takes in data from a user.  This data will then link to an external Google sheet and retrieve matching data based on what data is entered.  For example, if I enter my DOB as 12/08/1979 (separate prompts) this means that I am a Leo star sign, so if the user indicates they want to see the horoscope for today, the program will retrieve todays reading from the Google sheet, based on a worksheet and Cell reference which is linked to todays reading… if its Tomorrows, same logic, but using different cell reference.
There is a Worksheet for each star sign, and different readings for each sign and day.  So a user can retrieve a reading for yesterday, Today and Tomorrow for any star sign all via the prompts. 

![Horoscope_P3 Main Page](images/Intro_Page.png)

# Features

- __Error Handling__
    
    - Year of birth
    When a user enters a year of birth, the program code checks if the data entered is numeric.  If not numeric, the program will post an error (This is not a number, please re-enter), and will re-prompt until a valid number is entered. 

    - Month of birth
    When a user enters a month of birth, again the program will check if the data entered is a numeric value, and if not will provide an error (Value must be a number between 1-12), and will continue to re-prompt until numeric value is added.  The program will also check if the value entered is >12, and if so will display an error (Value must be a number between 1-12) and will re-prompt until a numeric value between 1-12 is entered.

    - Day of birth
    When a user enters a value the program will once again check if numeric and will display an error if not.  There will also be an error displayed if the day does not match the month added…. this is controlled by the imported datetime method.  


- __Star Sign calculation__

- The program code will decipher what the user star sign is based on the data the user enters.  This is why instead of asking for DOB as one input, it was vital is ask for year, month and day separate.  The calculations are done by using the month and in particular the day of month to understand what sign is correct.


- __Data retrieval__

- I have created an external [Google Sheet](https://docs.google.com/spreadsheets/d/1CEI56um2eTA1yMyG832TtSUhkDg4cUDIjdaxL32IrFg/edit?pli=1#gid=0) in which I house all the horoscope data.  Based on the calculations and the options chosen by user, the program will select the correct worksheet and cell in relation to the data that will need to be displayed.  Based on sign, and whether its yesterday, today or Tomorrow, the program will grab the correct value. 


- __Multiple choice options__

- During the program, the user will be prompted with options to choose on whether they want to continue with more readings, if after todays reading, if the user wants tomorrows, they will be prompted about yesterdays, then again if chooisng to see yesterdays, they can start program again to run through with fresh data or end the program.  The user can choose no for Tomorrows reading, but will still get the option to see yesterdays, but again if chooisng no, the user will get a chance to start again or exit.  I feel that the usability of the program is strong, with the user is never left confused as to what are next steps or how to continue running it with different options.


# Features left to implement

- If I had further time, I would ideally like to add better error handling around the day entry input.  It would probably have required an array or set of data, or I may have been able to do it via the external sheet.
- Adding data - My program only retreives data and displays for the user.  Another feature that could be implemented is the option to perhaps add or manipulate the data.  Perhaps add a admin user to add or update the readings via the program and not just update via the physical sheet.


# Testing

- There was a lot of testing of this program throughout.  It was a tricky piece of code to write, so required lots of test, re-run, modification of code and repeat.  Testing that will not neccearily documented.
- I would say the bulk of the testing was around the if statements, and trying to make sure that the program carried out the correct action based on option slected by the user.
- The sharing and passing of variable data also caused me a lot of problems, and it meant I was calling functions from within other functions, which was not really my plan... this took a lot of time and testing to get right.
- I have tested this program thoroughly, lots of negative testing, error handling checks, correct readings being displayed etc... I have documented the user case testing [here](https://docs.google.com/spreadsheets/d/1qZD24CFKM44kvPzQZTWK6VcLEgmZM38yjjDgyqbEkqw/edit#gid=0)
- Technical Testing/Code validator was done via importing the PEP8 validator into GitPod.  There still remains some slight issues in the code with different coloured lines...but I have tried my best to clear these for when it makes sense.  There are some I really dont understand nor can I fix...but these do not hamper my program.

# Unfixed Bugs

- I missed the fact that a user can add a year greater than today or over all date greater than today, so there age is actually a minus number... This is not great.  If time permitted, I would retreive todays date, extract the year, and make sure the input is not greater than this year.  As a quick fix, I've hardcoded 2022. 
- I'm pretty happy with how the code is working, I wouldn't say there many other remaining bugs.  What I already referenced perhaps is the fact that I rely on the datetime method to handle the day entry errors..which actually ends the program - ideally this would be handled and remain in program.  This only happens if a day is entered that does not satisfy the day.





