import pandas as pd
from cleaning import *

data = pd.read_csv('/Users/margaretschaub/Desktop/taylor_swift_setlist.csv')
start, stop = 2, -1

#need to build in for errors
data["Location"] = data["Location"].str.slice(start, stop)
data["Track"] = data["Track"].str.slice(start, stop)
data["Counter"] = data["Counter"].apply(clean_to_int)
data["Special"] = data["Special"].str.replace("[()]", "", regex=True)
data["Date"] = data["Date"].apply(convert_date)
data["Location"] = data["Location"].apply(location_clean)

df_location = pd.DataFrame(data['Location'].tolist()).fillna('').add_prefix('location_')
data = pd.concat([data,df_location], axis = 1)
data = data[['Counter','Track','Special','Date','location_0','location_1','location_2','location_3']]

print(data["Track"].head(10))

df = pd.DataFrame(data)
df.to_csv(r'/Users/margaretschaub/Desktop/test_clean2.csv', index = False)

