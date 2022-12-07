# encoding: utf-8
# module Siemens.Engineering.Hmi calls itself Hmi
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84,Siemens.Engineering.Hmi,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ConstValue(object,ILimit):
 """
 Represents an constant value.

 

 ConstValue(value: object)
 """
 def ToString(self):
  """
  ToString(self: ConstValue) -> str

  

   Returns a String that represents the current Object.

   Returns: A String representing the current Object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,value):
  """
  __new__(cls: type,value: object)

  __new__[ConstValue]() -> ConstValue
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the Siemens.Engineering.Hmi.ConstValue.



Get: Value(self: ConstValue) -> object



Set: Value(self: ConstValue)=value

"""



class DateTimeValues(Enum,IComparable,IFormattable,IConvertible):
 """
 A value indicating the granularity of the data or time (eg. Year,Month,etc.).

 

 enum (flags) DateTimeValues,values: Day (4),Hour (8),Minute (16),Month (2),None (0),Second (32),Year (1)
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
 Day=None
 Hour=None
 Minute=None
 Month=None
 None=None
 Second=None
 value__=None
 Year=None


class HmiTarget(Software,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IInstanceSearchScope,IUpdateProjectScope,IEngineeringServiceProvider,IServiceProvider):
 """ Represents the target device """
 def Equals(self,obj):
  """
  Equals(self: HmiTarget,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: HmiTarget,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: HmiTarget) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HmiTarget) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def ImportScreenGlobalElements(self,path,importOptions):
  """
  ImportScreenGlobalElements(self: HmiTarget,path: FileInfo,importOptions: ImportOptions)

   Simatic ML import of screen global elements

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import
  """
  pass
 def ImportScreenOverview(self,path,importOptions):
  """
  ImportScreenOverview(self: HmiTarget,path: FileInfo,importOptions: ImportOptions)

   Simatic ML import of a screen overview

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import
  """
  pass
 def SetAttribute(self,name,value):
  """
  SetAttribute(self: HmiTarget,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def ToString(self):
  """
  ToString(self: HmiTarget) -> str

  

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
 Author=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Author of the device



Get: Author(self: HmiTarget) -> str



"""

 Connections=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of connections



Get: Connections(self: HmiTarget) -> ConnectionComposition



"""

 Cycles=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of cycles



Get: Cycles(self: HmiTarget) -> CycleComposition



"""

 GraphicLists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of graphic lists



Get: GraphicLists(self: HmiTarget) -> GraphicListComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the Hmi target



Get: Name(self: HmiTarget) -> str



"""

 ScreenFolder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Hmi screen system folder



Get: ScreenFolder(self: HmiTarget) -> ScreenSystemFolder



"""

 ScreenGlobalElements=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Hmi screen global elements



Get: ScreenGlobalElements(self: HmiTarget) -> ScreenGlobalElements



"""

 ScreenOverview=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Hmi screen overview



Get: ScreenOverview(self: HmiTarget) -> ScreenOverview



"""

 ScreenPopupFolder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """System folder for the HMI pop-up screens



Get: ScreenPopupFolder(self: HmiTarget) -> ScreenPopupSystemFolder



"""

 ScreenSlideinFolder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """System folder for the HMI slide-in screens



Get: ScreenSlideinFolder(self: HmiTarget) -> ScreenSlideinSystemFolder



"""

 ScreenTemplateFolder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of screen template folders



Get: ScreenTemplateFolder(self: HmiTarget) -> ScreenTemplateSystemFolder



"""

 TagFolder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Hmi tag system folder



Get: TagFolder(self: HmiTarget) -> TagSystemFolder



"""

 TextLists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of text lists



Get: TextLists(self: HmiTarget) -> TextListComposition



"""

 VBScriptFolder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the VBScript system folder



Get: VBScriptFolder(self: HmiTarget) -> VBScriptSystemFolder



"""



class ILimit:
 """ Represents an object which can serve as a limit. """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class NullableDateTime(object):
 """
 Represents an instant in time,typically expressed as a date and time

 

 NullableDateTime(dateTime: DateTime)

 NullableDateTime(dateTime: DateTime,dateTimeValues: DateTimeValues)

 NullableDateTime(nullableDateTime: NullableDateTime)

 NullableDateTime(value: str)
 """
 def Equals(self,obj):
  """
  Equals(self: NullableDateTime,obj: object) -> bool

  

   Indicates whether this instance and a specified object are equal.

  

   obj: Another object to compare to.

   Returns: true if obj and this instance are the same type and represent the same value; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: NullableDateTime) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer that is the hash code for this instance.
  """
  pass
 def ToString(self):
  """
  ToString(self: NullableDateTime) -> str

  

   Converts the value of the current NullableDateTime object to its equivalent string representation.

   Returns: A string representation of the value of the current NullableDateTime object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,dateTime: DateTime)

  __new__(cls: type,dateTime: DateTime,dateTimeValues: DateTimeValues)

  __new__(cls: type,nullableDateTime: NullableDateTime)

  __new__(cls: type,value: str)

  __new__[NullableDateTime]() -> NullableDateTime
  """
  pass
 def __ne__(self,*args):
  pass
 DateTimeValues=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The granularity of the wrapped System.DateTime.



Get: DateTimeValues(self: NullableDateTime) -> DateTimeValues



"""

 Day=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Day



Get: Day(self: NullableDateTime) -> Nullable[int]



Set: Day(self: NullableDateTime)=value

"""

 Hour=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Hour



Get: Hour(self: NullableDateTime) -> Nullable[int]



Set: Hour(self: NullableDateTime)=value

"""

 Minute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Minute



Get: Minute(self: NullableDateTime) -> Nullable[int]



Set: Minute(self: NullableDateTime)=value

"""

 Month=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Month



Get: Month(self: NullableDateTime) -> Nullable[int]



Set: Month(self: NullableDateTime)=value

"""

 Second=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Second



Get: Second(self: NullableDateTime) -> Nullable[int]



Set: Second(self: NullableDateTime)=value

"""

 Year=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Year



Get: Year(self: NullableDateTime) -> Nullable[int]



Set: Year(self: NullableDateTime)=value

"""



# variables with complex values

