import streamlit as st

def defaultPlSettings():

    defaultPlSettings = {
        "envelopes" : {
                                "NA_SLSQP"  : ["C10","C11","C31","C32","C52","C53","C73","C74"],
                                "NA_ULSB" : ["C12","C13","C14","C15","C16","C17",
                                            "C33","C34","C35","C36","C37","C38",
                                            "C54","C55","C56","C57","C58","C59",
                                            "C75","C76","C77","C78","C79","C80"],
                                "NA_SLS" : ["C18","C19","C20","C21","C22","C23",
                                            "C39","C40","C41","C42","C43","C44",
                                            "C60","C61","C62","C62","C64","C65",
                                            "C81","C82","C83","C84","C85","C86"]
        },

        

    }

    return defaultPlSettings