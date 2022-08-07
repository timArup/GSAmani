# Example showcasing how to interact with an ArupCompute function that returns an 'ArupComputeResult'
# Not all libraries return 'ArupComputeResult', but the majority of the popular libaries do
# These contain additional data such as:
# - Errors, warnings or remarks
# - Reports
# - Additional information alongside the value of their results

# import the libraries we need
import arupcomputepy

# set up our connection ArupCompute
jobNumber = '00000000' # for testing only - please use a real job number
connection = arupcomputepy.Connection(jobNumber)

# Set calculation details and inputs
calcID = 5460340 # DesignCheck2 > Examples > SimpleCalculation v145.0.17 https://compute.arup.digital/calcs/5460340

variables = {
    'ID': 'test',
    'A': 1.0,
    'B': 2.0
}

response = arupcomputepy.MakeCalculationRequest(connection, calcID, isBatch=False, variables=variables)

print(response['C'])