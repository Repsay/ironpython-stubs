# encoding: utf-8
# module Siemens.Engineering.Hmi.Cycle calls itself Cycle
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Cycle(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a time period for a pass with a possible starting point """
 def Delete(self):
  """
  Delete(self: Cycle)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Cycle,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: Cycle,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of a cycle

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: Cycle,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Cycle) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: Cycle,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: Cycle) -> str

  

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
 IsSystemObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that identifies this is as a system cycle



Get: IsSystemObject(self: Cycle) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the cycle



Get: Name(self: Cycle) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: Cycle) -> IEngineeringObject



"""



class CycleComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[Cycle],IEquatable[object]):
 """ Composition of Cycles """
 def Contains(self,item):
  """
  Contains(self: CycleComposition,item: Cycle) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: CycleComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: CycleComposition,name: str) -> Cycle

  

   Finds a given cycle

  

   name: Name to find

   Returns: Siemens.Engineering.Hmi.Cycle.Cycle
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: CycleComposition) -> IEnumerator[Cycle]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CycleComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def Import(self,path,importOptions):
  """
  Import(self: CycleComposition,path: FileInfo,importOptions: ImportOptions) -> IList[Cycle]

  

   Simatic ML import of a cycle

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import

   Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Cycle.Cycle>
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: CycleComposition,item: Cycle) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: CycleComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Cycle](enumerable: IEnumerable[Cycle],value: Cycle) -> bool """
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



Get: Count(self: CycleComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: CycleComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: CycleComposition) -> IEngineeringObject



"""



