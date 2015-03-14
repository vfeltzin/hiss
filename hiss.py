#!/usr/bin/python

import argparse
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import math

def parse_command_line_input():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--inputfiles', required=True,action='append')
	parser.add_argument('--concatenate',action='store_true')
	parser.add_argument('--Xcolname', required=True)
	parser.add_argument('-b','--bins',type=int)
	parser.add_argument('--groupbycolumn')
	args = parser.parse_args()
	return args	
	
def load_data_from_file(filepaths,concatenate,groupbycolumn):
	input_data = [pd.read_csv(filepath,sep='[\t,]',engine='python') for filepath in filepaths]
	if concatenate:
		input_data = (pd.concat(input_data,ignore_index=True))
	if groupbycolumn != None:
		grouped_input_data=[]
		for datum in input_data:
			grouped = datum.groupby(groupbycolumn)
			for k,gp in grouped:
				grouped_input_data.append(gp)
		input_data = grouped_input_data
	return input_data

def determine_bins_for_hist(x):
	Doanes_bins = (1 + math.log(x.count(),2)+scipy.stats.moment(x,3))
	print("Optimal number of bins for a histogram of these data according to Doane's formula: " + str(Doanes_bins))
	return Doanes_bins

def main():	
	args = parse_command_line_input()
	input_data = load_data_from_file(args.inputfiles, args.concatenate, args.groupbycolumn)
	
	print(input_data)
	pd.options.display.mpl_style = 'default'	

	for datum in input_data:
		if args.bins == None:
			args.bins = determine_bins_for_hist(datum[args.Xcolname])
		datum[args.Xcolname].hist(bins=args.bins)
		plt.show()

	
if __name__ == '__main__':
	main()
