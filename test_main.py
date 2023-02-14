import numpy as np
import pandas as pd
from cw33 import Mycw



eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'
output_dir = 'test_for_cw3'

mycw=Mycw(
	eplus_run_path=eplus_run_path,
	idf_path=idf_path,
	output_dir=output_dir
		)


parameter_key1 = ['WindowMaterial:SimpleGlazingSystem',
		 'SimpleWindow:DOUBLE PANE WINDOW',
		 'solar_heat_gain_coefficient']
parameter_key2 = ['WindowMaterial:SimpleGlazingSystem',
		 'SimpleWindow:DOUBLE PANE WINDOW', 
		 'u_factor']	
parameter_vals1 = [i for i in np.arange(0.25, 0.75+0.1, 0.1)]
parameter_vals2 = [k for k in np.arange(1.0, 2.5+0.5, 0.5)]

output_paths=mycw.run_function(
	parameter_key1,
	parameter_key2,
	parameter_vals1,
	parameter_vals2
	)

print(output_paths)

mycw.cw_name=33
print('print sth out for getter {}'.format(mycw.cw_name))
print(f'This group can obtain the maximal result!!')

