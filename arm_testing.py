# arm_testing.py

''' This test script is adjusted to work for remote control from the
    facial tracking script. This is linked to a Google Excel Sheet and
    voice commands are sent here. This script reads the command and performs
    the corresponding exercise.'''


# This script will read and write from an google excel file.

import pyfirmata
import time
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

col = sheet.col_values(3) # specify a certain cell you want to read from

board = pyfirmata.ArduinoMega("COM3")
pin = board.get_pin('d:9:s')
numRowsprevious = len(data)
while 1==1:
    data = sheet.get_all_records()
    cell = sheet.cell(1,1).value # get a particular cell
    print(cell)
    numRows = len(data) # get num rows filled in sheet
    print(numRows)

    #Write to arduino to move arm to certain positions
    if numRows!=numRowsprevious:
        numRowsprevious = numRows
        if cell == 'exercise':
            pin.write(130)
            time.sleep(3)
            pin.write(90)
            time.sleep(3)
        if cell == 'lift arm':
            pin.write(90)
            time.sleep(5)
            pin.write(10)
            time.sleep(5)


    time.sleep(5)

sheet.update_cell(2,2, "updated")


