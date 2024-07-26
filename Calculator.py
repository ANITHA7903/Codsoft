# pip install tkinter
import tkinter as tk

root = tk.Tk()
root.geometry("370x500")
root.title('CALCULATOR')
frame = tk.Frame(root, background='grey',padx=50)

frame.pack(expand=True,fill='both')
entry = tk.Entry(frame, borderwidth=3, width=20,font = ('Arial',18),background='white')
entry.grid(row=0, column=0, columnspan=3, ipady=10, pady=10)


def myclick(number):
	entry.insert(tk.END, number)


def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
	entry.delete(0, tk.END)


button_1 = tk.Button(frame, text='1', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(1))

button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(frame, text='2', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(frame, text='3', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(frame, text='4', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(frame, text='5', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(frame, text='6', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(frame, text='7', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(frame, text='8', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(frame, text='9', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)

button_0 = tk.Button(frame, text='0', padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

button_add = tk.Button(frame, text="+", padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)

button_subtract = tk.Button(frame, text="-", padx=20, pady=15, width=3,background='skyblue',command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1, pady=2)

button_multiply = tk.Button(frame, text="*", padx=20, pady=15, width=3,background='skyblue' ,command=lambda: myclick('*'))
button_multiply.grid(row=5, column=2, pady=2)

button_div = tk.Button(frame, text="/", padx=20,
					pady=15, width=3, background='skyblue',command=lambda: myclick('/'))
button_div.grid(row=6, column=0, pady=2)

button_clear = tk.Button(frame, text="clear",
						padx=20, pady=15, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)

button_equal = tk.Button(frame, text="=", padx=20,
						pady=15, width=9, background='green',fg = 'white',command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

root.mainloop()
