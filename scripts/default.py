import pandas as pd

# create a sample dataframe
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'gender': ['F', 'M', 'M']
        }
df = pd.DataFrame(data)

# display the original dataframe
print('Original DataFrame:\n', df)

# drop the 'gender' column
df = df.drop(columns=['gender'])

# display the modified dataframe
print('Modified DataFrame:\n', df)