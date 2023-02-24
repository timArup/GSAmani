import datetime
from pathlib import Path
import os 
import re
import json

def userParams():
    #For SP temp
    userParams={}
    userParams["Cs"] = ["C09","C10","C11","C12","C13","C14"]
    # userParams["modelPrefix"] = " model_03_-"
    userParams["addl_pts"] = 0
    userParams["selLists"] = ["piles under pilecap_AR"] ### Only temporary and set up better
    userParams["heightFilter"] =  { #None, greater than, less than, between, val_1, val_2, . Only specify val_1 for > or <, specify both for between. None is no filter
    "type":None} 
    # "type":"between","val_1":-3, "val_2": -4} 
    # "type":"less than","val_1":-11} 
    # "type":None} 
    userParams["modelsList"]=[
    "./models/SP model_03_+Fy_+Fz.gwb",
    "./models/SP model_03_+Fy_-Fz.gwb",
    "./models/SP model_03_-Fy_+Fz.gwb",
    "./models/SP model_03_-Fy_-Fz.gwb",
    "./models/SP model_03_no-wall_+Fy_-Fz.gwb",
    "./models/SP model_03_no-wall_-Fy_-Fz.gwb"
    ]		
    userParams["loc"] = "SP"
    userParams["strNMCurve"] = "SP_double"
    return userParams


def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

def get_next_available_number(parent_folder,prefix):
    allItems = os.listdir(parent_folder)
    numbers = []
    for item in allItems:
        if item.startswith(prefix):
            numbers.append(get_trailing_number(item)) 
    try:
        nextNumber = max(numbers) + 1
    except:
        nextNumber = 1
    return nextNumber

def get_next_available_path(parent_folder,prefix):
    numberString = str(get_next_available_number(parent_folder,prefix))
    if len(numberString) == 1:
        numberString = "00"+numberString
    elif len(numberString) == 2:
        numberString = "0"+numberString
    elif len(numberString) == 3:
        pass
    else:
        print("something is not working with the save name function. Might be you exceeded 99 results")

    return prefix + "_" + numberString

def save_raw_results(parentFolderString):

    parent_folder = Path(parentFolderString)

    results_folder = Path(parent_folder,get_next_available_path(parent_folder,"res"))

    os.mkdir(results_folder)

    userParams = userParams()

    with open(results_folder / 'settings.txt', 'w') as file:
        file.write(json.dumps(userParams)) # use `json.loads` to do the reverse

save_raw_results("results_test")

save_



