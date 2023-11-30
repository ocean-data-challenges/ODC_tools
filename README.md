# ODC tools

## Available modules

- mod_compare 
- mod_filter 
- mod_interp 
- mod_plot 
- mod_powerspec 
- mod_read 
- mod_spectral 
- mod_stat 
- mod_switchvar 
- mod_traj 
- mod_utils 
- mod_xscale 

## How to get started

### pip install the package to set up the odc_tools environment
  
```
pip install git+https://github.com/ocean-data-challenges/ODC_tools.git#egg=odc_tools
```
### Activate odc_tools environment

```
source activate odc_env
```
os.system("ipython kernel install --name 'odc_env' --user")

### pip intall the package again now that your in the odc_tools environment 
  
```
pip install git+https://github.com/ocean-data-challenges/ODC_tools.git#egg=odc_tools
```

### add environment to the available kernels for jupyter to see: 
```
ipython kernel install --name "odc_env" --user
```
finally, select the "odc_env" kernel in your notebook with Kernel > Change Kernel.


You're now good to go ! 