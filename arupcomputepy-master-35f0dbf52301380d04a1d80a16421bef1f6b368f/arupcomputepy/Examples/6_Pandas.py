# Showcasing how to use ArupCompute with the popular data processing library 'pandas'

import arupcomputepy

# set up our connection ArupCompute
jobNumber = '00000000' # for testing only - please use a real job number
connection = arupcomputepy.Connection(jobNumber)

calcID = 5459313 # DesignCheck2 v145.0.17 Structural.EC.Calcs.Concrete > Slab overall depth

l_input = [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
slab_type_input = ['OneWaySolidSlab_SingleSpan'] * 11
q_k_input = [3.1] * 11
g_ksdl_input = [1.2] * 11

# Note that we use lists of input data for a batch calculation
variables = {
    'ID' : list(range(1,12)),
    'slab_type' : slab_type_input,
    'q_k' : q_k_input,
    'g_ksdl' : g_ksdl_input,
    'l' : l_input
}

# Note that we need to set the variable isBatch = True
response = arupcomputepy.MakeCalculationRequest(connection, calcID, isBatch=True, variables=variables)

import pandas as pd

# Create DataFrame
df = pd.DataFrame(columns=['Slab Type', 'q_k (kPa)', 'g_ksdl (kPa)', 'Span (m)', 'Depth (mm)'])

for i in range(len(response)):
    df.loc[i] = [slab_type_input[i], q_k_input[i], g_ksdl_input[i], l_input[i], response[i]['h']]  # 'h' = cross section depth 'mm'

print(df)