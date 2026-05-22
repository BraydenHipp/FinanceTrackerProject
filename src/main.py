import app as ap
import frames as frm
import testDataGenerator
import data
import pandas as pd
def main():
    
    # should rename the file, the first part is the file, the second part is the class
    # so you are accessing the class from the file
    
    # generator = testDataGenerator.TestDataGenerator()
    # generator.generate_test_data()
        
    # Use a dictionary to import data. Will go like:
    #  Type of transaction (Deposit/Withdrawl),
    #  Amount,
    #  Category(Housing/Utilities, Food/Dining, Transportation, Medical, Entertainment/Leisure, Personal Care/Shopping), Other, N/A (Deposits)
    #  Date (mm/dd/yy)

    # data  = pd.DataFrame({
    #     'type' : ['deposit', 'withdrawl', 'withdrawl'],
    #     'amount' : [20.10, 7.10, 29.01], 
    #     'category' : ['N/A', 'transportation', 'personal care/shopping'],
    #     'date' : ['04/28/2006', '11/19/2022', '01/20/2019']
    #         })
        
    # data.to_csv('data_small.csv', index = False)
    
    # extractor = data.extractData()
    
    # extractor.getTotal()
    # generator = testDataGenerator.Generator()
    # generator.generate_test_data()
    
    # adder = data.manipulateData()    
    # adder.add_observation("Withdrawal", 12.90, "Transportation", "04/28/06")
    j = 1
    
if __name__ == "__main__":
    main()
    