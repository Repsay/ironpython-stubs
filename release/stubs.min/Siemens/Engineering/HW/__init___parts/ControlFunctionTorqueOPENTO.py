class ControlFunctionTorqueOPENTO(Enum,IComparable,IFormattable,IConvertible):
 """
 Possible values for property ControlFunctionTorqueOPENTO

 

 enum ControlFunctionTorqueOPENTO,values: AcyclicReceiveBit00 (40),AcyclicReceiveBit01 (41),AcyclicReceiveBit02 (42),AcyclicReceiveBit03 (43),AcyclicReceiveBit04 (44),AcyclicReceiveBit05 (45),AcyclicReceiveBit06 (46),AcyclicReceiveBit07 (47),AcyclicReceiveBit10 (48),AcyclicReceiveBit11 (49),AcyclicReceiveBit12 (50),AcyclicReceiveBit13 (51),AcyclicReceiveBit14 (52),AcyclicReceiveBit15 (53),AcyclicReceiveBit16 (54),AcyclicReceiveBit17 (55),BUInput1 (9),BUInput2 (10),BUInput3 (11),BUInput4 (12),BUTestResetButton (8),ContactorControl1QE1 (80),ContactorControl2QE2 (81),ContactorControl3QE3 (82),ContactorControl4QE4 (83),ContactorControl5QE5 (84),Counter1Output (236),Counter2Output (237),Counter3Output (238),Counter4Output (239),Counter5Output (228),Counter6Output (229),CyclicReceiveBit00 (56),CyclicReceiveBit01 (57),CyclicReceiveBit02 (58),CyclicReceiveBit03 (59),CyclicReceiveBit04 (60),CyclicReceiveBit05 (61),CyclicReceiveBit06 (62),CyclicReceiveBit07 (63),CyclicReceiveBit10 (64),CyclicReceiveBit11 (65),CyclicReceiveBit12 (66),CyclicReceiveBit13 (67),CyclicReceiveBit14 (68),CyclicReceiveBit15 (69),CyclicReceiveBit16 (70),CyclicReceiveBit17 (71),DisplayQLAOff (90),DisplayQLEForward (91),DisplayQLEForwardFast (92),DisplayQLEReverse (89),DisplayQLEReverseFast (88),DisplayQLSFault (93),DM1Input1 (16),DM1Input2 (17),DM1Input3 (18),DM1Input4 (19),DM1SensorChannel1 (24),DM1SensorChannel2 (25),DM2Input1 (20),DM2Input2 (21),DM2Input3 (22),DM2Input4 (23),EnabledControlCommandOff (74),EnabledControlCommandOnForward (75),EnabledControlCommandOnForwardFast (76),EnabledControlCommandOnReverse (73),EnabledControlCommandOnReverseFast (72),EventAM1OpenCircuit (180),EventAM1TripLevel0420mAGt (158),EventAM1TripLevel0420mALt (159),EventAM1WarningLevel0420mAGt (150),EventAM1WarningLevel0420mALt (151),EventAM2OpenCircuit (179),EventAM2TripLevel0420mAGt (6),EventAM2TripLevel0420mALt (7),EventAM2WarningLevel0420mAGt (4),EventAM2WarningLevel0420mALt (5),EventConfiguredOperatorPanelMissing (188),EventDMFLOCALOk (186),EventExternalFault1 (172),EventExternalFault2 (173),EventExternalFault3 (174),EventExternalFault4 (175),EventExternalFault5 (176),EventExternalFault6 (177),EventExternalGroundFault (133),EventExternalGroundFaultWarning (134),EventInternalGroundFault (132),EventJustOneStartPossible (165),EventLimitMonitor1 (168),EventLimitMonitor2 (169),EventLimitMonitor3 (170),EventLimitMonitor4 (171),EventLimitMonitor5 (38),EventLimitMonitor6 (39),EventMonitoringPeriodForMandatoryTestingTestRequirement (182),EventMotorOperatingHoursGt (166),EventNoStartPermitted (163),EventNumberOfStartsGt (164),EventOverload (130),EventOverloadAndPhaseFailure (131),EventPrewarningOverload (128),EventPROFIsafeActive (187),EventSafetyrelatedTripping (181),EventStalledRotor (160),EventStopTimeGt (167),EventThermistorOpenCircuit (137),EventThermistorShortCircuit (136),EventThermistorTripLevel (135),EventTimestampfctActiveAndOk (184),EventTM1OutOfRange (141),EventTM1SensorFault (140),EventTM1TripLevelTGt (139),EventTM1WarningLevelTGt (138),EventTM2OutOfRange (29),EventTM2SensorFault (28),EventTM2TripLevelTGt (31),EventTM2WarningLevelTGt (30),EventTripLevelCosPhiLt (156),EventTripLevelIGt (152),EventTripLevelILt (153),EventTripLevelPGt (154),EventTripLevelPLt (155),EventTripLevelULt (157),EventUnbalance (129),EventWarningLevelCosPhiLt (148),EventWarningLevelIGt (144),EventWarningLevelILt (145),EventWarningLevelPGt (146),EventWarningLevelPLt (147),EventWarningLevelULt (149),FaultAntivalence (208),FaultBus (197),FaultConfigurationError (195),FaultDouble0 (205),FaultDouble1 (206),FaultEndPosition (207),FaultExecutionOnCommand (200),FaultExecutionSTOPCommand (201),FaultFeedbackOff (203),FaultFeedbackOn (202),FaultHardwareFaultBasicUnit (192),FaultModuleFault (193),FaultOperationalProtectionOff (211),FaultParameterization (196),FaultPLCPCS (198),FaultPowerFailure (210),FaultStalledPositioner (204),FaultTemporaryComponents (194),FaultTestPositionFeedback (209),FixedLevel0 (1),FixedLevel1 (2),Flashing1Output (248),Flashing2Output (249),Flashing3Output (250),Flicker1Output (251),Flicker2Output (252),Flicker3Output (253),NonvolatileElement1Output (244),NonvolatileElement2Output (245),NonvolatileElement3Output (246),NonvolatileElement4Output (247),NotConnected (0),OPButton1 (33),OPButton2 (34),OPButton3 (35),OPButton4 (36),OPTestResetButton (32),PWMOutput (254),SignalConditioning1Output (240),SignalConditioning2Output (241),SignalConditioning3Output (242),SignalConditioning4Output (243),SignalConditioning5Output (214),SignalConditioning6Output (215),StatusBusOk (99),StatusChangeoverPauseActive (111),StatusCoolingDownPeriodActive (122),StatusCurrentFlowing (101),StatusDeviceOk (98),StatusDeviceTestActive (124),StatusEmergencyStartExecuted (121),StatusEnablingCircuitClosed (127),StatusFeedbackCLOSED (114),StatusFeedbackOPEN (115),StatusGroupFault (96),StatusGroupWarning (97),StatusInterlockingTimeActive (110),StatusOff (106),StatusOnForward (107),StatusOnForwardFast (108),StatusOnReverse (105),StatusOnReverseFast (104),StatusOperationalProtectionOff (119),StatusPauseTimeActive (123),StatusPhaseSequence123 (125),StatusPhaseSequence321 (126),StatusPLCPCSInRun (100),StatusPositionerRunsInCLOSEDDirection (113),StatusPositionerRunsInOPENDirection (112),StatusPROFIenergyCommandStartPausePending (102),StatusRemoteMode (120),StatusStartActive (109),StatusTestPosition (118),StatusTorqueCLOSED (116),StatusTorqueOPEN (117),Timer1Output (232),Timer2Output (233),Timer3Output (234),Timer4Output (235),Timer5Output (230),Timer6Output (231),TruthTable10Output (226),TruthTable11Output (227),TruthTable1Output (216),TruthTable2Output (217),TruthTable3Output (218),TruthTable4Output (219),TruthTable5Output (220),TruthTable6Output (221),TruthTable7Output (222),TruthTable8Output (223),TruthTable9Output1 (224),TruthTable9Output2 (225),WarningFeedbackCircuit (190),WarningSimultaneity (191)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AcyclicReceiveBit00=None
 AcyclicReceiveBit01=None
 AcyclicReceiveBit02=None
 AcyclicReceiveBit03=None
 AcyclicReceiveBit04=None
 AcyclicReceiveBit05=None
 AcyclicReceiveBit06=None
 AcyclicReceiveBit07=None
 AcyclicReceiveBit10=None
 AcyclicReceiveBit11=None
 AcyclicReceiveBit12=None
 AcyclicReceiveBit13=None
 AcyclicReceiveBit14=None
 AcyclicReceiveBit15=None
 AcyclicReceiveBit16=None
 AcyclicReceiveBit17=None
 BUInput1=None
 BUInput2=None
 BUInput3=None
 BUInput4=None
 BUTestResetButton=None
 ContactorControl1QE1=None
 ContactorControl2QE2=None
 ContactorControl3QE3=None
 ContactorControl4QE4=None
 ContactorControl5QE5=None
 Counter1Output=None
 Counter2Output=None
 Counter3Output=None
 Counter4Output=None
 Counter5Output=None
 Counter6Output=None
 CyclicReceiveBit00=None
 CyclicReceiveBit01=None
 CyclicReceiveBit02=None
 CyclicReceiveBit03=None
 CyclicReceiveBit04=None
 CyclicReceiveBit05=None
 CyclicReceiveBit06=None
 CyclicReceiveBit07=None
 CyclicReceiveBit10=None
 CyclicReceiveBit11=None
 CyclicReceiveBit12=None
 CyclicReceiveBit13=None
 CyclicReceiveBit14=None
 CyclicReceiveBit15=None
 CyclicReceiveBit16=None
 CyclicReceiveBit17=None
 DisplayQLAOff=None
 DisplayQLEForward=None
 DisplayQLEForwardFast=None
 DisplayQLEReverse=None
 DisplayQLEReverseFast=None
 DisplayQLSFault=None
 DM1Input1=None
 DM1Input2=None
 DM1Input3=None
 DM1Input4=None
 DM1SensorChannel1=None
 DM1SensorChannel2=None
 DM2Input1=None
 DM2Input2=None
 DM2Input3=None
 DM2Input4=None
 EnabledControlCommandOff=None
 EnabledControlCommandOnForward=None
 EnabledControlCommandOnForwardFast=None
 EnabledControlCommandOnReverse=None
 EnabledControlCommandOnReverseFast=None
 EventAM1OpenCircuit=None
 EventAM1TripLevel0420mAGt=None
 EventAM1TripLevel0420mALt=None
 EventAM1WarningLevel0420mAGt=None
 EventAM1WarningLevel0420mALt=None
 EventAM2OpenCircuit=None
 EventAM2TripLevel0420mAGt=None
 EventAM2TripLevel0420mALt=None
 EventAM2WarningLevel0420mAGt=None
 EventAM2WarningLevel0420mALt=None
 EventConfiguredOperatorPanelMissing=None
 EventDMFLOCALOk=None
 EventExternalFault1=None
 EventExternalFault2=None
 EventExternalFault3=None
 EventExternalFault4=None
 EventExternalFault5=None
 EventExternalFault6=None
 EventExternalGroundFault=None
 EventExternalGroundFaultWarning=None
 EventInternalGroundFault=None
 EventJustOneStartPossible=None
 EventLimitMonitor1=None
 EventLimitMonitor2=None
 EventLimitMonitor3=None
 EventLimitMonitor4=None
 EventLimitMonitor5=None
 EventLimitMonitor6=None
 EventMonitoringPeriodForMandatoryTestingTestRequirement=None
 EventMotorOperatingHoursGt=None
 EventNoStartPermitted=None
 EventNumberOfStartsGt=None
 EventOverload=None
 EventOverloadAndPhaseFailure=None
 EventPrewarningOverload=None
 EventPROFIsafeActive=None
 EventSafetyrelatedTripping=None
 EventStalledRotor=None
 EventStopTimeGt=None
 EventThermistorOpenCircuit=None
 EventThermistorShortCircuit=None
 EventThermistorTripLevel=None
 EventTimestampfctActiveAndOk=None
 EventTM1OutOfRange=None
 EventTM1SensorFault=None
 EventTM1TripLevelTGt=None
 EventTM1WarningLevelTGt=None
 EventTM2OutOfRange=None
 EventTM2SensorFault=None
 EventTM2TripLevelTGt=None
 EventTM2WarningLevelTGt=None
 EventTripLevelCosPhiLt=None
 EventTripLevelIGt=None
 EventTripLevelILt=None
 EventTripLevelPGt=None
 EventTripLevelPLt=None
 EventTripLevelULt=None
 EventUnbalance=None
 EventWarningLevelCosPhiLt=None
 EventWarningLevelIGt=None
 EventWarningLevelILt=None
 EventWarningLevelPGt=None
 EventWarningLevelPLt=None
 EventWarningLevelULt=None
 FaultAntivalence=None
 FaultBus=None
 FaultConfigurationError=None
 FaultDouble0=None
 FaultDouble1=None
 FaultEndPosition=None
 FaultExecutionOnCommand=None
 FaultExecutionSTOPCommand=None
 FaultFeedbackOff=None
 FaultFeedbackOn=None
 FaultHardwareFaultBasicUnit=None
 FaultModuleFault=None
 FaultOperationalProtectionOff=None
 FaultParameterization=None
 FaultPLCPCS=None
 FaultPowerFailure=None
 FaultStalledPositioner=None
 FaultTemporaryComponents=None
 FaultTestPositionFeedback=None
 FixedLevel0=None
 FixedLevel1=None
 Flashing1Output=None
 Flashing2Output=None
 Flashing3Output=None
 Flicker1Output=None
 Flicker2Output=None
 Flicker3Output=None
 NonvolatileElement1Output=None
 NonvolatileElement2Output=None
 NonvolatileElement3Output=None
 NonvolatileElement4Output=None
 NotConnected=None
 OPButton1=None
 OPButton2=None
 OPButton3=None
 OPButton4=None
 OPTestResetButton=None
 PWMOutput=None
 SignalConditioning1Output=None
 SignalConditioning2Output=None
 SignalConditioning3Output=None
 SignalConditioning4Output=None
 SignalConditioning5Output=None
 SignalConditioning6Output=None
 StatusBusOk=None
 StatusChangeoverPauseActive=None
 StatusCoolingDownPeriodActive=None
 StatusCurrentFlowing=None
 StatusDeviceOk=None
 StatusDeviceTestActive=None
 StatusEmergencyStartExecuted=None
 StatusEnablingCircuitClosed=None
 StatusFeedbackCLOSED=None
 StatusFeedbackOPEN=None
 StatusGroupFault=None
 StatusGroupWarning=None
 StatusInterlockingTimeActive=None
 StatusOff=None
 StatusOnForward=None
 StatusOnForwardFast=None
 StatusOnReverse=None
 StatusOnReverseFast=None
 StatusOperationalProtectionOff=None
 StatusPauseTimeActive=None
 StatusPhaseSequence123=None
 StatusPhaseSequence321=None
 StatusPLCPCSInRun=None
 StatusPositionerRunsInCLOSEDDirection=None
 StatusPositionerRunsInOPENDirection=None
 StatusPROFIenergyCommandStartPausePending=None
 StatusRemoteMode=None
 StatusStartActive=None
 StatusTestPosition=None
 StatusTorqueCLOSED=None
 StatusTorqueOPEN=None
 Timer1Output=None
 Timer2Output=None
 Timer3Output=None
 Timer4Output=None
 Timer5Output=None
 Timer6Output=None
 TruthTable10Output=None
 TruthTable11Output=None
 TruthTable1Output=None
 TruthTable2Output=None
 TruthTable3Output=None
 TruthTable4Output=None
 TruthTable5Output=None
 TruthTable6Output=None
 TruthTable7Output=None
 TruthTable8Output=None
 TruthTable9Output1=None
 TruthTable9Output2=None
 value__=None
 WarningFeedbackCircuit=None
 WarningSimultaneity=None

