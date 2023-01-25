import streamlit as st

def settings():

    userParams={}
    userParams["Cs"] = [
        # "C9","C10","C26","C27","C40","C41","C54","C55"] # SLSQP
        "C9"] # SLSQP

    userParams["addl_pts"] = 0
    userParams["selLists"] = ["piles under pilecap"] ### Only temporary and set up better
    userParams["heightFilter"] =  { #None, greater than, less than, between, val_1, val_2, . Only specify val_1 for > or <, specify both for between. None is no filter. Works off midpoint of elements.
    "type":None} 

    userParams["modelsList"]=[
    # "./models/NP model_04d_comp-springs_+3m_1.25x.gwb"
    "./models/NP model_04g 20 v spring.gwb"
    ]
    userParams["loc"] = "NP"
    userParams["strNMCurve"] = "SP_NR_top_10B16_16"
    userParams["annotate"] = True # True or False
    userParams["combCaseToExtract"] = "all" #"all" if run for all, list if run for some
    userParams["cCaseAttempts"] = ["C"+str(x) for x in range(1,150)]


    return userParams