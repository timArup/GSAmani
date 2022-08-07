# Example showcasing how to interact with a basic ArupCompute function

# import the libraries we need
import arupcomputepy

# set up our connection ArupCompute
jobNumber = '00000000' # for testing only - please use a real job number
connection = arupcomputepy.Connection(jobNumber)

# Set calculation details and inputs
calcID = 2081643  # Sample Library v2.1.60 Examples.BasicUse > Basic Calc https://compute.arup.digital/calcs/2081643

variables = {
    'a': 1,
    'b': 2
}

# Send off to ArupCompute
response = arupcomputepy.MakeCalculationRequest(connection, calcID, isBatch=False, variables=variables)

print(response)