import json
import pandas as pd

# Data to be written
df['New_Column'] = np.arange(df[0])+1
df['New_Column'] = 'str' + df['New_Column'].astype(str)