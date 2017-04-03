import openpyxl,pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
county_data = {}
print('Reading rows now...')
for row in range(2,sheet.max_row + 1):
    state  = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value
    county_data.setdefault(state,{})
    county_data[state].setdefault(county,{'tracts':0,'pop':0})
    county_data[state][county]['tracts'] += 1
    county_data[state][county]['pop'] += int(pop)

print('Writing results...')
result_file = open('census2010.py','w')
result_file.write('all_date =' + pprint.pformat(county_data))
result_file.close()
print('The work is done!')
    
#print('Writing results...')
#result_file = open('census2010_1.py','w')
#result_file.write('all_date = ' + str(county_data))
#result_file.close()
#print('The work is done!')

