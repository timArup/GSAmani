# May ArupCompute libraries produce useful reports
# These are transmitted in HTML format, but can be converted
# into PDF using the ArupCompute HTML --> PDF conversion API

import arupcomputepy
import arupcomputepy.pdf
import tempfile
import os

# set up our connection ArupCompute
jobNumber = '00000000' # for testing only - please use a real job number
connection = arupcomputepy.Connection(jobNumber)

# Set calculation details and inputs
calcID = 5460340 # DesignCheck2 > Examples > SimpleCalculation v145.0.17 https://compute.arup.digital/calcs/5460340

variables = {
    'ID': 'Test',
    'A': 1,
    'B': 2
}

 # Note: must use 'simple' or 'full' result type to get HTML from library (the default 'mini' just returns numbers to keep response size down)
response = arupcomputepy.MakeCalculationRequest(connection, calcID, isBatch=False, variables=variables, resultType='simple')

html = response.arupComputeReport_HTML

path = os.path.join(tempfile.gettempdir(),'arupcomputepy','arupcompute.pdf') # temporary file location for demonstration purposes
print(path)

arupcomputepy.pdf.Create(html, "A.Nonymous", path, replace=True)