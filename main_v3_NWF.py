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
        "C21","C22","C23","C24"]
        # "C4"] #testing 2 perms
         #create_list('C', 18, 23) + create_list('C', 39, 44) + create_list('C', 60, 65) + create_list('C', 81, 86) ]  #ULS C
    userParams["addl_pts"] = 0
    userParams["selEleLists"] = ["Piles Head under pilecap"] ### Only temporary and set up better
    # userParams["selNodLists"] = ["foundation nodes"] ### Only temporary and set up better
    # userParams["modelsList"]=[
    # "./models/2023-11-24 Footbridge canopies.gwb"]
    userParams["version"] = "10.2"
    userParams["modelsList"]=[
    # "./models/South Pier - Pilecap (STQ062)_+Fy+Fz.gwb",
    # "./models/South Pier - Pilecap (STQ062)_+Fy-Fz.gwb",
    # "./models/South Pier - Pilecap (STQ062)_-Fy+Fz.gwb",
    # "./models/South Pier - Pilecap (STQ062)_-Fy-Fz.gwb"
    "./models/South Pier - Pilecap (100% Design)_+Fy+Fz.gwb",
    "./models/South Pier - Pilecap (100% Design)_+Fy-Fz.gwb",
    "./models/South Pier - Pilecap (100% Design)_-Fy+Fz.gwb",
    "./models/South Pier - Pilecap (100% Design)_-Fy-Fz.gwb"
    ]
    return userParams


class Model():

    kind="GSA"

    def __init__(self,path,version): #,lists=None
        self.version = version
        self.path = path
        try:
            self.exists = path.exists()
            # print(self.version)
            self.model = GSA(path, version=self.version)
            # GSA.Output_Init_Flags(self.model)
            print("Model loaded successfully: " + str(self.path))
        except:
            print("Failure to Load model: " + self.path)

        # self.model.save_as("test.gwb")
        # print(self.model.version())

        self.results = []
        self.lists = self.model.get_all_saved_lists()
        self.selEleLists = None
        self.selNodLists = None
        self.elements = [ExtElement(x[1],self) for x in self.model.get_elements().items()] # .items converst the dictionary into a list, [1] is to drop the key returned from items()
        # print(self.elements)
        self.nodes = [ExtNode(x[1]) for x in self.model.get_nodes().items()]


        ######## Depends if I'm happy of method of filtering lists
        # if not lists:
        #     print("no list specified")
        #     self.lists = self.model.get_all_saved_lists()

    def setCombinationCases(self,userParams):
        self.resCombinationCases = userParams["Cs"]

    def getSelectedResultsElements(self,userParams):
        for element in self.resElements:
            # element.getResults(self,userParams,"element-case")
            element.getResults(self,userParams,"element-perm")
            self.results.append(element.results)

    def getSelectedResultsNodes(self,userParams):
        for node in self.resNodes:
            node.getResults(self,userParams,"node-perm")
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


class CombinedModels():		
    def __init__(self,userParams):
        self.modelsList = userParams["modelsList"]
        self.models = []
        for modelString in self.modelsList:
            self.models.append(Model(Path(modelString),userParams["version"]))

    def getCombResults(self,userParams):
        self.combResults = []
        for model in self.models:
            print("Beginning to extract results from: " + str(model.path))
            model.setCombinationCases(userParams)
            # model.setElementMidpointHeight()
            model.setResElements(userParams)
            model.getSelectedResultsElements(userParams)
            self.combResults.extend(model.resElements)

    def getResData(self):
        results = {"elementIndex":[],"modelName":[],"combCasePerm":[],"Fx":[],"Fy":[],"Fz":[],"Mxx":[],"Myy":[],"Mzz":[]}
        for element in self.combResults:
            for result in element.results:
                results["elementIndex"].append(element.index)
                results["modelName"].append(element.modelName)
                results["combCasePerm"].append(result.combCase)
                results["Fx"].append(result.Fx)
                results["Fy"].append(result.Fy)
                results["Fz"].append(result.Fz)
                results["Mxx"].append(result.Mxx)
                results["Myy"].append(result.Myy)
                results["Mzz"].append(result.Mzz)
        return results

    def close(self):
        for model in self.models:
            del model.model

    # self.NMplot

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


    def getResults(self,model,userParams,style):

        if style == "node-perm":
            for combCase in model.resCombinationCases:
                # print(f"Starting {combCase}")
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
        elif style=="element-case":
            for combCase in model.resCombinationCases:
                results = model.model.get_1D_elem_resultants(self.index,  # the element number
                                            combCase,  # analysis case or combination number
                                            axis="local",  # output axis - if omitted, it uses the default axis
                                            addl_pts=userParams["addl_pts"])  # additional number of points along the 
                                                                            #element to output forces, if ommited it defaults to 0
                for result in results:
                    self.results.append(Result(result,self,combCase))

        elif style=="element-perm":
            for combCase in model.resCombinationCases:

                # print(f"Starting {combCase}")
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




if __name__ == '__main__':

    userParams = userParams()

    combinedModels = CombinedModels(userParams)
    combinedModels.getCombResults(userParams)
    results = pd.DataFrame(combinedModels.getResData())
    results.to_csv("./NWFdata/100pcResults.csv")
    combinedModels.close()

    # userParams = userParams()
    # save_name = userParams["save_name"]
    # modelString = userParams["modelsList"][0]

    # print("Beginning to extract results from: " + str(modelString))
    # myModel = Model(Path(modelString),userParams["version"])
    # myModel.setCombinationCases(userParams)
    # # myModel.setResElements(userParams)
    # myModel.setResNodes(userParams)
    # # myModel.getSelectedResultsElements(userParams)
    # myModel.getSelectedResultsNodes(userParams)

    # results = {"nodeIndex":[],"combCasePerm":[],"Fx":[],"Fy":[],"Fz":[],"Mxx":[],"Myy":[],"Mzz":[]}
    # for node in myModel.resNodes:
    #     for result in node.results:
    #             results["nodeIndex"].append(node.index)
    #             # results["modelName"].append(node.modelName)
    #             results["Fx"].append(result.Fx)
    #             results["Fy"].append(result.Fy)
    #             results["Fz"].append(result.Fz)
    #             results["Mxx"].append(result.Mxx)
    #             results["Myy"].append(result.Myy)
    #             results["Mzz"].append(result.Mzz)
    #             results["combCasePerm"].append(result.combCase)

    # ### clean results and add info
    # results = pd.DataFrame(results)
    # results["combCase"] = results["combCasePerm"].apply(getCombCase)
    # results["Location"] = results["nodeIndex"].apply(getLocation) 
    # results["set"] = results["combCase"].apply(getSet)
    
    # results.to_csv(f"hudData/{save_name}Results.csv")


    # #### ENVELOPED RESULTS

    # nodes = results["nodeIndex"].unique()
    # combCases = results["combCase"].unique()

    # tabulatedResults = pd.DataFrame({"Location":[],"nodeIndex":[],"Type":[],"combCasePerm":[],"combCase":[],"set":[],"Fx":[],"Fy":[],"Fz":[],"Mxx":[],"Myy":[],"Mzz":[]})
    # numCombCases = len(combCases)
    # i=0
    # for combCase in combCases:
    #     combRes = results[results["combCase"]==combCase]
    #     print("Starting CombCase: "+str(combCase)+" "+(str((i/numCombCases)*100)+" %")
    #     i+=1
    #     for nodeIndex in nodes:
    #         nodeRes = combRes[combRes["nodeIndex"]==nodeIndex]
            
    #         maxFx = pd.DataFrame(nodeRes.loc[nodeRes['Fx'].idxmax()]).T
    #         maxFx["Type"]="maxFx"
    #         minFx = pd.DataFrame(nodeRes.loc[nodeRes['Fx'].idxmin()]).T
    #         minFx["Type"]="minFx"
    #         maxFy = pd.DataFrame(nodeRes.loc[nodeRes['Fy'].idxmax()]).T
    #         maxFy["Type"]="maxFy"
    #         minFy = pd.DataFrame(nodeRes.loc[nodeRes['Fy'].idxmin()]).T
    #         minFy["Type"]="minFy"
    #         maxFz = pd.DataFrame(nodeRes.loc[nodeRes['Fz'].idxmax()]).T
    #         maxFz["Type"]="maxFz"
    #         minFz = pd.DataFrame(nodeRes.loc[nodeRes['Fz'].idxmin()]).T
    #         minFz["Type"]="minFz"
            
    #         maxMxx = pd.DataFrame(nodeRes.loc[nodeRes['Mxx'].idxmax()]).T
    #         maxMxx["Type"]="maxMxx"
    #         minMxx = pd.DataFrame(nodeRes.loc[nodeRes['Mxx'].idxmin()]).T
    #         minMxx["Type"]="minMxx"
    #         maxMyy = pd.DataFrame(nodeRes.loc[nodeRes['Myy'].idxmax()]).T
    #         maxMyy["Type"]="maxMyy"
    #         minMyy = pd.DataFrame(nodeRes.loc[nodeRes['Myy'].idxmin()]).T
    #         minMyy["Type"]="minMyy"
    #         maxMzz = pd.DataFrame(nodeRes.loc[nodeRes['Mzz'].idxmax()]).T
    #         maxMzz["Type"]="maxMzz"
    #         minMzz = pd.DataFrame(nodeRes.loc[nodeRes['Mzz'].idxmin()]).T
    #         minMzz["Type"]="minMzz"

    #         tabulatedResults = pd.concat([tabulatedResults,maxFx,minFx,maxFy,minFy,maxFz,minFz,maxMxx,minMxx,maxMyy,minMyy,maxMzz,minMzz])


    # tabulatedResults["Location"] = tabulatedResults["nodeIndex"].apply(getLocation) 
    # tabulatedResults["set"] = tabulatedResults["combCase"].apply(getSet)
    # tabulatedResults.to_csv(f"hudData/{save_name}TabResults.csv")
        
    # myModel.close()


