
import pandas as pd

class manipulateData:
    
    def __init__(self):
        pass
    
    # This function reads the output.csv file and computes the balance
    def getTotal(self):
        
        # the .. tells python to go up one level out of the src directory to look for the test folder
        df = pd.read_csv("../test/data_small.csv") # turns the csv file into a data frame
        
        data = df.to_dict(orient = "records")
        
        total = 0
        
        for transaction in data:
            transaction_type = transaction["type"]
            amount = transaction["amount"]
            if (transaction_type == "deposit"):
                total += amount
            elif (transaction_type == "withdrawal"):
                total -= amount
            
        return round(total, 2)
    
    
    # TODO Write a method to count the total amounts for each of the categories
    
    def count_total(self):
        df = pd.read_csv("../test/output.csv", keep_default_na = False)
        
        data = df.to_dict(orient = "records")
        # Define the dictoinary
        frequency: dict = {
            "Housing/Utilities" : 0,
            "Food/Dining" : 0,
            "Transportation" : 0,
            "Medical" : 0,
            "Entertainment/Leisure" : 0,
            "Personal Care/Shopping" : 0,
            "Other" : 0,
            "N/A" : 0
        }
        
        for observation in data:
            frequency[observation] += 1
            
        return frequency
    
    
    def add_observation(self, type_t, amount_t, category_t, date_t):
        # keep_default_na makes it so it doesn't remove the N/A in data
        df = pd.read_csv("../test/output.csv", keep_default_na = False)
        
        # This actually creates a list of dictionaries
        data = df.to_dict(orient = "records")
        
        # asumes all data is valid
        new_dict: dict = {
            "type" : type_t,
            "amount" : round(amount_t, 2),
            "category" : category_t,
            "date" : date_t
        }
        
        data.append(new_dict)
        
        df = pd.DataFrame(data)
        df.to_csv("../test/output.csv", index=False)
        
        return data
    
    