# import numpy
from numpy import sqrt
import pandas as pd
from gsapy import GSA
from matplotlib import pyplot as plt
# import arupcomputepy
# import setuptools
# from pathlib import Path

def open_model(loc):
    if loc == "NP":
        model = GSA(r'.\\NPmodel_02.gwb', version = "10.1")
    elif loc =="SA_top" or loc == "SA_bot":
        model = GSA(r'.\\SA model_03.gwb', version = "10.1")

    return model

# def which_location():

#     loc = input("Which location are you designing for? enter either: NA, NP, SP or SA:")
#     if loc != "" 


def user_params(loc):
    global Cs_ULS
    global Cs_ULS_C
    global Cs_SLS
    global Cs_SLS_QP

    if loc == "NP":
        Cs_ULS = create_list('C',11,16) + create_list('C',28,33) + create_list('C',42,47) + create_list('C',56,61)
        # Cs_ULS_C = create_list('C',11,16) + create_list('C',28,33) + create_list('C',42,47) + create_list('C',56,61)
        # Cs_SLS = create_list('C',3,8) + create_list('C',20,25) + create_list('C',34,39) + create_list('C',48,53)
        # Cs_SLS_QP = ["C9","C10","C26","C27","C40","C41","C54","C55"]
    elif loc == "SA_top" or loc == "SA_bot":
        Cs_ULS = create_list('C',11,16) + create_list('C',25,30) + create_list('C',39,44) + create_list('C',53,58)+ create_list('C',67,72) + create_list('C',81,86) + create_list('C',95,100) + create_list('C',109,114)

    global all_PN
    all_PN = create_list('PN',1,12)

    global addl_pts
    addl_pts = 0

def create_list(prefix,first,last):
    list = []
    for i in range(first,last+1):
        list.append(prefix + str(i))
    return list

def convert_to_2_list(to_string):

    to_list = to_string.split()

    updated = to_list.copy()
    updated_index = 0
    offset = 0
    for i,value in enumerate(to_list):
        updated_index = i + offset
        if value == 'to':
            del updated[updated_index]
            list_to_insert = list(range(int(to_list[i-1])+1,int(to_list[i+1])))
            list_to_insert.reverse()
            offset = offset + len(list_to_insert) - 1
            for inserted in list_to_insert:
                updated.insert(updated_index,inserted)
    
    updated = [int(item) for item in updated]
    return updated

def beam_results(no,combination,addl_pts):
    return model.get_1D_elem_resultants(no, # the element number
     combination, # analysis case or combination number
    axis="local", # output axis - if omitted, it uses the default axis
    addl_pts=addl_pts) # additional number of points along the element to output forces, if ommited it defaults to 0

def distance_along_element(index,addl_pts):
    return index/(addl_pts+1)

def get_multiple_beam_results(elements,Cs_ULS,addl_pts):
    Fx = []
    Mres = []
    Cs = []
    xDivL = []
    element_nos = []

    for combination in Cs_ULS:

        for element_no in elements:
            results = beam_results(element_no,combination,addl_pts)

            for i in range(addl_pts + 2):
                result = results[i]

                Fx.append(result[0])
                Mres.append((result[4]**2+result[5]**2)**0.5)
                Cs.append(combination)
                xDivL.append(distance_along_element(i,addl_pts))
                element_nos.append(element_no)

    # print(element_nos)

    # aggregated = [element_nos,Cs,xDivL,Fx,Mres]
    # for item in aggregated:
    #     print(len(item))
    # aggregated_names = ["element_nos","Cs","xDivL2","Fx","Mres"]

    df = pd.DataFrame({"element_nos":element_nos,"Cs":Cs,"xDivL":xDivL,"Fx":Fx,"Mres":Mres})

    return df

def settings(ax):
    plt.xlabel('Moment (kNm)')
    plt.ylabel('Axial Load (kN)')
    # plt.xlim(0, t.max()*1.1)
    # plt.ylim(0, network[column_string].max()*1.1)
    plt.grid(which='both')
    plt.title("NM plot")
    ax.tick_params(axis="y",direction="in")
    ax.tick_params(axis="x",direction="in")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)

def plotting(DF,NMcurve):
    fig,ax = plt.subplots()
    settings(ax)
    plt.scatter(df["Mres"],df["Fx"])
    plt.plot(NMcurve["Moment (kNm)"],NMcurve["Fx (kN)"], color="red")

    max_Mres = df["Mres"].max()

    for x, y, C, e in zip(df["Mres"], df["Fx"], df["Cs"], df["element_nos"]):
        if x > 0.98*max_Mres: 
            if x == max_Mres:
                print("Max moment and accompanying axial load (kN [Mres,Fx]):")
                print ("[", str(x)+","+str(y)+"]")
            t = C + "," + str(e)
            plt.text(x, y, t)

    plt.show()

def loadNMCurve(loc):
    NMcurve = pd.read_excel(r'.\\NMcurve\\'+loc+'.xlsx', skiprows=1)
    return NMcurve


if __name__ == '__main__':

    loc = "SA_top"
    model = open_model(loc)
    user_params(loc)

    lists = model.get_all_saved_lists()
    # print(lists)

    # piles_under_pilecap = lists[4] ## NP
    piles_under_pilecap = lists[0] ## SA


    elements_string = piles_under_pilecap.description
    elements = convert_to_2_list(elements_string)

    df= get_multiple_beam_results(elements,Cs_ULS,addl_pts)
    # df= get_multiple_beam_results(elements,["C1"],addl_pts)

    NMcurve = loadNMCurve(loc)
    # print(NMcurve)

    plotting(df,NMcurve)

    del model

    









# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org openpyxl
