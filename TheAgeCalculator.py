from tkinter import *
from datetime import *
from calendar import *



Window = Tk()
Window.geometry('400x430')
Window.title('AGE CALCULATOR | GBOLAHAN ALABA')
Window.wm_iconbitmap('ageicon.ico')
Window.configure(bg='#c0392b')
Window.resizable(width=False, height=False)



def checkdate():
    a = datetime.now().year
    b = int(YearEntry.get())
    c = datetime.now().month
    d = int(MonthEntry.get())
    e = datetime.now().day
    f = int(DayEntry.get())
    g = monthrange(a, d)[1]
    ab = a - b
    cd = c - d
    ef = e - f
    # years
    YearResult.set(ab)

    # months
    cd = c - d
    if d > c and f > e:
        w = ab - 1
        x = 12 - d + c - 1
        y = c - 1
        z = monthrange(a, y)[1] + e - f
        YearResult.set(w)
        MonthResult.set(x)
        DayResult.set(z)
    elif d <= c and f <= e:
        YearResult.set(ab)
        MonthResult.set(cd)
        DayResult.set(ef)
    elif d > c and f < e:
        x = ab - 1
        y = 12 - d + c
        YearResult.set(x)
        MonthResult.set(y)
        DayResult.set(ef)
    elif d == c and f > e:
        w = ab - 1
        x = 12 - d + c - 1
        y = c - 1
        z = monthrange(a, y)[1] + e - f
        YearResult.set(w)
        MonthResult.set(x)
        DayResult.set(z)
    elif d < c and f > e:
        x = cd - 1
        y = monthrange(a, cd)[1] + e - f
        YearResult.set(ab)
        MonthResult.set(x)
        DayResult.set(y)

    else:
        MonthResult.set(cd)
    if b > a:
        Wrong.set('Incorrect year entry!')
        YearResult.set(0)
        MonthResult.set(0)
        DayResult.set(0)
    elif d > 12:
        Wrong.set('Incorrect month entry!')
        YearResult.set(0)
        MonthResult.set(0)
        DayResult.set(0)
    elif f > g:
        Wrong.set('Incorrect day entry!')
        YearResult.set(0)
        MonthResult.set(0)
        DayResult.set(0)
    elif b == a and d == c and f > e:
        Wrong.set('Incorrect, year, month or day!')
        YearResult.set(0)
        MonthResult.set(0)
        DayResult.set(0)


def clear():
    YearResult.set(0)
    MonthResult.set(0)
    DayResult.set(0)
    Wrong.set('')

    YearEntry.delete(0, END)
    MonthEntry.delete(0, END)
    DayEntry.delete(0, END)
    

    

TitleFrame = Frame(Window, highlightthickness=5, highlightbackground='yellow')
TitleFrame.pack(fill=X, expand='no', padx=10, pady=10)

TitleLabel = Label(TitleFrame, text='AGE CALCULATOR', font=('calibri', 18, 'bold'))
TitleLabel.pack(padx=10, pady=10)

YearResult = IntVar()
MonthResult = IntVar()
DayResult = IntVar()
Wrong = StringVar()


RecordFrame = LabelFrame(Window, text='Date Of Birth')
RecordFrame.pack(fill=X, expand='no', padx=10, pady=10)

YearLabel = Label(RecordFrame, text='Year', font=('calibri', 13, 'bold'))
YearLabel.grid(row=0, column=0, padx=10, pady=10)
YearEntry = Entry(RecordFrame, font=('calibri', 12, 'bold'))
YearEntry.grid(row=0, column=1, padx=10, pady=10)

MonthLabel = Label(RecordFrame, text='Month', font=('calibri', 13, 'bold'))
MonthLabel.grid(row=1, column=0, padx=10, pady=10)
MonthEntry = Entry(RecordFrame, font=('calibri', 12, 'bold'))
MonthEntry.grid(row=1, column=1, padx=10, pady=10)

DayLabel = Label(RecordFrame, text='Day', font=('calibri', 13, 'bold'))
DayLabel.grid(row=2, column=0, padx=10, pady=10)
DayEntry = Entry(RecordFrame, font=('calibri', 12, 'bold'))
DayEntry.grid(row=2, column=1, padx=10, pady=10)

ResultFrame = LabelFrame(Window, text='Outcome')
ResultFrame.pack(fill=X, expand='no', padx=10, pady=10)

ResultLabel = Label(ResultFrame, text='Result:', font=('calibri', 13, 'bold'))
ResultLabel.grid(row=0, column=0, padx=10)

ResultLabelYR = Label(ResultFrame, textvariable=YearResult, font=('calibri', 15, 'bold'), bg='white', fg='green')
ResultLabelYR.grid(row=0, column=1)

ResultLabelY = Label(ResultFrame, text='Years,', font=('calibri', 13, 'bold'))
ResultLabelY.grid(row=0, column=2, padx=5)

ResultLabelMR = Label(ResultFrame, textvariable=MonthResult, font=('calibri', 15, 'bold'), bg='white', fg='green')
ResultLabelMR.grid(row=0, column=3)

ResultLabelM = Label(ResultFrame, text='Months,', font=('calibri', 13, 'bold'))
ResultLabelM.grid(row=0, column=4, padx=5)

ResultLabelDR = Label(ResultFrame, textvariable=DayResult, font=('calibri', 15, 'bold'), bg='white', fg='green')
ResultLabelDR.grid(row=0, column=5)

ResultLabelD = Label(ResultFrame, text='Days', font=('calibri', 13, 'bold'))
ResultLabelD.grid(row=0, column=6, padx=5)

ErrorLabel = Label(Window, textvariable=Wrong, bg='#c0392b', fg='white', font=('calibri', 13, 'bold'))
ErrorLabel.pack(fill=X, padx=40, pady=180)
Button1 = Button(Window, text='Check', font=('calibri', 12, 'bold'), bd=5, bg='white', fg='green',
                 activebackground='green', activeforeground='white', command=checkdate)
Button1.place(x=70, y=370)

Button2 = Button(Window, text='Clear', font=('calibri', 12, 'bold'), bd=5, bg='white', fg='red',
                 activebackground='red', activeforeground='white', command=clear)
Button2.place(x=272, y=370)

mainloop()

# EntryYear.insert(1, 'Type in')
# # Entry1.config(state=DISABLED)
