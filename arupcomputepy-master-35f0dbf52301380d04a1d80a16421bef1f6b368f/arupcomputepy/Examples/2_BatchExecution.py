# All ArupCompute functions can work in batch mode
# This enables many calculations to be sent to ArupCompute at the same time
# This reduces overheads and improves throughput

import arupcomputepy

jobNumber = '00000000' # for testing only - please use a real job number
connection = arupcomputepy.Connection(jobNumber)

calcID = 2081643  # Sample Library v2.1.60 Examples.BasicUse > Basic Calc

# Note that we use lists of input data for a batch calculation
variables = {
    'a': [1,20,300,4000,500,60],
    'b': [2,40,600,7000,800,90]
}

# Note that we need to set the variable isBatch = True
response = arupcomputepy.MakeCalculationRequest(connection, calcID, isBatch=True, variables=variables)

for item in response:
    print(item)