import pandas as pd

#Check the number of maximum returned rows:

print(pd.options.display.max_rows)

#Increase the maximum number of rows to display the entire DataFrame:

"""
import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df) 
"""