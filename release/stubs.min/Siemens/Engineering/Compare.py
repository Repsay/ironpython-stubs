# encoding: utf-8
# module Siemens.Engineering.Compare calls itself Compare
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CompareResult(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Summary object that contains the result of a comparison """
 def Equals(self,obj):
  """
  Equals(self: CompareResult,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: CompareResult,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CompareResult) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: CompareResult,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: CompareResult) -> str

  

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
 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: CompareResult) -> IEngineeringObject



"""

 RootElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Browse to the element containing the result of a given compare scenario



Get: RootElement(self: CompareResult) -> CompareResultElement



"""



class CompareResultElement(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Compare results on an element """
 def Equals(self,obj):
  """
  Equals(self: CompareResultElement,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: CompareResultElement,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CompareResultElement) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: CompareResultElement,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: CompareResultElement) -> str

  

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
 ComparisonResult=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The result of a comparison



Get: ComparisonResult(self: CompareResultElement) -> CompareResultState



"""

 DetailedInformation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Information on the result of a given compare scenario



Get: DetailedInformation(self: CompareResultElement) -> str



"""

 Elements=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Browse to the collection of compare scenarios on a single element



Get: Elements(self: CompareResultElement) -> CompareResultElementComposition



"""

 LeftName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Left side name of a compare scenario on a single element



Get: LeftName(self: CompareResultElement) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: CompareResultElement) -> IEngineeringObject



"""

 RightName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Right side name of a compare scenario on a single element



Get: RightName(self: CompareResultElement) -> str



"""



class CompareResultElementComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[CompareResultElement],IEquatable[object]):
 """ Composition of CompareResultElements """
 def Contains(self,item):
  """
  Contains(self: CompareResultElementComposition,item: CompareResultElement) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: CompareResultElementComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CompareResultElementComposition) -> IEnumerator[CompareResultElement]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CompareResultElementComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: CompareResultElementComposition,item: CompareResultElement) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: CompareResultElementComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[CompareResultElement](enumerable: IEnumerable[CompareResultElement],value: CompareResultElement) -> bool """
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



Get: Count(self: CompareResultElementComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: CompareResultElementComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: CompareResultElementComposition) -> IEngineeringObject



"""



class CompareResultState(Enum,IComparable,IFormattable,IConvertible):
 """
 The list of possible states of a compare result

 

 enum CompareResultState,values: CompareIrrelevant (8),FolderContainsDifferencesOwnStateDifferent (2),FolderContentEqualOwnStateDifferent (3),FolderContentsDifferent (0),FolderContentsIdentical (1),LeftMissing (5),ObjectsDifferent (4),ObjectsIdentical (7),RightMissing (6)
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
 CompareIrrelevant=None
 FolderContainsDifferencesOwnStateDifferent=None
 FolderContentEqualOwnStateDifferent=None
 FolderContentsDifferent=None
 FolderContentsIdentical=None
 LeftMissing=None
 ObjectsDifferent=None
 ObjectsIdentical=None
 RightMissing=None
 value__=None


