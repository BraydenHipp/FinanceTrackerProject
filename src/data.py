import pandas as pd


# Use a dictionary to import data. Will go like:
#  Type of transaction (Deposit/Withdrawl),
#  Amount,
#  Category(Housing/Utilities, Food/Dining, Transportation, Medical, Entertainment/Leisure, Personal Care/Shopping), Other, N/A (Deposits)
#  Date (mm/dd/yy)

data  = pd.DataFrame({
    'type' : ['deposit', 'withdrawl', 'withdrawl'],
    'amount' : [20.10, 7.10, 29.01], 
    'category' : ['N/A', 'transportation', 'personal care/shopping'],
    'data' : ['04/28/2006', '11/19/2022', '01/20/2019']
        })
    
data.to_csv('output.csv', index = False)