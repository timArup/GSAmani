import numpy as np 
import pandas as pd
from gsapy import GSA
from gsapy.modules import Element
from gsapy.modules import Node
from matplotlib import pyplot as plt
import datetime
from pathlib import Path
from pprint import pprint
import re

# import logging
# logging.basicConfig(level=logging.DEBUG)

def create_list(prefix, first, last):
    list = []
    for i in range(first, last+1):
        if i < 10:
            list.append(prefix + str(0) + str(i))
        else:
            list.append(prefix + str(i))
    return list


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
    "./models/Hud Footbridge_rev31.gwb"]
    userParams["version"] = "10.1"
    userParams["save_name"] = "hudData/foot31_UB"
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
#     userParams["Cs"] = [#create_list('C', 18, 23) + create_list('C', 39, 44) + create_list('C', 60, 65) + create_list('C', 81, 86)   #ULS C
#         "C53","C57","C61","C65"]
#     # userParams["addl_pts"] = 0
#     userParams["selEleLists"] = ["Connecting elements typical"] ### Only temporary and set up better
#     userParams["selNodLists"] = ["foundation nodes"] ### Only temporary and set up better
#     userParams["modelsList"]=[
#     "./models/A19 FB_rev0.gwb"]
#     userParams["version"] = "10.2"
#     userParams["save_name"] = "A19Data/A19"
#     userParams["locMap"] =  {
#             123:"Abutment x-",
#             124:"Abutment x+",
#             117:"Pier x-",
#             118:"Pier x+",
#         }
#     userParams["groups"] = {
#         "Abutments" : [123,124],
#         "Piers" : [117,118],
#     }
#     userParams["setMap"] =  {
#             53:"QD ULS B env.",
#             57:"QD ULS C env.",
#             61:"QD SLS char env.",
#             65:"QD ALS env.",
#         }
#     return userParams

# def userParams():
#     userParams={}
#     userParams["Cs"] = [#create_list('C', 18, 23) + create_list('C', 39, 44) + create_list('C', 60, 65) + create_list('C', 81, 86)   #ULS C
#         "C9","C14","C19"] #Actual
#         # "C4"] #testing 2 perms
#     userParams["addl_pts"] = 0
#     userParams["selEleLists"] = ["Platform 34"] ### Only temporary and set up better
#     userParams["selNodLists"] = ["foundation nodes"] ### Only temporary and set up better
#     userParams["modelsList"]=[
#     "./models/2024-04-03 Footbridge canopies.gwb"]
#     userParams["version"] = "10.2"
#     userParams["save_name"] = "hudData/can240403UB"
#     userParams["locMap"] =  {
#             144:"C3/4A",
#             142:"C3/4B",
#             143:"C3/4C",
#             147:"C5/6A",
#             145:"C5/6B",
#             146:"C5/6C",
#         }
#     userParams["setMap"] =  {
#                     9:"SLS",
#             14:"STR/GEO Set B",
#             19:"STR/GEO Set C",
#             5: "SLS - Maintenance",
#             6: "SLS - Snow Leading",
#             7: "SLS - Wind Leading",
#             8: "SLS - Aerodynamic Leading",
#             10: "STR/GEO Set B - Maintenance",
#             11: "STR/GEO Set B - Snow Leading",
#             12: "STR/GEO Set B - Wind Leading",
#             13: "STR/GEO Set B - Aerodynamic Leading",
#             15: "STR/GEO Set C - Maintenance",
#             16: "STR/GEO Set C - Snow Leading",
#             17: "STR/GEO Set C - Wind Leading",
#             18: "STR/GEO Set C - Aerodynamic Leading"
#         }
#     return userParams

# def userParams():
#     userParams={}
#     userParams["Cs"] = [#create_list('C', 18, 23) + create_list('C', 39, 44) + create_list('C', 60, 65) + create_list('C', 81, 86)   #ULS C
#         "C36","C37","C31"] #Actual - BUT NO ACC NO ULS C
#         # "C4"] #testing 2 perms
#     userParams["addl_pts"] = 0
#     # userParams["selEleLists"] = ["Platform 34"] ### Only temporary and set up better
#     userParams["selNodLists"] = ["Foundation node"] ### Only temporary and set up better
#     userParams["modelsList"]=[
#     "./models/Lift Shaft_rev3.gwb"] #models\Lift Shaft_rev2.gwb
#     userParams["version"] = "10.2"
#     userParams["save_name"] = "hudData/LS_r3"
#     userParams["locMap"] =  {
#             69:"FN"
#         }
#     userParams["setMap"] =  {
#             36:"ULS B",
#             37:"SLS",
#             31:"ULS Set C no accidental"
#         }
#     return userParams




class Model():

    kind="GSA"

    def __init__(self,path,version): #,lists=None
        self.version = version
        self.path = path
        try:
            self.exists = path.exists()
            # print(self.path)
            # print(self.version)
            self.model = GSA(path, version=self.version)
            # GSA.Output_Init_Flags(self.model)
            print("Model loaded successfully: " + str(self.path))
        except:
            print("Failure to Load model: " + str(self.path))

        # self.model.save_as("test.gwb")
        print("version: " + self.model.version())

        self.results = []
        self.lists = self.model.get_all_saved_lists()
        # print(self.lists)
        self.selEleLists = None
        self.selNodLists = ["foundation nodes"]
        self.elements = [ExtElement(x[1],self) for x in self.model.get_elements().items()] # .items converst the dictionary into a list, [1] is to drop the key returned from items()
        self.nodes = [ExtNode(x[1]) for x in self.model.get_nodes().items()]


        ######## Depends if I'm happy of method of filtering lists
        # if not lists:
        #     print("no list specified")
        #     self.lists = self.model.get_all_saved_lists()

    def setCombinationCases(self,userParams):
        self.resCombinationCases = userParams["Cs"]

    def getSelectedResultsElements(self,userParams):
        for element in self.resElements:
            element.getResults(self,userParams)
            self.results.append(element.results)

    def getSelectedResultsNodes(self,userParams):
        for node in self.resNodes:
            node.getResults(self,userParams)
            self.results.append(node.results)

    def setResLists(self,strResLists):
        self.resLists = []
        for strResList in strResLists:
            _found = False
            for list in self.lists:
                if strResList == list.name:
                    self.resLists.append(list)
                    _found = True
                    break
            if not _found:
                print("List is not in model: " + strResList)
    
    def setResElements(self,userParams):
        self.setResLists(userParams["selEleLists"])

        self.resElements = []
        for list in self.resLists:
            elements_string = list.description
            elementNos = self.convert_to_2_list(elements_string)
            self.resElements = [self.getElement(elementIndex) for elementIndex in elementNos]

    def setResNodes(self,userParams):
        self.setResLists(userParams["selNodLists"])

        self.resNodes = []
        for list in self.resLists:
            nodes_string = list.description
            nodeNos = self.convert_to_2_list(nodes_string)
            self.resNodes = [self.getNode(nodeIndex) for nodeIndex in nodeNos]

    def getElement(self,elementIndex):
        for element in self.elements:
            if element.index == elementIndex:
                return element
                
    def getNode(self,nodeIndex):
        for node in self.nodes:
            if node.index == nodeIndex:
                return node

    def convert_to_2_list(self,to_string):

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
        return updated

    # self.lists    
    def close(self):
        try:
            self.path.exists()
            del self.model
            print("Model closed: " + str(self.path))
        except:
            pass

# def generate_permutations(base_string):
#     permutations = []
#     p_number = 1

#     while True:
#         permutation = f"{base_string}p{p_number}"
#         permutations.append(permutation)
#         p_number += 1
#     return permutations

# # Example usage
# result = generate_permutations(combCase)

class ExtNode(Node):
    def __init__(self,node):
        self.index = node.index
        self.name = node.name
        self.colour = node.colour
        self.coords = node.coords
        self.x = node.coords[0]
        self.y = node.coords[1]
        self.z = node.coords[2]
        self.restraint = node.restraint
        self.axis = node.axis
        self.mesh_size = node.mesh_size
        self.spring_property = node.spring_property
        self.mass_property = node.mass_property
        self.damper_property = node.damper_property
        self.sID = node.sID
        self.results = []

    def getResults(self,model,userParams):
        
        for combCase in model.resCombinationCases:
            p_number =1
            while True:
                permutation = f"{combCase}p{p_number}"
                try:
                    # print(self.index)
                    # print(permutation)
                    result = model.model.get_node_reactions(self.index,  # the element number
                                                permutation,  # analysis case or combination number
                                                axis="local",  # output axis - if omitted, it uses the default axis
                    )
                    # print(results)
    
                    self.results.append(Result(result,self,permutation))
                    # print(self.results)
                except:
                    break
                p_number += 1

class ExtElement(Element):
    def __init__(self,element,model):
        self.index = element.index
        self.name = element.name
        self.colour = element.colour
        self.type = element.type
        self.prop = element.prop
        self.group = element.group
        self.topo = element.topo
        self.orient_node = element.orient_node
        self.orient_angle = element.orient_angle
        self.releases = element.releases
        self.offsets = element.offsets
        self.dummy = element.dummy
        self.parent_member = element.parent_member
        self.sID = element.sID
        self.results = []
        self.modelName = model.path


    def getResults(self,model,userParams):
        
        for combCase in model.resCombinationCases:
            print(f"Starting {combCase}")
            p_number =1
            while True:
                permutation = f"{combCase}p{p_number}"
                try:
                    # print(self.index)
                    # print(permutation)

                    results = model.model.get_1D_elem_resultants(self.index,  # the element number
                                                permutation,  # analysis case or combination number
                                                axis="local",  # output axis - if omitted, it uses the default axis
                                                addl_pts=userParams["addl_pts"])  # additional number of points along the 
                                                                                #element to output forces, if ommited it defaults to 0
                    # print(results)
                    for result in results:
                        self.results.append(Result(result,self,permutation))
                except:
                    break
                p_number += 1

    def getNodeFromIndex(self,index,nodeList):
        for node in nodeList:
            if node.index == index:
                return node
        print("Cannot locate node instance: " + index)

class Result():

    def __init__(self,result,object,combCase):
        # print(result)
        # print(object)
        # print(combCase)
        self.Index = object.index
        self.combCase = combCase
        self.Fx = result[0]
        self.Fy = result[1]
        self.Fz = result[2]
        self.Mxx = result[3]
        self.Myy = result[4]
        self.Mzz = result[5]
        self.Mres = (result[4]**2+result[5]**2)**0.5# combination of Myy and Mzz, absolute value
        self.Fres = (result[1]**2+result[2]**2)**0.5# combination of shear forces, absolute value


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
    save_name = userParams["save_name"]
    modelString = userParams["modelsList"][0]
    # print(modelString)

    print("Beginning to extract results from: " + str(modelString))
    myModel = Model(Path(modelString),userParams["version"])
    myModel.setCombinationCases(userParams)
    # myModel.setResElements(userParams)
    myModel.setResNodes(userParams)
    # print(myModel.resNodes)
    # myModel.getSelectedResultsElements(userParams)
    myModel.getSelectedResultsNodes(userParams)
    # print(myModel.res)

    results = {"nodeIndex":[],"combCasePerm":[],"Fx":[],"Fy":[],"Fz":[],"Mxx":[],"Myy":[],"Mzz":[]}
    for node in myModel.resNodes:
        # print(node)
        for result in node.results:
                # print(result)
                results["nodeIndex"].append(node.index)
                # results["modelName"].append(node.modelName)
                results["Fx"].append(result.Fx)
                results["Fy"].append(result.Fy)
                results["Fz"].append(result.Fz)
                results["Mxx"].append(result.Mxx)
                results["Myy"].append(result.Myy)
                results["Mzz"].append(result.Mzz)
                results["combCasePerm"].append(result.combCase)

    ### clean results and add info
    results = pd.DataFrame(results)
    results["combCase"] = results["combCasePerm"].apply(getCombCase)
    results["Location"] = results["nodeIndex"].apply(getLocation) 
    results["set"] = results["combCase"].apply(getSet)
    
    results.to_csv(f"Data/{save_name}Results.csv")


    #### ENVELOPED RESULTS

    nodes = results["nodeIndex"].unique()
    combCases = results["combCase"].unique()

    tabulatedResults = pd.DataFrame({"Location":[],"nodeIndex":[],"Type":[],"combCasePerm":[],"combCase":[],"set":[],"Fx":[],"Fy":[],"Fz":[],"Mxx":[],"Myy":[],"Mzz":[]})
    numCombCases = len(combCases)
    i=0
    for combCase in combCases:
        combRes = results[results["combCase"]==combCase]
        print("Starting CombCase: "+str(combCase)+" "+(str((i/numCombCases)*100)+" %"))
        i+=1
        for nodeIndex in nodes:
            nodeRes = combRes[combRes["nodeIndex"]==nodeIndex]
            
            maxFx = pd.DataFrame(nodeRes.loc[nodeRes['Fx'].idxmax()]).T
            maxFx["Type"]="maxFx"
            minFx = pd.DataFrame(nodeRes.loc[nodeRes['Fx'].idxmin()]).T
            minFx["Type"]="minFx"
            maxFy = pd.DataFrame(nodeRes.loc[nodeRes['Fy'].idxmax()]).T
            maxFy["Type"]="maxFy"
            minFy = pd.DataFrame(nodeRes.loc[nodeRes['Fy'].idxmin()]).T
            minFy["Type"]="minFy"
            maxFz = pd.DataFrame(nodeRes.loc[nodeRes['Fz'].idxmax()]).T
            maxFz["Type"]="maxFz"
            minFz = pd.DataFrame(nodeRes.loc[nodeRes['Fz'].idxmin()]).T
            minFz["Type"]="minFz"
            
            maxMxx = pd.DataFrame(nodeRes.loc[nodeRes['Mxx'].idxmax()]).T
            maxMxx["Type"]="maxMxx"
            minMxx = pd.DataFrame(nodeRes.loc[nodeRes['Mxx'].idxmin()]).T
            minMxx["Type"]="minMxx"
            maxMyy = pd.DataFrame(nodeRes.loc[nodeRes['Myy'].idxmax()]).T
            maxMyy["Type"]="maxMyy"
            minMyy = pd.DataFrame(nodeRes.loc[nodeRes['Myy'].idxmin()]).T
            minMyy["Type"]="minMyy"
            maxMzz = pd.DataFrame(nodeRes.loc[nodeRes['Mzz'].idxmax()]).T
            maxMzz["Type"]="maxMzz"
            minMzz = pd.DataFrame(nodeRes.loc[nodeRes['Mzz'].idxmin()]).T
            minMzz["Type"]="minMzz"

            tabulatedResults = pd.concat([tabulatedResults,maxFx,minFx,maxFy,minFy,maxFz,minFz,maxMxx,minMxx,maxMyy,minMyy,maxMzz,minMzz])


    tabulatedResults["Location"] = tabulatedResults["nodeIndex"].apply(getLocation) 
    tabulatedResults["set"] = tabulatedResults["combCase"].apply(getSet)
    tabulatedResults.to_csv(f"Data/{save_name}TabResults.csv")
        
    myModel.close()


