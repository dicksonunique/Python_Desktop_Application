import tkinter as tk
from functools import partial

def weight(result,weight, unit):
    weight = float(weight.get())
    unit   = (unit.get())
    if unit.upper() == 'K':
        results = float( weight / 0.45)
        result.config(text = 'Result of {}{} = {}'.format(weight, unit, results))
        
    else:
        results =float(weight * 0.45)
        result.config(text = 'Result = %d' %results)
    return

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200+100+200")
    root.title('Convert from to k(g) or L(bs)')
    enter_weight = tk.StringVar()
    enter_unit = tk.StringVar()
    tk.Label(root, text = 'Convert from to k(g) to L(bs) and vice versa',fg ='navy', font = ('Times',14)).place(x = 0, y = 0)
    l_num1 = tk.Label(root, text = 'Enter weight', font = ('Times',14)).place(x = 30, y = 50)
    l_num2 = tk.Label(root, text = 'Enter Unit in k(g) or L(bs)', font = ('Times',14)).place(x = 30, y = 90)
    weight_result = tk.Label(root, fg = 'navy', font = ('Times',12))
    weight_result.place(x = 130, y = 120)
    t1 = tk.Entry(root, textvariable = enter_weight )
    t2 = tk.Entry(root, textvariable = enter_unit)
    t1.place(x = 240, y = 50)
    t2.place(x = 240, y = 90)
    weight = partial(weight, weight_result, enter_weight, enter_unit)
    b1 = tk.Button(root, text = 'Submit', fg = 'brown',font = ('Times',11), command = weight )
    b1.place(x = 140, y = 150)
    root.mainloop()
