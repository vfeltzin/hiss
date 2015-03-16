#!/usr/bin/python

import tkinter as tk
import hiss

class Application(tk.Frame):
	
	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.grid()
		self.createWidgets()
		
	def createWidgets(self):
		self.quitButton = tk.Button(self, text='Make histograms', command=hiss.make_hist)
		self.quitButton.grid()
		
app = Application()

app.master.title('Sample application')

app.mainloop()