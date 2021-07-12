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
    # print(sheet.cell(2, 3).value.lower())
    # print(sheet.cell(2, 3).value.lower())
    if(sheet.cell(1, 3).value == '0'):
        sheet.update_cell(1, 3, '1')
        if(sheet.cell(2, 3).value.lower() == 'true' and sheet.cell(3, 3).value.lower() == 'true'):
            sheet.update_cell(len(sheet.col_values(1))+1, 1, 'bot 0')
        sheet.update_cell(1, 3, '0')
    #     print("masuk")
    # print("keluar")
    sleep(1)