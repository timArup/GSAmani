
import plotly.express as px
import pandas as pd
import numpy as np
from pathlib import Path
from pprint import pprint
from matplotlib import pyplot as plt

resString = f"hudData\can24Results.csv"

results = pd.read_csv(resString)
pprint(results)

boringx = [1,2,3]
boringy=[2,6,3]
boring = px.scatter(boringx,boringy)
boring.show()


# fig = px.scatter(results,x="Fx",y="Fy")
# fig.show()


results.plot(x="Fx",y="Fy")
import matplotlib
print matplotlib.rcParams['backend']
# plt.scatter(results,x="Fx",y="Fy")
# plt.show()

