from tkinter import *

def calculate():
    KM = int(m_enter.get()) * 1.60934
    km_enter.config(text=KM)

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=500, height=500)

m_enter = Entry(width=50)
m_enter.grid(column=1, row=0)


m_label = Label(text="Miles", font="bold")
m_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_enter = Label(text="0", font="bold")
km_enter.grid(column=1, row=1)

km_label = Label(text="KM", font="bold")
km_label.grid(column=2, row=1)

calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=2)


window.mainloop()
