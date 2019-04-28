import pandas as pd

df = pd.read_csv('Web_Database.csv')

def zipfinder(target, prefs):
    target_frame = df.loc[df['TargetID'] == target]
    target_frame.sort_values(by=['Distance'], inplace=True)
    print(target_frame)
zipfinder(2210, [])