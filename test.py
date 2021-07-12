import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("tes spreadsheet api").sheet1

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

sheet.update_cell(1, 1, int(sheet.cell(1, 1).value)+1)

print(len(sheet.row_values(1)))

print(sheet.col_values(1))

print(sheet.cell(1, 2).value)