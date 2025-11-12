import numpy as np
import pandas as pd

# To load data
# So, this is going to load the csv file for us. And it's going to store it in a dataframe
df = pd.read_csv("orders - Copy.csv")

# To print the dataframe
'''
Pandas will assign indexes such as 0, 1, ... on the left-most side of the dataframe.
This helps us to locate data in a Dataframe.
'''
print(df)




