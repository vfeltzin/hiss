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
	
filepath = "/Users/lekova/Desktop/dl1.mirnas.mature.ratio.csv"	
def load_data_from_file(filepath):
	array = pd.read_csv(filepath,sep='[\t,]',engine='python')
	print(array)
	
	
load_data_from_file(filepath)