import numpy as np 
import pandas as pd
from gsapy import GSA
from gsapy.modules import Element
from gsapy.modules import Node
from matplotlib import pyplot as plt
import datetime
from pathlib import Path
from pprint import pprint

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
        "C25"]
    userParams["addl_pts"] = 0
    userParams["selEleLists"] = ["Connecting elements typical"] ### Only temporary and set up better
    userParams["selNodLists"] = ["foundation nodes"] ### Only temporary and set up better
    userParams["modelsList"]=[
    "./models/Hud Footbridge_rev17.gwb"]
    return userParams


class Model():

    kind="GSA"
    version="10.1"

    def __init__(self,path): #,lists=None
        self.path = path
        try:
            self.exists = path.exists()
            self.model = GSA(path, version=self.version)
            print("Model loaded successfully: " + str(self.path))
        except:
            print("Failure to Load model: " + self.path)
        self.results = []
        self.lists = self.model.get_all_saved_lists()
        self.selEleLists = None
        self.selNodLists = None
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
            print(elements_string)
            elementNos = self.convert_to_2_list(elements_string)
            self.resElements = [self.getElement(elementIndex) for elementIndex in elementNos]

    def setResNodes(self,userParams):
        self.setResLists(userParams["selNodLists"])

        self.resNodes = []
        for list in self.resLists:
            nodes_string = list.description
            print(nodes_string)
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

    modelString = userParams["modelsList"][0]
    myModel = Model(Path(modelString))

    print("Beginning to extract results from: " + str(modelString))
    myModel.setCombinationCases(userParams)
    # myModel.setResElements(userParams)
    myModel.setResNodes(userParams)
    # myModel.getSelectedResultsElements(userParams)
    myModel.getSelectedResultsNodes(userParams)

    # print(myModel.resElements)
    # print(myModel.resNodes)

    results = {"nodeIndex":[],"combCase":[],"Fx":[],"Fy":[],"Fz":[],"Mxx":[],"Myy":[],"Mzz":[]}
    for node in myModel.resNodes:
        # print(node)
        # print(node.results)
        for result in node.results:
                results["nodeIndex"].append(node.index)
                # results["modelName"].append(node.modelName)
                results["Fx"].append(result.Fx)
                results["Fy"].append(result.Fy)
                results["Fz"].append(result.Fz)
                results["Mxx"].append(result.Mxx)
                results["Myy"].append(result.Myy)
                results["Mzz"].append(result.Mzz)
                results["combCase"].append(result.combCase)
            # print(f"node:{node.index} perm:{result.combCase} Fx:{result.Fx} Fy:{result.Fy} Fz:{result.Fz}")

    results = pd.DataFrame(results)
    results.to_csv("results.csv")

    def get_max_min_rows(group):
        # print(group)
        max_values = pd.DataFrame(group.loc[group['Fx'].idxmax()]).T
        min_values = pd.DataFrame(group.loc[group['Fx'].idxmin()]).T

        max_values = pd.concat([max_values, pd.DataFrame(group.loc[group['Fy'].idxmax()]).T])
        min_values = pd.concat([min_values, pd.DataFrame(group.loc[group['Fy'].idxmin()]).T])

        max_values = pd.concat([max_values, pd.DataFrame(group.loc[group['Fz'].idxmax()]).T])
        min_values = pd.concat([min_values, pd.DataFrame(group.loc[group['Fz'].idxmin()]).T])

        max_values = pd.concat([max_values, pd.DataFrame(group.loc[group['Mxx'].idxmax()]).T])
        min_values = pd.concat([min_values, pd.DataFrame(group.loc[group['Mxx'].idxmin()]).T])

        max_values = pd.concat([max_values, pd.DataFrame(group.loc[group['Myy'].idxmax()]).T])
        min_values = pd.concat([min_values, pd.DataFrame(group.loc[group['Myy'].idxmin()]).T])

        max_values = pd.concat([max_values, pd.DataFrame(group.loc[group['Mzz'].idxmax()]).T])
        min_values = pd.concat([min_values, pd.DataFrame(group.loc[group['Mzz'].idxmin()]).T])

        return pd.concat([max_values, min_values])

    tabulatedResults = results.groupby('nodeIndex').apply(get_max_min_rows).reset_index(drop=True)
    # print(tabulatedResults)
    # tabulatedResults = tabulatedResults.T.reset_index(drop=True).T
    # print(tabulatedResults)
    tabulatedResults.to_csv("tabResults.csv")

    myModel.close()


