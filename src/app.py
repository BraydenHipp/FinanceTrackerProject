import customtkinter
import data
import frames as frm
 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Finance Tracker")
        self.geometry("900x575")
        
        # Heres where you make each column
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=50)
        
        # Total Balance Frame
        self.balance_frame = frm.BalanceFrame(self)
        self.balance_frame.grid(row = 0, column = 0, padx = 20, pady = (5, 10), sticky = "ns")
        # Transaction Frame
        self.transaction_frame = frm.TransactionsFrame(self)
        self.transaction_frame.grid(row = 0, column = 1, padx = 20, pady = (5, 10), sticky = "ne")

        # New observation frame
        self.observation_frame = frm.NewObservationFrame(self, update_callback = self.balance_frame.update_balance,
                                                         update_callback_2 = self.transaction_frame.update_transactions)
        self.observation_frame.grid(row = 1, column = 0, padx = 20, pady = (5, 10), sticky = "ns")
        
        # Pie Chart Frame
        self.pie_chart_frame = frm.PieChartFrame(self)
        self.pie_chart_frame.grid(row = 1, column = 1, padx = 20, pady = (5, 10), sticky = "se")
        
app = App()
app.mainloop()
