import pandas as pd

#create DataFrame
df = pd.DataFrame({'points': [25, 12, 15, 14, 19, 23, 25, 29, 32],
                   'assists': [5, 7, 7, 9, 12, 9, 9, 4, 5],
                   'rebounds': [11, 8, 10, 6, 6, 5, 9, 12, 8]})

#view DataFrame
print(df)


#create duplicate points column
df['points_duplicate'] = df.loc[:, 'points']

#view updated DataFrame
print(df)