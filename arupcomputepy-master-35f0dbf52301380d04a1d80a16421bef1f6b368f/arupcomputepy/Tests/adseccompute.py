import arupcomputepy

jobNumber = '07706090' # insert real job number
connection = arupcomputepy.Connection(jobNumber)

# Create Rectangular Section
# Creates a rectangular section.

calcID_rect = 4885324

variables = {
    'W': 100, # Width (mm)
    'D': 200, # Depth (mm)
    'M': 'Concrete.EN1992.Part1_1.Edition_2004.NationalAnnex.GB.Edition_2014.C32_40' # Material
}

section_justConcrete = arupcomputepy.MakeCalculationRequest(connection, calcID_rect, isBatch=False, variables=variables)

calcID_cover = 4885305

variables = {
    'S': section_justConcrete, # Section
    'C': 30 # Cover (mm)
}

section_withCover = arupcomputepy.MakeCalculationRequest(connection, calcID_cover, isBatch=False, variables=variables)

print(section_withCover)