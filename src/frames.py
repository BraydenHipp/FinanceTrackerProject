import customtkinter
import components as comp

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
    
    def get_new_observation_data(self):
        # Returns a list of all the parts of a new observation
        # [type, category, amount, date]
        new_observation = []
        
        new_observation.append(self.get_type())
        new_observation.append(self.get_category())
        
        
        
        unprocessed_amount = self.get_amount()
        try:
            processed_amount = float(unprocessed_amount)
            round(processed_amount, 2)
            new_observation.append(processed_amount)
        except ValueError:
            comp.InvalidAmountPopUp(self)
            
        # TODO need to add the date parsing which is gonna suck
        
            

        

        
            
            
        
        
                
         
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