# encoding: utf-8
# module Siemens.Engineering.SW.TechnologicalObjects calls itself TechnologicalObjects
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class TechnologicalInstanceDB(InstanceDB,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource):
 """ Instance of a technological DB """
 def Equals(self,obj):
  """
  Equals(self: TechnologicalInstanceDB,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: TechnologicalInstanceDB,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of a TechnlogicalInstanceDB

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TechnologicalInstanceDB) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: TechnologicalInstanceDB) -> str

  

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
 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the Block



Get: Name(self: TechnologicalInstanceDB) -> str



Set: Name(self: TechnologicalInstanceDB)=value

"""

 OfSystemLibElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the system library element associated with the DB



Get: OfSystemLibElement(self: TechnologicalInstanceDB) -> str



"""

 OfSystemLibVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the version of the system library element associated with the DB



Get: OfSystemLibVersion(self: TechnologicalInstanceDB) -> Version



Set: OfSystemLibVersion(self: TechnologicalInstanceDB)=value

"""

 Parameters=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all technological parameters



Get: Parameters(self: TechnologicalInstanceDB) -> TechnologicalParameterComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Parent of this object



Get: Parent(self: TechnologicalInstanceDB) -> IEngineeringObject



"""



class TechnologicalInstanceDBAssociation(object,IEngineeringAssociation,IEngineeringInstance,IEnumerable,IInternalAssociationAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TechnologicalInstanceDB],IEquatable[object]):
 """ TO Association """
 def Add(self,item):
  """
  Add(self: TechnologicalInstanceDBAssociation,item: TechnologicalInstanceDB)

   Adds an item.

  

   item: The item to be added.
  """
  pass
 def Contains(self,item):
  """
  Contains(self: TechnologicalInstanceDBAssociation,item: TechnologicalInstanceDB) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TechnologicalInstanceDBAssociation,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TechnologicalInstanceDBAssociation) -> IEnumerator[TechnologicalInstanceDB]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TechnologicalInstanceDBAssociation) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TechnologicalInstanceDBAssociation,item: TechnologicalInstanceDB) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def Remove(self,item):
  """
  Remove(self: TechnologicalInstanceDBAssociation,item: TechnologicalInstanceDB) -> bool

  

   Removes an item.

  

   item: The item to be removed.

   Returns: true if the item was removed; otherwise false.
  """
  pass
 def ToString(self):
  """
  ToString(self: TechnologicalInstanceDBAssociation) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__[TechnologicalInstanceDB](enumerable: IEnumerable[TechnologicalInstanceDB],value: TechnologicalInstanceDB) -> bool """
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



Get: Count(self: TechnologicalInstanceDBAssociation) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TechnologicalInstanceDBAssociation) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent..



Get: Parent(self: TechnologicalInstanceDBAssociation) -> IEngineeringObject



"""



class TechnologicalInstanceDBComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TechnologicalInstanceDB],IEquatable[object]):
 """ TO composition """
 def Contains(self,item):
  """
  Contains(self: TechnologicalInstanceDBComposition,item: TechnologicalInstanceDB) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self,name,ofSystemLibElement,ofSystemLibVersion):
  """
  Create(self: TechnologicalInstanceDBComposition,name: str,ofSystemLibElement: str,ofSystemLibVersion: Version) -> TechnologicalInstanceDB

  

   Create a new TechnologicalInstanceDB

  

   name: Name of the newly created TechnologicalInstanceDB

   ofSystemLibElement: Associated system library element

   ofSystemLibVersion: Associated system library version

   Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalInstanceDB
  """
  pass
 def CreateFrom(self,sourceMasterCopy):
  """
  CreateFrom(self: TechnologicalInstanceDBComposition,sourceMasterCopy: MasterCopy) -> TechnologicalInstanceDB

  

   Create TechnologicalInstanceDB from MasterCopy

  

   sourceMasterCopy: The source master copy

   Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalInstanceDB
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TechnologicalInstanceDBComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TechnologicalInstanceDBComposition,name: str) -> TechnologicalInstanceDB

  

   Find by its name

  

   name: Name of the TechnologicalInstanceDB

   Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalInstanceDB
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TechnologicalInstanceDBComposition) -> IEnumerator[TechnologicalInstanceDB]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TechnologicalInstanceDBComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TechnologicalInstanceDBComposition,item: TechnologicalInstanceDB) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TechnologicalInstanceDBComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TechnologicalInstanceDB](enumerable: IEnumerable[TechnologicalInstanceDB],value: TechnologicalInstanceDB) -> bool """
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



Get: Count(self: TechnologicalInstanceDBComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TechnologicalInstanceDBComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TechnologicalInstanceDBComposition) -> IEngineeringObject



"""



class TechnologicalInstanceDBGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Contains Technological Objects """
 def Equals(self,obj):
  """
  Equals(self: TechnologicalInstanceDBGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TechnologicalInstanceDBGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TechnologicalInstanceDBGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def SetAttributes(self,attributes):
  """ SetAttributes(self: TechnologicalInstanceDBGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TechnologicalInstanceDBGroup) -> str

  

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
 """Name of external source group



Get: Name(self: TechnologicalInstanceDBGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Parent of this object



Get: Parent(self: TechnologicalInstanceDBGroup) -> IEngineeringObject



"""

 TechnologicalObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get all technological objects



Get: TechnologicalObjects(self: TechnologicalInstanceDBGroup) -> TechnologicalInstanceDBComposition



"""



class TechnologicalInstanceDBSystemGroup(TechnologicalInstanceDBGroup,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Contains Technological Objects """
 def Equals(self,obj):
  """
  Equals(self: TechnologicalInstanceDBSystemGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TechnologicalInstanceDBSystemGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: TechnologicalInstanceDBSystemGroup) -> str

  

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
 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TechnologicalInstanceDBSystemGroup) -> IEngineeringObject



"""



class TechnologicalParameter(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represenst a technological parameter """
 def Equals(self,obj):
  """
  Equals(self: TechnologicalParameter,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TechnologicalParameter,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TechnologicalParameter) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TechnologicalParameter,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TechnologicalParameter) -> str

  

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
 """Represents the name of a technological parameter



Get: Name(self: TechnologicalParameter) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TechnologicalParameter) -> IEngineeringObject



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Represents the value of a technological parameter



Get: Value(self: TechnologicalParameter) -> object



Set: Value(self: TechnologicalParameter)=value

"""



class TechnologicalParameterComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TechnologicalParameter],IEquatable[object]):
 """ Parameter composition """
 def Contains(self,item):
  """
  Contains(self: TechnologicalParameterComposition,item: TechnologicalParameter) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TechnologicalParameterComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TechnologicalParameterComposition,name: str) -> TechnologicalParameter

  

   Finds a TechnologicalParameter by name

  

   name: The name of the TechnologicalParameter

   Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalParameter
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TechnologicalParameterComposition) -> IEnumerator[TechnologicalParameter]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TechnologicalParameterComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TechnologicalParameterComposition,item: TechnologicalParameter) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TechnologicalParameterComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TechnologicalParameter](enumerable: IEnumerable[TechnologicalParameter],value: TechnologicalParameter) -> bool """
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



Get: Count(self: TechnologicalParameterComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TechnologicalParameterComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TechnologicalParameterComposition) -> IEngineeringObject



"""



# variables with complex values

