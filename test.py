requests = []
spreadsheet_id = "1B4OEqZxA9YTeH8GAPUgwtBva8glYWMvOtwlmwwt8VfY"
# Change the spreadsheet's title.
requests.append({
    'updateSpreadsheetProperties': {
        'properties': {
            'title': title
        },
        'fields': 'title'
    }
})
# Find and replace text
requests.append({
    'findReplace': {
        'find': find,
        'replacement': replacement,
        'allSheets': True
    }
})
# Add additional requests (operations) ...

body = {
    'requests': requests
}
response = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body=body).execute()
find_replace_response = response.get('replies')[1].get('findReplace')
print('{0} replacements made.'.format(
    find_replace_response.get('occurrencesChanged')))