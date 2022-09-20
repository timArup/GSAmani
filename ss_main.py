# import numpy
from numpy import sqrt
import pandas as pd
from gsapy import GSA
from matplotlib import pyplot as plt
# import arupcomputepy
# import setuptools
# from pathlib import Path
import datetime


def open_model(loc):
    if loc == "NP":
        model = GSA(r'.\\NPmodel_02.gwb', version="10.1")
    elif loc == "SA_top" or loc == "SA_bot":
        model = GSA(r'.\\SA model_03.gwb', version="10.1")
    elif loc == "NA":
        model = GSA(
            r'.\\models\\code_NAmodel_04_620_2ndstep_yK0.gwb', version="10.1")
    # elif loc == "SP":
    #     model = GSA(
    #         r'.\\models\\code_NAmodel_04_620_2ndstep_yK0.gwb', version="10.1")

    return model


# def which_location():

#     loc = input("Which location are you designing for? enter either: NA, NP, SP or SA:")
#     if loc != ""


def user_params(loc):
    global Cs_ULS
    global Cs_ULS_C
    global Cs_SLS
    global Cs_SLS_QP
    global all_PN

    if loc == "NP":
        Cs_ULS = create_list('C', 11, 16) + create_list('C', 28, 33) + \
            create_list('C', 42, 47) + create_list('C', 56, 61)
        # Cs_ULS_C = create_list('C',11,16) + create_list('C',28,33) + create_list('C',42,47) + create_list('C',56,61)
        # Cs_SLS = create_list('C',3,8) + create_list('C',20,25) + create_list('C',34,39) + create_list('C',48,53)
        # Cs_SLS_QP = ["C9","C10","C26","C27","C40","C41","C54","C55"]
        all_PN = create_list('PN', 1, 12)
    elif loc == "SA_top" or loc == "SA_bot":
        Cs_ULS = create_list('C', 11, 16) + create_list('C', 25, 30) + create_list('C', 39, 44) + create_list('C', 53, 58) + \
            create_list('C', 67, 72) + create_list('C', 81, 86) + \
            create_list('C', 95, 100) + create_list('C', 109, 114)
        all_PN = create_list('PN', 1, 12)
    elif loc == "NA":
        Cs_ULS = create_list('C', 12, 17) + create_list('C', 33, 38) + \
            create_list('C', 54, 59) + create_list('C', 75, 80)
        all_PN = create_list('PN', 1, 8)

    print(Cs_ULS)

    global addl_pts
    addl_pts = 0

    print(Cs_ULS)
    print(all_PN)


def create_list(prefix, first, last):
    list = []
    for i in range(first, last+1):
        if i < 10:
            list.append(prefix + str(0) + str(i))
        else:
            list.append(prefix + str(i))
    return list


def convert_to_2_list(to_string):
    # print(to_string)

    to_list = to_string.split()

    updated = to_list.copy()
    updated_index = 0
    offset = 0
    for i, value in enumerate(to_list):
        updated_index = i + offset
        if value == 'to':
            del updated[updated_index]
            list_to_insert = list(
                range(int(to_list[i-1])+1, int(to_list[i+1])))
            list_to_insert.reverse()
            offset = offset + len(list_to_insert) - 1
            for inserted in list_to_insert:
                updated.insert(updated_index, inserted)

    updated = [int(item) for item in updated]
    # print(updated)
    return updated


def beam_results(no, combination, addl_pts):
    return model.get_1D_elem_resultants(no,  # the element number
                                        combination,  # analysis case or combination number
                                        axis="local",  # output axis - if omitted, it uses the default axis
                                        addl_pts=addl_pts)  # additional number of points along the element to output forces, if ommited it defaults to 0


def distance_along_element(index, addl_pts):
    return index/(addl_pts+1)


def get_multiple_beam_results(elements, Cs_ULS, addl_pts):
    Fx = []
    Mres = []
    Cs = []
    xDivL = []
    element_nos = []

    for combination in Cs_ULS:

        for element_no in elements:
            results = beam_results(element_no, combination, addl_pts)

            for i in range(addl_pts + 2):
                result = results[i]

                Fx.append(result[0])
                Mres.append((result[4]**2+result[5]**2)**0.5)
                Cs.append(combination)
                xDivL.append(distance_along_element(i, addl_pts))
                element_nos.append(element_no)

    # print(element_nos)

    # aggregated = [element_nos,Cs,xDivL,Fx,Mres]
    # for item in aggregated:
    #     print(len(item))
    # aggregated_names = ["element_nos","Cs","xDivL2","Fx","Mres"]

    df = pd.DataFrame({"element_nos": element_nos, "Cs": Cs,
                      "xDivL": xDivL, "Fx": Fx, "Mres": Mres})

    return df


def settings(ax):
    plt.xlabel('Moment (kNm)')
    plt.ylabel('Axial Load (kN)')
    # plt.xlim(0, t.max()*1.1)
    # plt.ylim(0, network[column_string].max()*1.1)
    plt.grid(which='both')
    plt.title("NM plot")
    ax.tick_params(axis="y", direction="in")
    ax.tick_params(axis="x", direction="in")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)


def plotting(DF, NMcurve):
    fig, ax = plt.subplots()
    settings(ax)
    plt.scatter(df["Mres"], df["Fx"])
    plt.plot(NMcurve["Moment (kNm)"], NMcurve["Fx (kN)"], color="red")
    plt.title(loc + ", " + str(datetime.datetime.now()))

    # max_Mres = df["Mres"].max()
    # min_Mres = df["Mres"].min()
    # max_Fx = df["Fx"].max()
    # min_Fx = df["Fx"].min()

    # print("Salient results (kN [Mres,Fx]):")

    # for x, y, C, e in zip(df["Mres"], df["Fx"], df["Cs"], df["element_nos"]):
    #     if x > 0.98*max_Mres or y > 0.98*max_Fx:
    #         print ("[", str(x)+","+str(y)+"]")
    #         t = C + "," + str(e)
    #         plt.text(x, y, t)
    annotateSalientPoints(df, loc)

    plt.savefig(".\\graphs\\" + loc + ".jpg")
    plt.show()


def annotateSalientPoints(df, loc):
    max_Mres = df["Mres"].max()
    min_Mres = df["Mres"].min()
    max_Fx = df["Fx"].max()
    min_Fx = df["Fx"].min()

    MresPercentAlong = pd.Series((1-df["Mres"]/min_Mres)/(1-max_Mres/min_Mres))
    FxPercentAlong = pd.Series((1-df["Fx"]/min_Fx)/(1-max_Fx/min_Fx))
    # print(df)
    # print(df['Mres'].abs() > 0.2)
    toAnnotate = df[(((MresPercentAlong < 0.005) | (MresPercentAlong > 0.98)) | (
        (FxPercentAlong < 0.01) | (FxPercentAlong > 0.99)))].copy()
    toAnnotate = toAnnotate[toAnnotate['Mres'].abs() > 0.2]

    for x, y, C, e in zip(toAnnotate["Mres"], toAnnotate["Fx"], toAnnotate["Cs"], toAnnotate["element_nos"]):
        c = C + "," + str(e)
        plt.text(x, y, c)

    toAnnotate.to_csv(r'.\\salient\\salient_'+loc+'.csv')


def loadNMCurve(loc):

    NMcurve = pd.read_excel(r'.\\NMcurve\\'+loc+'.xlsx', skiprows=1)
    return NMcurve


if __name__ == '__main__':

    loc = "NA"
    model = open_model(loc)
    user_params(loc)

    lists = model.get_all_saved_lists()
    # print(lists)
    print(lists[3])

    # piles_under_pilecap = lists[4] ## NP
    # piles_under_pilecap = lists[0] ## SA
    piles_under_pilecap = lists[3]  # NA

    elements_string = piles_under_pilecap.description
    elements = convert_to_2_list(elements_string)

    df = get_multiple_beam_results(elements, Cs_ULS, addl_pts)
    # df= get_multiple_beam_results(elements,["C1"],addl_pts)
    df.to_csv(r'.\\results\\results_'+loc+'.csv')
    del model

    NMcurve = loadNMCurve(loc)
    # print(NMcurve)

    plotting(df, NMcurve)


# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org openpyxl
