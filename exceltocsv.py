from operator import index
import pandas as pd
import os

path = 'C:\\Users\\tuand\\Tuan Usher\\Desktop\\deanchereden-superstore-dataset\\deanchereden-superstore-dataset\\'
files = os.listdir(path)

for file in files:
    if file.endswith('.xlsx'):
        cln = file.replace('.xlsx', '')
        xlfile = pd.ExcelFile(file)
        sheets = xlfile.sheet_names
        for sheet in sheets:
            sheetdata = xlfile.parse(sheet)
            csvname = cln + '.csv'
            sheetdata.to_csv(csvname, index = False)