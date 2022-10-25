#Date of the first creation:2022-10-18
#Author: Zihan Yuan
#This file is for EnergyPlus parametric simulation
import os
import json
import copy
from StaticEplusEngine import run_eplus_model,convert_json_idf

def run_one_simulation_helper_origin(eplus_run_path, 
	idf_path, output_dir, parameter_key, parameter_val):


	######step1 : convert an IDF file into JSON file ######
	convert_json_idf(eplus_run_path, idf_path)
	epjson_path = idf_path.split('.idf')[0] + '.epJSON'


	######step2 : load the JSON file into a JSON dict ######
	with open(epjson_path) as epJSON:
		epjson_dict = json.load(epJSON)
	print(epjson_dict)


	######step3 : change the JSON dict value ######
	inner_dict = epjson_dict
	for i in range(len (parameter_key)):
		if i < len(parameter_key) - 1:
			inner_dict = inner_dict[parameter_key[i]]
	inner_dict[parameter_key[-1]] = parameter_val
	

	######step4 : dump the JSON dict to JSON file ######
	with open(epjson_path,"w") as epjson:
		json.dump(epjson_dict,epjson)


	######step5 : convert JSON file to IDF file ######
	convert_json_idf(eplus_run_path,epjson_path)


	######step6 : run simulation ######
	run_eplus_model(eplus_run_path, idf_path, output_dir)


def run_one_simulation_helper(eplus_run_path, 
	idf_path, output_dir, parameter_key, parameter_val):
	
	######step1 : convert an IDF file into JSON file ######
	convert_json_idf(eplus_run_path, idf_path)
	epjson_path = idf_path.split('.idf')[0] + '.epJSON'


	######step2 : load the JSON file into a JSON dict ######
	with open(epjson_path) as epJSON:
		epjson_dict = json.load(epJSON)
	print(epjson_dict)
	
	######step3 : change the JSON dict value ######
	inner_dict = epjson_dict
	for i in range(len (parameter_key)):
		if i < len(parameter_key) - 1:
			inner_dict = inner_dict[parameter_key[i]]
	inner_dict[parameter_key[-1]] = parameter_val


	######step4 : dump the JSON dict to JSON file ######
	with open(epjson_path,"w") as epjson:
		json.dump(epjson_dict,epjson)


	######step5 : convert JSON file to IDF file ######
	convert_json_idf(eplus_run_path,epjson_path)
	# make new dir for each para val 

	
	######step6 : run simulation ######
	run_eplus_model(eplus_run_path, idf_path, output_dir)
	res_pt=os.path.join(output_dir,"eplusout.csv")
	return res_pt



def run_one_parameter_parametric(eplus_run_path, idf_path, output_dir,
	                              parameter_key, parameter_vals):
	output_paths={}
	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)
	for i in range(0,len(parameter_vals)):
		para_val=parameter_vals[i]
		new_output=output_dir+"//run{0}".format(str(i))
		if not os.path.exists(new_output):
			os.mkdir(new_output)
		this_res_path=run_one_simulation_helper(eplus_run_path, idf_path, 
			new_output, parameter_key, para_val)
		output_paths[para_val]=this_res_path
	return output_paths

