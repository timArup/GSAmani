import numpy as np 
import pandas as pd
# from gsapy import GSA
# from gsapy.modules import Element
# from gsapy.modules import Node
# from matplotlib import pyplot as plt
import datetime
from pathlib import Path
from pprint import pprint
import re


def userParams():
    userParams={}
    userParams["Cs"] = [#create_list('C', 18, 23) + create_list('C', 39, 44) + create_list('C', 60, 65) + create_list('C', 81, 86)   #ULS C
        # "C25","C31"]
        "C31","C41","C51"]
        # "C24"]
        # "C23","C24","C25","C26","C28", "C29",
        # "C33","C34","C35","C36","C38", "C39",
        # "C43","C44","C35","C36","C38", "C49",
        # ]
    # userParams["addl_pts"] = 0
    userParams["selEleLists"] = ["Connecting elements typical"] ### Only temporary and set up better
    userParams["selNodLists"] = ["foundation nodes"] ### Only temporary and set up better
    userParams["modelsList"]=[
    "./models/Hud Footbridge_rev17.gwb"]
    userParams["version"] = "10.1"
    userParams["save_name"] = "foot"
    userParams["locMap"] =  {
            2628:"MC5/6",
            2629:"MC3/4",
            2630:"MC1/2",
            2631:"S3/4",
            2632:"S1/2",
            2633:"S5/6",
        }
    userParams["setMap"] =  {
            25:"Testing",
            31:"ULS B (full envelope)",
            41:"ULS C (full envelope)",
            51:"SLS char (full envelope)",
            23 :"ULS B Dead",
            24: "ULS B Wind Lead",
            25 :"ULS B Aero Lead",
            26 :"ULS B Thermal Lead",
            27 :"ULS B Snow Lead",
            28 :"ULS B Maintenance Lead",
            29 :"ULS B Pedestrian Lead",
            30 :"ULS B Live Envelope",
            33 :"ULS C Dead",
            34: "ULS C Wind Lead",
            35 :"ULS C Aero Lead",
            36 :"ULS C Thermal Lead",
            37 :"ULS C Snow Lead",
            38 :"ULS C Maintenance Lead",
            39 :"ULS C Pedestrian Lead",
            40 :"ULS C Live Envelope",
            43 :"SLS Char Dead",
            44: "SLS Char Wind Lead",
            45 :"SLS Char Aero Lead",
            46 :"SLS Char Thermal Lead",
            47 :"SLS Char Snow Lead",
            48 :"SLS Char Maintenance Lead",
            49 :"SLS Char Pedestrian Lead",
            50 :"SLS Char Live Envelope",
        }
    return userParams

# def userParams():
#     userParams={}
#     userParams["save_name"] = "100pcFullRun"
#     userParams["locMap"] =  {
#             112:"PN01",
#             111:"PN02",
#             113:"PN03",
#             114:"PN04",
#             116:"PN05",
#             115:"PN06",
#             109:"PN07",
#             110:"PN8",
#             108:"PN09",
#             107:"PN10",
#         }
#     userParams["setMap"] =  {
#             21: "SLS - Variable Actions (Env.)",
#             22: "SLS - Quasi-permanent (Env.)",
#             23: "ULS - Set A/B - Variable Actions (Env.)",
#             24: "ULS - Set C - Variable Actions (Env.)"
#         }
#     return userParams

def getCombCase(combCasePermString):
    pattern = re.compile(r'C(\d+)p')
    try:
        return int(pattern.search(combCasePermString).group(1))
    except:
        return "Unexpected comb case format"

def getLocation(nodeIndex):
    locMap = userParams["locMap"]
    try:
        return locMap[nodeIndex]
    except:
        return "Error in node to foundation location hashmap"

def getSet(combCase):
    setMap = userParams["setMap"]
    try:
        return setMap[combCase]
    except:
        return "Error in combCase to set hashmap"

if __name__ == '__main__':

    userParams = userParams()
    results = pd.read_csv("./hudData/footResults.csv")
    save_name = userParams["save_name"]

    ### clean results and add info
    results["combCase"] = results["combCasePerm"].apply(getCombCase)
    results["PN"] = results["elementIndex"].apply(getLocation) 
    results["set"] = results["combCase"].apply(getSet)
    
    # results.to_csv(f"hudData/{save_name}ExtResults.csv")

    #### ENVELOPED RESULTS
    nodes = results["nodeIndex"].unique()
    # elements = results["elementIndex"].unique()
    combCases = results["combCase"].unique()

    results = results.drop(["Mxx","Myy","Mzz","Fy","Fz"],axis="columns")

    tabulatedResults = pd.DataFrame({"Location":[],"nodeIndex":[],"Type":[],"combCasePerm":[],"combCase":[],"set":[],"Fx":[],"Fy":[],"Fz":[],"Mxx":[],"Myy":[],"Mzz":[]})
    # tabulatedResults = pd.DataFrame({"PN":[],"elementIndex":[],"Type":[],"modelName":[],"combCasePerm":[],"combCase":[],"set":[],"Fx":[]})
    numCombCases = len(combCases)
    i=0

    for combCase in combCases:
        combRes = results[results["combCase"]==combCase]
        print("Starting CombCase: "+str(combCase)+" "+(str((i/numCombCases)*100)+" %"))
        i+=1
        for nodeIndex in nodes:
            subRes = combRes[combRes["nodeIndex"]==nodeIndex]
            
            maxFx = pd.DataFrame(subRes.loc[subRes['Fx'].idxmax()]).T
            maxFx["Type"]="maxFx"
            minFx = pd.DataFrame(subRes.loc[subRes['Fx'].idxmin()]).T
            minFx["Type"]="minFx"
            maxFy = pd.DataFrame(subRes.loc[subRes['Fy'].idxmax()]).T
            maxFy["Type"]="maxFy"
            minFy = pd.DataFrame(subRes.loc[subRes['Fy'].idxmin()]).T
            minFy["Type"]="minFy"
            maxFz = pd.DataFrame(subRes.loc[subRes['Fz'].idxmax()]).T
            maxFz["Type"]="maxFz"
            minFz = pd.DataFrame(subRes.loc[subRes['Fz'].idxmin()]).T
            minFz["Type"]="minFz"
            
            maxMxx = pd.DataFrame(subRes.loc[subRes['Mxx'].idxmax()]).T
            maxMxx["Type"]="maxMxx"
            minMxx = pd.DataFrame(subRes.loc[subRes['Mxx'].idxmin()]).T
            minMxx["Type"]="minMxx"
            maxMyy = pd.DataFrame(subRes.loc[subRes['Myy'].idxmax()]).T
            maxMyy["Type"]="maxMyy"
            minMyy = pd.DataFrame(subRes.loc[subRes['Myy'].idxmin()]).T
            minMyy["Type"]="minMyy"
            maxMzz = pd.DataFrame(subRes.loc[subRes['Mzz'].idxmax()]).T
            maxMzz["Type"]="maxMzz"
            minMzz = pd.DataFrame(subRes.loc[subRes['Mzz'].idxmin()]).T
            minMzz["Type"]="minMzz"

            tabulatedResults = pd.concat([tabulatedResults,maxFx,minFx,maxFy,minFy,maxFz,minFz,maxMxx,minMxx,maxMyy,minMyy,maxMzz,minMzz])
            # tabulatedResults = pd.concat([tabulatedResults,maxFx,minFx])


    tabulatedResults["Location"] = tabulatedResults["elementIndex"].apply(getLocation) 
    tabulatedResults["set"] = tabulatedResults["combCase"].apply(getSet)
    tabulatedResults.to_csv(f"hudData/{save_name}TabResults.csv")
