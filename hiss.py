#!/usr/bin/python

import argparse
import matplotlib.pyplot as plt
import pandas as pd

def parse_command_line_input():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--input_filepath', help='Path to the input file with forward reads', required=True)
	command_line_args=parser.parse_args()	
	return command_line_args

def make_hist(x):
	plt.figure(num=1)
	plt.hist(x,bins=10)
	plt.show()
	
#Input options: 1) one histogram from one spreadsheet, one histogram from multiple spreadsheets, multiple histograms from multiple spreadsheets, multiple histograms from one spreadsheet.

def load_data_from_file(filepaths,concatenate):
	input_data = []
	for filepath in filepaths:
		input_data.append(pd.read_csv(filepath,sep='[\t,]',engine='python'))
	if concatenate:
		input_data = (pd.concat(input_data,ignore_index=True))
	return input_data
	
filepath = "/Users/lekova/Desktop/dl1.mirnas.mature.ratio.txt"
filepath2 = "/Users/lekova/Desktop/dl1.mirnas.mature.ratio.csv"
input_data = load_data_from_file([filepath,filepath2],concatenate=False)
print(input_data)