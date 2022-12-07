# encoding: utf-8
# module Siemens.Engineering.Hmi.Globalization calls itself Globalization
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MultiLingualGraphic(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a multilingual graphic object of the project """
 def Delete(self):
  """
  Delete(self: MultiLingualGraphic)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: MultiLingualGraphic,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: MultiLingualGraphic,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of a multilingual graphic

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: MultiLingualGraphic,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: MultiLingualGraphic) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: MultiLingualGraphic,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: MultiLingualGraphic) -> str

  

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
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the multilingual graphic



Get: Name(self: MultiLingualGraphic) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: MultiLingualGraphic) -> IEngineeringObject



"""



class MultiLingualGraphicComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[MultiLingualGraphic],IEquatable[object]):
 """ Composition of MultiLingualGraphics """
 def Contains(self,item):
  """
  Contains(self: MultiLingualGraphicComposition,item: MultiLingualGraphic) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: MultiLingualGraphicComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: MultiLingualGraphicComposition,name: str) -> MultiLingualGraphic

  

   Finds a given multilingual graphic

  

   name: Name to find

   Returns: Siemens.Engineering.Hmi.Globalization.MultiLingualGraphic
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: MultiLingualGraphicComposition) -> IEnumerator[MultiLingualGraphic]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: MultiLingualGraphicComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def Import(self,path,importOptions):
  """
  Import(self: MultiLingualGraphicComposition,path: FileInfo,importOptions: ImportOptions) -> IList[MultiLingualGraphic]

  

   Simatic ML import of a multilingual graphic

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import

   Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Globalization.MultiLingualGraphic>
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: MultiLingualGraphicComposition,item: MultiLingualGraphic) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: MultiLingualGraphicComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[MultiLingualGraphic](enumerable: IEnumerable[MultiLingualGraphic],value: MultiLingualGraphic) -> bool """
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



Get: Count(self: MultiLingualGraphicComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: MultiLingualGraphicComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: MultiLingualGraphicComposition) -> IEngineeringObject



"""



