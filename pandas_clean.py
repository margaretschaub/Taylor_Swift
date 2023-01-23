import pandas as pd

data = pd.read_csv('/Users/margaretschaub/Desktop/test_edit.csv')
start, stop = 2, -1

try:
    data["Location"] = data["Location"].str.slice(start,stop)
    data["Track"] = data["Track"].str.slice(start,stop)
except SyntaxError:
    print("Error")
    pass

print(data["Track"].head(10))

df = pd.DataFrame(data)
df.to_csv(r'/Users/margaretschaub/Desktop/test_clean.csv', index = False)

