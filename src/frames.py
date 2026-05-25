import customtkinter
import components as comp
import testDataGenerator
from testDataGenerator import Generator as TGD

class NewObservationFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master,
                         fg_color = "#2B2B2B",
                         border_color = "#404040",
                         border_width = 2,
                         corner_radius = 10
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
        self.add_observation_button = comp.AddObservationButton(self, command = self.get_new_observation_data)
        self.add_observation_button.grid(row = 5, column = 0, padx = 10, pady = (5, 10), sticky = "ns")        
    
    # Moving the methods oout of the initializer make them actual class methods instead of local ones
    # TODO add the data parsing 
    def get_type(self):
        return self.type_dropdown.type_variable.get()
        
    def get_amount(self):
        return self.amount_entry.amount_variable.get()

    
    def get_category(self):
        return self.category_dropdown.category_variable.get()
    
    def get_date(self):
        return self.date_entry.date_variable.get()
    
    # TODO once finished prolly should add parameters and add this function to the data class
    def get_new_observation_data(self):

        
        
        unprocessed_amount = self.get_amount()
        try:
            processed_amount = float(unprocessed_amount)
            processed_amount = round(processed_amount, 2)
        except ValueError:
            comp.InvalidEntryPopUp(self, "Amount")
            return
            
        # TODO need to add the date parsing which is gonna suck
        
        unprocessed_date: str = self.get_date()
        
        # Needs to make sure length of the date is 10 and that it contains 2 slashes
        
        
        if len(unprocessed_date) != 10:
            comp.InvalidEntryPopUp(self, "Date")
            return
            
        # Count the number of slashes
        slash_count: int = 0
        for i in range(0, len(unprocessed_date) - 1):
            if unprocessed_date[i] == '/':
                slash_count += 1
                
        if slash_count != 2:
            comp.InvalidEntryPopUp(self, "Date")
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
            comp.InvalidEntryPopUp(self, "Date")
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
            comp.InvalidEntryPopUp(self, "Date")
            return
            
        # Check that each of the numbers are valid 
        
        # Make sure that month is 1-12

        if int_month > 12 or int_month < 1:
            comp.InvalidEntryPopUp(self, "Balls")
            return
        
        # Dictionary mapping months to the possible number of days
        months_to_days: dict = TGD.months_to_days
        months: list = TGD.months
        
        current_month: str = months[int_month - 1]
        max_days: int = months_to_days[current_month]
        
        
        
        if int_day > max_days or int_day < 1:
            comp.InvalidEntryPopUp(self, "Date")
            return
        
        if int_year > 9999 or int_year < 1000:
            comp.InvalidEntryPopUp(self, "Date")
            return
        
        
        # Returns a list of all the parts of a new observation
        # [type, category, amount, date]
        new_observation = []
        
        new_observation.append(self.get_type())
        new_observation.append(self.get_category())
        new_observation.append(processed_amount)
        new_observation.append(unprocessed_date)
        
        print(new_observation)
        
             
        
            

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