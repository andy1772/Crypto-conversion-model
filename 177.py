import tkinter
import tkinter.messagebox
import tkinter.ttk
import pandas as pd
import numpy as np
import json
import requests
import sys
"""Using the api link we print the response text in order to fetch the rates of the coins. If the link is wrong the code will end"""
try:
    response = requests.get('http://api.coinlayer.com/api/live?access_key=712c2202a94c299a4f61ad72410075ac&symbols=BNB,BTC,ETH,XRP')
    data = json.loads(response.text)
    print(json.dumps(data, indent=7))
    rate = data["rates"]
except Exception as err:
    raise Exception("Double check the API link")
    sys.exit(1)
"""Convert_currency fetches the numbers written from the program's labels and creates a list of the coins in the order the response text is. If the user doesn't write a number an error will appear"""
"""After creating the list I used numpy to multiply the rate times the quantity the user put and divide 1 by the rate to find the exchange rate"""
"""Using pandas I created a dataframe following the specifications from the Homework instructions"""
def convert_currency():
    global number_1,number_2,number_3,number_4

    try:
        enter_1 = float(number_1.get())
        enter_2 = float(number_2.get())
        enter_3 = float(number_3.get())
        enter_4 = float(number_4.get())

        coins = [enter_2,enter_1,enter_3,enter_4]

        tkinter.messagebox.showinfo("Complete", "The conversions were stored in crypto_conversion.csv.")
    except ValueError:
        tkinter.messagebox.showerror("Error", "Sorry, the report could not be written. Check that only numeric values are entered/All entries are filled.")

    currency = rate.keys()
    price = rate.values()
    price = list(price)
    cost_usd = list(np.multiply(price,coins))
    exchange_rate = list(np.divide(1, price))

    info = {'Currency': currency,
               'Price': price,
               'Quantity': coins,
               'Cost (USD)': cost_usd,
               'Exchange Rate USD:COIN': exchange_rate
               }

    df = pd.DataFrame(info)

    total_cost_usd = df['Cost (USD)'].sum()
    new_row = {'Currency': '--', 'Price': '--', 'Quantity': '--', 'Cost (USD)': '--', 'Exchange Rate USD:COIN': '--'}
    new_row1 = {'Currency': 'Total', 'Price': '--', 'Quantity': '--', 'Cost (USD)': total_cost_usd, 'Exchange Rate USD:COIN': '--'}

    df1 = df.append(new_row, ignore_index=True)
    df2 = df1.append(new_row1, ignore_index=True)
    df2.to_csv('crypto_conversion.csv', index=False)

def closeConverter():
    print("Have a nice day!")
    root.destroy()
"""Four labels with four different entries and two buttons that allows the user to write any number that follow the code set up for the functions."""
root = tkinter.Tk()
root.title("Crypto Exchange Rate Calculator.")
root.configure(bg = "bisque")

label_1 = tkinter.Label(root, text = "BTC:")
label_1.configure(bg = "bisque")
label_1.grid(row = 0, column = 0)

number_1 = tkinter.Entry(root, width = 7)
number_1.grid(row = 0, column = 1)

label_2 = tkinter.Label(root, text = "BNB:")
label_2.configure(bg = "bisque")
label_2.grid(row = 2, column = 0)

number_2 = tkinter.Entry(root, width = 7)
number_2.grid(row = 2, column = 1)

label_3 = tkinter.Label(root, text = "ETH:")
label_3.configure(bg = "bisque")
label_3.grid(row = 0, column = 2)

number_3 = tkinter.Entry(root, width = 7)
number_3.grid(row = 0, column = 3)

label_4 = tkinter.Label(root, text = "XRP:")
label_4.configure(bg = "bisque")
label_4.grid(row = 2, column = 2)

number_4 = tkinter.Entry(root, width = 7)
number_4.grid(row = 2, column = 3)

convert_button = tkinter.Button(root, text = "Convert Currency", command = convert_currency)
convert_button.grid(row = 0, column = 7, padx=5,pady=5)
convert_button.configure(bg = "pale green")

close_button = tkinter.Button(root, text = "Close Converter", command = closeConverter)
close_button.grid(row = 2, column = 7, padx=5,pady=5)
close_button.configure(bg = "dark orange")

root.mainloop()
