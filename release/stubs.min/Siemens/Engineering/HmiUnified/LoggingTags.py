# encoding: utf-8
# module Siemens.Engineering.HmiUnified.LoggingTags calls itself LoggingTags
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HmiLimitScope(Enum,IComparable,IFormattable,IConvertible):
 """
 Defines the limit scope for the logging tag

 

 enum HmiLimitScope,values: Greater (1),GreaterOrEqual (3),Less (2),LessOrEqual (4),NoLimitsUsed (0),OutsideLimits (7),OutsideOrEqualLimits (8),WithinLimits (5),WithinOrEqualLimits (6)
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
 Greater=None
 GreaterOrEqual=None
 Less=None
 LessOrEqual=None
 NoLimitsUsed=None
 OutsideLimits=None
 OutsideOrEqualLimits=None
 value__=None
 WithinLimits=None
 WithinOrEqualLimits=None


class HmiLoggingMode(Enum,IComparable,IFormattable,IConvertible):
 """
 Hmi Logging mode enum

 

 enum HmiLoggingMode,values: Cyclic (1),OnChange (3),OnDemand (2),Undefined (0)
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
 Cyclic=None
 OnChange=None
 OnDemand=None
 Undefined=None
 value__=None


class HmiLoggingTag(object,IValidator,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents the LoggingTag """
 def Delete(self):
  """
  Delete(self: HmiLoggingTag)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: HmiLoggingTag,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: HmiLoggingTag,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HmiLoggingTag) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: HmiLoggingTag,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: HmiLoggingTag) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def Validate(self):
  """
  Validate(self: HmiLoggingTag) -> IList[HmiValidationResult]

  

   Validates the object

   Returns: System.Collections.Generic.IList<Siemens.Engineering.HmiUnified.Common.HmiValidationResult>
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 HighLimit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the Higher limit



Get: HighLimit(self: HmiLoggingTag) -> object



Set: HighLimit(self: HmiLoggingTag)=value

"""

 LimitScope=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """LimitScope of Hmi Logging Tag



Get: LimitScope(self: HmiLoggingTag) -> HmiLimitScope



Set: LimitScope(self: HmiLoggingTag)=value

"""

 LogConfiguration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Reference to the used data log configuration



Get: LogConfiguration(self: HmiLoggingTag) -> str



Set: LogConfiguration(self: HmiLoggingTag)=value

"""

 LoggingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Logging Mode



Get: LoggingMode(self: HmiLoggingTag) -> HmiLoggingMode



"""

 LowLimit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the Lower limit



Get: LowLimit(self: HmiLoggingTag) -> object



Set: LowLimit(self: HmiLoggingTag)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the Logging Tag



Get: Name(self: HmiLoggingTag) -> str



Set: Name(self: HmiLoggingTag)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: HmiLoggingTag) -> IEngineeringObject



"""

 SmoothingDeltaValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Smoothing delta value



Get: SmoothingDeltaValue(self: HmiLoggingTag) -> float



Set: SmoothingDeltaValue(self: HmiLoggingTag)=value

"""

 SmoothingMaxTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Smoothing max time



Get: SmoothingMaxTime(self: HmiLoggingTag) -> TimeSpan



Set: SmoothingMaxTime(self: HmiLoggingTag)=value

"""

 SmoothingMinTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Smoothing min time



Get: SmoothingMinTime(self: HmiLoggingTag) -> TimeSpan



Set: SmoothingMinTime(self: HmiLoggingTag)=value

"""

 SmoothingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Smoothing mode of the logging tag



Get: SmoothingMode(self: HmiLoggingTag) -> HmiSmoothingMode



Set: SmoothingMode(self: HmiLoggingTag)=value

"""



class HmiLoggingTagComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[HmiLoggingTag],IEquatable[object]):
 """ Represensts Logging Tag Composition """
 def Contains(self,item):
  """
  Contains(self: HmiLoggingTagComposition,item: HmiLoggingTag) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self,name):
  """
  Create(self: HmiLoggingTagComposition,name: str) -> HmiLoggingTag

  

   Create method for Logging Tag

  

   name: Name of the Logging Tag

   Returns: Siemens.Engineering.HmiUnified.LoggingTags.HmiLoggingTag
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: HmiLoggingTagComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: HmiLoggingTagComposition,name: str) -> HmiLoggingTag

  

   Find method for Logging Tag

  

   name: Name of the Logging Tag

   Returns: Siemens.Engineering.HmiUnified.LoggingTags.HmiLoggingTag
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: HmiLoggingTagComposition) -> IEnumerator[HmiLoggingTag]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HmiLoggingTagComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: HmiLoggingTagComposition,item: HmiLoggingTag) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: HmiLoggingTagComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[HmiLoggingTag](enumerable: IEnumerable[HmiLoggingTag],value: HmiLoggingTag) -> bool """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the count.



Get: Count(self: HmiLoggingTagComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: HmiLoggingTagComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: HmiLoggingTagComposition) -> IEngineeringObject



"""



class HmiSmoothingMode(Enum,IComparable,IFormattable,IConvertible):
 """
 Hmi Smoothing Mode

 

 enum HmiSmoothingMode,values: NoSmoothing (0),SwingingDoor (11),Value (1),ValueRelative (8)
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
 NoSmoothing=None
 SwingingDoor=None
 Value=None
 ValueRelative=None
 value__=None


