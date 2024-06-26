import streamlit as st

def create_list(prefix, first, last):
    list = []
    for i in range(first, last+1):
        if i < 10:
            list.append(prefix + str(0) + str(i))
        else:
            list.append(prefix + str(i))
    return list

# def defaultExSettings():

#     defaultExSettings={
#         "addl_pts" : 0,
#         "selLists" : ["piles below pilecap"],
#         "heightFilter" : { #None, greater than, less than, between, val_1, val_2, . Only specify val_1 for > or <, specify both for between. None is no filter. Works off midpoint of elements.
#     "type":None},
#     "modelsList" : [
#     # "./models/NP model_04d_comp-springs_+3m_1.25x.gwb"
#     # "./models/NP model_04g 20 v spring.gwb"
#     # "./models/NAmodel_08_test_Nslope.gwb",
#     # "./models/NAmodel_08_VSExcavation.gwb",
#     # "./models/NAmodel_08_0.5springs_VSExcavation.gwb",
#     # "./models/NAmodel_08_0.5weaksprings_VSExcavation.gwb",
#     # "./models/NAmodel_08_2springs_VSExcavation.gwb"
#     # "NAmodel_08_EastGL 25.5_additionalPiles",
#     # "NAmodel_08_0.5springs_EastGL 25.5_additionalPiles",
#     # "NAmodel_08_0.5weaksprings_EastGL 25.5_additionalPiles",
#     # "NAmodel_08_2springs_EastGL 25.5_additionalPiles"
#     "NAmodel_09",
#     "NAmodel_09_0.5springs",
#     "NAmodel_09_0.5weaksprings",
#     "NAmodel_09_2springs"
#     # "./models/NAmodel_08_EastGL 23.5 EPS.gwb",
#     # "./models/NAmodel_08_0.5springs_EastGL 23.5 EPS.gwb",
#     # "./models/NAmodel_08_0.5weaksprings_EastGL 23.5 EPS.gwb",
#     # "./models/NAmodel_08_2springs_EastGL 23.5 EPS.gwb"
#     # "./models/test.gwb"
#     ],

#     # "cCaseAttempts" : create_list("C", 1, 150),
#     # "cCaseAttempts" : ["C12","C13","C14","C15","C16","C17",
#     #                         "C33","C34","C35","C36","C37","C38",
#     #                         "C54","C55","C56","C57","C58","C59",
#     #                         "C75","C76","C77","C78","C79","C80"], #ULS B NA
#     "cCaseAttempts" : ["C12","C13","C14","C15","C16","C17",
#                         "C33","C34","C35","C36","C37","C38",
#                         "C54","C55","C56","C57","C58","C59",
#                         "C75","C76","C77","C78","C79","C80",
#                         "C10","C11","C31","C32","C52","C53","C73","C74"], #ULS B AND SLS QP NA

#     "saveExSettingsName" : ""
                        
    
#     }

#     return defaultExSettings

def perm_out(prefix, first, last):
    list = []
    for i in range(first, last+1):
        list.append(prefix + "p" + str(i))
    return list

def defaultExSettings():

    defaultExSettings={
        "addl_pts" : 0,
        "selLists" : ["piles below pilecap top"],
        "heightFilter" : { #None, greater than, less than, between, val_1, val_2, . Only specify val_1 for > or <, specify both for between. None is no filter. Works off midpoint of elements.
    "type":None},
    "modelsList" : [
    "NAmodel_09","NAmodel_09_0.5weaksprings","NAmodel_09_0.5prings","NAmodel_09_2springs"
    ],
    "cCaseAttempts" : ["C12","C13","C14","C15","C16","C17",
                            "C33","C34","C35","C36","C37","C38",
                            "C54","C55","C56","C57","C58","C59",
                            "C75","C76","C77","C78","C79","C80"], #ULS B NA
    "saveExSettingsName" : ""
    }
    # defaultExSettings={
    #     "addl_pts" : 0,
    #     "selLists" : ["columns"],
    #     "heightFilter" : { #None, greater than, less than, between, val_1, val_2, . Only specify val_1 for > or <, specify both for between. None is no filter. Works off midpoint of elements.
    # "type":None},
    # "modelsList" : [
    # "Hud Footbridge_rev9"
    # ],
    # "cCaseAttempts" : perm_out("C31",1,13328), #ULS B AND SLS QP NA
    # "saveExSettingsName" : ""
    # }

    return defaultExSettings