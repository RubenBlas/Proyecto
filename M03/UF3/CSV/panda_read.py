import pandas as pd

#Load the CSV into a DataFrame:

df = pd.read_csv('data.csv')

print(df.to_string())


#Print the DataFrame without the to_string() method:

"""
import pandas as pd

df = pd.read_csv('data.csv')

print(df) 
"""