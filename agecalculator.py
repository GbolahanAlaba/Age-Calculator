from tkinter import *

from datetime import *
Window = Tk()
Window.geometry('400x300')
Window.title('AGE CALCULATOR')
Window.configure(bg='indianred')



def check():
    x = int(Entry1.get())
    y = datetime.now().year

    if x > y:
        Result.set('Error! (Out of range)')

    elif Entry1.get():
        x = Entry1.get()
        y = datetime.now().year
        z = y - int(x)
        Result.set(z)
    else:
        Result.set('Error! (Input the year)')

    # if Entry1.get():
    #     x = Entry1.get()
    #     y = datetime.now().year
    #     z = y - int(x)
    #     Result.set(z)
    # else:
    #     Result.set('Error! (Input the year)')


TitleFrame = Frame(Window, highlightthickness=5, highlightbackground='red')
TitleFrame.pack(fill=X, expand='no', padx=10, pady=10)

TitleLabel = Label(TitleFrame, text='AGE CALCULATOR', font=('calibri', 18, 'bold'))
TitleLabel.pack(padx=10, pady=10)

Result = IntVar()

Label1 = Label(Window, text='Enter Your Age/Year', font=('calibri', 13, 'bold'))
Label1.pack(pady=5)

Entry1 = Entry(Window, font=('calibri', 12, 'bold'))
Entry1.insert(0, 'Type in')
# Entry1.config(state=DISABLED)
Entry1.pack(pady=10)

Button1 = Button(Window, text='Check', font=('calibri', 12, 'bold'), bd=5, fg='green',
                 activebackground='red', activeforeground='white', command=check)
Button1.pack(pady=10)

ResultLabel = Label(Window, text='The Age Is', font=('calibri', 12, 'bold'))
ResultLabel.pack()

ResultLabel1 = Label(Window, textvariable=Result, font=('calibri', 20, 'bold'), bg='white', fg='red')
ResultLabel1.pack()

mainloop()
