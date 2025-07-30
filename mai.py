from  tkinter import *

window = Tk()
window.title('miles to kilometer converter')
window.config(padx=20, pady=20)
my_miles = Label(text="mile")
my_miles.grid(row=1, column=4)

def miles_to_km():
    miles = float(mile_input.get())
    km =round(miles*1.609344)
    result_in_km.config(text=f'{km}')



mile_input = Entry(width=7)
mile_input.grid(row = 1, column=3)

equal_to = Label(text="equal to")
equal_to.grid(row=3, column=2)

in_km  = Label(text='km')
in_km.grid(row=3, column=4)

result_in_km = Label(text= "0")
result_in_km.grid(row=3, column=3)

calculate_button = Button(text="claculate", command=miles_to_km)
calculate_button.grid(row=5 , column=2)

window.mainloop()