import streamlit as st
import numpy as np 
import pandas as pd
from gsapy import GSA
from gsapy.modules import Element
from gsapy.modules import Node
from matplotlib import pyplot as plt
import datetime
from pathlib import Path
import pythoncom

# def runExtraction(userParams):

#     combinedModels.getCombResults(userParams)
#     plotResults = combinedModels.listElementsToPlot()
#     plotResults = pd.DataFrame(plotResults)
#     st.dataframe(combinedModels.listElementsToPlot())
#     combinedModels.close()
#     return combinedModels

class Model(): 

    kind="GSA"
    version="10.1"

    def __init__(self,path): #,lists=None
        self.path = path
        try:
            self.exists = path.exists()
            pythoncom.CoInitialize()
            self.model = GSA(path, version=self.version)
            st.write("Model loaded successfully: " + str(self.path)) # This doesn't seem to work. 
            # # st.write([x for x in self.model.get_analysis_case().items()])
            # # self.combCasesInModel = ["C"+ str(x[0]) for x in self.model.get_analysis_case().items()]
            # self.lists = self.model.get_all_saved_lists()
            # self.elements = [ExtElement(x[1],self) for x in self.model.get_elements().items()] # .items converst the dictionary into a list, [1] is to drop the key returned from items()
            # self.nodes = [ExtNode(x[1]) for x in self.model.get_nodes().items()]
        except:
            st.write("Failure to Load model: " + str(self.path))
        self.results = []
        self.selLists = None

    

    def setElementMidpointHeight(self):
        for element in self.elements:
            element.setMightpointHeight(self)

    # def setCombinationCases(self,userParams):
    #     self.resCombinationCases = userParams["Cs"]

        # if userParams["combCaseToExtract"] == "all":
        #     self.resCombinationCases = self.combCasesInModel
        # else:
        #     self.resCombinationCases = userParams["combCaseToExtract"]

    def getSelectedResults(self,userParams):
        hFdf = userParams["heightFilter"] # Short for "height Filter dataframe"
        if not ( hFdf["type"]=="less than" or hFdf["type"]=="greater than" or hFdf["type"]=="between" or hFdf==None or hFdf["type"]==None ):
            st.write("filter is not wokring correctly, investigate.")
        for element in self.resElements:
            if hFdf["type"]=="less than":
                if element.midpointHeight < hFdf["val_1"]:
                    element.getResults(self,userParams)
                    self.results.append(element.results)
            elif hFdf["type"]=="greater than":
                if element.midpointHeight > hFdf["val_1"]:
                    element.getResults(self,userParams)
                    self.results.append(element.results)
            elif hFdf["type"]=="between":
                if min(hFdf["val_1"],hFdf["val_2"]) < element.midpointHeight < max(hFdf["val_1"],hFdf["val_2"]):
                    element.getResults(self,userParams)
                    self.results.append(element.results)
            elif hFdf==None or hFdf["type"]==None:
                element.getResults(self,userParams)
                self.results.append(element.results)
            else:
                element.getResults(self,userParams)
                self.results.append(element.results)

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
                st.write("List is not in model: " + strResList)
    
    def setResElements(self,userParams):
        self.setResLists(userParams["selLists"])

        self.resElements = []
        for list in self.resLists:
            elements_string = list.description
            elementNos = self.convert_to_2_list(elements_string)
            self.resElements = [self.getElement(elementIndex) for elementIndex in elementNos]

    def getElement(self,elementIndex):
        for element in self.elements:
            if element.index == elementIndex:
                return element

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

    def close(self):
        try:
            self.path.exists()
            del self.model
            st.write("Model closed: " + str(self.path))
        except:
            pass

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
        # for combCase in model.resCombinationCases:
        for combCase in userParams["cCaseAttempts"]:
            try:
                results = model.model.get_1D_elem_resultants(self.index,  # the element number
                                        combCase,  # analysis case or combination number
                                        axis="local",  # output axis - if omitted, it uses the default axis
                                        addl_pts=userParams["addl_pts"])  # additional number of points along the 
                                                                        #element to output forces, if ommited it defaults to 0
                for result in results:
                    self.results.append(Result(result,self,combCase))
            except:
                print("Not working"+combCase)
                userParams["cCaseAttempts"].remove(combCase)

    def setMightpointHeight(self,model):
        if self.type == "BEAM":
            _node1z = self.getNodeFromIndex(self.topo[0],model.nodes).z
            _node2z = self.getNodeFromIndex(self.topo[1],model.nodes).z
            self.midpointHeight = (_node1z + _node2z)/2
            # return self.midpointHeight
        else:
            pass
            # st.write("setMidpointHeight has only been tested on Beam. Currently unavailable.")

    def getNodeFromIndex(self,index,nodeList):
        for node in nodeList:
            if node.index == index:
                return node
        st.write("Cannot locate node instance: " + index)

    # self.addlPointsResults
    # self.results
    # self.midpointZ
    # Could have lots of functions to do bits with Adsec etc.

class Result():

    def __init__(self,result,element,combCase):
        self.elementIndex = element.index
        self.combCase = combCase
        self.Fx = result[0]
        self.Fy = result[1]
        self.Fz = result[2]
        self.Mxx = result[3]
        self.Myy = result[4]
        self.Mzz = result[5]
        self.Mres = (result[4]**2+result[5]**2)**0.5# combination of Myy and Mzz, absolute value
        self.Fres = (result[1]**2+result[2]**2)**0.5# combination of shear forces, absolute value

    # self.distanceAlongElement

class CombinedModels():		
    def __init__(self,userParams):
        self.modelsList = userParams["modelsList"]
        self.models = []
        for modelString in self.modelsList:
            self.models.append(Model(Path(modelString)))

    def getCombResults(self,userParams):
        self.combResults = []
        for model in self.models:
            st.write("Beginning to extract results from: " + str(model.path))
            # model.setCombinationCases(userParams)
            model.setElementMidpointHeight()
            model.setResElements(userParams)
            model.getSelectedResults(userParams)
            self.combResults.extend(model.resElements)
        return self.combResults

    def listElementsToPlot(self):
        plotResults = {"Fx":[],"Mres":[],"Fres":[],"elementIndex":[],"modelName":[],"combCase":[]}
        for element in self.combResults:
            for result in element.results:
                plotResults["elementIndex"].append(element.index)
                plotResults["modelName"].append(element.modelName)
                plotResults["Fx"].append(result.Fx)
                plotResults["Mres"].append(result.Mres)
                plotResults["Fres"].append(result.Fres)
                plotResults["combCase"].append(result.combCase)
        return plotResults

    def close(self):
        for model in self.models:
            del model.model


def extract1x1(userParams):
    resElements = []
    plotResults = {"Fx":[],"Mres":[],"Fres":[],"elementIndex":[],"modelName":[],"combCase":[],"midpointHeight":[]}

    for modelStr in userParams["modelsList"]:
        # GSA.export_to_csv(Path(modelStr))
        modelStr += '.gwb'
        model = Model(Path(".")/"data/models"/modelStr)
        # model.model.export_to_csv(Path("./helper"))
        st.write("Beginning to extract results from: " + str(modelStr))
        # model.setCombinationCases(userParams)
        model.setElementMidpointHeight()
        model.setResElements(userParams)
        model.getSelectedResults(userParams)
        resElements.extend(model.resElements)
        del model
        st.write("Model closed.")

    for element in resElements:
        for result in element.results:
            plotResults["elementIndex"].append(element.index)
            plotResults["modelName"].append(element.modelName)
            plotResults["Fx"].append(result.Fx)
            plotResults["Mres"].append(result.Mres)
            plotResults["Fres"].append(result.Fres)
            plotResults["combCase"].append(result.combCase)
            plotResults["midpointHeight"].append(element.midpointHeight)

    return plotResults

def experimentCSV():
    modelStr = "NAmodel_08_EastGL 25.5_additionalPiles.gwb"
    modelObj = Model(Path(".")/"data/models"/modelStr)
    # GSA.export_to_csv(Path(modelStr))

    try:
        GSA.export_to_csv(Path("./test"))
    except:
        print("no bueno")
        pass
    modelObj.model.export_to_csv(Path("./test/"))

    del modelObj