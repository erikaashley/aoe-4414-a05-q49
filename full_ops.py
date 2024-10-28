# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
#  
#
# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors
# Output:
#output channel count, output height count, output width count, number of additions performed, number of multiplications performed, number of divisions performed
#
# Written by: Erika Ashley
# Other contributors: None
#
# import Python modules
import math # math module
import sys  # argv

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions


# initialize script arguments
c_in = float('nan') 
n_wv = float('nan') 


# parse script arguments
if len(sys.argv)==3:
  c_in = float(sys.argv[1])
  n_wv = float(sys.argv[2])
else:
  print(\
   'Usage: '\
   'python3 full_ops.py c_in n_wv'\
  )
  exit()

# write script below this line

c_out=n_wv
h_out=1
w_out=1
muls=n_wv*c_in
adds=muls
divs=0

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed