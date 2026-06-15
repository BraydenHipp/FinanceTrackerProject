import components as comp
import pandas as pd
from testDataGenerator import Generator as TGD

class manipulateData:
    
    def __init__(self):
        pass
    
    # This function reads the output.csv file and computes the balance
    def getTotal(self):
        
        # the .. tells python to go up one level out of the src directory to look for the test folder
        df = pd.read_csv("../test/output.csv") # turns the csv file into a data frame
        
        data = df.to_dict(orient = "records")
        
        
        total = 0
        
        for transaction in data:
            transaction_type = transaction["type"]
            amount = transaction["amount"]
            if (transaction_type == "Deposit"):
                total += amount
            elif (transaction_type == "Withdrawal"):
                total -= amount
            
        return round(total, 2)
    
    
    # This function counts the total amount of deposits
    def getDeposits(self):
        
        df = pd.read_csv("../test/output.csv")
        data = df.to_dict(orient = "records")
        
        total: int = 0
        
        for transaction in data:
            
            transaction_type: str = transaction["type"]
            amount: int = transaction["amount"]
            
            if (transaction_type == "Deposit"):
                total += amount
                
        return round(total, 2)
    
    def getWithdrawals(self):
                
        df = pd.read_csv("../test/output.csv")
        data = df.to_dict(orient = "records")
        
        total: int = 0
        
        for transaction in data:
            
            transaction_type: str = transaction["type"]
            amount: int = transaction["amount"]
            
            if (transaction_type == "Withdrawal"):
                total += amount
                
        return round(total, 2)
        
        
    # This method counts the total number of each type of transactions
    
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
    
    
    def display_csv(self):
        
        df = pd.read_csv("../test/output.csv") # turns the csv file into a data frame
        
        data: list = df.to_dict(orient = "records") # converts the csv to a list containing all of the observations
        data.reverse()
        
        all_transactions: str = ""
        margin:str = "           "
        line_break:str = margin + "-------------------------------------------------"
        for transaction in data:
            type_t: str = transaction["type"]
            amount: str = str(transaction["amount"])
            category: str = str(transaction["category"])
            date: str = transaction["date"]
            
            all_transactions += margin + type_t + ", " +  amount + ", " + category + ", " + date +  "\n" + line_break + "\n"
        
        return all_transactions
    
    def get_new_observation_data(self, type_t, amount, category, date, parent_ui):

        unprocessed_amount = amount
        try:
            processed_amount = float(unprocessed_amount)
            processed_amount = round(processed_amount, 2)
        except ValueError:
            comp.InvalidEntryPopUp(parent_ui, "Amount")
            return
            
        # TODO need to add the date parsing which is gonna suck
        
        unprocessed_date: str = date
        
        # Needs to make sure length of the date is 10 and that it contains 2 slashes
        
        
        if len(unprocessed_date) != 10:
            comp.InvalidEntryPopUp(parent_ui, "Date")
            return
            
        # Count the number of slashes
        slash_count: int = 0
        for i in range(0, len(unprocessed_date) - 1):
            if unprocessed_date[i] == '/':
                slash_count += 1
                
        if slash_count != 2:
            comp.InvalidEntryPopUp(parent_ui, "Date")
            return
        
        # Step 1 get the chars at index [0, 1] [3, 4] and [6, 7, 8, 9]
        str_day: str = ""
        str_month: str = ""
        str_year: str = ""
        try:
            str_month = unprocessed_date[0] + unprocessed_date[1]
            str_day = unprocessed_date[3] + unprocessed_date[4]
            str_year = unprocessed_date[6] + unprocessed_date[7] + unprocessed_date[8] + unprocessed_date[9]
        except IndexError:
            comp.InvalidEntryPopUp(parent_ui, "Date")
            return
            
            
        
        # Check to make sure they are all numbers
        int_day: int = 0
        int_month: int = 0
        int_year: int = 0
        try:
            int_day = int(str_day)
            int_month = int(str_month)
            int_year = int(str_year)
        except ValueError:
            comp.InvalidEntryPopUp(parent_ui, "Date")
            return
            
        # Check that each of the numbers are valid 
        
        # Make sure that month is 1-12

        if int_month > 12 or int_month < 1:
            comp.InvalidEntryPopUp(parent_ui, "Date")
            return
        
        # Dictionary mapping months to the possible number of days
        months_to_days: dict = TGD.months_to_days
        months: list = TGD.months
        
        current_month: str = months[int_month - 1]
        max_days: int = months_to_days[current_month]
        
        
        
        if int_day > max_days or int_day < 1:
            comp.InvalidEntryPopUp(parent_ui, "Date")
            return
        
        if int_year > 9999 or int_year < 1000:
            comp.InvalidEntryPopUp(parent_ui, "Date")
            return
        
        # Can use self because it is a method of the same class
        self.add_observation(type_t, processed_amount, category, unprocessed_date)
        
        comp.SuccessfulEntry(parent_ui)
    
    
    
