import streamlit as st
import utils.extraction as extraction
import numpy as np 
import pandas as pd
# from gsapy import GSA
from gsapy.modules import Element
from gsapy.modules import Node
from matplotlib import pyplot as plt
from pathlib import Path
import plotly.express as px
import utils.plotting as plotting
import utils.extractionSettings as extractionSettings
import utils.plotSettings as plotSettings
import plotly.graph_objects as go
from utils.flags import Flags
import os
import json

st.set_page_config(page_title="GSAmani",layout="wide") #page_icon="🧰"

### Parameters intialisation
if "plotResults" not in st.session_state:
    st.session_state.plotResults = False
if "plotted" not in st.session_state:
    st.session_state.plotted = False
if "flags" not in st.session_state:
    st.session_state.flags = Flags()
if "exSettings" not in st.session_state:
    st.session_state.exSettings = extractionSettings.defaultExSettings()
if "plSettings" not in st.session_state:
    st.session_state.plSettings = plotSettings.defaultPlSettings()


#### Rough layout
with st.sidebar: 
    sidebarPlaceholder = st.empty()

with sidebarPlaceholder.container():
    st.write("Settings:")
    loadType = st.radio("Run Type",["Full Extraction","Load data"])
    if loadType == "Full Extraction":
        show_elements = st.checkbox(label="Height Filter?")
        saveExtraction = st.checkbox(label="Save Extraction?")
    

# Specify Settings for extraction 

### Functions

### Layout
extractionArea = st.container()

def extractAndSave(exSettings):
    st.write(exSettings)

def get_files_in_folder(folderName,fileExtension):
    path = "./" + folderName
    files={}
    for filename in os.listdir(path):
        if filename.endswith(fileExtension):
            # st.write(os.path.splitext(filename)[0])
            files[path+os.path.splitext(filename)[0]+fileExtension] = [path,os.path.splitext(filename)[0],fileExtension]
    return files

def save_Settings(dictionary,filename):
    path = Path("./" + filename)
    if os.path.exists(path):
        st.error("Extraction Settings have not been saved as file path already exists.")
    else:
        with open(path,'w') as f:
            json.dump(dictionary,f)

def read_Settings(filename):
    path = Path("./" + filename)
    if os.path.exists(path):
        with open(path,'r') as f:
            dictionary = json.load(f)
    else:
        st.write("can't read" + path)
    return dictionary

def updateChangeExSettingsForm(exSettingName):
    st.session_state.exSettings = read_Settings("data/exSettings/"+exSettingName+".txt")



with extractionArea:
    exSet = st.session_state.exSettings ## This two way links these variables. Done for reducing text

    with st.form(key="loadExSettings",clear_on_submit=False):
        files = get_files_in_folder("data/exSettings",".txt")
        longNamesFiles = list(files.keys())
        shortNamesFiles = [files[key][1] for key,value in files.items()]
        st.write(files)
        exSettingName = st.selectbox(label="Select saved extraction settings:",options=shortNamesFiles)
        loadExSet = st.form_submit_button(label='loadExSet',on_click=updateChangeExSettingsForm(exSettingName))

    if loadExSet:
        st.write("data/exSettings/"+exSettingName+".txt")
        st.session_state.exSettings = read_Settings("data/exSettings/"+exSettingName+".txt")

    with st.form(key="changeSettings",clear_on_submit=False):
        col1,col2 = st.columns(2, gap="small")
        with col1:
            filesModels = get_files_in_folder("data/models",".gwb")
            longNamesModels = list(filesModels.keys())
            shortNamesModels = [filesModels[key][1] for key,value in filesModels.items()]
            exSet["modelsList"] = st.multiselect("Select models:",shortNamesModels,default=exSet["modelsList"])
            
            exSet["selLists"] = eval(st.text_input(label='Selected lists:',value=exSet["selLists"]))
            exSet["addl_pts"] = st.number_input(label="Pick additional points:",min_value=0,value=exSet["addl_pts"],step=1)
            extractButton = st.form_submit_button(label='Extract')
        with col2:
            if show_elements:
                st.write("Height Filter not plugged in yet. Has become depricated due to the new graph filtering funcitonaility.")
                st.number_input(label="Lower height:",min_value=0,step=1)
                st.number_input(label="Upperheight height:",min_value=0,step=1)
            exSet["cCaseAttempts"] = eval(st.text_input(label='Choose combination cases to extract for:',value=exSet["cCaseAttempts"]))
            if saveExtraction:
                exSet["saveExSettingsName"] = st.text_input(label='Save name of extraction results:',value = exSet["saveExSettingsName"])
            # saveButton = st.form_submit_button(label='Save')


    if extractButton:
        if saveExtraction:
            save_Settings(st.session_state.exSettings,"data/exSettings/"+exSet["saveExSettingsName"]+".txt")
        st.session_state.plotResults = extraction.extract1x1(st.session_state.exSettings)
        # (st.session_state.flags.runExtraction,st.session_state.flags.extracted) = (False,True)
        st.write("done")
        st.session_state.flags.extracted = True


            # st.error("No saved nameso can't save")



plotArea = st.container()

if st.session_state.flags.extracted:
    if st.button("Plot"):
        st.session_state.plotted=True
else:
    st.write("Extract data to get plotting function")

if st.session_state.plotted:
    with plotArea:

        selectedEnvelopes = st.multiselect("Select saved envelope:",st.session_state.plSettings["envelopes"].keys())
        
        CsToDisplay = []
        for key in selectedEnvelopes:
            CsToDisplay.extend([x for x in st.session_state.plSettings["envelopes"][key]])

        plotResultsToDisplay = pd.DataFrame(st.session_state.plotResults).round({"midpointHeight":2})
        bottomPileHeight = plotResultsToDisplay["midpointHeight"].min()
        plotResultsToDisplay["relHeight"] = plotResultsToDisplay["midpointHeight"] - bottomPileHeight

        filesNMs = get_files_in_folder("data/NMcurves",".xlsx")
        longNamesNMs = list(filesNMs.keys())
        shortNamesNMs = [filesNMs[key][1] for key,value in filesNMs.items()]
        NMCurveStrs = st.multiselect("Select NM Curve:",shortNamesNMs,default=["NA_top","NA_bot"])
            
        modelsToDisplay = st.multiselect("Select mdoels:",plotResultsToDisplay['modelName'].unique())

        (lowHeight,upHeight) = st.select_slider("Choose relative height change:",options=np.sort(plotResultsToDisplay["relHeight"].unique()),value=(float(plotResultsToDisplay["relHeight"].min()),float(plotResultsToDisplay["relHeight"].max())))
        
        plotResultsToDisplay = plotResultsToDisplay[plotResultsToDisplay['relHeight'].between(lowHeight,upHeight)]

        if CsToDisplay:
            plotResultsToDisplay = plotResultsToDisplay[plotResultsToDisplay['combCase'].isin(CsToDisplay)]

        if modelsToDisplay:
            plotResultsToDisplay = plotResultsToDisplay[plotResultsToDisplay['modelName'].isin(modelsToDisplay)]


        tab1, tab2, tab3 = st.tabs(["Plot", "Data", "results summary"])
        with tab1:
            fig = plotting.plot("Mres","Fx",plotResultsToDisplay,{})
            if NMCurveStrs:
                for NMCurveStr in NMCurveStrs:
                    NMcurve = plotting.loadNMCurve(NMCurveStr)
                    fig.add_trace(go.Scatter(x=NMcurve["Moment (kNm)"],y=NMcurve["Fx (kN)"],mode='lines',name=NMCurveStr))
            st.plotly_chart(fig)
        with tab2:
            st.dataframe(plotResultsToDisplay,width=1000)
            st.session_state.flags.dataBelow = st.checkbox("Show data below graph too? (useful for detailed checking)")

        with tab3:
            unique_values = {}
            for col in plotResultsToDisplay.drop(["Mres","Fx","Fres"],axis="columns").columns:
                unique_values[col] = plotResultsToDisplay[col].unique()
            st.write(unique_values)

        if st.session_state.flags.dataBelow:
            st.dataframe(plotResultsToDisplay,width=1000)

