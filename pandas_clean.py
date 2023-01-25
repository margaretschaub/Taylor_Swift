import pandas as pd
from cleaning import clean_to_int, convert_date, location_clean

data = pd.read_csv('/Users/margaretschaub/Desktop/taylor_swift_setlist.csv')
start, stop = 2, -1

# need to build in for errors
data["Location"] = data["Location"].str.slice(start, stop)
data["Track"] = data["Track"].str.slice(start, stop)
data["Counter"] = data["Counter"].apply(clean_to_int)
data["Special"] = data["Special"].str.replace("[()]", "", regex=True)
data["Date"] = data["Date"].apply(convert_date)
data["Location"] = data["Location"].apply(location_clean)

df_location = pd.DataFrame(data['Location'].tolist()).fillna('').add_prefix('location_')
data = pd.concat([data, df_location], axis=1)
data = data[['Counter', 'Track', 'Special', 'Date', 'location_0', 'location_1', 'location_2', 'location_3']]

row_count = 0
for row in data['location_3']:
    if row == '':
        data.loc[row_count, 'location_3'] = data.loc[row_count, 'location_2']
        data.loc[row_count, 'location_2'] = ''
    row_count += 1

data.rename(columns={'location_0': 'Venue', 'location_1': 'City', 'location_2': 'State', 'location_3': 'Country'})

df = pd.DataFrame(data)
df.to_csv(r'/Users/margaretschaub/Desktop/test_clean2.csv', index=False)
