import customtkinter
import components as comp
from testDataGenerator import Generator as TGD
from data import manipulateData as MD

class NewObservationFrame(customtkinter.CTkFrame):
    def __init__(self, master, update_callback, update_callback_2, update_callback_3, update_callback_4):
        super().__init__(master,
                         fg_color = "#2B2B2B",
                         border_color = "#404040",
                         border_width = 2,
                         corner_radius = 10,
                         width = 400,
                         height = 1000
                         )
        
        self.observation_label = comp.ObservationLabel(self)
        self.observation_label.grid(row = 0, column = 0, padx = 20,  pady = (0, 10), sticky = "ns")
        
        
        self.type_dropdown = comp.ObservationTypeDropBox(self)
        self.type_dropdown.grid(row = 1, column = 0, padx = 10, pady = (5, 10), sticky = "ns")
        
        self.amount_entry = comp.ObservationAmountEntry(self)
        self.amount_entry.grid(row = 3, column = 0, padx = 10, pady = (5, 10), sticky = "ns")
        
        self.category_dropdown = comp.ObservationCategory(self)
        self.category_dropdown.grid(row = 2, column = 0, padx = 10, pady = (5, 10), sticky = "ns")
        
        self.date_entry = comp.ObservationDate(self)
        self.date_entry.grid(row = 4, column = 0, padx = 10, pady = (5, 10), sticky = "ns")
        
        
        # How to call get new observation data function
        observation_adder = MD()
        
        # need to wrap this in a lamda function so that it isn't executed immediately
        self.add_observation_button = comp.AddTransactionButton(
                    self, 
                    command=lambda: [
                        observation_adder.get_new_observation_data(
                            self.get_type(),
                            self.get_amount(),
                            self.get_category(),
                            self.get_date(),
                            self
                        ),
                        update_callback(), # This refreshes the total 
                        update_callback_2(), # This refreshes the observations
                        update_callback_3(), # This refreshes the total withdrawals
                        update_callback_4() # This refreshes the total deposits 
                    ]
                )
                
        self.add_observation_button.grid(row = 5, column = 0, padx = 10, pady = (5, 10), sticky = "ns")     
        
        
    
    # Moving the methods oout of the initializer make them actual class methods instead of local ones
    def get_type(self):
        return self.type_dropdown.type_variable.get()
    
    def get_category(self):
        return self.category_dropdown.category_variable.get()
        
    def get_amount(self):
        return self.amount_entry.amount_variable.get()

    def get_date(self):
        return self.date_entry.date_variable.get()
    
        
            
        
#-----------------------------------------------------------------------------------------------------------#        

class BalanceFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(
                         master,
                         fg_color = "#2B2B2B",
                         border_color = "#404040",
                         border_width = 2,
                         corner_radius = 10
                        )
        
        
        # Total Balance label
        self.balance_label = comp.TotalBalanceLabel(self)
        self.balance_label.grid(row = 0, column = 0, padx = 20,  pady = (10,0), sticky = "w")
        
        # The actual amount        
        self.total = comp.TotalDisplay(self) # pady(t , b) says t pixels above b pixels below 
        self.total.grid(row = 1, column = 0, padx = 20,  pady = (0, 10), sticky = "ns")
        
        # The total withdrawals header
        self.withdrawal_header = comp.TotalWithdrawalsHeader(self)
        self.withdrawal_header.grid(row = 2, column = 0, padx = 20, pady = (10, 0), sticky = "sw")
        
        # The total withdrawls amount
        self.withdrawal_amount = comp.TotalWithdrawals(self)
        self.withdrawal_amount.grid(row = 3, column = 0, padx = (35, 0), pady = (10,0), sticky = "sw")
        
        # The total deposit Header
        self.deposit_header = comp.TotalDepositsHeader(self)
        self.deposit_header.grid(row = 2, column = 0, padx = (10, 20), pady = (10, 0), sticky = "se")
        
        # The total deposits amount
        self.deposit_amount = comp.TotalDeposits(self)
        self.deposit_amount.grid(row = 3, column = 0, padx = (10, 20), pady = (10, 0), sticky = "se")
        
        
    def update_balance(self):
        self.total.refresh_total()
        
    def update_withdrawals(self):
        self.withdrawal_amount.refresh_withdrawals()
        
    def update_deposits(self):
        self.deposit_amount.refresh_deposits()
        


#-----------------------------------------------------------------------------------------------------------#        

class TransactionsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(
                        master,
                        fg_color = "#2B2B2B",
                        border_color = "#404040",
                        border_width = 2,
                        corner_radius = 10,
                        width = 500,
                        height = 150
                        )
        
        self.all_transactions = comp.TransactionsLabel(self)
        self.all_transactions.grid(row = 0, column = 0, padx = 20,  pady = (10,10), sticky = "w")

    def update_transactions(self):
        self.all_transactions.refresh_transactions()
    


#-----------------------------------------------------------------------------------------------------------#        


class PieChartFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master,
                         fg_color = "#2B2B2B",
                        border_color = "#404040",
                        border_width = 2,
                        corner_radius = 10,
                        width = 527,
                        height = 400
                        )
        
        