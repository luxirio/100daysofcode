import tkinter

window = tkinter.Tk()
window.title("Miles to Km Widget")
window.minsize(width=500, height=150)
window.geometry("500x100")
window.config(padx=10, pady=10)

font_defaults = {"font" : ("Arial", 20, "bold")}

# Labels using grid method
miles_text = tkinter.Label(text="Miles", **font_defaults)
miles_text.grid(row=0,column=2)

is_equal_to = tkinter.Label(text="is equal to", **font_defaults)
is_equal_to.grid(row=1,column=0)

km_text = tkinter.Label(text="kilometers", **font_defaults)
km_text.grid(row=1,column=2)


# Converter
def miles_convert():
    miles = int(miles_input.get())
    kilometers = miles * 1.609
    result_text["text"] = round(kilometers,2)
    return result_text["text"]

#Buttons
calculate = tkinter.Button(text="Calculate", command=miles_convert)
calculate.grid(row=2, column=1)

# Input
miles_input = tkinter.Entry(width=30)
miles_input.grid(row=0, column=1)

# Result
result_text = tkinter.Label(text="0", **font_defaults)
result_text.grid(row=1, column=1)

window.mainloop()
