import tkinter

root = tkinter.Tk()
var = tkinter.StringVar()
label = tkinter.Label( root, textvariable=var)

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()

Btn = tkinter.Button(root, text="wow")
Btn.pack()

window.mainloop()