import pandas as pd
import csv
#df = pd.read_csv("Demo.txt",header=None,delim_whitespace=True) -- working 
#df.columns = ['host', 'b', 'user' ,'timestamp', 'response', 'status' , 'bytes']
#df.rename(columns={'0': 'host', '1': 'b' , '2': 'user' ,'3' : 'timestamp' , '4':'c' ,'5': 'response' , '6' : 'status' ,'7': 'bytes' }, inplace=True)
#df.rename(columns=lambda x: x[1:], inplace=True)
#df.to_csv (r'C:\Users\212777374\Desktop\work\mediawiki\readlog\demo2.csv', index = False, header=True) -- working 
#W#df = pd.read_csv("demo2.csv")
#w#df ['bytes'] = df ['bytes'] >5000
#w#true_count = df.bytes.sum()

#w#df = pd.read_csv("demo2.csv" )
#w#df ['status'] = df['bytes'].apply(lambda x: x if x >=5000  else None)
#w#total = df.status.sum()
#w#df.rename(columns = {'0':'Hostname','1':'-'}, inplace= True)
#w#columns= df.columns
#Total = df ['s'].apply( lambda x: x== True + s  )
#df ['DataFrame.columns: 7'] = df ['DataFrame.columns: 7'] >5000
#true_count = total.sum(df ['bytes'] > 5000 )
#total = df.bytes.add(df['bytes' == True] )
#total = df.bytes.add(df ['bytes'])
#numOfRows = len(df[df == True].index)
#print('Number of Rows in dataframe in which bytes > 5000 : ', total)
df = pd.read_csv("Demo.txt",header=None,delim_whitespace=True)
df.columns = ['host', 'b', 'user' ,'timestamp','c', 'response', 'status' , 'bytes']
#df.rename(columns = {'0':'Hostname','1':'-','2':'name','3':'timestamp','4':'-','5':'response','6':'status','7':'bytes'}, inplace= True)
df.to_csv (r'C:\Users\212777374\Desktop\work\mediawiki\readlog\demo.csv', index = False, header=True)
columns= df.columns
print(columns)

    