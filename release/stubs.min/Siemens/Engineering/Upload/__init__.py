# encoding: utf-8
# module Siemens.Engineering.Upload calls itself Upload
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class StationUploadProvider(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Service provides station upload """
 def Equals(self,obj):
  """
  Equals(self: StationUploadProvider,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: StationUploadProvider,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: StationUploadProvider) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: StationUploadProvider,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def StationUpload(self,configurationAddress,uploadConfigurationDelegate):
  """
  StationUpload(self: StationUploadProvider,configurationAddress: ConfigurationAddress,uploadConfigurationDelegate: UploadConfigurationDelegate) -> UploadResult

  

   Service provides station upload functionality

  

   configurationAddress: Configuration address for station upload

   uploadConfigurationDelegate: Upload parameter

   Returns: Siemens.Engineering.Upload.UploadResult
  """
  pass
 def ToString(self):
  """
  ToString(self: StationUploadProvider) -> str

  

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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Configuration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Connection Configuration.



Get: Configuration(self: StationUploadProvider) -> ConnectionConfiguration



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: StationUploadProvider) -> IEngineeringObject



"""



class UploadConfigurationDelegate(MulticastDelegate,ICloneable,ISerializable):
 """ UploadConfigurationDelegate(object: object,method: IntPtr) """
 def BeginInvoke(self,uploadConfiguration,callback,object):
  """ BeginInvoke(self: UploadConfigurationDelegate,uploadConfiguration: UploadConfiguration,callback: AsyncCallback,object: object) -> IAsyncResult """
  pass
 def CombineImpl(self,*args):
  """
  CombineImpl(self: MulticastDelegate,follow: Delegate) -> Delegate

  

   Combines this System.Delegate with the specified System.Delegate to form a new delegate.

  

   follow: The delegate to combine with this delegate.

   Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
  """
  pass
 def DynamicInvokeImpl(self,*args):
  """
  DynamicInvokeImpl(self: Delegate,args: Array[object]) -> object

  

   Dynamically invokes (late-bound) the method represented by the current delegate.

  

   args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- 

    

     ll,if the method represented by the current delegate does not require arguments.

  

   Returns: The object returned by the method represented by the delegate.
  """
  pass
 def EndInvoke(self,result):
  """ EndInvoke(self: UploadConfigurationDelegate,result: IAsyncResult) """
  pass
 def GetMethodImpl(self,*args):
  """
  GetMethodImpl(self: MulticastDelegate) -> MethodInfo

  

   Returns a static method represented by the current System.MulticastDelegate.

   Returns: A static method represented by the current System.MulticastDelegate.
  """
  pass
 def Invoke(self,uploadConfiguration):
  """ Invoke(self: UploadConfigurationDelegate,uploadConfiguration: UploadConfiguration) """
  pass
 def RemoveImpl(self,*args):
  """
  RemoveImpl(self: MulticastDelegate,value: Delegate) -> Delegate

  

   Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified 

    delegate.

  

  

   value: The delegate to search for in the invocation list.

   Returns: If value is found in the invocation list for this instance,then a new System.Delegate without value in its 

    invocation list; otherwise,this instance with its original invocation list.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,object,method):
  """ __new__(cls: type,object: object,method: IntPtr) """
  pass
 def __reduce_ex__(self,*args):
  pass

class UploadResult(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ The results of a Upload """
 def Equals(self,obj):
  """
  Equals(self: UploadResult,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: UploadResult,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: UploadResult) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: UploadResult,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: UploadResult) -> str

  

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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 ErrorCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of errors in a given Upload scenario



Get: ErrorCount(self: UploadResult) -> int



"""

 Messages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection of output messages for the result of a given Upload scenario.



Get: Messages(self: UploadResult) -> UploadResultMessageComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: UploadResult) -> IEngineeringObject



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Final state of a given compile scenario



Get: State(self: UploadResult) -> UploadResultState



"""

 UploadedStation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The uploaded station if upload was successful.



Get: UploadedStation(self: UploadResult) -> Device



"""

 WarningCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of warnings in a given Upload scenario



Get: WarningCount(self: UploadResult) -> int



"""



class UploadResultMessage(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Upload result message """
 def Equals(self,obj):
  """
  Equals(self: UploadResultMessage,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: UploadResultMessage,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: UploadResultMessage) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: UploadResultMessage,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: UploadResultMessage) -> str

  

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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 DateTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Date and time in a Upload message



Get: DateTime(self: UploadResultMessage) -> DateTime



"""

 ErrorCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of errors in a Upload message



Get: ErrorCount(self: UploadResultMessage) -> int



"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Description or content of a Upload message



Get: Message(self: UploadResultMessage) -> str



"""

 Messages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Access to the Upload messages for a given Upload scenario



Get: Messages(self: UploadResultMessage) -> UploadResultMessageComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: UploadResultMessage) -> IEngineeringObject



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Final state in a Upload message



Get: State(self: UploadResultMessage) -> UploadResultState



"""

 WarningCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of warnings in a Upload message



Get: WarningCount(self: UploadResultMessage) -> int



"""



class UploadResultMessageComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[UploadResultMessage],IEquatable[object]):
 """ Composition of Upload result messages. """
 def Contains(self,item):
  """
  Contains(self: UploadResultMessageComposition,item: UploadResultMessage) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: UploadResultMessageComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: UploadResultMessageComposition) -> IEnumerator[UploadResultMessage]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: UploadResultMessageComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: UploadResultMessageComposition,item: UploadResultMessage) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: UploadResultMessageComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[UploadResultMessage](enumerable: IEnumerable[UploadResultMessage],value: UploadResultMessage) -> bool """
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



Get: Count(self: UploadResultMessageComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: UploadResultMessageComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: UploadResultMessageComposition) -> IEngineeringObject



"""



class UploadResultState(Enum,IComparable,IFormattable,IConvertible):
 """
 The list of possible compiler result options

 

 enum UploadResultState,values: Error (3),Information (1),Success (0),Warning (2)
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
 Error=None
 Information=None
 Success=None
 value__=None
 Warning=None


# variables with complex values

