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
    #For SP temp
    userParams={}
    userParams["Cs"] = [#create_list('C', 18, 23) + create_list('C', 39, 44) + create_list('C', 60, 65) + create_list('C', 81, 86)   #ULS C
    # create_list('C', 65, 88)   #SLS
    # create_list('C', 1, 10) + create_list('C', 20, 27) + create_list('C', 34, 41) + create_list('C', 49, 55)   #SLS
    # create_list('C', 11, 16) + create_list('C', 28, 33) + create_list('C', 42, 47) + create_list('C', 56, 61)   #ULS B
    # create_list('C', 65, 88)   #ULS C
    # create_list('C', 11, 16) + create_list('C', 25, 30) + create_list('C', 39, 44) + create_list('C', 53, 58) + \
    #         create_list('C', 67, 72) + create_list('C', 81, 86) + \
    #         create_list('C', 95, 100) + create_list('C', 109, 114)
    # create_list('C', 1, 92)
            # create_list('C', 12, 17) + create_list('C', 33, 38) + create_list('C', 54, 59) + create_list('C', 75, 80) + \
        # "C09","C10","C11","C12","C13","C14"] # ULS B
        # "C15","C16","C17","C18","C19","C20"] # ULS C
        # "C01","C02","C03","C04","C05","C06"] # SLS
        "C07","C08"] # SLS QP

        # NA
        # create_list('C', 4, 9) + create_list('C', 25, 30) + create_list('C', 46, 51) + create_list('C', 67, 72)   #SLS
        # create_list('C', 12, 17) + create_list('C', 33, 38) + create_list('C', 54, 59) + create_list('C', 75, 80)   #ULS B
        # create_list('C', 18, 23) + create_list('C', 39, 44) + create_list('C', 60, 65) + create_list('C', 81, 86)   #ULS C


        # NP
        # "C9","C10","C26","C27","C40","C41","C54","C55"] # SLSQP
    
    # print(userParams["Cs"])

    # userParams["modelPrefix"] = " model_03_-"
    userParams["addl_pts"] = 0
    # userParams["selLists"] = ["top pile elem under pilecap"] ### Only temporary and set up better
    # userParams["selLists"] = ["top pile elem"] ### Only temporary and set up better
    userParams["selLists"] = ["piles under pilecap_AR"] ### Only temporary and set up better
    userParams["heightFilter"] =  { #None, greater than, less than, between, val_1, val_2, . Only specify val_1 for > or <, specify both for between. None is no filter. Works off midpoint of elements.
    "type":None} 
    # "type":"between","val_1":-3, "val_2": -4} 
    # "type":"less than","val_1":-9.8}   
    # "type":None} 
    # userParams["modelsList"]=[
    #     "./models/NAmodel_06.gwb"
    # ]
    userParams["modelsList"]=[
    "./models/SP model_15_+Fy_+Fz_LB.gwb",
    "./models/SP model_15_+Fy_-Fz_LB.gwb",
    "./models/SP model_15_-Fy_+Fz_LB.gwb",
    "./models/SP model_15_-Fy_-Fz_LB.gwb",
    "./models/SP model_15_+Fy_+Fz_UB.gwb",
    "./models/SP model_15_+Fy_-Fz_UB.gwb",
    "./models/SP model_15_-Fy_+Fz_UB.gwb",
    "./models/SP model_15_-Fy_-Fz_UB.gwb"
    # "./models/SP model_03_no-wall_+Fy_-Fz.gwb",
    # "./models/SP model_03_no-wall_-Fy_-Fz.gwb"
    # "./models/SA model_04.gwb"
    # "./models/NP model_04d_comp-springs_+3m_1.25x.gwb",
    # "./models/NP model_04d_comp-springs-1.25x.gwb", 
    # "./models/NP model_04d_deflection.gwb", 
    # "./models/NP model_04d_translate.gwb", 
    # "./models/NP model_04g 20 v spring.gwb", 
    # "./models/NP model_04h 10 v spring.gwb", 
    # "./models/NP model_04i tuned.gwb", 
    # "./models/NP model_04d.gwb", 
    # "./models/NP model_04d_comp-springs.gwb", 
    # "./models/NP model_04d_comp-springs_+3m.gwb"
    # "./models/NAmodel_06.gwb"
    ]
    # # userParams["modelsList"]=[
    # "./models/SP model_05_+Fy_+Fz.gwb",
    # "./models/SP model_05_+Fy_-Fz.gwb",
    # "./models/SP model_05_-Fy_+Fz.gwb",
    # "./models/SP model_05_-Fy_-Fz.gwb",
    # "./models/SP model_05_no-wall_+Fy_-Fz.gwb",
    # "./models/SP model_05_no-wall_-Fy_-Fz.gwb",
    # "./models/SP model_05a_no-wall_-Fy_-Fz.gwb"
    # ]
    userParams["loc"] = "NP"
    # userParams["strNMCurve"] = r'SP_NR_top_12B40_16_retrospectively'
    userParams["strNMCurve"] = r'SP_AR_top_12(2)B40_16_retrospectively'
    userParams["annotate"] = True # True or False
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
    plt.ylabel(yStr + ' (kN)')
    plt.xlabel(xStr + ' (kNm)')
    ax.set_xlim(left=-500,right=None)
    # plt.xlim(0, t.max()*1.1)
    # plt.ylim(0, network[column_string].max()*1.1)
    plt.grid(which='both')
    plt.title("NM plot")
    ax.tick_params(axis="y", direction="in")
    ax.tick_params(axis="x", direction="in")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    modelsStr = "\n".join([str(x[9:-4]) for x in userParams["modelsList"]])
    ax.text(0.05, 0.95, modelsStr, transform=ax.transAxes, fontsize=6,
        verticalalignment='top', bbox=props)
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
    filter = (((xPercentAlong < 0.01) | (xPercentAlong > 0.97)) | (
        (yPercentAlong < 0.04) | (yPercentAlong > 0.96))) & (y.abs() > 50) #& (x.abs() > 100) 
    plotResults = pd.DataFrame(plotResults)
    toAnnotate = plotResults[filter].copy()
    x = x[filter]
    y = y[filter]
    for x, y, m, C, e in zip(x, y, toAnnotate["modelName"],toAnnotate["combCase"], toAnnotate["elementIndex"]):
        c = C + "," + str(e) + ",", m
        plt.text(x, y, c, fontsize=8)
    toAnnotate.to_csv(r'.\\salient\\salient_'+userParams["loc"]+'_'+xStr+yStr+'_'+ str(userParams["selLists"]) + '.csv')

def plotting(xStr,yStr,plotResults,userParams,NMcurve=False):
    fig, ax = plt.subplots()
    plt.scatter(plotResults[xStr],plotResults[yStr])
    try:
        NMcurve.empty
        plt.plot(NMcurve["Moment (kNm)"], NMcurve["Fx (kN)"], color="red")
        # NMCurve2 = loadNMCurve("SP_double_12")
        # plt.plot(NMCurve2["Moment (kNm)"], NMCurve2["Fx (kN)"], color="green")
    except:
        pass
    settings(ax,xStr,yStr)
    plt.title(str(userParams["strNMCurve"]) + ", " + str(userParams["selLists"]) + "," + str(datetime.datetime.now()))
    # plt.text(0, 1, userParams["heightFilter"].items(), fontsize=12)
    if userParams["annotate"]:
        filterPlotResult(xStr,yStr,plotResults,userParams)
    # plt.savefig(".\\graphs\\shear\\" + str(userParams["strNMCurve"]) + str(userParams["selLists"]) + ".jpg")

def loadNMCurve(loc):
    NMcurve = pd.read_excel(r'.\\NMcurve\\'+loc+'.xlsx', skiprows=1)
    return NMcurve

if __name__ == '__main__':

    userParams = userParams()

    combinedModels = CombinedModels(userParams)
    combinedModels.getCombResults(userParams)
    # plotResults = combinedModels.listElementsToPlot()
    # pprint(vars(combinedModels))
    # plotting("Mres","Fx",plotResults,userParams)
    # plt.show()

    # df = pd.DataFrame({
    #     "element index":[], 
    #     "maxFx":[],"minFx":[],"maxMyy":[],"minMyy":[],
    #     "maxMres":[],"minMres":[],"maxFres":[],"minFres":[]
    #     })

    # for element in combinedModels.combResults:
    #     index_list = df.index[df["element index"]==element.index].tolist()
    #     if not index_list: # if its empty its not there
    #         maxFx = element.results[0].Fx
    #         minFx = element.results[0].Fx
    #         maxMyy = element.results[0].Myy
    #         minMyy = element.results[0].Myy
    #         maxMres = element.results[0].Mres
    #         minMres = element.results[0].Mres
    #         maxFres = element.results[0].Fres
    #         minFres = element.results[0].Fres
    #     else:
    #         maxFx = df.iloc[index_list[0]]["maxFx"]
    #         minFx = df.iloc[index_list[0]]["minFx"]
    #         maxMyy = df.iloc[index_list[0]]["maxMyy"]
    #         minMyy = df.iloc[index_list[0]]["minMyy"]
    #         maxMres = df.iloc[index_list[0]]["maxMres"]
    #         minMres = df.iloc[index_list[0]]["minMres"]
    #         maxFres = df.iloc[index_list[0]]["maxFres"]
    #         minFres = df.iloc[index_list[0]]["minFres"]
    #     for result in element.results:
    #         if result.Fx > maxFx:
    #             maxFx = result.Fx
    #         if result.Fx < minFx:
    #             minFx = result.Fx
    #         if result.Myy > maxMyy:
    #             maxMyy = result.Myy
    #         if result.Myy < minMyy:
    #             minMyy = result.Myy
    #         if result.Mres > maxMres:
    #             maxMres = result.Mres
    #         if result.Mres < minMres:
    #             minMres = result.Mres
    #         if result.Fres > maxFres:
    #             maxFres = result.Fres
    #         if result.Fres < minFres:
    #             minFres = result.Fres

    #     if not index_list:
    #         df = pd.concat([df,pd.DataFrame({
    #             "element index":[element.index], 
    #             "maxFx":[maxFx],"minFx":[minFx],"maxMyy":[maxMyy],"minMyy":[minMyy],
    #             "maxMres":[maxMres],"minMres":[minMres],"maxFres":[maxFres],"minFres":[minFres]
    #             })])
    #         df = df.reset_index(drop=True)
    #     else:
    #         df.at[index_list[0],"maxFx"] = maxFx
    #         df.at[index_list[0],"minFx"] = minFx
    #         df.at[index_list[0],"maxMyy"] = maxMyy
    #         df.at[index_list[0],"minMyy"] = minMyy
    #         df.at[index_list[0],"maxMres"] = maxMres
    #         df.at[index_list[0],"minMres"] = minMres
    #         df.at[index_list[0],"maxFres"] = maxFres
    #         df.at[index_list[0],"minFres"] = minFres

    # print(df)
    # df.to_csv(r'.\\pilecap\\SLSQP_'+userParams["loc"] + '_' + str(userParams["selLists"]) + '.csv')

    #     # print(f"{element.index}: {max(Fx)}")

    plotResults = combinedModels.listElementsToPlot()
    plotResults = pd.DataFrame(plotResults)
    # plotResults.to_csv(Path("results/results_NA_ULSC.csv"),index=False)
    # pprint(plotResults)
    plotting("Mres","Fres",plotResults,userParams)
    # plotting("Mres","Fx",plotResults,userParams,loadNMCurve(userParams["strNMCurve"]))
    plotting("Mres","Fx",plotResults,userParams)
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


