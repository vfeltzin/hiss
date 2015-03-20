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
		self.bins = tk.IntVar()
		self.bintext = tk.StringVar()
		self.grouping_column = tk.StringVar()
		
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
		
	def create_more_widgets(self):
		self.optframe = ttk.Frame(self, padding=10)
		self.optframe.grid()
		self.concatcheck = ttk.Checkbutton(self.optframe, text='Combine data from multiple files', variable=self.concatenate)
		self.concatcheck.grid(row=4, column=0)
		self.groupbycheck = ttk.Checkbutton(self.optframe, text='Separate data by value in one column', variable=self.groupbycolumn, command=self.show_groupcolumnmenu)
		self.groupbycheck.grid(row=5, column=0)
		self.choosecolumnbutton = ttk.Menubutton(self.optframe, text='Choose column')
		self.binlabel = ttk.Label(self.optframe, text='Number of bins:')
		self.binlabel.grid(row=6, column=0)
		self.binslide = ttk.Scale(self.optframe, from_=10, to=150, variable=self.bins, value=50, command=self.change_bintext)
		self.binslide.grid(row=6, column=1)
		self.binvalue = ttk.Label(self.optframe, justify='center', textvariable=self.bintext)
		self.binvalue.grid(row=7, column=1)

		self.buttonframe = ttk.Frame(self, padding=10, style='TFrame')
		self.buttonframe.grid()
		self.histbutton = ttk.Button(self.buttonframe, text='Make histograms', command=self.make_hist)
		self.histbutton.grid()
				
	def choose_input_files(self):
		filepaths_to_open = fdialog.askopenfilenames()
		self.filepaths_to_open.set(filepaths_to_open)
		self.create_more_widgets()
		
	def choose_output_dir(self):
		output_dir = fdialog.askdirectory()
		self.output_dir.set(output_dir)

	def show_groupcolumnmenu(self):
		if self.groupbycolumn.get()==1:
			self.choosecolumnbutton.grid(row=5, column=1)
		else:
			self.choosecolumnbutton.grid_forget()

	def change_bintext(self, binval):
		binval = int(round(float(binval)))
		self.bintext.set(str(binval))
		
	def make_hist(self):
		list_of_input_filepaths = [hiss.process_path(apath) for apath in self.filepaths_to_open.get()]
		output_dir = hiss.process_path(self.output_dir.get())
		self.input_data = [hiss.load_data_from_file(apath) for apath in list_of_input_filepaths]

		if args.concatenate.get()==1:
			input_data = [concatenate_data(input_data)]
				
		if self.groupbycolumn == 1:
			grouped_temp = []
			for datum in input_data:
				grouped_temp.extend(group_data_by_column(datum))
			input_data = grouped_temp
			
		pd.options.display.mpl_style = 'default'	
			
		make_hist (input_data,args.Xcolname,args.bins,output_dir,args.groupbycolumn)


		hiss.make_hist(self.filepaths_to_open.get(), self.concatenate, int(self.bins.get()), self.output_dir.get(), self.groupbycolumn)

				
app = Application()

if sys.platform == 'darwin':
	os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' ''')

app.master.title('Histographer')

app.mainloop()
