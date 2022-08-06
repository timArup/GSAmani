# import numpy
from numpy import sqrt
import pandas as pd
from gsapy import GSA
from matplotlib import pyplot as plt
# from pathlib import Path

def create_list(prefix,first,last):
    list = []
    for i in range(first,last+1):
        list.append(prefix + str(i))
    return list

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

def open_model():
    model = GSA(r'.\\NPmodel_02.gwb', version = "10.1")
    return model

def beam_results(no,combination):
    return model.get_1D_elem_resultants(no, # the element number
     combination, # analysis case or combination number
    axis="local", # output axis - if omitted, it uses the default axis
    addl_pts=0) # additional number of points along the element to output forces, if ommited it defaults to 0

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

def get_multiple_beam_results(elements):
    # R0 = []
    # R1 = []
    # Rs = {}
    # layers = {}
    # # first = True

    Fx = []
    Mres = []
    Cs = []
    for combination in Cs_ULS:
        for element_no in elements:
            results = beam_results(element_no,combination)
        #     print(results)
        #     R0.append({'0Fx':results[0][0],'0Fy':results[0][1],'0Fz':results[0][2],'0Mxx':results[0][3],'0Myy':results[0][4],'0Mzz':results[0][5]})
        #     R1.append({'1Fx':results[1][0],'1Fy':results[1][1],'1Fz':results[1][2],'1Mxx':results[1][3],'1Myy':results[1][4],'1Mzz':results[1][5]})

        #     Rs.update({'0Fx':results[0][0],'0Fy':results[0][1],'0Fz':results[0][2],'0Mxx':results[0][3],'0Myy':results[0][4],'0Mzz':results[0][5],
        # '1Fx':results[1][0],'1Fy':results[1][1],'1Fz':results[1][2],'1Mxx':results[1][3],'1Myy':results[1][4],'1Mzz':results[1][5]})
        
        #     layers.update({element_no: {'Res_0': {'Fx':results[0][0],'Fy':results[0][1],'Fz':results[0][2],'Mxx':results[0][3],'Myy':results[0][4],'Mzz':results[0][5]}, 'Res_1':
        #     {'Fx':results[1][0],'Fy':results[1][1],'Fz':results[1][2],'Mxx':results[1][3],'Myy':results[1][4],'Mzz':results[1][5]}}})
        #     print(Rs)  

        # # return layers
        # return Rs

            Fx.append(results[0][0])
            Fx.append(results[1][0])
            Mres.append((results[0][4]**2+results[0][5]**2)**0.5)
            Mres.append((results[1][4]**2+results[1][5]**2)**0.5)
            Cs.append(combination)

    return Fx, Mres, Cs

def results_analysis(df):
    df['WC_0'] = {'Fx': df['Res_0']['Fx'] ,'Mres': sqrt( df['Res_0']['Myy']**2 + df['Res_0']['Mzz']**2 )}


if __name__ == '__main__':

    model = open_model()
    # beam_results(115)
    user_params()
    # print(Cs_ULS)

    lists = model.get_all_saved_lists()
    # print(lists)

    piles_under_pilecap = lists[4]
    # print(piles_under_pilecap)

    elements_string = piles_under_pilecap.description
    elements = convert_to_2_list(elements_string)
    # print(elements)


    Fx, Mres, Cs= get_multiple_beam_results(elements)
    # results = pd.DataFrame.from_dict(get_multiple_beam_results(elements))
    # results = pd.DataFrame.from_dict(Rs, orient='index')
    # user_dict = get_multiple_beam_results(elements)
    # results = pd.DataFrame.from_dict({(i,j): user_dict[i][j] 
    #                        for i in user_dict.keys() 
    #                        for j in user_dict[i].keys()},
    #                    orient='index')

    # results.to_csv('data.csv')

    # results['0Mres'] = (results['0Myy']**2+results['0Mzz']**2)
    # results['1Mres'] = (results['1Myy']**2+results['1Mzz']**2)
    # print(Cs)
    plt.scatter(Mres,Fx)

    for i in range(len(Mres)-1):
        M = Mres[i]
        F = Fx[i]
        C = Cs[i] 
        plt.text(x=M, y=F, s=C)
    plt.show()
    # print(Fx)
    # print(Mres)

    # results = pd.DataFrame.from_dict({'Res_0':R0,'Res_1':R1}, index=elements)
    # results_analysis(results)

    del model
