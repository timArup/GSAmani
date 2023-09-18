import streamlit as st

def create_list(prefix, first, last):
    list = []
    for i in range(first, last+1):
        if i < 10:
            list.append(prefix + str(0) + str(i))
        else:
            list.append(prefix + str(i))
    return list

def defaultPlSettings():

    defaultPlSettings = {
        "envelopes" : {
                                "NA_SLSQP"  : ["C10","C11","C31","C32","C52","C53","C73","C74"],
                                "NA_ULSB" : ["C12","C13","C14","C15","C16","C17",
                                            "C33","C34","C35","C36","C37","C38",
                                            "C54","C55","C56","C57","C58","C59",
                                            "C75","C76","C77","C78","C79","C80"],
                                "NA_SLS" : create_list("C", 4, 9) + create_list("C", 25, 30) + create_list("C", 46, 51) + create_list("C", 67, 72),
                                "NA_ULSC" : create_list("C", 18, 23) + create_list("C", 39, 44) + create_list("C", 60, 65) + create_list("C", 81, 86),
                                "SA_ULSB" : ["C11","C12","C13","C14","C15","C16",
                                            "C25","C26","C27","C28","C29","C30",
                                            "C39","C40","C41","C42","C43","C44",
                                            "C53","C54","C55","C56","C57","C58",
                                            "C67","C68","C69","C70","C71","C72",
                                            "C81","C82","C83","C84","C85","C86",
                                            "C95","C96","C97","C98","C99","C100",
                                            "C109","C110","C111","C112","C113","C114"],
                                "SA_SLSQP" : ["C09","C10","C23","C24","C37","C38",
                                            "C51","C52","C65","C66","C79","C80",
                                            "C93","C94","C107","C108"],
                                # "NA_ULSC" : create_list("C", 18, 23) + create_list("C", 39, 44) + create_list("C", 60, 65) + create_list("C", 81, 86),
                                "SA_SLS" : create_list("C", 3, 8) + create_list("C", 17, 22) + create_list("C", 31, 36) + create_list("C", 45, 50) + create_list("C", 59, 64) + create_list("C", 73, 78) + create_list("C", 87, 92) + create_list("C", 101, 106),
                                "SA_ULSC" : create_list("C", 118, 165),
                                "NP_ULSB" : create_list("C",11,16) + create_list("C",28,33) + create_list("C",42,47) + create_list("C",56,61),
                                "NP_SLS" : create_list("C",3,8) + create_list("C",20,25) + create_list("C",34,39) + create_list("C",48,53),
                                "NP_SLSQP" : ["C09","C10","C26","C27","C40","C41","C54","C55"],
                                "NP_ULSC" : create_list("C",65,70) + create_list("C",71,76) + create_list("C",77,82) + create_list("C",83,88),
                                "SP_ULSB" : ["C09","C10","C11","C12","C13","C14"],
                                "SP_SLSQP" : ["C07","C08"],
                                "SP_SLS" : ["C01","C02","C03","C04","C05","C06"],
                                "SP_ULSC" : ["C15","C16","C17","C18","C19","C20"],
        },
    }
    return defaultPlSettings