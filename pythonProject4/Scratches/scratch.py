from tkinter import *

root = Tk()

variable1 = StringVar(root)
variable2 = StringVar(root)

variable1.set("currency")
variable2.set("currency")

usdCurrency = 92.75


def RealTimeCurrencyConversion():
    clear_result()
    from_currency = variable1.get()
    to_currency = variable2.get()

    amount = float(Amount1_field.get())

    if from_currency == "USD" and to_currency == "RUB":
        result = amount * usdCurrency
    else:
        result = amount / usdCurrency

    new_amount = round(result, 3)
    Amount2_field.insert(0, str(new_amount))

    report_text = "Пользователь перевел из " + from_currency + " в " + to_currency + ". Результат: " + str(new_amount)
    with open("report.txt", "w") as file:
        file.write(report_text)


def clear_result():
    Amount2_field.delete(0, END)


if __name__ == "__main__":
    root.configure(background='light green')
    root.geometry("400x175")
    headlabel = Label(root, text='Конвертер валют', fg='black', bg="red")
    label1 = Label(root, text="Количество: ", fg='black', bg='dark green')
    label2 = Label(root, text="Из валюты", fg='black', bg='dark green')
    label3 = Label(root, text="В валюту", fg='black', bg='dark green')
    label4 = Label(root, text="Итог:", fg='black', bg='dark green')

    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    label3.grid(row=3, column=0)
    label4.grid(row=5, column=0)

    Amount1_field = Entry(root)
    Amount2_field = Entry(root)

    Amount1_field.grid(row=1, column=1, ipadx="25")
    Amount2_field.grid(row=5, column=1, ipadx="25")

    CurrenyCode_list = ["USD", "RUB"]

    FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list)
    ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list)

    FromCurrency_option.grid(row=2, column=1, ipadx=10)
    ToCurrency_option.grid(row=3, column=1, ipadx=10)

    button1 = Button(root, text="Конвертировать", bg="red", fg="black",
                     command=RealTimeCurrencyConversion)

    button1.grid(row=4, column=1)

    button2 = Button(root, text="Очистить", bg="red",
                     fg="black", command=clear_result)
    button2.grid(row=6, column=1)

    root.mainloop()
