from matplotlib import pyplot as plt
import pandas as pd
import datetime
import streamlit as st
import mpld3
import streamlit.components.v1 as components


def settings(ax,xStr,yStr,userParams):
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

def plot(xStr,yStr,plotResults,userParams,NMcurve=False):
    fig, ax = plt.subplots()
    plt.scatter(plotResults[xStr],plotResults[yStr])
    try:
        NMcurve.empty
        plt.plot(NMcurve["Moment (kNm)"], NMcurve["Fx (kN)"], color="red")
        # NMCurve2 = loadNMCurve("SP_double_12")
        # plt.plot(NMCurve2["Moment (kNm)"], NMCurve2["Fx (kN)"], color="green")
    except:
        pass
    settings(ax,xStr,yStr,userParams)
    plt.title(str(userParams["strNMCurve"]) + ", " + str(userParams["selLists"]) + "," + str(datetime.datetime.now()))
    # plt.text(0, 1, userParams["heightFilter"].items(), fontsize=12)
    if userParams["annotate"]:
        filterPlotResult(xStr,yStr,plotResults,userParams)
    # plt.savefig(".\\graphs\\shear\\" + str(userParams["strNMCurve"]) + str(userParams["selLists"]) + ".jpg")
    st.pyplot(fig)
    # components.html(fig_html, height=1200)
    # st.pyplot(fig)

def loadNMCurve(loc):
    NMcurve = pd.read_excel(r'.\\NMcurve\\'+loc+'.xlsx', skiprows=1)
    return NMcurve