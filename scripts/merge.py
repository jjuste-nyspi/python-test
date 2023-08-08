import pandas
import pandas as pd
import openpyxl

#read in excel files

irbno = pandas.read_excel('protocol-details.xlsx', sheet_name='Sheet 1')
prod_proj = pandas.read_excel('query_export.xlsx', sheet_name='query_export')


#merge and output

df = pd.merge(irbno, prod_proj, on="IRBNO", how="right")

dfresult = df.dropna(subset=['IRBNO'])


print(dfresult)


dfresult.to_excel('results.xlsx', index=False)



