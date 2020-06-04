# arm_testing.py

# Rev 1.1
# Last updated: 6/4/2020

''' This test script is adjusted to work for remote control from the
    facial tracking script. This is linked to a Google Excel Sheet and
    voice commands are sent here. This script reads the command and performs
    the corresponding exercise.

    There are 2 exercises included below! Check out our website for the hardware/electronic configuration and more detailed instructions. '''

import pyfirmata
import time
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from pprint import pprint #pretty outputs

# HOW TO: Connect to google sheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("instructions").sheet1 #  cannot include weird characters in excel sheet name

# HOW TO: Reading from Google Sheet
data = sheet.get_all_records()  # prints all data from excel sheet into an array!

row = sheet.row_values(3) # specify a certain row you want to read from
#why is this in a dictionary format?
col = sheet.col_values(3) # specify a certain cell you want to read from

board = pyfirmata.ArduinoMega("COM3")


pin12 = board.get_pin('d:12:s')
pin12.write(90)
pin11 = board.get_pin('d:11:s')
pin11.write(35)
time.sleep(2)

count = 0
ph = list(range(1,3)) # 1, 2 bc only 2 exercises
print(ph)
print(len(ph))
random.shuffle(ph)
print(ph)
numRowsprevious = len(data)

while(1):
    # this continously checks the online database for new commands from Simon's brain
    data = sheet.get_all_records()
    cell = sheet.cell(1,1).value # get a particular cell
    print(cell)
    numRows = len(data) # get num rows filled in sheet
    print(numRows)

    if numRows!=numRowsprevious:
        numRowsprevious = numRows
        if cell.find("hello") >= 0:
            pin12.write(90)
            time.sleep(2)
            pin12.write(150)
            pin11.write(0)
            time.sleep(3)

            for x in range(4):
                pin11.write(0)
                time.sleep(.75)
                pin11.write(25)
                time.sleep(.75)

            pin12.write(90)
            time.sleep(4)
        if cell.find("exercise") >= 0:
            print(ph)
            print(count)
            if count > len(ph):
                count = 0
            y = ph[count]
            if y == 0:
                print("breaking out of y==0 if statement")
                break;
            if y == 1:
                sheet.update_cell(1, 2, "We will be doing Bicep Curls")
                time.sleep(5)
                pin11.write(10)
                time.sleep(3)


                pin11.write(90)
                time.sleep(3)
                sheet.update_cell(1, 2, "1 down")
                time.sleep(1)
                pin11.write(10)
                time.sleep(3)
                pin11.write(90)
                time.sleep(3)
                sheet.update_cell(1, 2, "2, Nice going")
                time.sleep(1)
                pin11.write(10)
                time.sleep(3)
                pin11.write(90)
                time.sleep(3)
                sheet.update_cell(1, 2, "That's 3")
                time.sleep(1)
                pin11.write(0)
                time.sleep(3)
                pin11.write(90)
                time.sleep(3)
                sheet.update_cell(1, 2, "4, Almost there")
                time.sleep(1)
                pin11.write(10)
                time.sleep(3)
                pin11.write(90)
                time.sleep(3)
                sheet.update_cell(1, 2, "Excellent, that's 5")
                time.sleep(2)
                sheet.update_cell(1, 2, 'Complete')
                pin11.write(45)
                time.sleep(3)

                count += 1
            if y == 2:

                sheet.update_cell(1, 2, "We will be doing arm lifts")
                time.sleep(5)
                pin11.write(0)
                time.sleep(2)
                pin12.write(115)
                time.sleep(4)


                pin12.write(180)
                time.sleep(3)
                pin12.write(115)
                sheet.update_cell(1, 2, "First one done")
                time.sleep(3)
                pin12.write(180)
                time.sleep(3)
                pin12.write(115)
                sheet.update_cell(1, 2, "There's 2")
                time.sleep(3)
                pin12.write(180)
                time.sleep(3)
                pin12.write(115)
                sheet.update_cell(1, 2, "Done with 3")
                time.sleep(3)
                pin12.write(180)
                time.sleep(3)
                pin12.write(115)
                sheet.update_cell(1, 2, "Finished 4")
                time.sleep(3)
                pin12.write(180)
                time.sleep(3)
                pin12.write(115)
                sheet.update_cell(1, 2, "Great job, that's 5")
                time.sleep(4)
                pin12.write(90)
                sheet.update_cell(1, 2, "Complete")
                time.sleep(3)

                count += 1

        if cell == 'stop':
            # wave

            pin12.write(90)
            time.sleep(2)
            pin12.write(150)
            pin11.write(0)
            time.sleep(4)

            for x in range(4):
                pin11.write(0)
                time.sleep(.75)
                pin11.write(25)
                time.sleep(.75)

            pin12.write(90)
            time.sleep(3)




            exit(board)
            break


    time.sleep(5)
    sheet.update_cell(1, 2, "end")

sheet.update_cell(2,2, "updated")


