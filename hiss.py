#!/usr/bin/python

import argparse
import matplotlib.pyplot as plt
import pandas as pd

def parse_command_line_input():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--input_filepath', help='Path to the input file with forward reads', required=True)
	command_line_args=parser.parse_args()	
	return command_line_args

def make_hist(n,input_data,Xcolname,bins):
	curr_num=0
	while curr_num<n:
		afig = input_data[curr_num][Xcolname].hist(bins=bins)
		yield afig
		curr_num=curr_num+1
		
	
#Input options: 1) one histogram from one spreadsheet, one histogram from multiple spreadsheets, multiple histograms from multiple spreadsheets, multiple histograms from one spreadsheet.

def load_data_from_file(filepaths,concatenate):
	input_data = []
	for filepath in filepaths:
		input_data.append(pd.read_csv(filepath,sep='[\t,]',engine='python'))
	if concatenate:
		input_data = (pd.concat(input_data,ignore_index=True))
	return input_data

def main():	
	filepath = "/Users/lekova/Desktop/dl1.mirnas.mature.ratio.txt"
	filepath2 = "/Users/lekova/Desktop/dl1.mirnas.mature.ratio.csv"
	input_data = load_data_from_file([filepath,filepath2],concatenate=False)

	Xcolname = 's5/s6'
	
	pd.options.display.mpl_style = 'default'	

	bins=10

	n=2

	figs=list(make_hist(n,input_data,Xcolname,bins))
	
	print(figs)
	
if __name__ == '__main__':
	main()
