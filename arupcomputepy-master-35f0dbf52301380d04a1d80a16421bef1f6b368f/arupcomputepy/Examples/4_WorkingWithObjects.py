# ArupCompute functions can work with complex objects
# in this case the function calculates structural section properties
# from two lists of coordinates

import arupcomputepy

# set up our connection ArupCompute
jobNumber = '00000000' # for testing only - please use a real job number
connection = arupcomputepy.Connection(jobNumber)

calcID = 4239475 # SectionProperties > Calculate > AutoProp v1.1.7 https://compute.arup.digital/calcs/4239475

variables = {
    'y_coords': [0,0,100,100,0],
    'z_coords': [0,100,100,0,0]
}

response = arupcomputepy.MakeCalculationRequest(connection, calcID, isBatch=False, variables=variables)

print(response.availableResults())
print(response['A'])