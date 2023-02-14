import os
import json
import copy
from StaticEplusEngine import run_eplus_model, convert_json_idf
import numpy as np
import pandas as pd
import time

class Mycw:
	start=0
	end=0
	
	
	def __init__(self,eplus_run_path,idf_path,output_dir):
		self.eplus_run_path=eplus_run_path
		self.idf_path=idf_path
		self.output_dir=output_dir
		self._cw_name=0
	
	def run_one_simulation_helper(self,
					parameter_key1, 
					parameter_key2,
					parameter_val1, 
					parameter_val2):
		convert_json_idf(self.eplus_run_path,self.idf_path)
		epjson_path = self.idf_path.split('.idf')[0] + '.epJSON'

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
		print(self.output_dir)
		print('============================================')

		with open(epjson_path, "w") as f:
			json.dump(epjson_dict, f)

		convert_json_idf(self.eplus_run_path, epjson_path)

		run_eplus_model(self.eplus_run_path,
				self.idf_path, 
				self.output_dir)
		res_pt = os.path.join(self.output_dir, "eplusout.csv")
		return res_pt
		
	def run_function(self,
			 parameter_key1,
			 parameter_key2, 
			 parameter_vals1,
			 parameter_vals2):
		Mycw.times()
		output_paths = {}
		if not os.path.isdir(self.output_dir):
			os.mkdir(self.output_dir)
		max_y = 0
		max_y_x = None
		for i in range(0,len(parameter_vals1)):
			para_val1=parameter_vals1[i]
			for k in range(0,len(parameter_vals2)):
				para_val2=parameter_vals2[k]
				this_res_path=self.run_one_simulation_helper(

				    parameter_key1, 
				    parameter_key2, 
				    para_val1, 
				    para_val2)
				output_paths[para_val1,para_val2]=this_res_path
				this_df = pd.read_csv(this_res_path)
				this_x = this_df['ZN001:WALL001:WIN001:Surface Inside Face Temperature [C](TimeStep)']
				this_y = this_df['ZN001:WALL001:Surface Inside Face Temperature [C](TimeStep)']
				this_y_vals = this_y.values
				y_val = np.mean(this_y_vals)
				if y_val > max_y:
					max_y = y_val
					max_y_x = (para_val1, para_val2)
		print(max_y_x)
		Mycw.timee()
		print('*'*50)
		print('time takes {}'.format(Mycw.end-Mycw.start))
		return output_paths
		
	@classmethod
	def times(cls):
		cls.start=time.time()
		
	
	@classmethod
	def timee(cls):
		cls.end=time.time()
	
	@property
	def cw_name(self):
		return self._cw_name
	
	@cw_name.setter
	def cw_name(self,name):
		self._cw_name=name
		
	@cw_name.getter
	def cw_name(self):
		return self._cw_name	

	
		
	
	
