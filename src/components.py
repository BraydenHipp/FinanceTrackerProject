import customtkinter
import data
import pandas as pd
from testDataGenerator import Generator as TGD



class TotalBalanceLabel(customtkinter.CTkLabel): # inheritance (new label has all features of regular label)
    def __init__(self, master):
        super().__init__(master) # this initializes the parent class label
        
        self.configure(text = "Total Balance:", height = 50, width = 150,
                       font = ("Inter", 35), fg_color = "transparent"),

class TotalDisplay(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)
        
        
        extractor = data.manipulateData()
        total = extractor.getTotal()
        
        # To change the font size all you do is font = font (font type, size)
        self.configure(text = total, height = 50, width = 150, font = ("Inter", 35), fg_color="transparent")
        
        
    def refresh_total(self): 
        extractor = data.manipulateData()
        total = extractor.getTotal()

        self.configure(text = total)
        

class TotalWithdrawalsHeader(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)
        
        self.configure(text = "Withdrawals:", height = 25, width = 50, font = ("Inter", 15), fg_color = "transparent")        
        
        
class TotalWithdrawals(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)
        
        extractor = data.manipulateData()
        total_withdrawals: float = extractor.getWithdrawals()
        
        self.configure(text = total_withdrawals, height = 25, width = 50, font = ("Inter", 15), fg_color = "transparent", text_color = "red")
        
    def refresh_withdrawals(self):
        extractor = data.manipulateData()
        withdrawal_total = extractor.getWithdrawals()
        
        self.configure(text = withdrawal_total)
        
class TotalDepositsHeader(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)
        
        self.configure(text = "Deposits:", height = 25, width = 50, font = ("Inter", 15), fg_color = "transparent")
            
class TotalDeposits(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)
        
        extractor = data.manipulateData()
        total_deposits: float = extractor.getDeposits()
        
        self.configure(text = total_deposits, height = 25, width = 50, font = ("Inter", 15), fg_color = "transparent", text_color = "#60e806")
        
    def refresh_deposits(self):
        
        extractor = data.manipulateData()
        total_deposits: float = extractor.getDeposits()
        
        self.configure(text = total_deposits)
        

#-----------------------------------------------------------------------------------------------------------#


class ObservationLabel(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)
        
        self.configure(text = "Add New Transaction", height = 50, width = 150,
                       font = ("Inter", 23), fg_color = "transparent")
            
        
class ObservationTypeDropBox(customtkinter.CTkOptionMenu):
    def __init__(self, master):
        
        
        self.type_variable = customtkinter.StringVar(value = "Deposit")
        super().__init__(master,
                         values = ["Withdrawal", "Deposit"],
                         variable = self.type_variable
                         )
        
class ObservationAmountEntry(customtkinter.CTkEntry):
    def __init__(self, master):
        self.amount_variable = customtkinter.StringVar(value = "0.00")
        super().__init__(master, 
                         placeholder_text= "Amount",
                         textvariable = self.amount_variable
                         )

class ObservationCategory(customtkinter.CTkOptionMenu):
    def __init__(self, master):
        
        self.category_variable = customtkinter.StringVar(value = "Housing/Utilities")
        super().__init__(master,
                         values = ["Housing/Utilities",
                                   "Food/Dining",
                                   "Transportation",
                                   "Medical",
                                   "Entertainment/Leisure",
                                   "Personal Care/Shopping",
                                   "Other",
                                   "N/A(Deposit)"],
                         variable = self.category_variable
                        )
class ObservationDate(customtkinter.CTkEntry):
    def __init__(self, master):
        self.date_variable = customtkinter.StringVar(value = "mm/dd/year")
        super().__init__(master,
                         placeholder_text = "enter a date",
                         textvariable = self.date_variable)
        

class AddTransactionButton(customtkinter.CTkButton):
    def __init__(self, master, command = None):
    
        super().__init__(master,
                         text = "Add Transaction",
                         command = command)
        
#-----------------------------------------------------------------------------------------------------------#

class InvalidEntryPopUp(customtkinter.CTkToplevel):
    def __init__(self, master, type): # Type is a string indicating which part of the observation is wrong
        super().__init__(master)
        
        self.title("Error Message")
        self.geometry("300x200")

        # Makes sure the pop up window appears on top of all other windows
        self.attributes("-topmost", True)
        
        self.after(200, lambda: self.focus())
        
        label = customtkinter.CTkLabel(self, text = "Please Enter A Valid " + type)
        label.pack(pady = 20)
        
        
class SuccessfulEntry(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.title("Success")
        self.geometry("300x200")
        
        self.attributes("-topmost", True)
        
        self.after(200, lambda: self.focus())
        
        label = customtkinter.CTkLabel(self, text = "Transaction Added Succesfully")
        label.pack(pady = 20)
    
class mismatchTypePopUp(customtkinter.CTkToplevel):
    def __init__(self, master):
         super().__init__(master)       
         
         self.title("Error Message")
         self.geometry("300x200")
         
         self.attributes("-topmost", True)
         
         self.after(200, lambda: self.focus())
         
         label = customtkinter.CTkLabel(self, text = "Deposit must have category 'N/A(Deposit)")
         label.pack(pady=20) 
#-----------------------------------------------------------------------------------------------------------#


class TransactionsLabel(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)
        
        transaction_adder = data.manipulateData()
        all_transactions: str = transaction_adder.display_csv()
        
                
        self.configure(text = all_transactions, height = 50, width = 150, font = ("inter", 15), fg_color = "transparent")
        
        
    def refresh_transactions(self):
        
        transaction_adder = data.manipulateData()
        all_transactions: str = transaction_adder.display_csv()
        
        self.configure(text = all_transactions)        
#-----------------------------------------------------------------------------------------------------------#

