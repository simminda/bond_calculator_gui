from tkinter import *

# Setup window parameters
window = Tk()
window.title("Finance Calculators")
window.geometry("450x380")  
window.resizable(False, False)

# add a contextual background image
background = PhotoImage(file = "fc.gif")
# Create Canvas to place image
canvas1 = Canvas( window, width = 450, height = 380)
canvas1.pack(fill = "both", expand = True)
# Display image
canvas1.create_image( 0, 0, image = background, anchor = "nw")

# create container to organize widgets which will be used
frame = Frame(window)

# Widgets
Label(frame, text='BOND CALCULATOR', font=('Arial Bold', 16)).grid(row = 0, column = 0, columnspan=2, pady=20)

Label(frame, text='Annual Interest Rate').grid(row = 5, column = 0, sticky=W, padx=5)
entry_int = Entry(frame)
entry_int.grid(row=5, column=1)

Label(frame, text='Number of Years').grid(row = 6, column = 0, sticky=W, padx=5)
entry_period = Entry(frame)
entry_period.grid(row=6, column=1)

Label(frame, text='Loan Amount').grid(row = 7, column = 0, sticky=W, padx=5)
entry_amount = Entry(frame)
entry_amount.grid(row=7, column=1, padx=10)

Label(frame).grid(row = 8, column = 0, sticky=W, padx=5)    # empty label for spacing
Label(frame).grid(row = 10, column = 0, sticky=W, padx=5)   # empty label for spacing

# CALCULATION
# formula: x = L * ((I * ((1+I) ** n)) / ((1+I) ** n - 1))
def calculate():
    try:
        #getting the value in the entry boxes
        int_rate  = float(entry_int.get())/12/100
        payment_term = float(entry_period.get()) * 12
        house_price = float(entry_amount.get())

        repayment = round(house_price * (int_rate * (1 + int_rate) ** payment_term)/ ((1+ int_rate) ** payment_term -1), 2)

        output = Label(frame, text=f'Monthly repayment = \tR {repayment:,}',font=('Arial Bold', 12))
        output.grid(row = 11, column = 0, columnspan=2, padx=5, pady=5)

        return repayment
    except:
	    print("Please insert a valid number.")
      
# Submit button
submit = Button(frame, text='CALCULATE',font=('Arial Bold',10),command=calculate)
submit.grid(row=9, column=0, columnspan=2)

# keep contents always centre of window
frame.place(relx=0.5, rely=0.5, anchor=CENTER) # .pack will not work because of the canvas

window.mainloop()
