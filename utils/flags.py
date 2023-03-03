import streamlit as st

class Flags():
    def __init__(self):
        self.extracted = False
        self.plotted = False
        self.runExtraction = False
        self.dataBelow = False

    def setExtracted(self,state):
        if state not in [True,False]:
            raise Exception("extracted can only be true or false")
        self.extracted = state
    
    def setPlotted(self,state):
        if state not in [True,False]:
            raise Exception("plotted can only be true or false")
        self.plotted = state
    