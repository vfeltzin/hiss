#!/usr/bin/python

import argparse
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import math
import os

def parse_command_line_input():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--inputfiles', required=True,action='append')
	parser.add_argument('-o','--output_dir',required=True)
	parser.add_argument('--concatenate',action='store_true')
	parser.add_argument('--Xcolname', required=True)
	parser.add_argument('-b','--bins',type=int)
	parser.add_argument('--groupbycolumn')
	args = parser.parse_args()
	return args	
	
def process_paths(filepaths):
	for apath in filepaths:
		apath = os.path.abspath(apath)
		if os.path.isdir(apath):
			for (dirpaths, dirnames, filenames) in os.walk(apath):
				filepaths.extend(filenames)
				break
		elif os.path.isfile(apath):
			pass
		else:
			print('ERROR: No such file or directory ' + filepath)
	return filepaths

def process_output_dir(dirpath):
	dirpath = os.path.abspath(dirpath)
	if os.path.isdir(dirpath):
		pass
	else:
		print('ERROR: No such directory ' + dirpath)
	return dirpath

def load_data_from_file(filepaths,concatenate,groupbycolumn):
	input_data = [pd.read_csv(filepath,sep='[\t,]',engine='python') for filepath in filepaths]
	if concatenate:
		input_data = [pd.concat(input_data,ignore_index=True)]
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

def make_hist(input_data,Xcolname,bins,output_dir):
	for datum in input_data:
		if bins == None:
			bins = determine_bins_for_hist(datum[Xcolname])
		datum[Xcolname].hist(bins=bins)
		plt.savefig(os.path.abspath(output_dir+'\\'+'hist'+str(input_data.index(datum)+1)+'.png'))

def main():	
	args = parse_command_line_input()
	filepaths = process_paths(args.inputfiles)
	output_dir = process_output_dir(args.output_dir)
	input_data = load_data_from_file(filepaths, args.concatenate, args.groupbycolumn)
	
	print(input_data)
	pd.options.display.mpl_style = 'default'	
	
	make_hist (input_data,args.Xcolname,args.bins,output_dir)

	
if __name__ == '__main__':
	main()
