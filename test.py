# import numpy
from numpy import sqrt
import pandas as pd
from gsapy import GSA
from matplotlib import pyplot as plt
# from pathlib import Path

def open_model():
    model = GSA(r'.\\NPmodel_02.gwb', version = "10.1")
    return model

def user_params():
    global Cs_ULS
    global Cs_ULS_C
    global Cs_SLS
    global Cs_SLS_QP
    Cs_ULS = create_list('C',11,16) + create_list('C',28,33) + create_list('C',42,47) + create_list('C',56,61)
    Cs_ULS_C = create_list('C',11,16) + create_list('C',28,33) + create_list('C',42,47) + create_list('C',56,61)
    Cs_SLS = create_list('C',3,8) + create_list('C',20,25) + create_list('C',34,39) + create_list('C',48,53)
    Cs_SLS_QP = ["C9","C10","C26","C27","C40","C41","C54","C55",]

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

def get_multiple_beam_results(elements):
    Fx = []
    Mres = []
    Cs = []
    xDivL = []

    for combination in Cs_ULS:

        for element_no in elements:
            results = beam_results(element_no,combination,addl_pts)

            for i in range(addl_pts + 1):
                result = results[i]

                Fx.append(result[0])
                Fx.append(result[0])
                Mres.append((result[4]**2+result[5]**2)**0.5)
                Mres.append((result[4]**2+result[5]**2)**0.5)
                Cs.append(combination)
                xDivL.append(distance_along_element(i,addl_pts))

    return Fx, Mres, Cs


if __name__ == '__main__':

    model = open_model()
    user_params()

    lists = model.get_all_saved_lists()

    piles_under_pilecap = lists[4]

    elements_string = piles_under_pilecap.description
    elements = convert_to_2_list(elements_string)

    Fx, Mres, Cs= get_multiple_beam_results(elements)

    # results.to_csv('data.csv')

    ##################################

    plt.scatter(Mres,Fx)

    # for i in range(len(Mres)-1):
    #     M = Mres[i]
    #     F = Fx[i]
    #     # C = Cs[i] 
    #     plt.text(x=M, y=F, s=C)

    plt.show()



    del model
