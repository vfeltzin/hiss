#!/usr/bin/python

import argparse
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import moment
from math import log as mathlog
import os

##To do:
##Refactor this so that most functions take a simgle element instead of a list and the for-loop is executed in the main fuction instead
##Add a way to handle excel spreadsheets - pandas can do it, so I might as well put it in
##What happens if there are no header columns in the supplied spreadsheets
##Sort out the file naming logic again
##Change the function that validates filepaths, so that it raises an exception, rather than print an error message - the exception can then also be handled by the gui

def parse_command_line_input():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--input_files', required=True,action='append')
	parser.add_argument('-o','--output_dir',required=True)
	parser.add_argument('x','--Xcolname', required=True)
	parser.add_argument('-c','--concatenate',action='store_true')
	parser.add_argument('-b','--bins',type=int)
	parser.add_argument('g','--groupbycolumn')
	args = parser.parse_args()
	return args	
	
def process_path(apath):
	filepath = os.path.abspath(apath)
	if os.path.exists(apath) == False:    ##This should be changed to try, except statement
		print('ERROR: No such file or directory ' + apath)
	return apath

def load_data_from_file(filepath):
	input_dataframe = pd.read_csv(filepath,sep='[\t,]',engine='python')
	return input_dataframe
	
def concatenate_data (list_of_dataframes):
	"""Concatenate list of pandas DataFrames."""
	cooncatenated = pd.concat(input_data,ignore_index=True)
	return concatenated
	
def group_data_by_column(dataframe,groupbycolumn):
	"""This function takes a pandas DataFrame object and a string specifying the name of a column in the DataFrame. It separates the data into two or more smaller DataFrames based on the values in the specified column, and returns a list of the smaller DataFrames."""
	grouped = dataframe.groupby(groupbycolumn)
	input_dataframes = [gp for k,gp in grouped]
	return input_dataframes
	
def determine_bins_for_hist(x):
	"""Estimate optimal number of bins for a histogram based on Doane's formula"""
	Doanes_bins = (1 + mathlog(x.count(),2) + moment(x,3))
	print("Optimal number of bins for a histogram of these data according to Doane's formula: " + str(Doanes_bins))
	return Doanes_bins

def make_hist(input_data,Xcolname,bins,output_dir,groupbycolumn):
	for datum in input_data:
		if bins == None:
			bins = determine_bins_for_hist(datum[Xcolname])
		datum[Xcolname].hist(bins=bins)
		plt.savefig(os.path.abspath(output_dir+'/'+groupbycolumn+'_hist'+str(input_data.index(datum)+1)+'.png'))

def main():	
	args = parse_command_line_input()
	list_of_input_filepaths = [process_path(apath) for apath in args.input_files]
	output_dir = process_path(args.output_dir)
	input_data = [load_data_from_file(apath) for apath in list_of_input_filepaths]
	
	if args.concatenate:
		input_data = [concatenate_data(input_data)]
		
	if args.groupbycolumn != None:
		grouped_temp = []
		for datum in input_data:
				grouped_temp.extend(group_data_by_column(datum))
		input_data = grouped_temp
	
	pd.options.display.mpl_style = 'default'	
	
	make_hist (input_data,args.Xcolname,args.bins,output_dir,args.groupbycolumn)

	
if __name__ == '__main__':
	main()
