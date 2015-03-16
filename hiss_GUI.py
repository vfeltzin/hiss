#!/usr/bin/python

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fdialog
import hiss

class Application(tk.Frame):
	
	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		
		self.filepaths_to_open = tk.StringVar()
		self.output_dir = tk.StringVar()
		
		self.grid()
		self.createWidgets()
		
		
		
	def createWidgets(self):
		
		s = ttk.Style()
		s.configure('TFrame', bg='maroon')
		s.configure('TButton', bg='white', relief='flat' )
		s.configure('File.TButton', bg='#AAAAAA', relief='flat')
		s.configure('File.TFrame', bg='#EAEAEA')
		
		self.fileframe = ttk.Frame(self, padding=10)
		self.fileframe.grid()
		
		self.openfilelabel = ttk.Label(self.fileframe, text='Select files to open:')
		self.openfilelabel.grid(row=0)
		self.openfileentry = ttk.Entry(self.fileframe, textvariable = self.filepaths_to_open, width=40)
		self.openfileentry.grid(row=1,column=0)
		self.openfilebutton = ttk.Button(self.fileframe, text='Browse', command=self.choose_input_files, style='Gray.TButton')
		self.openfilebutton.grid(row=1,column=1)
		
		self.outputdirlabel = ttk.Label(self.fileframe, text='Select folder to save histograms:', justify='left')
		self.outputdirlabel.grid(row=2)
		self.outputdirentry = ttk.Entry(self.fileframe, textvariable = self.output_dir, width=40)
		self.outputdirentry.grid(row=3,column=0)
		self.savefilebutton = ttk.Button(self.fileframe, text='Browse', command=self.choose_output_dir, style='Gray.TButton')
		self.savefilebutton.grid(row=3,column=1)
		
		self.buttonframe = ttk.Frame(self, padding=10, style='TFrame')
		self.buttonframe.grid()
		self.histbutton = ttk.Button(self.buttonframe, text='Make histograms', command=self.make_hist, style='TButton')
		self.histbutton.grid()
				


	def choose_input_files(self):
		filepaths_to_open = fdialog.askopenfilenames()
		self.filepaths_to_open.set(filepaths_to_open)
		
	def choose_output_dir(self):
			output_dir = fdialog.askdirectory()
			self.output_dir.set(output_dir)
		
	def make_hist(self):
		hiss.make_hist(self.filepaths_to_open)
				
app = Application()

app.master.title('Sample application')

app.mainloop()