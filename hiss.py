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
	
def load_data_from_file(filepaths):
	input_data = []
	for filepath in filepaths:
		input_data.append(pd.read_csv(filepath,sep='[\t,]',engine='python'))
	data = (pd.concat(input_data,ignore_index=True))
	
filepath = "/Users/lekova/Desktop/dl1.mirnas.mature.ratio.txt"
filepath2 = "/Users/lekova/Desktop/dl1.mirnas.mature.ratio.csv"
load_data_from_file([filepath,filepath2])