import pandas as pd

cols = ['frame', 'count']
N = 4
dat = pd.DataFrame(columns = cols)
for i in range(N):

    dat = dat.append({'frame': str(i), 'count':i},ignore_index=True)

print(dat)


