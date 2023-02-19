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
            "name": "FAIL - all springs - North Abutment Pile 508/450 - trial top 4B40",
            "components": [
                {
                    "material": "concrete",
                    "grade": "C40/50",
                    "profile": "STD C(mm) 482.6",
                    "reinforcement": {
                        "cover": 0.091,
                        "positionsRelativeTo": "ORIGIN",
                        "groups": [
                            {
                                "type": "LINK",
                                "position": "",
                                "description": "B10",
                                "preload": {
                                    "preloadType": "NONE",
                                    "value": 0.0,
                                    "exclude": true
                                }
                            },
                            {
                                "type": "PERIMETER",
                                "position": "",
                                "description": "4B40",
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
                            "momentRatio": false,
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
                    "componentActiveStates": [
                        {
                            "componentID": 1,
                            "activeState": true
                        }
                    ],
                    "cases": [
                        {
                            "load": {
                                "fx": -623443.3148,
                                "myy": 288370.8424
                            }
                        },
                        {
                            "load": {
                                "fx": -63554.83335,
                                "myy": 259421.03730000006
                            }
                        },
                        {
                            "load": {
                                "fx": -2456383.9699999999,
                                "myy": 0.000439
                            }
                        },
                        {
                            "load": {
                                "fx": -544805.0815,
                                "myy": 29965.0644
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
                        "Cnom": 0.06,
                        "userDefinedPhiLower": 0.0,
                        "userDefinedPhiHigher": 0.0,
                        "userDefinedStrainLower": 0.0,
                        "userDefinedStrainHigher": 0.0
                    },
                    "loadTerm": "LONG",
                    "creepCoefficients": [
                        {
                            "componentID": 1,
                            "creepCoefficient": 2.0
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
                                "fx": -1199450.42,
                                "myy": 112703.5301
                            }
                        },
                        {
                            "load": {
                                "fx": -1199450.42,
                                "myy": 112703.5301
                            }
                        },
                        {
                            "load": {
                                "fx": -1276063.477,
                                "myy": 110325.8524
                            }
                        },
                        {
                            "load": {
                                "fx": -1276063.477,
                                "myy": 110325.8524
                            }
                        },
                        {
                            "load": {
                                "fx": -1207600.4789999999,
                                "myy": 107331.4217
                            }
                        },
                        {
                            "load": {
                                "fx": -1207600.4789999999,
                                "myy": 107331.4217
                            }
                        },
                        {
                            "load": {
                                "fx": -563089.8671,
                                "myy": 105635.4599
                            }
                        },
                        {
                            "load": {
                                "fx": -563089.8671,
                                "myy": 105635.4599
                            }
                        },
                        {
                            "load": {}
                        }
                    ]
                }
            ],
            "extents": {
                "yMin": -0.24207748802426705,
                "yMax": 0.24207748802426705,
                "zMin": 0.24207748802426705,
                "zMax": -0.24207748802426705
            },
            "properties": [
                {
                    "analysis": {
                        "area": 0.18292139995419658,
                        "localAxis": {
                            "iyy": 0.0026627032703603326,
                            "izz": 0.002662703270360333,
                            "iyz": -1.352088657603921e-19
                        },
                        "principalAxis": {
                            "iuu": 0.0026627032703603335,
                            "ivv": 0.0026627032703603326,
                            "angle": 1.2920216565290286
                        },
                        "shear": {
                            "ky": 0.8571429,
                            "kz": 0.8571429
                        },
                        "torsion": {
                            "j": 0.005325362364049536
                        },
                        "elastic": {
                            "zy": 0.010999384090161288,
                            "zz": 0.010999384090161289
                        },
                        "plastic": {
                            "zpy": 0.018733087143240007,
                            "zpz": 0.01873308714324001
                        },
                        "centroid": {
                            "cy": -4.2230928042829e-18,
                            "cz": -1.0076151252324112e-17
                        },
                        "radiusOfGyration": {
                            "ry": 0.1206505004264456,
                            "rz": 0.1206505004264456
                        },
                        "physical": {
                            "surfaceArea": 1.518575559315336
                        }
                    },
                    "paths": [
                        {
                            "isVoid": false,
                            "points": [
                                {
                                    "y": -0.047226975091509807,
                                    "z": 0.23742603697119039
                                },
                                {
                                    "y": -0.09263904401544558,
                                    "z": 0.2236504364673664
                                },
                                {
                                    "y": -0.134491046430442,
                                    "z": 0.20128007511471136
                                },
                                {
                                    "y": -0.1711746333545645,
                                    "z": 0.17117463335456443
                                },
                                {
                                    "y": -0.2012800751147114,
                                    "z": 0.1344910464304419
                                },
                                {
                                    "y": -0.22365043646736644,
                                    "z": 0.09263904401544548
                                },
                                {
                                    "y": -0.2374260369711904,
                                    "z": 0.0472269750915097
                                },
                                {
                                    "y": -0.24207748802426705,
                                    "z": -4.446891312818255e-17
                                },
                                {
                                    "y": -0.23742603697119039,
                                    "z": -0.04722697509150979
                                },
                                {
                                    "y": -0.2236504364673664,
                                    "z": -0.09263904401544557
                                },
                                {
                                    "y": -0.20128007511471136,
                                    "z": -0.134491046430442
                                },
                                {
                                    "y": -0.17117463335456446,
                                    "z": -0.1711746333545645
                                },
                                {
                                    "y": -0.13449104643044194,
                                    "z": -0.2012800751147114
                                },
                                {
                                    "y": -0.0926390440154454,
                                    "z": -0.2236504364673665
                                },
                                {
                                    "y": -0.047226975091509717,
                                    "z": -0.2374260369711904
                                },
                                {
                                    "y": 2.964594208545504e-17,
                                    "z": -0.24207748802426705
                                },
                                {
                                    "y": 0.047226975091509779,
                                    "z": -0.2374260369711904
                                },
                                {
                                    "y": 0.09263904401544546,
                                    "z": -0.22365043646736647
                                },
                                {
                                    "y": 0.134491046430442,
                                    "z": -0.20128007511471139
                                },
                                {
                                    "y": 0.17117463335456449,
                                    "z": -0.17117463335456446
                                },
                                {
                                    "y": 0.20128007511471139,
                                    "z": -0.13449104643044194
                                },
                                {
                                    "y": 0.22365043646736647,
                                    "z": -0.09263904401544541
                                },
                                {
                                    "y": 0.2374260369711904,
                                    "z": -0.04722697509150967
                                },
                                {
                                    "y": 0.24207748802426705,
                                    "z": 1.482297104272752e-17
                                },
                                {
                                    "y": 0.2374260369711904,
                                    "z": 0.04722697509150971
                                },
                                {
                                    "y": 0.22365043646736647,
                                    "z": 0.09263904401544544
                                },
                                {
                                    "y": 0.20128007511471136,
                                    "z": 0.13449104643044203
                                },
                                {
                                    "y": 0.17117463335456449,
                                    "z": 0.17117463335456449
                                },
                                {
                                    "y": 0.134491046430442,
                                    "z": 0.20128007511471136
                                },
                                {
                                    "y": 0.09263904401544543,
                                    "z": 0.22365043646736647
                                },
                                {
                                    "y": 0.047226975091509689,
                                    "z": 0.2374260369711904
                                },
                                {
                                    "y": 0.0,
                                    "z": 0.24207748802426705
                                }
                            ]
                        }
                    ],
                    "links": [
                        {
                            "grade": 1,
                            "diameter": 0.01,
                            "path": "M -0.025957 0.143056 A 0.025000 0.025000 0 0 1 -0.030764 0.142100 L -0.053367 0.135244 L -0.053367 0.135244 A 0.025000 0.025000 0 0 1 -0.057895 0.133368 L -0.078727 0.122233 L -0.078727 0.122233 A 0.025000 0.025000 0 0 1 -0.082802 0.119511 L -0.101061 0.104526 L -0.101061 0.104526 A 0.025000 0.025000 0 0 1 -0.104526 0.101061 L -0.119511 0.082802 L -0.119511 0.082802 A 0.025000 0.025000 0 0 1 -0.122233 0.078727 L -0.133368 0.057895 L -0.133368 0.057895 A 0.025000 0.025000 0 0 1 -0.135244 0.053367 L -0.142100 0.030764 L -0.142100 0.030764 A 0.025000 0.025000 0 0 1 -0.143056 0.025957 L -0.145372 0.002450 L -0.145372 0.002450 A 0.025000 0.025000 0 0 1 -0.145372 -0.002450 L -0.143056 -0.025957 L -0.143056 -0.025957 A 0.025000 0.025000 0 0 1 -0.142100 -0.030764 L -0.135244 -0.053367 L -0.135244 -0.053367 A 0.025000 0.025000 0 0 1 -0.133368 -0.057895 L -0.122233 -0.078727 L -0.122233 -0.078727 A 0.025000 0.025000 0 0 1 -0.119511 -0.082802 L -0.104526 -0.101061 L -0.104526 -0.101061 A 0.025000 0.025000 0 0 1 -0.101061 -0.104526 L -0.082802 -0.119511 L -0.082802 -0.119511 A 0.025000 0.025000 0 0 1 -0.078727 -0.122233 L -0.057895 -0.133368 L -0.057895 -0.133368 A 0.025000 0.025000 0 0 1 -0.053367 -0.135244 L -0.030764 -0.142100 L -0.030764 -0.142100 A 0.025000 0.025000 0 0 1 -0.025957 -0.143056 L -0.002450 -0.145372 L -0.002450 -0.145372 A 0.025000 0.025000 0 0 1 0.002450 -0.145372 L 0.025957 -0.143056 L 0.025957 -0.143056 A 0.025000 0.025000 0 0 1 0.030764 -0.142100 L 0.053367 -0.135244 L 0.053367 -0.135244 A 0.025000 0.025000 0 0 1 0.057895 -0.133368 L 0.078727 -0.122233 L 0.078727 -0.122233 A 0.025000 0.025000 0 0 1 0.082802 -0.119511 L 0.101061 -0.104526 L 0.101061 -0.104526 A 0.025000 0.025000 0 0 1 0.104526 -0.101061 L 0.119511 -0.082802 L 0.119511 -0.082802 A 0.025000 0.025000 0 0 1 0.122233 -0.078727 L 0.133368 -0.057895 L 0.133368 -0.057895 A 0.025000 0.025000 0 0 1 0.135244 -0.053367 L 0.142100 -0.030764 L 0.142100 -0.030764 A 0.025000 0.025000 0 0 1 0.143056 -0.025957 L 0.145372 -0.002450 L 0.145372 -0.002450 A 0.025000 0.025000 0 0 1 0.145372 0.002450 L 0.143056 0.025957 L 0.143056 0.025957 A 0.025000 0.025000 0 0 1 0.142100 0.030764 L 0.135244 0.053367 L 0.135244 0.053367 A 0.025000 0.025000 0 0 1 0.133368 0.057895 L 0.122233 0.078727 L 0.122233 0.078727 A 0.025000 0.025000 0 0 1 0.119511 0.082802 L 0.104526 0.101061 L 0.104526 0.101061 A 0.025000 0.025000 0 0 1 0.101061 0.104526 L 0.082802 0.119511 L 0.082802 0.119511 A 0.025000 0.025000 0 0 1 0.078727 0.122233 L 0.057895 0.133368 L 0.057895 0.133368 A 0.025000 0.025000 0 0 1 0.053367 0.135244 L 0.030764 0.142100 L 0.030764 0.142100 A 0.025000 0.025000 0 0 1 0.025957 0.143056 L 0.002450 0.145372 L 0.002450 0.145372 A 0.025000 0.025000 0 0 1 -0.002450 0.145372 L -0.025957 0.143056"
                        }
                    ],
                    "bars": [
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 1.1589343301154229e-17,
                            "z": 0.12030000000000002
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -0.1203,
                            "z": 2.480865224606677e-17
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": -1.7875658686331089e-17,
                            "z": -0.12029999999999999
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.04,
                            "y": 0.1203,
                            "z": -1.9388850735161206e-17
                        }
                    ]
                }
            ]
        },
        {
            "name": "* all springs - North Abutment Pile 508/450 - 1.5m down",
            "components": [
                {
                    "material": "concrete",
                    "grade": "C40/50",
                    "profile": "STD C(mm) 482.6",
                    "reinforcement": {
                        "cover": 0.091,
                        "positionsRelativeTo": "ORIGIN",
                        "groups": [
                            {
                                "type": "LINK",
                                "position": "",
                                "description": "B10",
                                "preload": {
                                    "preloadType": "NONE",
                                    "value": 0.0,
                                    "exclude": true
                                }
                            },
                            {
                                "type": "PERIMETER",
                                "position": "",
                                "description": "4B32",
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
                            "momentRatio": false,
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
                    "componentActiveStates": [
                        {
                            "componentID": 1,
                            "activeState": true
                        }
                    ],
                    "cases": [
                        {
                            "load": {
                                "fx": -491751.6253,
                                "myy": 134392.82030000003
                            }
                        },
                        {
                            "load": {
                                "fx": -1542123.399,
                                "myy": 138358.9844
                            }
                        },
                        {
                            "load": {
                                "fx": -104809.763,
                                "myy": 112086.0602
                            }
                        },
                        {
                            "load": {
                                "fx": -2456383.9699999999,
                                "myy": 0.000439
                            }
                        },
                        {
                            "load": {
                                "fx": -70351.29418,
                                "myy": 63990.20619
                            }
                        },
                        {
                            "load": {
                                "fx": -630241.8953999999,
                                "myy": 74562.837
                            }
                        },
                        {
                            "load": {
                                "fx": -1535681.801,
                                "myy": 102904.9737
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
                        "Cnom": 0.06,
                        "userDefinedPhiLower": 0.0,
                        "userDefinedPhiHigher": 0.0,
                        "userDefinedStrainLower": 0.0,
                        "userDefinedStrainHigher": 0.0
                    },
                    "loadTerm": "LONG",
                    "creepCoefficients": [
                        {
                            "componentID": 1,
                            "creepCoefficient": 2.0
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
                                "fx": -1270856.7459999999,
                                "myy": 72731.0517
                            }
                        },
                        {
                            "load": {
                                "fx": -1270856.7459999999,
                                "myy": 72731.0517
                            }
                        },
                        {
                            "load": {
                                "fx": -1270856.082,
                                "myy": 72731.00185
                            }
                        },
                        {
                            "load": {
                                "fx": -1270856.082,
                                "myy": 72731.00185
                            }
                        },
                        {
                            "load": {
                                "fx": -615593.5564,
                                "myy": 72199.70904
                            }
                        },
                        {
                            "load": {
                                "fx": -615593.5564,
                                "myy": 72199.70904
                            }
                        },
                        {
                            "load": {
                                "fx": -615593.0282000001,
                                "myy": 72199.69016
                            }
                        },
                        {
                            "load": {
                                "fx": -615593.0282000001,
                                "myy": 72199.69016
                            }
                        },
                        {
                            "load": {}
                        }
                    ]
                }
            ],
            "extents": {
                "yMin": -0.24207748802426705,
                "yMax": 0.24207748802426705,
                "zMin": 0.24207748802426705,
                "zMax": -0.24207748802426705
            },
            "properties": [
                {
                    "analysis": {
                        "area": 0.18292139995419658,
                        "localAxis": {
                            "iyy": 0.0026627032703603326,
                            "izz": 0.002662703270360333,
                            "iyz": -1.352088657603921e-19
                        },
                        "principalAxis": {
                            "iuu": 0.0026627032703603335,
                            "ivv": 0.0026627032703603326,
                            "angle": 1.2920216565290286
                        },
                        "shear": {
                            "ky": 0.8571429,
                            "kz": 0.8571429
                        },
                        "torsion": {
                            "j": 0.005325362364049536
                        },
                        "elastic": {
                            "zy": 0.010999384090161288,
                            "zz": 0.010999384090161289
                        },
                        "plastic": {
                            "zpy": 0.018733087143240007,
                            "zpz": 0.01873308714324001
                        },
                        "centroid": {
                            "cy": -4.2230928042829e-18,
                            "cz": -1.0076151252324112e-17
                        },
                        "radiusOfGyration": {
                            "ry": 0.1206505004264456,
                            "rz": 0.1206505004264456
                        },
                        "physical": {
                            "surfaceArea": 1.518575559315336
                        }
                    },
                    "paths": [
                        {
                            "isVoid": false,
                            "points": [
                                {
                                    "y": -0.047226975091509807,
                                    "z": 0.23742603697119039
                                },
                                {
                                    "y": -0.09263904401544558,
                                    "z": 0.2236504364673664
                                },
                                {
                                    "y": -0.134491046430442,
                                    "z": 0.20128007511471136
                                },
                                {
                                    "y": -0.1711746333545645,
                                    "z": 0.17117463335456443
                                },
                                {
                                    "y": -0.2012800751147114,
                                    "z": 0.1344910464304419
                                },
                                {
                                    "y": -0.22365043646736644,
                                    "z": 0.09263904401544548
                                },
                                {
                                    "y": -0.2374260369711904,
                                    "z": 0.0472269750915097
                                },
                                {
                                    "y": -0.24207748802426705,
                                    "z": -4.446891312818255e-17
                                },
                                {
                                    "y": -0.23742603697119039,
                                    "z": -0.04722697509150979
                                },
                                {
                                    "y": -0.2236504364673664,
                                    "z": -0.09263904401544557
                                },
                                {
                                    "y": -0.20128007511471136,
                                    "z": -0.134491046430442
                                },
                                {
                                    "y": -0.17117463335456446,
                                    "z": -0.1711746333545645
                                },
                                {
                                    "y": -0.13449104643044194,
                                    "z": -0.2012800751147114
                                },
                                {
                                    "y": -0.0926390440154454,
                                    "z": -0.2236504364673665
                                },
                                {
                                    "y": -0.047226975091509717,
                                    "z": -0.2374260369711904
                                },
                                {
                                    "y": 2.964594208545504e-17,
                                    "z": -0.24207748802426705
                                },
                                {
                                    "y": 0.047226975091509779,
                                    "z": -0.2374260369711904
                                },
                                {
                                    "y": 0.09263904401544546,
                                    "z": -0.22365043646736647
                                },
                                {
                                    "y": 0.134491046430442,
                                    "z": -0.20128007511471139
                                },
                                {
                                    "y": 0.17117463335456449,
                                    "z": -0.17117463335456446
                                },
                                {
                                    "y": 0.20128007511471139,
                                    "z": -0.13449104643044194
                                },
                                {
                                    "y": 0.22365043646736647,
                                    "z": -0.09263904401544541
                                },
                                {
                                    "y": 0.2374260369711904,
                                    "z": -0.04722697509150967
                                },
                                {
                                    "y": 0.24207748802426705,
                                    "z": 1.482297104272752e-17
                                },
                                {
                                    "y": 0.2374260369711904,
                                    "z": 0.04722697509150971
                                },
                                {
                                    "y": 0.22365043646736647,
                                    "z": 0.09263904401544544
                                },
                                {
                                    "y": 0.20128007511471136,
                                    "z": 0.13449104643044203
                                },
                                {
                                    "y": 0.17117463335456449,
                                    "z": 0.17117463335456449
                                },
                                {
                                    "y": 0.134491046430442,
                                    "z": 0.20128007511471136
                                },
                                {
                                    "y": 0.09263904401544543,
                                    "z": 0.22365043646736647
                                },
                                {
                                    "y": 0.047226975091509689,
                                    "z": 0.2374260369711904
                                },
                                {
                                    "y": 0.0,
                                    "z": 0.24207748802426705
                                }
                            ]
                        }
                    ],
                    "links": [
                        {
                            "grade": 1,
                            "diameter": 0.01,
                            "path": "M -0.025957 0.143056 A 0.025000 0.025000 0 0 1 -0.030764 0.142100 L -0.053367 0.135244 L -0.053367 0.135244 A 0.025000 0.025000 0 0 1 -0.057895 0.133368 L -0.078727 0.122233 L -0.078727 0.122233 A 0.025000 0.025000 0 0 1 -0.082802 0.119511 L -0.101061 0.104526 L -0.101061 0.104526 A 0.025000 0.025000 0 0 1 -0.104526 0.101061 L -0.119511 0.082802 L -0.119511 0.082802 A 0.025000 0.025000 0 0 1 -0.122233 0.078727 L -0.133368 0.057895 L -0.133368 0.057895 A 0.025000 0.025000 0 0 1 -0.135244 0.053367 L -0.142100 0.030764 L -0.142100 0.030764 A 0.025000 0.025000 0 0 1 -0.143056 0.025957 L -0.145372 0.002450 L -0.145372 0.002450 A 0.025000 0.025000 0 0 1 -0.145372 -0.002450 L -0.143056 -0.025957 L -0.143056 -0.025957 A 0.025000 0.025000 0 0 1 -0.142100 -0.030764 L -0.135244 -0.053367 L -0.135244 -0.053367 A 0.025000 0.025000 0 0 1 -0.133368 -0.057895 L -0.122233 -0.078727 L -0.122233 -0.078727 A 0.025000 0.025000 0 0 1 -0.119511 -0.082802 L -0.104526 -0.101061 L -0.104526 -0.101061 A 0.025000 0.025000 0 0 1 -0.101061 -0.104526 L -0.082802 -0.119511 L -0.082802 -0.119511 A 0.025000 0.025000 0 0 1 -0.078727 -0.122233 L -0.057895 -0.133368 L -0.057895 -0.133368 A 0.025000 0.025000 0 0 1 -0.053367 -0.135244 L -0.030764 -0.142100 L -0.030764 -0.142100 A 0.025000 0.025000 0 0 1 -0.025957 -0.143056 L -0.002450 -0.145372 L -0.002450 -0.145372 A 0.025000 0.025000 0 0 1 0.002450 -0.145372 L 0.025957 -0.143056 L 0.025957 -0.143056 A 0.025000 0.025000 0 0 1 0.030764 -0.142100 L 0.053367 -0.135244 L 0.053367 -0.135244 A 0.025000 0.025000 0 0 1 0.057895 -0.133368 L 0.078727 -0.122233 L 0.078727 -0.122233 A 0.025000 0.025000 0 0 1 0.082802 -0.119511 L 0.101061 -0.104526 L 0.101061 -0.104526 A 0.025000 0.025000 0 0 1 0.104526 -0.101061 L 0.119511 -0.082802 L 0.119511 -0.082802 A 0.025000 0.025000 0 0 1 0.122233 -0.078727 L 0.133368 -0.057895 L 0.133368 -0.057895 A 0.025000 0.025000 0 0 1 0.135244 -0.053367 L 0.142100 -0.030764 L 0.142100 -0.030764 A 0.025000 0.025000 0 0 1 0.143056 -0.025957 L 0.145372 -0.002450 L 0.145372 -0.002450 A 0.025000 0.025000 0 0 1 0.145372 0.002450 L 0.143056 0.025957 L 0.143056 0.025957 A 0.025000 0.025000 0 0 1 0.142100 0.030764 L 0.135244 0.053367 L 0.135244 0.053367 A 0.025000 0.025000 0 0 1 0.133368 0.057895 L 0.122233 0.078727 L 0.122233 0.078727 A 0.025000 0.025000 0 0 1 0.119511 0.082802 L 0.104526 0.101061 L 0.104526 0.101061 A 0.025000 0.025000 0 0 1 0.101061 0.104526 L 0.082802 0.119511 L 0.082802 0.119511 A 0.025000 0.025000 0 0 1 0.078727 0.122233 L 0.057895 0.133368 L 0.057895 0.133368 A 0.025000 0.025000 0 0 1 0.053367 0.135244 L 0.030764 0.142100 L 0.030764 0.142100 A 0.025000 0.025000 0 0 1 0.025957 0.143056 L 0.002450 0.145372 L 0.002450 0.145372 A 0.025000 0.025000 0 0 1 -0.002450 0.145372 L -0.025957 0.143056"
                        }
                    ],
                    "bars": [
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": 1.18342726609837e-17,
                            "z": 0.12430000000000002
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": -0.12430000000000001,
                            "z": 2.5298510965725715e-17
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": -1.86104467658195e-17,
                            "z": -0.1243
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": 0.12430000000000001,
                            "z": -2.0368568174479093e-17
                        }
                    ]
                }
            ]
        },
        {
            "name": "* all springs - North Abutment Pile 508/450 - current top",
            "components": [
                {
                    "material": "concrete",
                    "grade": "C40/50",
                    "profile": "STD C(mm) 482.6",
                    "reinforcement": {
                        "cover": 0.091,
                        "positionsRelativeTo": "ORIGIN",
                        "groups": [
                            {
                                "type": "LINK",
                                "position": "",
                                "description": "B10",
                                "preload": {
                                    "preloadType": "NONE",
                                    "value": 0.0,
                                    "exclude": true
                                }
                            },
                            {
                                "type": "PERIMETER",
                                "position": "",
                                "description": "4(2)B32",
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
                            "momentRatio": false,
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
                    "componentActiveStates": [
                        {
                            "componentID": 1,
                            "activeState": true
                        }
                    ],
                    "cases": [
                        {
                            "load": {
                                "fx": -623443.3148,
                                "myy": 288370.8424
                            }
                        },
                        {
                            "load": {
                                "fx": -63554.83335,
                                "myy": 259421.03730000006
                            }
                        },
                        {
                            "load": {
                                "fx": -2456383.9699999999,
                                "myy": 0.000439
                            }
                        },
                        {
                            "load": {
                                "fx": -544805.0815,
                                "myy": 29965.0644
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
                        "Cnom": 0.06,
                        "userDefinedPhiLower": 0.0,
                        "userDefinedPhiHigher": 0.0,
                        "userDefinedStrainLower": 0.0,
                        "userDefinedStrainHigher": 0.0
                    },
                    "loadTerm": "LONG",
                    "creepCoefficients": [
                        {
                            "componentID": 1,
                            "creepCoefficient": 2.0
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
                                "fx": -1199450.42,
                                "myy": 112703.5301
                            }
                        },
                        {
                            "load": {
                                "fx": -1199450.42,
                                "myy": 112703.5301
                            }
                        },
                        {
                            "load": {
                                "fx": -1276063.477,
                                "myy": 110325.8524
                            }
                        },
                        {
                            "load": {
                                "fx": -1276063.477,
                                "myy": 110325.8524
                            }
                        },
                        {
                            "load": {
                                "fx": -1207600.4789999999,
                                "myy": 107331.4217
                            }
                        },
                        {
                            "load": {
                                "fx": -1207600.4789999999,
                                "myy": 107331.4217
                            }
                        },
                        {
                            "load": {
                                "fx": -563089.8671,
                                "myy": 105635.4599
                            }
                        },
                        {
                            "load": {
                                "fx": -563089.8671,
                                "myy": 105635.4599
                            }
                        },
                        {
                            "load": {}
                        }
                    ]
                }
            ],
            "extents": {
                "yMin": -0.24207748802426705,
                "yMax": 0.24207748802426705,
                "zMin": 0.24207748802426705,
                "zMax": -0.24207748802426705
            },
            "properties": [
                {
                    "analysis": {
                        "area": 0.18292139995419658,
                        "localAxis": {
                            "iyy": 0.0026627032703603326,
                            "izz": 0.002662703270360333,
                            "iyz": -1.352088657603921e-19
                        },
                        "principalAxis": {
                            "iuu": 0.0026627032703603335,
                            "ivv": 0.0026627032703603326,
                            "angle": 1.2920216565290286
                        },
                        "shear": {
                            "ky": 0.8571429,
                            "kz": 0.8571429
                        },
                        "torsion": {
                            "j": 0.005325362364049536
                        },
                        "elastic": {
                            "zy": 0.010999384090161288,
                            "zz": 0.010999384090161289
                        },
                        "plastic": {
                            "zpy": 0.018733087143240007,
                            "zpz": 0.01873308714324001
                        },
                        "centroid": {
                            "cy": -4.2230928042829e-18,
                            "cz": -1.0076151252324112e-17
                        },
                        "radiusOfGyration": {
                            "ry": 0.1206505004264456,
                            "rz": 0.1206505004264456
                        },
                        "physical": {
                            "surfaceArea": 1.518575559315336
                        }
                    },
                    "paths": [
                        {
                            "isVoid": false,
                            "points": [
                                {
                                    "y": -0.047226975091509807,
                                    "z": 0.23742603697119039
                                },
                                {
                                    "y": -0.09263904401544558,
                                    "z": 0.2236504364673664
                                },
                                {
                                    "y": -0.134491046430442,
                                    "z": 0.20128007511471136
                                },
                                {
                                    "y": -0.1711746333545645,
                                    "z": 0.17117463335456443
                                },
                                {
                                    "y": -0.2012800751147114,
                                    "z": 0.1344910464304419
                                },
                                {
                                    "y": -0.22365043646736644,
                                    "z": 0.09263904401544548
                                },
                                {
                                    "y": -0.2374260369711904,
                                    "z": 0.0472269750915097
                                },
                                {
                                    "y": -0.24207748802426705,
                                    "z": -4.446891312818255e-17
                                },
                                {
                                    "y": -0.23742603697119039,
                                    "z": -0.04722697509150979
                                },
                                {
                                    "y": -0.2236504364673664,
                                    "z": -0.09263904401544557
                                },
                                {
                                    "y": -0.20128007511471136,
                                    "z": -0.134491046430442
                                },
                                {
                                    "y": -0.17117463335456446,
                                    "z": -0.1711746333545645
                                },
                                {
                                    "y": -0.13449104643044194,
                                    "z": -0.2012800751147114
                                },
                                {
                                    "y": -0.0926390440154454,
                                    "z": -0.2236504364673665
                                },
                                {
                                    "y": -0.047226975091509717,
                                    "z": -0.2374260369711904
                                },
                                {
                                    "y": 2.964594208545504e-17,
                                    "z": -0.24207748802426705
                                },
                                {
                                    "y": 0.047226975091509779,
                                    "z": -0.2374260369711904
                                },
                                {
                                    "y": 0.09263904401544546,
                                    "z": -0.22365043646736647
                                },
                                {
                                    "y": 0.134491046430442,
                                    "z": -0.20128007511471139
                                },
                                {
                                    "y": 0.17117463335456449,
                                    "z": -0.17117463335456446
                                },
                                {
                                    "y": 0.20128007511471139,
                                    "z": -0.13449104643044194
                                },
                                {
                                    "y": 0.22365043646736647,
                                    "z": -0.09263904401544541
                                },
                                {
                                    "y": 0.2374260369711904,
                                    "z": -0.04722697509150967
                                },
                                {
                                    "y": 0.24207748802426705,
                                    "z": 1.482297104272752e-17
                                },
                                {
                                    "y": 0.2374260369711904,
                                    "z": 0.04722697509150971
                                },
                                {
                                    "y": 0.22365043646736647,
                                    "z": 0.09263904401544544
                                },
                                {
                                    "y": 0.20128007511471136,
                                    "z": 0.13449104643044203
                                },
                                {
                                    "y": 0.17117463335456449,
                                    "z": 0.17117463335456449
                                },
                                {
                                    "y": 0.134491046430442,
                                    "z": 0.20128007511471136
                                },
                                {
                                    "y": 0.09263904401544543,
                                    "z": 0.22365043646736647
                                },
                                {
                                    "y": 0.047226975091509689,
                                    "z": 0.2374260369711904
                                },
                                {
                                    "y": 0.0,
                                    "z": 0.24207748802426705
                                }
                            ]
                        }
                    ],
                    "links": [
                        {
                            "grade": 1,
                            "diameter": 0.01,
                            "path": "M -0.025957 0.143056 A 0.025000 0.025000 0 0 1 -0.030764 0.142100 L -0.053367 0.135244 L -0.053367 0.135244 A 0.025000 0.025000 0 0 1 -0.057895 0.133368 L -0.078727 0.122233 L -0.078727 0.122233 A 0.025000 0.025000 0 0 1 -0.082802 0.119511 L -0.101061 0.104526 L -0.101061 0.104526 A 0.025000 0.025000 0 0 1 -0.104526 0.101061 L -0.119511 0.082802 L -0.119511 0.082802 A 0.025000 0.025000 0 0 1 -0.122233 0.078727 L -0.133368 0.057895 L -0.133368 0.057895 A 0.025000 0.025000 0 0 1 -0.135244 0.053367 L -0.142100 0.030764 L -0.142100 0.030764 A 0.025000 0.025000 0 0 1 -0.143056 0.025957 L -0.145372 0.002450 L -0.145372 0.002450 A 0.025000 0.025000 0 0 1 -0.145372 -0.002450 L -0.143056 -0.025957 L -0.143056 -0.025957 A 0.025000 0.025000 0 0 1 -0.142100 -0.030764 L -0.135244 -0.053367 L -0.135244 -0.053367 A 0.025000 0.025000 0 0 1 -0.133368 -0.057895 L -0.122233 -0.078727 L -0.122233 -0.078727 A 0.025000 0.025000 0 0 1 -0.119511 -0.082802 L -0.104526 -0.101061 L -0.104526 -0.101061 A 0.025000 0.025000 0 0 1 -0.101061 -0.104526 L -0.082802 -0.119511 L -0.082802 -0.119511 A 0.025000 0.025000 0 0 1 -0.078727 -0.122233 L -0.057895 -0.133368 L -0.057895 -0.133368 A 0.025000 0.025000 0 0 1 -0.053367 -0.135244 L -0.030764 -0.142100 L -0.030764 -0.142100 A 0.025000 0.025000 0 0 1 -0.025957 -0.143056 L -0.002450 -0.145372 L -0.002450 -0.145372 A 0.025000 0.025000 0 0 1 0.002450 -0.145372 L 0.025957 -0.143056 L 0.025957 -0.143056 A 0.025000 0.025000 0 0 1 0.030764 -0.142100 L 0.053367 -0.135244 L 0.053367 -0.135244 A 0.025000 0.025000 0 0 1 0.057895 -0.133368 L 0.078727 -0.122233 L 0.078727 -0.122233 A 0.025000 0.025000 0 0 1 0.082802 -0.119511 L 0.101061 -0.104526 L 0.101061 -0.104526 A 0.025000 0.025000 0 0 1 0.104526 -0.101061 L 0.119511 -0.082802 L 0.119511 -0.082802 A 0.025000 0.025000 0 0 1 0.122233 -0.078727 L 0.133368 -0.057895 L 0.133368 -0.057895 A 0.025000 0.025000 0 0 1 0.135244 -0.053367 L 0.142100 -0.030764 L 0.142100 -0.030764 A 0.025000 0.025000 0 0 1 0.143056 -0.025957 L 0.145372 -0.002450 L 0.145372 -0.002450 A 0.025000 0.025000 0 0 1 0.145372 0.002450 L 0.143056 0.025957 L 0.143056 0.025957 A 0.025000 0.025000 0 0 1 0.142100 0.030764 L 0.135244 0.053367 L 0.135244 0.053367 A 0.025000 0.025000 0 0 1 0.133368 0.057895 L 0.122233 0.078727 L 0.122233 0.078727 A 0.025000 0.025000 0 0 1 0.119511 0.082802 L 0.104526 0.101061 L 0.104526 0.101061 A 0.025000 0.025000 0 0 1 0.101061 0.104526 L 0.082802 0.119511 L 0.082802 0.119511 A 0.025000 0.025000 0 0 1 0.078727 0.122233 L 0.057895 0.133368 L 0.057895 0.133368 A 0.025000 0.025000 0 0 1 0.053367 0.135244 L 0.030764 0.142100 L 0.030764 0.142100 A 0.025000 0.025000 0 0 1 0.025957 0.143056 L 0.002450 0.145372 L 0.002450 0.145372 A 0.025000 0.025000 0 0 1 -0.002450 0.145372 L -0.025957 0.143056"
                        }
                    ],
                    "bars": [
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": 0.01600000000000001,
                            "z": 0.12430000000000002
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": -0.01599999999999999,
                            "z": 0.12430000000000002
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": -0.12430000000000001,
                            "z": 0.016000000000000026
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": -0.12430000000000001,
                            "z": -0.015999999999999977
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": -0.01600000000000002,
                            "z": -0.1243
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": 0.01599999999999998,
                            "z": -0.1243
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": 0.12430000000000001,
                            "z": -0.01600000000000002
                        },
                        {
                            "groupId": 1,
                            "grade": 1,
                            "diameter": 0.032,
                            "y": 0.12430000000000001,
                            "z": 0.01599999999999998
                        }
                    ]
                }
            ]
        }
    ]
}