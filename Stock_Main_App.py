#importing libraries
import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import tkinter as tk
from PIL import ImageTk, Image
import requests
import pandas as pd 
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from matplotlib import style  

root=tk.Tk()
root.title("Stock App")
inputValue=tk.StringVar()
DATA=tk.StringVar()
#========================API No:1 Getting the data from the API and printing data in the new tab with same format=============================================	
def get_name():
    inputValue=Entry.get()
    ts=TimeSeries(key='Q5PZV4ADMZIUI2VT',output_format='pandas')
    DATA, meta_data=ts.get_daily(symbol=inputValue)
    root=tk.Toplevel()
    tk.Canvas()
    Label=tk.Label()
    photo = ImageTk.PhotoImage(Image.open("D:\\Profile\\Desktop\\Photos\\stockmrkt.jpg"))
    logo = tk.Label(root, image=photo)
    logo.pack()
    lower_frame=tk.Entry(root,bg="#80c1ff",bd=5)
    lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')
    label=tk.Label(lower_frame,text=DATA,font=('courier',10),anchor='nw',justify='left',bd=4)
    label.place(relwidth=1,relheight=1)
    tk.mainloop()
#===================API No:2 Getting data from the different API to understand API's better, and use matplotlib for data visualization=====================================
def open_graph():
	style.use('seaborn')
	figure=plt.figure(0)
	inputValue=Entry.get()
	figure.canvas.set_window_title(inputValue+" Graph")
	start=dt.datetime(2020,2,14)
	end=dt.datetime(2020,3,14)
	df=web.DataReader(inputValue,'yahoo',start,end)
	df['Open'].plot(ls='--',color='r')
	df['Close'].plot(color='B')
	plt.show()
tk.Canvas()
#=====================================Adding background  image  ======================     ===================================================================================
photo = ImageTk.PhotoImage(Image.open("D:\\Profile\\Desktop\\Photos\\stockmrkt.jpg"))
logo = tk.Label(root, image=photo)
logo.pack()
#================================================Body parts of the GUI====================================================================================================
Frame=tk.Frame(root,bg="#80c1ff",bd=5)
Frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

Entry=tk.Entry(Frame,font=40,bd=4)
Entry.place(relwidth=0.3,relheight=1)

Button=tk.Button(Frame,text="Stock Values",bg="Grey",font=40,command=lambda:get_name())
Button.place(relx=0.48,rely=0.1,anchor='n',relwidth=0.32)

Buttongraph=tk.Button(Frame,text="Stock Graphs",bg="Grey",font=40,command=lambda:open_graph())
Buttongraph.place(relx=0.83,rely=0.1,anchor='n',relwidth=0.32)

lower_frame=tk.Entry(root,bg="#80c1ff",bd=5)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame,text="The main purpose of this program\nis getting the stock values and \nplotting the opening and closing values.\nIf you want to see the stock values,\nPlease insert the name of the stock(i.g MSFT), \nand click the stock values button.\nFurthermore, if you want to see the graphs,\nPlease click Stock Graphs button.\nMoving average,\nand date setting will be implemented.",
	font=('courier',14),anchor='nw',justify='left',bd=4)
label.place(relwidth=1,relheight=1)


tk.mainloop()
