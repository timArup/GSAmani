import streamlit as st
import extraction
import numpy as np 
import pandas as pd
from gsapy import GSA
from gsapy.modules import Element
from gsapy.modules import Node
from matplotlib import pyplot as plt
import datetime
from pathlib import Path
import pythoncom
import plotly.express as px
import plotting
import extractionSettings
import plotly.graph_objects as go


# """
# How to run:
# streamlit run main.py
# """

# st.set_page_config(layout="wide")

# with st.sidebar:


### Parameters intialisation
if "plotResults" not in st.session_state:
    st.session_state.plotResults = False
if "plotted" not in st.session_state:
    st.session_state.plotted = False
# Specify Settings for extraction 
userParams = extractionSettings.settings()
# st.session_state.userParams = userParams
savedEnvelopes = {}
savedEnvelopes["NA_SLSQP"] = ["C10","C11","C31","C32","C52","C53","C73","C74"]
savedEnvelopes["NA_ULSB"] = ["C12","C13","C14","C15","C16","C17",
                            "C33","C34","C35","C36","C37","C38",
                            "C54","C55","C56","C57","C58","C59",
                            "C75","C76","C77","C78","C79","C80"]


### Functions


### Layout

if st.button("Run Extraction"):
    runExtraction=True
else:
    runExtraction = False

if st.button("Plot"):
    st.session_state.plotted=True
# else:
#     plotted=False

st.json(userParams)


#### CHANGE FORMAT LATER

if runExtraction:
    # Run extraction
    combinedModels = extraction.CombinedModels(userParams)
    combinedModels.getCombResults(userParams)
    plotResults = combinedModels.listElementsToPlot()
    st.session_state.plotResults = plotResults

    # Close Models
    combinedModels.close()
    st.write("done")
#     extracted = True


if st.session_state.plotResults:
    "Have run Extraction"

if st.session_state.plotted:

    selectedEnvelopes = st.multiselect("Select saved envelope:",savedEnvelopes.keys())
    
    CsToDisplay = []
    for key in selectedEnvelopes:
        CsToDisplay.extend([x for x in savedEnvelopes[key]])
    # st.write(CsToDisplay)

    plotResultsToDisplay = pd.DataFrame(st.session_state.plotResults)


    NMCurves = ["SP_NR_top_8B16_16","SP_NR_top_10B16_16"]

    NMCurveStrs = st.multiselect("Select NM Curve:",NMCurves)
    st.write(NMCurveStrs)
        
    


    if CsToDisplay:
        plotResultsToDisplay = plotResultsToDisplay[plotResultsToDisplay['combCase'].isin(CsToDisplay)]
    
    # st.write()
    # selectedCombinations = st.multiselect("Combinations selected:",plotResults[""])

    st.write(len(plotResultsToDisplay))
    fig = plotting.plot("Mres","Fx",plotResultsToDisplay,st.session_state.userParams)
    # NMcurve = plotting.loadNMCurve(NMCurveStr)
    if NMCurveStrs:
        for NMCurveStr in NMCurveStrs:
            NMcurve = plotting.loadNMCurve(NMCurveStr)
            fig.add_trace(go.Scatter(x=NMcurve["Moment (kNm)"],y=NMcurve["Fx (kN)"],mode='lines',name=NMCurveStr))
    st.plotly_chart(fig)
    st.dataframe(plotResultsToDisplay)


#     """
#     Plan:

#     QUICK PLAN:
#     1) GET PLOTS WORKING
#     2) GET DF SAVING
#     3) SEPERATE OUT ANALYSIS PARTS AND ADD TO NEW BUTTONS

#     If you click a button, run extraction on user defined settings:
#     - have default values
#     - have way not to run this and instead load in an old file

#     first part of analysis has to be done with the above. Getting element forces in a usable way is priority. 
#     Have a "elements" df which consists of ALL core data for elements (in time). 
#     -Saves into a .csv format somewhere

#     If you click an analysis button:
#     run all post analysis, add bits and bobs (some could include needing to load the model back up).

#     Plot Results
#     Choose input file



# Make functions for loading in or using analysis a general function called at different stages
#     Recording runs + analysis' would be valuable.
#     Eventually do different page stuff.

#     """

