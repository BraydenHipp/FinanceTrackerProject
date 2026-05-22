import customtkinter
import data
import frames as frm
 # TODO add functionality for pop ups based on error and success messages 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Finance Tracker")
        self.geometry("900x600")
        
        # Heres where you make each column
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=50)
        
        # Total Balance Frame
        self.balance_section = frm.BalanceFrame(self)
        self.balance_section.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = "nw")

        # New observation frame
        self.observation_frame = frm.NewObservationFrame(self)
        self.observation_frame.grid(row = 1, column = 0, padx = 20, pady = (5, 10), sticky = "nw")
        
app = App()
app.mainloop()
