import pandas as pd
df = pd.read_csv("Demo.txt",header=None,delim_whitespace=True)
df.columns = ['host', 'b', 'user' ,'timestamp','c', 'response', 'status' , 'bytes']
df.to_csv (r'C:\Users\212777374\Desktop\work\mediawiki\readlog\demo.csv', index = False, header=True)
columns= df.columns
print(columns)
df = pd.read_csv("demo.csv" )
df ['status'] = df['bytes'].apply(lambda x: x if x >=5000  else None)
total = df.status.sum()
df ['bytes'] = df ['bytes'] >5000
true_count = df.bytes.sum()
print('Total bytes : ', total)
print('Number of Rows in dataframe in which bytes > 5000 : ', true_count)
