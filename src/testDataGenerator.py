import random
import pandas as pd


class Generator:


    types = ["Deposit", "Withdrawal"]

    category = ["Housing/Utilities", "Food/Dining", "Transportation",
                "Medical", "Entertainment/Leisure", "Personal Care/Shopping",
                "Other", "N/A"]
    
    

    months = ["January", "Febuary", "March", "April", "May", "June",
               "July", "July", "August" , "September", "October", "November", "December"]

    
    # TODO Change it so the months are numbers
    months_to_days = {"January" : 31, 
                      "Febuary" : 28,
                      "March" : 31,
                      "April" : 30,
                      "May" : 31,
                      "June" : 30,
                      "July" : 31,
                      "August" : 31,
                      "September" : 30,
                      "October" : 31,
                      "November" : 30,
                      "December" : 31}

    
    # init is the constructor so it initializes the state of the object when you create it
    def __init__(self):
         pass # add this pass here because we dont need to setup any variables when the object is created

    def generate_test_data(self): # make sure to add the self here to access the class variables

    # Create a table to store the data

        data = {"type" : [],
                "amount" : [],
                "category" : [],
                "date" : []
                }
        
        number_of_observations = random.randint(20, 21) # Defines how many data points will be added

        for i in range(0 , number_of_observations):
            t = random.choice(self.types)
            amount = random.uniform(10, 1000)
            c = random.choice(self.category)

            # Build the date
            month = random.choice(self.months)
            day = random.randint(1 , self.months_to_days[month])
            year = random.randint(1970, 2026)

            date = month + "/" + str(day) + "/" + str(year)

            data["type"].append(t) # add the type

            data["amount"].append(round(amount , 2)) # add the amount

            
            if t == "Deposit":
                data["category"].append("N/A")
            else:
                data["category"].append(c)

            data["date"].append(date)
        
        df = pd.DataFrame(data) # turn it to a dataframe first before turning into a csv
        df.to_csv("../test/output.csv", index = False)
                
    