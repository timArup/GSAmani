from telnetlib import PRAGMA_HEARTBEAT
from turtle import xcor
import xdrlib
import numpy
import pandas as pd
from gsapy import GSA
from gsapy.modules import Element
from gsapy.modules import Node
from matplotlib import pyplot as plt
import datetime
from pathlib import Path


def userParams():
    #For SP temp
    userParams={}
    userParams["Cs"] = [
        "C09","C10","C11","C12","C13","C14"] # ULS B
        # "C15","C16","C17","C18","C19","C20"] # ULS C
        # "C01","C02","C03","C04","C05","C06"] # SLS
    # userParams["modelPrefix"] = " model_03_-"
    userParams["addl_pts"] = 0
    userParams["selLists"] = ["piles under pilecap"] ### Only temporary and set up better
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
        self.selLists = None
        self.elements = [ExtElement(x[1],self) for x in self.model.get_elements().items()] # .items converst the dictionary into a list, [1] is to drop the key returned from items()
        self.nodes = [ExtNode(x[1]) for x in self.model.get_nodes().items()]


        ######## Depends if I'm happy of method of filtering lists
        # if not lists:
        #     print("no list specified")
        #     self.lists = self.model.get_all_saved_lists()

    def setElementMidpointHeight(self):
        for element in self.elements:
            element.setMightpointHeight(self)

    def setCombinationCases(self,userParams):
        self.resCombinationCases = userParams["Cs"]

    def getSelectedResults(self,userParams):
        hFdf = userParams["heightFilter"] # Short for "height Filter dataframe"
        if not ( hFdf["type"]=="less than" or hFdf["type"]=="greater than" or hFdf["type"]=="between" or hFdf==None or hFdf["type"]==None ):
            print("filter is not wokring correctly, investigate.")
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
                print("List is not in model: " + strResList)
    
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

    # self.lists    
    def close(self):
        try:
            self.path.exists()
            del self.model
            print("Model closed: " + str(self.path))
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
        for combCase in model.resCombinationCases:
            results = model.model.get_1D_elem_resultants(self.index,  # the element number
                                        combCase,  # analysis case or combination number
                                        axis="local",  # output axis - if omitted, it uses the default axis
                                        addl_pts=userParams["addl_pts"])  # additional number of points along the 
                                                                        #element to output forces, if ommited it defaults to 0
            for result in results:
                self.results.append(Result(result,self,combCase))

    def setMightpointHeight(self,model):
        if self.type == "BEAM":
            _node1z = self.getNodeFromIndex(self.topo[0],model.nodes).z
            _node2z = self.getNodeFromIndex(self.topo[1],model.nodes).z
            self.midpointHeight = (_node1z + _node2z)/2
            # return self.midpointHeight
        else:
            pass
            # print("setMidpointHeight has only been tested on Beam. Currently unavailable.")

    def getNodeFromIndex(self,index,nodeList):
        for node in nodeList:
            if node.index == index:
                return node
        print("Cannot locate node instance: " + index)

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
            print("Beginning to extract results from: " + str(model.path))
            model.setCombinationCases(userParams)
            model.setElementMidpointHeight()
            model.setResElements(userParams)
            model.getSelectedResults(userParams)
            self.combResults.extend(model.resElements)

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

    # self.NMplot

def settings(ax,xStr,yStr):
    plt.ylabel(yStr + ' (kNm)')
    plt.xlabel(xStr + ' (kN)')
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

def filterPlotResult(xStr,yStr,plotResults,userParams):
    x=pd.Series(plotResults[xStr])
    y=pd.Series(plotResults[yStr])
    max_x = x.max()
    min_x = x.min()
    max_y = y.max()
    print(f"max {yStr}=: {str(max_y)}")
    min_y = y.min()
    print(f"min {yStr}=: {str(min_y)}")
    xPercentAlong = pd.Series((1-x/min_x)/(1-max_x/min_x))
    yPercentAlong = pd.Series((1-y/min_y)/(1-max_y/min_y))
    filter = (((xPercentAlong < 0.005) | (xPercentAlong > 0.90)) | (
        (yPercentAlong < 0.01) | (yPercentAlong > 0.99))) & (x.abs() > 200) & (y.abs() > 50)
    plotResults = pd.DataFrame(plotResults)
    toAnnotate = plotResults[filter].copy()
    x = x[filter]
    y = y[filter]
    for x, y, m, C, e in zip(x, y, toAnnotate["modelName"],toAnnotate["combCase"], toAnnotate["elementIndex"]):
        c = C + "," + str(e) + ",", m
        plt.text(x, y, c)
    toAnnotate.to_csv(r'.\\salient\\salient_'+userParams["loc"]+'_'+yStr+'_'+ str(userParams["selLists"]) + '.csv')

def plotting(xStr,yStr,plotResults,userParams,NMcurve=False):
    fig, ax = plt.subplots()
    settings(ax,xStr,yStr)
    plt.scatter(plotResults[xStr],plotResults[yStr])
    try:
        NMcurve.empty
        plt.plot(NMcurve["Moment (kNm)"], NMcurve["Fx (kN)"], color="red")
    except:
        pass
    plt.title(str(userParams["strNMCurve"]) + ", " + str(userParams["selLists"]) + "," + str(datetime.datetime.now()))
    # plt.text(0, 1, userParams["heightFilter"].items(), fontsize=12)
    filterPlotResult(xStr,yStr,plotResults,userParams)
    plt.savefig(".\\graphs\\shear\\" + str(userParams["strNMCurve"]) + str(userParams["selLists"]) + ".jpg")

def loadNMCurve(loc):
    NMcurve = pd.read_excel(r'.\\NMcurve\\'+loc+'.xlsx', skiprows=1)
    return NMcurve

if __name__ == '__main__':

    userParams = userParams()

    combinedModels = CombinedModels(userParams)
    combinedModels.getCombResults(userParams)

    plotResults = combinedModels.listElementsToPlot()
    plotting("Mres","Fres",plotResults,userParams)
    plotting("Mres","Fx",plotResults,userParams,loadNMCurve(userParams["strNMCurve"]))
    plt.show()

    combinedModels.close()


# class LocModel(Model):

#     self.location
#     self.path

#     self.elements ?????????????????????????????

# class CombinationCase():

#     self.index
#     self.name

#     self.type   # ULSB, ULSC, SLS or SLSQP










# class Plot():

# class NMPlot(Plot):


