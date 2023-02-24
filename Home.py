# """
# How to run:
# streamlit run main.py
# """

import streamlit as st
import extraction
import numpy as np 
import pandas as pd
# from gsapy import GSA
from gsapy.modules import Element
from gsapy.modules import Node
from matplotlib import pyplot as plt
# import datetime
from pathlib import Path
# import pythoncom
import plotly.express as px
import plotting
import extractionSettings
import plotly.graph_objects as go

# st.set_page_config(layout="wide")

with st.sidebar:
    sidebarPlaceholder = st.empty()

with sidebarPlaceholder.container():
    st.write("Settings:")
    st.radio("Run Type",["Full Extraction","Load data"])

extractionArea = st.empty()
plotArea = st.empty()

# with plotArea.container():
    




### Parameters intialisation
if "plotResults" not in st.session_state:
    st.session_state.plotResults = False
if "plotted" not in st.session_state:
    st.session_state.plotted = False
# Specify Settings for extraction 
userParams = extractionSettings.settings()
st.session_state.userParams = userParams
savedEnvelopes = {}
savedEnvelopes["NA_SLSQP"] = ["C10","C11","C31","C32","C52","C53","C73","C74"]
savedEnvelopes["NA_ULSB"] = ["C12","C13","C14","C15","C16","C17",
                            "C33","C34","C35","C36","C37","C38",
                            "C54","C55","C56","C57","C58","C59",
                            "C75","C76","C77","C78","C79","C80"]
savedEnvelopes["NA_SLS"] = ["C18","C19","C20","C21","C22","C23",
                            "C39","C40","C41","C42","C43","C44",
                            "C60","C61","C62","C62","C64","C65",
                            "C81","C82","C83","C84","C85","C86"]
                                    # NA
    # create_list('C', 4, 9) + create_list('C', 25, 30) + create_list('C', 46, 51) + create_list('C', 67, 72)   #SLS
    # create_list('C', 12, 17) + create_list('C', 33, 38) + create_list('C', 54, 59) + create_list('C', 75, 80)   #ULS B
    # create_list('C', 18, 23) + create_list('C', 39, 44) + create_list('C', 60, 65) + create_list('C', 81, 86)   #ULS C


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

st.write(userParams["modelsList"])

#### CHANGE FORMAT LATER

if runExtraction:
    plotResults = extraction.extract1x1(userParams)

    st.session_state.plotResults = plotResults

    st.write("done")


if st.session_state.plotResults:
    "Have run Extraction"

if st.session_state.plotted:

    selectedEnvelopes = st.multiselect("Select saved envelope:",savedEnvelopes.keys())
    
    CsToDisplay = []
    for key in selectedEnvelopes:
        CsToDisplay.extend([x for x in savedEnvelopes[key]])

    plotResultsToDisplay = pd.DataFrame(st.session_state.plotResults)
    bottomPileHeight = plotResultsToDisplay["midpointHeight"].min()
    plotResultsToDisplay["relHeight"] = plotResultsToDisplay["midpointHeight"] - bottomPileHeight


    NMCurves = ["SP_NR_top_8B16_16","SP_NR_top_10B16_16","NA_top","NA_bot","NA_trial","NA_top_check","NA_top_rotated"]

    NMCurveStrs = st.multiselect("Select NM Curve:",NMCurves)
    
    modelsToDisplay = st.multiselect("Select mdoels:",plotResultsToDisplay['modelName'].unique())
    st.write(modelsToDisplay)

    (lowHeight,upHeight) = st.select_slider("Choose relative height change:",options=np.sort(plotResultsToDisplay["relHeight"].unique()),value=(float(plotResultsToDisplay["relHeight"].min()),float(plotResultsToDisplay["relHeight"].max())))

    plotResultsToDisplay = plotResultsToDisplay[plotResultsToDisplay['relHeight'].between(lowHeight,upHeight)]

    if CsToDisplay:
        plotResultsToDisplay = plotResultsToDisplay[plotResultsToDisplay['combCase'].isin(CsToDisplay)]

    if modelsToDisplay:
        plotResultsToDisplay = plotResultsToDisplay[plotResultsToDisplay['modelName'].isin(modelsToDisplay)]

    

    
    # st.write()
    # selectedCombinations = st.multiselect("Combinations selected:",plotResults[""])

    st.write(len(plotResultsToDisplay))
    fig = plotting.plot("Mres","Fx",plotResultsToDisplay,st.session_state.userParams)
    # fig2 = plotting.plot("Fres","Fx",plotResultsToDisplay,st.session_state.userParams)
    # NMcurve = plotting.loadNMCurve(NMCurveStr)
    if NMCurveStrs:
        for NMCurveStr in NMCurveStrs:
            NMcurve = plotting.loadNMCurve(NMCurveStr)
            fig.add_trace(go.Scatter(x=NMcurve["Moment (kNm)"],y=NMcurve["Fx (kN)"],mode='lines',name=NMCurveStr))
    st.plotly_chart(fig)
    print(plotResultsToDisplay.dtypes)
    st.dataframe(plotResultsToDisplay,width=1000)

