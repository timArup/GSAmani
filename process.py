import pandas as pd
from pprint import pprint

df = pd.read_csv("results_NP_ULSC.csv")
# pprint(plotResults)

# combCaseLists =   [[     "C09","C10","C11","C12","C13","C14"], # ULS B
#         ["C15","C16","C17","C18","C19","C20"], # ULS C
#         ["C01","C02","C03","C04","C05","C06"]] # SLS

# elementsIndexesLists = list(range(239,250+1))
# print(type(elementsIndexesLists))
# print(elementsIndexesLists.append(255))
# for elementIndexes in elementsIndexesLists:


for elementIndex in df["elementIndex"].unique():
    dfSlice = df[df["elementIndex"] == elementIndex]
    dfSliceMax = dfSlice[dfSlice["Fx"] == dfSlice["Fx"].max()]
    dfSliceMin = dfSlice[dfSlice["Fx"] == dfSlice["Fx"].min()]
    # pprint(dfSliceMax)
    # pprint(dfSliceMin)
    print(str(elementIndex),"   ", "max","   ", dfSliceMax.iloc[0]["Fx"],"   ", dfSliceMax.iloc[0]["modelName"],"   ", dfSliceMax["combCase"].iloc[0])
    print(str(elementIndex),"   ", "min","   ", dfSliceMin.iloc[0]["Fx"],"   ", dfSliceMin.iloc[0]["modelName"],"   ", dfSliceMin["combCase"].iloc[0])


# for each list of elements
# for each ULS SLS or ULSC
#  Do that 