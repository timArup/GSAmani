{
    "writtenBy": {
        "ProgramName": "AdSec",
        "Company": "Oasys Ltd.",
        "Copyright": "Copyright © Oasys 1985-2022",
        "Description": "AdSec 10",
        "ProgramVersion": "10.0 build 7",
        "FullVersion": "10.0.7.15"
    },
    "titles": {
        "jobNumber": " "
    },
    "units": {
        "force": "kN",
        "length": "m",
        "sectionDims": "mm",
        "stress": "kPa",
        "mass": "t",
        "strain": "ε",
        "temperature": "°C"
    },
    "codes": {
        "concrete": "EC2_GB_04"
    },
    "materials": {
        "concrete": [
            {
                "name": "C40/50",
                "strength": 40000000.0,
                "elasticModulus": 35220462288.93441,
                "density": 2400.0,
                "coefficientOfThermalExpansion": 0.00001,
                "poissonsRatio": 0.2,
                "ULS": {
                    "gammaF": 1.65,
                    "gammaE": 1.0,
                    "tension": {
                        "model": "NO_TENSION",
                        "failureStrain": 1.0
                    },
                    "compression": {
                        "model": "RECT_PARABOLA",
                        "plasticStrainLimit": 0.002,
                        "failureStrain": 0.0035
                    }
                },
                "SLS": {
                    "gammaF": 1.1,
                    "gammaE": 1.0,
                    "tension": {
                        "model": "INTERPOLATED",
                        "yieldStrain": 0.0,
                        "plasticStrainLimit": 0.0,
                        "failureStrain": 0.0000996245096691375
                    },
                    "compression": {
                        "model": "FIB_SCHEMATIC",
                        "plasticStrainLimit": 0.002324249914209339,
                        "failureStrain": 0.0035
                    }
                },
                "type": "Normal weight concrete",
                "confinedStrength": 0.0,
                "materialType": "Concrete"
            }
        ],
        "reinforcement": [
            {
                "name": "500B",
                "strength": 500000000.0,
                "elasticModulus": 200000000000.0,
                "density": 7850.0,
                "coefficientOfThermalExpansion": 0.000012,
                "poissonsRatio": 0.3,
                "ULS": {
                    "gammaF": 1.15,
                    "gammaE": 1.0,
                    "tension": {
                        "model": "ELAS_HARD",
                        "yieldStrain": 0.002173913043478261,
                        "failureStrain": 0.045000000000000008
                    },
                    "compression": {
                        "model": "ELAS_HARD",
                        "yieldStrain": 0.002173913043478261,
                        "failureStrain": 0.045000000000000008
                    }
                },
                "SLS": {
                    "gammaF": 1.0,
                    "gammaE": 1.0,
                    "tension": {
                        "model": "ELAS_HARD",
                        "yieldStrain": 0.0025,
                        "failureStrain": 0.045000000000000008
                    },
                    "compression": {
                        "model": "ELAS_HARD",
                        "yieldStrain": 0.0025,
                        "failureStrain": 0.045000000000000008
                    }
                },
                "type": "Steel rebar",
                "label": "B",
                "ultimateStrain": 0.05,
                "hardeningModulus": 727272727.272728,
                "hardeningParameter": 1.08,
                "ductility": "NORMAL"
            }
        ]
    },
    "sections": [
        {
            "name": "South Pier Pile",
            "components": [
                {
                    "material": "concrete",
                    "grade": "C40/50",
                    "profile": "STD C(mm) 1130",
                    "reinforcement": {
                        "cover": 0.115,
                        "positionsRelativeTo": "ORIGIN",
                        "groups": [
                            {
                                "type": "LINK",
                                "position": "",
                                "description": "B16",
                                "preload": {
                                    "preloadType": "NONE",
                                    "value": 0.0,
                                    "exclude": true
                                }
                            },
                            {
                                "type": "PERIMETER",
                                "position": "",
                                "description": "16B40",
                                "preload": {
                                    "preloadType": "NONE",
                                    "value": 0.0,
                                    "exclude": true
                                }
                            }
                        ]
                    }
                }
            ],
            "tasks": [
                {
                    "action": "LOAD",
                    "state": "ULS",
                    "preloadInclCurv": false,
                    "outputOptions": {
                        "uls": {
                            "status": true,
                            "utilisation": true,
                            "momentRatio": true,
                            "response": false
                        },
                        "sls": {
                            "cracked": false,
                            "crackWidth": false,
                            "stiffness": false
                        }
                    },
                    "codeOptions": {
                        "crackCalc": "LOCAL",
                        "Cnom": 0.0,
                        "userDefinedPhiLower": 0.0,
                        "userDefinedPhiHigher": 0.0,
                        "userDefinedStrainLower": 0.0,
                        "userDefinedStrainHigher": 0.0
                    },
                    "loadTerm": "SHORT",
                    "creepCoefficients": [
                        {
                            "componentID": 1,
                            "creepCoefficient": 0.0
                        }
                    ],
                    "componentActiveStates": [
                        {
                            "componentID": 1,
                            "activeState": true
                        }
                    ],
                    "cases": [
                        {
                            "load": {
                                "fx": 3141000.0,
                                "myy": 2900000.0,
                                "mzz": 1312000.0
                            }
                        },
                        {
                            "load": {
                                "fx": -11480000.0,
                                "myy": 3106000.0,
                                "mzz": 920000.0
                            }
                        },
                        {
                            "load": {
                                "fx": 1742000.0,
                                "myy": 3481000.0,
                                "mzz": 925000.0
                            }
                        },
                        {
                            "load": {
                                "fx": -7796000.0,
                                "myy": 2878000.0,
                                "mzz": 1767000.0
                            }
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {
                                "fx": 2824000.0,
                                "myy": 2681000.0,
                                "mzz": 1398000.0
                            }
                        },
                        {
                            "load": {
                                "fx": -11110000.0,
                                "myy": 2116000.0,
                                "mzz": 680000.0
                            }
                        },
                        {
                            "load": {
                                "fx": 1467000.0,
                                "myy": 3310000.0,
                                "mzz": 1064000.0
                            }
                        },
                        {
                            "load": {
                                "fx": 2400000.0,
                                "myy": 3226000.0,
                                "mzz": 1606000.0
                            }
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {
                                "fx": 2003000.0,
                                "myy": 2499000.0,
                                "mzz": 988000.0
                            }
                        },
                        {
                            "load": {
                                "fx": -8526000.0,
                                "myy": 2249000.0,
                                "mzz": 635000.0
                            }
                        },
                        {
                            "load": {
                                "fx": 1149000.0,
                                "myy": 2534000.0,
                                "mzz": 652000.0
                            }
                        },
                        {
                            "load": {
                                "fx": -5612000.0,
                                "myy": 2195000.0,
                                "mzz": 1209000.0
                            }
                        }
                    ]
                },
                {
                    "action": "LOAD",
                    "state": "ULS",
                    "preloadInclCurv": false,
                    "outputOptions": {
                        "uls": {
                            "status": false,
                            "utilisation": false,
                            "momentRatio": false,
                            "response": false
                        },
                        "sls": {
                            "cracked": true,
                            "crackWidth": true,
                            "stiffness": false
                        }
                    },
                    "codeOptions": {
                        "crackCalc": "LOCAL",
                        "Cnom": 0.075,
                        "userDefinedPhiLower": 0.0,
                        "userDefinedPhiHigher": 0.0,
                        "userDefinedStrainLower": 0.0,
                        "userDefinedStrainHigher": 0.0
                    },
                    "loadTerm": "SHORT",
                    "creepCoefficients": [
                        {
                            "componentID": 1,
                            "creepCoefficient": 0.0
                        }
                    ],
                    "componentActiveStates": [
                        {
                            "componentID": 1,
                            "activeState": true
                        }
                    ],
                    "cases": [
                        {
                            "load": {
                                "fx": -7690000.0,
                                "myy": 165000.0
                            }
                        },
                        {
                            "load": {
                                "myy": 165000.0
                            }
                        },
                        {
                            "load": {
                                "fx": -3765000.0,
                                "myy": 165000.0
                            }
                        }
                    ]
                }
            ],
            "extents": {
                "yMin": -0.5668204754816033,
                "yMax": 0.5668204754816033,
                "zMin": 0.5668204754816033,
                "zMax": -0.5668204754816033
            },
            "properties": [
                {
                    "analysis": {
                        "area": 1.0028749148422019,
                        "localAxis": {
                            "iyy": 0.08003635011057842,
                            "izz": 0.08003635011057842,
                            "iyz": -0.0
                        },
                        "principalAxis": {
                            "iuu": 0.08003635011057842,
                            "ivv": 0.08003635011057842,
                            "angle": 0.0
                        },
                        "shear": {
                            "ky": 0.8571429,
                            "kz": 0.8571429
                        },
                        "torsion": {
                            "j": 0.160071372345251
                        },
                        "elastic": {
                            "zy": 0.1412022916825207,
                            "zz": 0.1412022916825207
                        },
                        "plastic": {
                            "zpy": 0.24048208638153535,
                            "zpz": 0.24048208638153535
                        },
                        "centroid": {
                            "cy": -3.3730136511461449e-17,
                            "cz": 1.0378503541988137e-17
                        },
                        "radiusOfGyration": {
                            "ry": 0.28250117174033048,
                            "rz": 0.28250117174033048
                        },
                        "physical": {
                            "surfaceArea": 3.5557198135647085
                        }
                    },
                    "paths": [
                        {
                            "isVoid": false,
                            "points": [
                                {
                                    "y": -0.11058118908704118,
                                    "z": 0.5559291789835167
                                },
                                {
                                    "y": -0.21691280509211253,
                                    "z": 0.5236738359057688
                                },
                                {
                                    "y": -0.31490858364359605,
                                    "z": 0.47129400099383308
                                },
                                {
                                    "y": -0.400802601928425,
                                    "z": 0.4008026019284248
                                },
                                {
                                    "y": -0.4712940009938332,
                                    "z": 0.31490858364359589
                                },
                                {
                                    "y": -0.5236738359057689,
                                    "z": 0.2169128050921123
                                },
                                {
                                    "y": -0.5559291789835167,
                                    "z": 0.11058118908704094
                                },
                                {
                                    "y": -0.5668204754816033,
                                    "z": -1.0412323214845893e-16
                                },
                                {
                                    "y": -0.5559291789835167,
                                    "z": -0.11058118908704115
                                },
                                {
                                    "y": -0.5236738359057688,
                                    "z": -0.21691280509211248
                                },
                                {
                                    "y": -0.47129400099383308,
                                    "z": -0.31490858364359605
                                },
                                {
                                    "y": -0.4008026019284249,
                                    "z": -0.400802601928425
                                },
                                {
                                    "y": -0.3149085836435959,
                                    "z": -0.4712940009938332
                                },
                                {
                                    "y": -0.2169128050921121,
                                    "z": -0.523673835905769
                                },
                                {
                                    "y": -0.11058118908704098,
                                    "z": -0.5559291789835167
                                },
                                {
                                    "y": 6.941548809897263e-17,
                                    "z": -0.5668204754816033
                                },
                                {
                                    "y": 0.11058118908704112,
                                    "z": -0.5559291789835167
                                },
                                {
                                    "y": 0.21691280509211223,
                                    "z": -0.5236738359057689
                                },
                                {
                                    "y": 0.31490858364359605,
                                    "z": -0.4712940009938331
                                },
                                {
                                    "y": 0.40080260192842495,
                                    "z": -0.4008026019284249
                                },
                                {
                                    "y": 0.4712940009938331,
                                    "z": -0.3149085836435959
                                },
                                {
                                    "y": 0.5236738359057689,
                                    "z": -0.21691280509211215
                                },
                                {
                                    "y": 0.5559291789835167,
                                    "z": -0.11058118908704089
                                },
                                {
                                    "y": 0.5668204754816033,
                                    "z": 3.4707744049486319e-17
                                },
                                {
                                    "y": 0.5559291789835167,
                                    "z": 0.11058118908704097
                                },
                                {
                                    "y": 0.5236738359057689,
                                    "z": 0.2169128050921122
                                },
                                {
                                    "y": 0.47129400099383308,
                                    "z": 0.31490858364359616
                                },
                                {
                                    "y": 0.40080260192842495,
                                    "z": 0.40080260192842495
                                },
                                {
                                    "y": 0.31490858364359605,
                                    "z": 0.47129400099383308
                                },
                                {
                                    "y": 0.21691280509211217,
                                    "z": 0.5236738359057689
                                },
                                {
                                    "y": 0.11058118908704091,
                                    "z": 0.5559291789835167
                                },
                                {
                                    "y": 0.0,
                                    "z": 0.5668204754816033
                                }
                            ]
                        }
                    ],
                    "links": [
                        {
                            "grade": 1,
                            "diameter": 0.016,
                            "path": "M -0.082548 0.435095 A 0.040000 0.040000 0 0 1 -0.090239 0.433565 L -0.165845 0.410630 L -0.165845 0.410630 A 0.040000 0.040000 0 0 1 -0.173089 0.407630 L -0.242768 0.370386 L -0.242768 0.370386 A 0.040000 0.040000 0 0 1 -0.249288 0.366029 L -0.310362 0.315907 L -0.310362 0.315907 A 0.040000 0.040000 0 0 1 -0.315907 0.310362 L -0.366029 0.249288 L -0.366029 0.249288 A 0.040000 0.040000 0 0 1 -0.370386 0.242768 L -0.407630 0.173089 L -0.407630 0.173089 A 0.040000 0.040000 0 0 1 -0.410630 0.165845 L -0.433565 0.090239 L -0.433565 0.090239 A 0.040000 0.040000 0 0 1 -0.435095 0.082548 L -0.442839 0.003921 L -0.442839 0.003921 A 0.040000 0.040000 0 0 1 -0.442839 -0.003921 L -0.435095 -0.082548 L -0.435095 -0.082548 A 0.040000 0.040000 0 0 1 -0.433565 -0.090239 L -0.410630 -0.165845 L -0.410630 -0.165845 A 0.040000 0.040000 0 0 1 -0.407630 -0.173089 L -0.370386 -0.242768 L -0.370386 -0.242768 A 0.040000 0.040000 0 0 1 -0.366029 -0.249288 L -0.315907 -0.310362 L -0.315907 -0.310362 A 0.040000 0.040000 0 0 1 -0.310362 -0.315907 L -0.249288 -0.366029 L -0.249288 -0.366029 A 0.040000 0.040000 0 0 1 -0.242768 -0.370386 L -0.173089 -0.407630 L -0.173089 -0.407630 A 0.040000 0.040000 0 0 1 -0.165845 -0.410630 L -0.090239 -0.433565 L -0.090239 -0.433565 A 0.040000 0.040000 0 0 1 -0.082548 -0.435095 L -0.003921 -0.442839 L -0.003921 -0.442839 A 0.040000 0.040000 0 0 1 0.003921 -0.442839 L 0.082548 -0.435095 L 0.082548 -0.435095 A 0.040000 0.040000 0 0 1 0.090239 -0.433565 L 0.165845 -0.410630 L 0.165845 -0.410630 A 0.040000 0.040000 0 0 1 0.173089 -0.407630 L 0.242768 -0.370386 L 0.242768 -0.370386 A 0.040000 0.040000 0 0 1 0.249288 -0.366029 L 0.310362 -0.315907 L 0.310362 -0.315907 A 0.040000 0.040000 0 0 1 0.315907 -0.310362 L 0.366029 -0.249288 L 0.366029 -0.249288 A 0.040000 0.040000 0 0 1 0.370386 -0.242768 L 0.407630 -0.173089 L 0.407630 -0.173089 A 0.040000 0.040000 0 0 1 0.410630 -0.165845 L 0.433565 -0.090239 L 0.433565 -0.090239 A 0.040000 0.040000 0 0 1 0.435095 -0.082548 L 0.442839 -0.003921 L 0.442839 -0.003921 A 0.040000 0.040000 0 0 1 0.442839 0.003921 L 0.435095 0.082548 L 0.435095 0.082548 A 0.040000 0.040000 0 0 1 0.433565 0.090239 L 0.410630 0.165845 L 0.410630 0.165845 A 0.040000 0.040000 0 0 1 0.407630 0.173089 L 0.370386 0.242768 L 0.370386 0.242768 A 0.040000 0.040000 0 0 1 0.366029 0.249288 L 0.315907 0.310362 L 0.315907 0.310362 A 0.040000 0.040000 0 0 1 0.310362 0.315907 L 0.249288 0.366029 L 0.249288 0.366029 A 0.040000 0.040000 0 0 1 0.242768 0.370386 L 0.173089 0.407630 L 0.173089 0.407630 A 0.040000 0.040000 0 0 1 0.165845 0.410630 L 0.090239 0.433565 L 0.090239 0.433565 A 0.040000 0.040000 0 0 1 0.082548 0.435095 L 0.003921 0.442839 L 0.003921 0.442839 A 0.040000 0.040000 0 0 1 -0.003921 0.442839 L -0.082548 0.435095"
                        }
                    ],
                    "bars": [
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 5.908032525381166e-17,
                            "z": 0.41400000000000006
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.15843094099914713,
                            "z": 0.3824861264596727
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.29274220741123066,
                            "z": 0.2927422074112307
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.38248612645967269,
                            "z": 0.15843094099914724
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.414,
                            "z": 4.032187394271229e-17
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.3824861264596727,
                            "z": -0.15843094099914716
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.2927422074112307,
                            "z": -0.2927422074112307
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.1584309409991474,
                            "z": -0.38248612645967269
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -4.232042971558919e-17,
                            "z": -0.41400000000000006
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.1584309409991473,
                            "z": -0.38248612645967269
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.2927422074112307,
                            "z": -0.29274220741123077
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.3824861264596727,
                            "z": -0.15843094099914743
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.4140000000000001,
                            "z": -1.11779258511389e-16
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.3824861264596728,
                            "z": 0.15843094099914727
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.2927422074112308,
                            "z": 0.29274220741123066
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.15843094099914749,
                            "z": 0.38248612645967269
                        }
                    ]
                }
            ]
        },
        {
            "name": "South Pier Pile (no wall)",
            "components": [
                {
                    "material": "concrete",
                    "grade": "C40/50",
                    "profile": "STD C(mm) 1130",
                    "reinforcement": {
                        "cover": 0.115,
                        "positionsRelativeTo": "ORIGIN",
                        "groups": [
                            {
                                "type": "LINK",
                                "position": "",
                                "description": "B16",
                                "preload": {
                                    "preloadType": "NONE",
                                    "value": 0.0,
                                    "exclude": true
                                }
                            },
                            {
                                "type": "PERIMETER",
                                "position": "",
                                "description": "12(2)B40",
                                "preload": {
                                    "preloadType": "NONE",
                                    "value": 0.0,
                                    "exclude": true
                                }
                            }
                        ]
                    }
                }
            ],
            "tasks": [
                {
                    "action": "LOAD",
                    "state": "ULS",
                    "preloadInclCurv": false,
                    "outputOptions": {
                        "uls": {
                            "status": true,
                            "utilisation": true,
                            "momentRatio": true,
                            "response": false
                        },
                        "sls": {
                            "cracked": false,
                            "crackWidth": false,
                            "stiffness": false
                        }
                    },
                    "codeOptions": {
                        "crackCalc": "LOCAL",
                        "Cnom": 0.0,
                        "userDefinedPhiLower": 0.0,
                        "userDefinedPhiHigher": 0.0,
                        "userDefinedStrainLower": 0.0,
                        "userDefinedStrainHigher": 0.0
                    },
                    "loadTerm": "SHORT",
                    "creepCoefficients": [
                        {
                            "componentID": 1,
                            "creepCoefficient": 0.0
                        }
                    ],
                    "componentActiveStates": [
                        {
                            "componentID": 1,
                            "activeState": true
                        }
                    ],
                    "cases": [
                        {
                            "load": {
                                "fx": 3141000.0,
                                "myy": 2900000.0,
                                "mzz": 1312000.0
                            }
                        },
                        {
                            "load": {
                                "fx": -11480000.0,
                                "myy": 3106000.0,
                                "mzz": 920000.0
                            }
                        },
                        {
                            "load": {
                                "fx": 1742000.0,
                                "myy": 3481000.0,
                                "mzz": 925000.0
                            }
                        },
                        {
                            "load": {
                                "fx": -7796000.0,
                                "myy": 2878000.0,
                                "mzz": 1767000.0
                            }
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {}
                        },
                        {
                            "load": {}
                        }
                    ]
                },
                {
                    "action": "LOAD",
                    "state": "ULS",
                    "preloadInclCurv": false,
                    "outputOptions": {
                        "uls": {
                            "status": false,
                            "utilisation": false,
                            "momentRatio": false,
                            "response": false
                        },
                        "sls": {
                            "cracked": true,
                            "crackWidth": true,
                            "stiffness": false
                        }
                    },
                    "codeOptions": {
                        "crackCalc": "LOCAL",
                        "Cnom": 0.075,
                        "userDefinedPhiLower": 0.0,
                        "userDefinedPhiHigher": 0.0,
                        "userDefinedStrainLower": 0.0,
                        "userDefinedStrainHigher": 0.0
                    },
                    "loadTerm": "SHORT",
                    "creepCoefficients": [
                        {
                            "componentID": 1,
                            "creepCoefficient": 0.0
                        }
                    ],
                    "componentActiveStates": [
                        {
                            "componentID": 1,
                            "activeState": true
                        }
                    ],
                    "cases": [
                        {
                            "load": {
                                "fx": -7690000.0,
                                "myy": 165000.0
                            }
                        },
                        {
                            "load": {
                                "myy": 165000.0
                            }
                        },
                        {
                            "load": {
                                "fx": -3765000.0,
                                "myy": 165000.0
                            }
                        }
                    ]
                }
            ],
            "extents": {
                "yMin": -0.5668204754816033,
                "yMax": 0.5668204754816033,
                "zMin": 0.5668204754816033,
                "zMax": -0.5668204754816033
            },
            "properties": [
                {
                    "analysis": {
                        "area": 1.0028749148422019,
                        "localAxis": {
                            "iyy": 0.08003635011057842,
                            "izz": 0.08003635011057842,
                            "iyz": -0.0
                        },
                        "principalAxis": {
                            "iuu": 0.08003635011057842,
                            "ivv": 0.08003635011057842,
                            "angle": 0.0
                        },
                        "shear": {
                            "ky": 0.8571429,
                            "kz": 0.8571429
                        },
                        "torsion": {
                            "j": 0.160071372345251
                        },
                        "elastic": {
                            "zy": 0.1412022916825207,
                            "zz": 0.1412022916825207
                        },
                        "plastic": {
                            "zpy": 0.24048208638153535,
                            "zpz": 0.24048208638153535
                        },
                        "centroid": {
                            "cy": -3.3730136511461449e-17,
                            "cz": 1.0378503541988137e-17
                        },
                        "radiusOfGyration": {
                            "ry": 0.28250117174033048,
                            "rz": 0.28250117174033048
                        },
                        "physical": {
                            "surfaceArea": 3.5557198135647085
                        }
                    },
                    "paths": [
                        {
                            "isVoid": false,
                            "points": [
                                {
                                    "y": -0.11058118908704118,
                                    "z": 0.5559291789835167
                                },
                                {
                                    "y": -0.21691280509211253,
                                    "z": 0.5236738359057688
                                },
                                {
                                    "y": -0.31490858364359605,
                                    "z": 0.47129400099383308
                                },
                                {
                                    "y": -0.400802601928425,
                                    "z": 0.4008026019284248
                                },
                                {
                                    "y": -0.4712940009938332,
                                    "z": 0.31490858364359589
                                },
                                {
                                    "y": -0.5236738359057689,
                                    "z": 0.2169128050921123
                                },
                                {
                                    "y": -0.5559291789835167,
                                    "z": 0.11058118908704094
                                },
                                {
                                    "y": -0.5668204754816033,
                                    "z": -1.0412323214845893e-16
                                },
                                {
                                    "y": -0.5559291789835167,
                                    "z": -0.11058118908704115
                                },
                                {
                                    "y": -0.5236738359057688,
                                    "z": -0.21691280509211248
                                },
                                {
                                    "y": -0.47129400099383308,
                                    "z": -0.31490858364359605
                                },
                                {
                                    "y": -0.4008026019284249,
                                    "z": -0.400802601928425
                                },
                                {
                                    "y": -0.3149085836435959,
                                    "z": -0.4712940009938332
                                },
                                {
                                    "y": -0.2169128050921121,
                                    "z": -0.523673835905769
                                },
                                {
                                    "y": -0.11058118908704098,
                                    "z": -0.5559291789835167
                                },
                                {
                                    "y": 6.941548809897263e-17,
                                    "z": -0.5668204754816033
                                },
                                {
                                    "y": 0.11058118908704112,
                                    "z": -0.5559291789835167
                                },
                                {
                                    "y": 0.21691280509211223,
                                    "z": -0.5236738359057689
                                },
                                {
                                    "y": 0.31490858364359605,
                                    "z": -0.4712940009938331
                                },
                                {
                                    "y": 0.40080260192842495,
                                    "z": -0.4008026019284249
                                },
                                {
                                    "y": 0.4712940009938331,
                                    "z": -0.3149085836435959
                                },
                                {
                                    "y": 0.5236738359057689,
                                    "z": -0.21691280509211215
                                },
                                {
                                    "y": 0.5559291789835167,
                                    "z": -0.11058118908704089
                                },
                                {
                                    "y": 0.5668204754816033,
                                    "z": 3.4707744049486319e-17
                                },
                                {
                                    "y": 0.5559291789835167,
                                    "z": 0.11058118908704097
                                },
                                {
                                    "y": 0.5236738359057689,
                                    "z": 0.2169128050921122
                                },
                                {
                                    "y": 0.47129400099383308,
                                    "z": 0.31490858364359616
                                },
                                {
                                    "y": 0.40080260192842495,
                                    "z": 0.40080260192842495
                                },
                                {
                                    "y": 0.31490858364359605,
                                    "z": 0.47129400099383308
                                },
                                {
                                    "y": 0.21691280509211217,
                                    "z": 0.5236738359057689
                                },
                                {
                                    "y": 0.11058118908704091,
                                    "z": 0.5559291789835167
                                },
                                {
                                    "y": 0.0,
                                    "z": 0.5668204754816033
                                }
                            ]
                        }
                    ],
                    "links": [
                        {
                            "grade": 1,
                            "diameter": 0.016,
                            "path": "M -0.082548 0.435095 A 0.040000 0.040000 0 0 1 -0.090239 0.433565 L -0.165845 0.410630 L -0.165845 0.410630 A 0.040000 0.040000 0 0 1 -0.173089 0.407630 L -0.242768 0.370386 L -0.242768 0.370386 A 0.040000 0.040000 0 0 1 -0.249288 0.366029 L -0.310362 0.315907 L -0.310362 0.315907 A 0.040000 0.040000 0 0 1 -0.315907 0.310362 L -0.366029 0.249288 L -0.366029 0.249288 A 0.040000 0.040000 0 0 1 -0.370386 0.242768 L -0.407630 0.173089 L -0.407630 0.173089 A 0.040000 0.040000 0 0 1 -0.410630 0.165845 L -0.433565 0.090239 L -0.433565 0.090239 A 0.040000 0.040000 0 0 1 -0.435095 0.082548 L -0.442839 0.003921 L -0.442839 0.003921 A 0.040000 0.040000 0 0 1 -0.442839 -0.003921 L -0.435095 -0.082548 L -0.435095 -0.082548 A 0.040000 0.040000 0 0 1 -0.433565 -0.090239 L -0.410630 -0.165845 L -0.410630 -0.165845 A 0.040000 0.040000 0 0 1 -0.407630 -0.173089 L -0.370386 -0.242768 L -0.370386 -0.242768 A 0.040000 0.040000 0 0 1 -0.366029 -0.249288 L -0.315907 -0.310362 L -0.315907 -0.310362 A 0.040000 0.040000 0 0 1 -0.310362 -0.315907 L -0.249288 -0.366029 L -0.249288 -0.366029 A 0.040000 0.040000 0 0 1 -0.242768 -0.370386 L -0.173089 -0.407630 L -0.173089 -0.407630 A 0.040000 0.040000 0 0 1 -0.165845 -0.410630 L -0.090239 -0.433565 L -0.090239 -0.433565 A 0.040000 0.040000 0 0 1 -0.082548 -0.435095 L -0.003921 -0.442839 L -0.003921 -0.442839 A 0.040000 0.040000 0 0 1 0.003921 -0.442839 L 0.082548 -0.435095 L 0.082548 -0.435095 A 0.040000 0.040000 0 0 1 0.090239 -0.433565 L 0.165845 -0.410630 L 0.165845 -0.410630 A 0.040000 0.040000 0 0 1 0.173089 -0.407630 L 0.242768 -0.370386 L 0.242768 -0.370386 A 0.040000 0.040000 0 0 1 0.249288 -0.366029 L 0.310362 -0.315907 L 0.310362 -0.315907 A 0.040000 0.040000 0 0 1 0.315907 -0.310362 L 0.366029 -0.249288 L 0.366029 -0.249288 A 0.040000 0.040000 0 0 1 0.370386 -0.242768 L 0.407630 -0.173089 L 0.407630 -0.173089 A 0.040000 0.040000 0 0 1 0.410630 -0.165845 L 0.433565 -0.090239 L 0.433565 -0.090239 A 0.040000 0.040000 0 0 1 0.435095 -0.082548 L 0.442839 -0.003921 L 0.442839 -0.003921 A 0.040000 0.040000 0 0 1 0.442839 0.003921 L 0.435095 0.082548 L 0.435095 0.082548 A 0.040000 0.040000 0 0 1 0.433565 0.090239 L 0.410630 0.165845 L 0.410630 0.165845 A 0.040000 0.040000 0 0 1 0.407630 0.173089 L 0.370386 0.242768 L 0.370386 0.242768 A 0.040000 0.040000 0 0 1 0.366029 0.249288 L 0.315907 0.310362 L 0.315907 0.310362 A 0.040000 0.040000 0 0 1 0.310362 0.315907 L 0.249288 0.366029 L 0.249288 0.366029 A 0.040000 0.040000 0 0 1 0.242768 0.370386 L 0.173089 0.407630 L 0.173089 0.407630 A 0.040000 0.040000 0 0 1 0.165845 0.410630 L 0.090239 0.433565 L 0.090239 0.433565 A 0.040000 0.040000 0 0 1 0.082548 0.435095 L 0.003921 0.442839 L 0.003921 0.442839 A 0.040000 0.040000 0 0 1 -0.003921 0.442839 L -0.082548 0.435095"
                        }
                    ],
                    "bars": [
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.02000000000000006,
                            "z": 0.41400000000000006
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.01999999999999994,
                            "z": 0.41400000000000006
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.18967949192431114,
                            "z": 0.36853451716675769
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.22432050807568869,
                            "z": 0.34853451716675767
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.3485345171667575,
                            "z": 0.22432050807568894
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.3685345171667575,
                            "z": 0.18967949192431139
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.414,
                            "z": 0.020000000000000043
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.414,
                            "z": -0.01999999999999996
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.36853451716675769,
                            "z": -0.18967949192431114
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.34853451716675767,
                            "z": -0.22432050807568869
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.22432050807568897,
                            "z": -0.34853451716675756
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.1896794919243114,
                            "z": -0.36853451716675758
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.020000000000000043,
                            "z": -0.41400000000000006
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.01999999999999996,
                            "z": -0.41400000000000006
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.189679491924311,
                            "z": -0.3685345171667578
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.22432050807568855,
                            "z": -0.34853451716675779
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.34853451716675756,
                            "z": -0.22432050807568899
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.36853451716675758,
                            "z": -0.18967949192431145
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.4140000000000001,
                            "z": -0.02000000000000011
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.4140000000000001,
                            "z": 0.01999999999999989
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.36853451716675786,
                            "z": 0.18967949192431095
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.3485345171667578,
                            "z": 0.22432050807568849
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.224320508075689,
                            "z": 0.3485345171667575
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.18967949192431148,
                            "z": 0.3685345171667575
                        }
                    ]
                }
            ]
        }
    ]
}