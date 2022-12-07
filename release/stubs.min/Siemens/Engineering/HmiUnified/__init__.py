# encoding: utf-8
# module Siemens.Engineering.HmiUnified calls itself HmiUnified
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HmiSoftware(Software,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents the software components of a Hmi """
 def Equals(self,obj):
  """
  Equals(self: HmiSoftware,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HmiSoftware) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: HmiSoftware) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AlarmClasses=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """AlarmClasses collection



Get: AlarmClasses(self: HmiSoftware) -> HmiAlarmClassComposition



"""

 AlarmLogs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies HmiAlarmLog collection



Get: AlarmLogs(self: HmiSoftware) -> HmiAlarmLogComposition



"""

 AnalogAlarms=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """AnalogAlarm collection



Get: AnalogAlarms(self: HmiSoftware) -> HmiAnalogAlarmComposition



"""

 Connections=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """HmiConnection Collection



Get: Connections(self: HmiSoftware) -> HmiConnectionComposition



"""

 DataLogs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies HmiDataLog collection



Get: DataLogs(self: HmiSoftware) -> HmiDataLogComposition



"""

 DiscreteAlarms=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """DiscreteAlarms collection



Get: DiscreteAlarms(self: HmiSoftware) -> HmiDiscreteAlarmComposition



"""

 RuntimeSettings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Runtime settings of the hmi device



Get: RuntimeSettings(self: HmiSoftware) -> HmiRuntimeSetting



"""

 SystemTags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Hmi system tag collection



Get: SystemTags(self: HmiSoftware) -> HmiSystemTagComposition



"""

 Tags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Hmi tag collection



Get: Tags(self: HmiSoftware) -> HmiTagComposition



"""

 TagTables=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Hmi tagtables



Get: TagTables(self: HmiSoftware) -> HmiTagTableComposition



"""



# variables with complex values

