#!/usr/bin/python

import argparse
import matplotlib.pyplot as plt
import pandas as pd

def parse_command_line_input():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--inputfiles', required=True,action='append')
	parser.add_argument('--concatenate',action='store_true')
	parser.add_argument('--groupbycolumn',action='store_true')
	args = parser.parse_args()
	return args	
	
#Input options: 1) one histogram from one spreadsheet, one histogram from multiple spreadsheets, multiple histograms from multiple spreadsheets, multiple histograms from one spreadsheet.

def load_data_from_file(filepaths,concatenate,groupbycolumn,grouping_column):
	input_data = [pd.read_csv(filepath,sep='[\t,]',engine='python') for filepath in filepaths]
	if concatenate:
		input_data = (pd.concat(input_data,ignore_index=True))
	if groupbycolumn:
		grouped_input_data=[]
		for datum in input_data:
			grouped = datum.groupby(grouping_column)
			for k,gp in grouped:
				grouped_input_data.append(gp)
		input_data = grouped_input_data
	return input_data

def main():	
	#filepath = "C:/Users/Virzhiniya/Desktop/test.txt"
	#filepath2 = "C:/Users/Virzhiniya/Desktop/test.txt"
	args = parse_command_line_input()
	input_data = load_data_from_file(args.inputfiles,args.concatenate,args.groupbycolumn,grouping_column='grouping')
	
	print(input_data)

	Xcolname = 's5/s6'
	
	pd.options.display.mpl_style = 'default'	

	bins=10

	n=2

	for datum in input_data:
		datum[Xcolname].hist(bins=bins)
		plt.show()

	
if __name__ == '__main__':
	main()
