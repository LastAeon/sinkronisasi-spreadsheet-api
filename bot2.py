import gspread
from oauth2client.service_account import ServiceAccountCredentials
from random import randint
from time import sleep


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("tes spreadsheet api").sheet1

#bot
while(True):
    if(sheet.cell(1, 3).value == '0'):
        sheet.update_cell(1, 3, '1')
        sheet.update_cell(len(sheet.col_values(1))+1, 1, 'bot 2')
        sheet.update_cell(2, 3, "false") 
        sheet.update_cell(3, 3, "false") 
        sheet.update_cell(1, 3, '0')
        sleep(randint(63, 70)/7)
    sleep(1)