from telnetlib import PRAGMA_HEARTBEAT
import numpy
import pandas as pd
from gsapy import GSA
from gsapy.modules import Element
from gsapy.modules import Node
from matplotlib import pyplot as plt
import datetime
from pathlib import Path

def tempParams():
    #For SP temp
    userParams={}
    userParams["Cs"] = ["C09","C10","C11","C12","C13","C14"]
    userParams["loc"] = "SP"
    userParams["modelPrefix"] = " model_03_-"
    userParams["addl_pts"] = 0
    return userParams

class Model():

    kind="GSA"
    version="10.1"

    def __init__(self,path):
        self.path = path
        try:
            self.exists = path.exists()
            self.model = GSA(path, version=self.version)
            print("Model loaded successfully: " + str(self.path))
        except:
            print("Failure to Load model: " + self.path)
        # self.localOrCloud = 
        # print(self.model.get_elements())
        self.elements = [ExtElement(x[1]) for x in self.model.get_elements().items()] # .items converst the dictionary into a list, [1] is to drop the key returned from items()
        self.nodes = [ExtNode(x[1]) for x in self.model.get_nodes().items()]
        # print(self.elements[1])
        self.results = []
        # print(self.elements)
        self.lists = self.model.get_all_saved_lists()

    def setCombinationCases(self,userParams):
        self.resCombinationCases = userParams["Cs"]

    def getSelectedResults(self,userParams):
        for element in self.resElements:
            element.getResults(self,userParams)
            self.results.append(element.results)

    def setResLists(self,strResLists):
        self.resLists = []

        for strResList in strResLists:
            for list in self.lists:
                if strResList == list.name:
                    self.resLists.append(list)
                    break
            print("List is not in model: " + strResList) # NOT WORKING PROPERLY
    
    def setResElements(self,strResLists):
        self.setResLists(strResLists)

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
    # save():

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

    def __init__(self,element):

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

    def getResults(self,model,userParams):
        for combCase in model.resCombinationCases:
            results = model.model.get_1D_elem_resultants(self.index,  # the element number
                                        combCase,  # analysis case or combination number
                                        axis="local",  # output axis - if omitted, it uses the default axis
                                        addl_pts=userParams["addl_pts"])  # additional number of points along the 
                                                                        #element to output forces, if ommited it defaults to 0
            for result in results:
                self.results.append(Result(result,self,combCase))

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

    modelsList=["./models/SP model_03_+Fy_+Fz.gwb",
    "./models/SP model_03_+Fy_-Fz.gwb",
    "./models/SP model_03_-Fy_+Fz.gwb",
    "./models/SP model_03_-Fy_-Fz.gwb",
    "./models/SP model_03_no-wall_+Fy_-Fz.gwb",
    "./models/SP model_03_no-wall_-Fy_-Fz.gwb"]				


    def __init__(self):
        self.models = []
        for modelString in self.modelsList:
            self.models.append(Model(Path(modelString)))

    def getCombResults(self,userParams):
        self.combResults = []
        for model in self.models:
            print("Beginning to extract results from: " + str(model.path))
            model.setCombinationCases(userParams)
            model.setResElements(["piles under pilecap"])
            model.getSelectedResults(userParams)
            self.combResults.extend(model.resElements)

    def listElementsToPlot(self):
        plotResults = {"Fx":[],"Mres":[]}
        for element in self.combResults:
            for result in element.results:
                plotResults["Fx"].append(result.Fx)
                plotResults["Mres"].append(result.Mres)

        return plotResults




    def close(self):
        for model in self.models:
            del model.model

    

    # self.NMplot

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

def plotting(x,y,NMcurve):
    fig, ax = plt.subplots()
    settings(ax)
    plt.scatter(x,y)
    plt.plot(NMcurve["Moment (kNm)"], NMcurve["Fx (kN)"], color="red")
    plt.title("SP_doubleBars" + ", " + str(datetime.datetime.now()))

    # annotateSalientPoints(df, loc)

    # plt.savefig(".\\graphs\\" + loc + ".jpg")
    plt.show()

def loadNMCurve(loc):

    NMcurve = pd.read_excel(r'.\\NMcurve\\'+loc+'.xlsx', skiprows=1)
    return NMcurve


if __name__ == '__main__':

    userParams = tempParams()

    combinedModels = CombinedModels()
    combinedModels.getCombResults(userParams)

    plotResults = combinedModels.listElementsToPlot()
    plotting(plotResults["Mres"],plotResults["Fx"],loadNMCurve("SP_double"))

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


