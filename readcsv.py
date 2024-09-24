import pandas as pd
from datetime import datetime
# Path to your CSV file
csv_file_path = 'MRLP_E_MEEN_SSP_20240917_0001_nTOU.csv'


# Reading the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

df['DateFrom'] = pd.to_datetime(df['DateFrom'])

# Sort the rows based on 'SSPAreaCode', 'DateFrom', 'TimeFrom', and 'UTCFrom'
df = df.sort_values(by=['SSPAreaCode', 'DateFrom', 'UTCFrom', 'TimeFrom'])  

df['ForecastCode'] = 'ROC'
df['CodeType'] = '02'
df['Partition'] = 'P001'
df['PriceType'] = 'F'
#df['DateFrom'] = df['DateFrom'].str.replace('-', '').astype(int)
df['DateFrom'] = df['DateFrom'].dt.strftime('%Y%m%d').astype(int)  # Transform DateFrom to integer
df['UTCFrom'] = '+' + df['UTCFrom'].astype(str)
df['UTCTo'] = '+' + df['UTCTo'].astype(str)

df['TimeFrom'] = df['TimeFrom'].astype(str).str.zfill(6)
df['TimeTo'] = df['TimeTo'].astype(str).str.zfill(6)

new_column_order = ['SSPAreaCode', 'ForecastCode', 'CodeType', 'Partition', 
                    'DateFrom', 'TimeFrom', 'UTCFrom',
                    'DateTo', 'TimeTo', 'UTCTo',
                     'EnergyCharge', 'PriceType', 'Unit', 'DailyCharge','Created_by', 'Version']
df = df[new_column_order]

current_time = datetime.now().strftime('%Y%m%d%H%M')
df['Version'] = int(current_time)

df.to_csv('csv', index=False)



# Display the first few rows of the DataFrame
print(df.head())