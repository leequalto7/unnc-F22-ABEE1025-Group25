import os
import json
import copy
from StaticEplusEngine import run_eplus_model, convert_json_idf
import numpy as np
import pandas as pd


def run_one_simulation_helper(eplus_run_path, idf_path, output_dir, parameter_key1, parameter_key2, parameter_val1, parameter_val2):
	convert_json_idf(eplus_run_path, idf_path)
	epjson_path = idf_path.split('.idf')[0] + '.epJSON'

	with open(epjson_path) as f:
		epjson_dict = json.load(f)

	inner_dict1 = epjson_dict
	inner_dict2 = epjson_dict
	for i in range(len(parameter_key1)):
		if i < len(parameter_key1) - 1:
			inner_dict1 = inner_dict1[parameter_key1[i]]
		inner_dict1[parameter_key1[-1]] = parameter_val1
	for k in range(len(parameter_key2)):
		if k < len(parameter_key2) - 1:
			inner_dict2 = inner_dict2[parameter_key2[k]]
		inner_dict2[parameter_key2[-1]] = parameter_val2
	print('============================================')
	print(inner_dict1)
	print(output_dir)
	print('============================================')

	with open(epjson_path, "w") as f:
		json.dump(epjson_dict, f)

	convert_json_idf(eplus_run_path, epjson_path)

	run_eplus_model(eplus_run_path, idf_path, output_dir)
	res_pt = os.path.join(output_dir, "eplusout.csv")
	return res_pt

def run_function(eplus_run_path, idf_path, output_dir, parameter_key1, parameter_key2, parameter_vals1, parameter_vals2):
	output_paths = {}
	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)
	max_y = 0
	max_y_x = None
	for i in range(0,len(parameter_vals1)):
		para_val1=parameter_vals1[i]
		for k in range(0,len(parameter_vals2)):
			para_val2=parameter_vals2[k]
			new_output=output_dir
			this_res_path = run_one_simulation_helper(eplus_run_path, idf_path, new_output, parameter_key1, parameter_key2, para_val1, para_val2)
			output_paths[para_val1, para_val2]=this_res_path
			this_df = pd.read_csv(this_res_path)
			this_x = this_df['SHGC, U']
			this_y = this_df['indoor_temperature']
			this_y_vals = this_y.values
			y_val = np.mean(this_y_vals)
			if y_val > max_y:
				max_y = y_val
				max_y_x = (para_val1, para_val2)
	print(max_y_x)
	return output_paths