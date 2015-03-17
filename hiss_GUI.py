#!/usr/bin/python

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fdialog
import hiss
import sys
import os

class Application(ttk.Frame):
	
	def __init__(self, master=None):
		ttk.Frame.__init__(self,master)
		
		self.filepaths_to_open = tk.StringVar()
		self.output_dir = tk.StringVar()
		self.concatenate = tk.IntVar()
		self.groupbycolumn = tk.IntVar()
		
		self.grid()
		self.create_styles()
		self.create_widgets()
		
	def create_styles(self):
		s = ttk.Style()
		s.configure('TFrame', bg='#EAEAEA')
		s.configure('TButton', bg='white', relief='flat' )
		s.configure('File.TButton', bg='#EAEAEA', relief='flat')
		s.configure('File.TFrame', bg='#EAEAEA')

	def create_widgets(self):
		self.fileframe = ttk.Frame(self, padding=10)
		self.fileframe.grid()
		
		self.openfilelabel = ttk.Label(self.fileframe, text='Select files to open:')
		self.openfilelabel.grid(row=0)
		self.openfileentry = ttk.Entry(self.fileframe, textvariable = self.filepaths_to_open, width=40)
		self.openfileentry.grid(row=1,column=0)
		self.openfilebutton = ttk.Button(self.fileframe, text='Browse', command=self.choose_input_files)
		self.openfilebutton.grid(row=1,column=1)
		
		self.outputdirlabel = ttk.Label(self.fileframe, text='Select folder to save histograms:', justify='left')
		self.outputdirlabel.grid(row=2)
		self.outputdirentry = ttk.Entry(self.fileframe, textvariable = self.output_dir, width=40)
		self.outputdirentry.grid(row=3,column=0)
		self.savefilebutton = ttk.Button(self.fileframe, text='Browse', command=self.choose_output_dir)
		self.savefilebutton.grid(row=3,column=1)
		
		self.optframe = ttk.Frame(self, padding=10)
		self.optframe.grid()
		self.concatcheck = ttk.Checkbutton(self.optframe, text='Combine data from multiple files.', variable=self.concatenate)
		self.concatcheck.grid(row=4, column=0)
		self.groupbycheck = ttk.Checkbutton(self.optframe, text='Separate data by value in one column.', variable=self.groupbycolumn, command=self.show_groupcolumnmenu)
		self.groupbycheck.grid(row=5, column=0)

		self.buttonframe = ttk.Frame(self, padding=10, style='TFrame')
		self.buttonframe.grid()
		self.histbutton = ttk.Button(self.buttonframe, text='Make histograms', command=self.make_hist)
		self.histbutton.grid()
				
	def choose_input_files(self):
		filepaths_to_open = fdialog.askopenfilenames()
		self.filepaths_to_open.set(filepaths_to_open)
		
	def choose_output_dir(self):
		output_dir = fdialog.askdirectory()
		self.output_dir.set(output_dir)

	def show_groupcolumnmenu(self):
		if self.groupbycolumn == 1:
			#Show menu to choose column to group by.
			pass
		else:
			#Hide menu to choose column to group by.
			pass

	def make_hist(self):
		hiss.make_hist(self.filepaths_to_open)

				
app = Application()

if sys.platform == 'darwin':
	os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

app.master.title('Histographer')

app.mainloop()
