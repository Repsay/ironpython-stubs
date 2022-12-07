# encoding: utf-8
# module Siemens.Engineering.SW.Types calls itself Types
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PlcType(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IMasterCopySource,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Represents a Plc type """
 def Delete(self):
  """
  Delete(self: PlcType)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcType,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: PlcType,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of a Plc type

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: PlcType,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: PlcType) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcType,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcType) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def SetAttribute(self,name,value):
  """
  SetAttribute(self: PlcType,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcType,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ShowInEditor(self):
  """
  ShowInEditor(self: PlcType)

   Show the indicated item in the Plc type editor
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcType) -> str

  

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
 CreationDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Creation date of this Plc type



Get: CreationDate(self: PlcType) -> DateTime



"""

 InterfaceModifiedDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get last breakable interface change of the PLC data type



Get: InterfaceModifiedDate(self: PlcType) -> DateTime



"""

 IsConsistent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if block and used data is consistent



Get: IsConsistent(self: PlcType) -> bool



"""

 IsKnowHowProtected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the know-how protection status of the block



Get: IsKnowHowProtected(self: PlcType) -> bool



"""

 ModifiedDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the last non-breakable modification of the PLC data type



Get: ModifiedDate(self: PlcType) -> DateTime



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the Plc type



Get: Name(self: PlcType) -> str



Set: Name(self: PlcType)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcType) -> IEngineeringObject



"""



class PlcStruct(PlcType,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IMasterCopySource,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Represents a Plc struct """
 def Equals(self,obj):
  """
  Equals(self: PlcStruct,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcStruct) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcStruct) -> str

  

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



Get: Parent(self: PlcStruct) -> IEngineeringObject



"""



class PlcSystemTypeGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Group containing Plc system types """
 def Equals(self,obj):
  """
  Equals(self: PlcSystemTypeGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcSystemTypeGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcSystemTypeGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcSystemTypeGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: PlcSystemTypeGroup) -> str

  

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
 """The name of the Plc system type group



Get: Name(self: PlcSystemTypeGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcSystemTypeGroup) -> IEngineeringObject



"""

 Types=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Plc system types



Get: Types(self: PlcSystemTypeGroup) -> PlcTypeComposition



"""



class PlcSystemTypeGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcSystemTypeGroup],IEquatable[object]):
 """ Composition of PlcSystemTypeGroups """
 def Contains(self,item):
  """
  Contains(self: PlcSystemTypeGroupComposition,item: PlcSystemTypeGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcSystemTypeGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcSystemTypeGroupComposition) -> IEnumerator[PlcSystemTypeGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcSystemTypeGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcSystemTypeGroupComposition,item: PlcSystemTypeGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcSystemTypeGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcSystemTypeGroup](enumerable: IEnumerable[PlcSystemTypeGroup],value: PlcSystemTypeGroup) -> bool """
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



Get: Count(self: PlcSystemTypeGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcSystemTypeGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcSystemTypeGroupComposition) -> IEngineeringObject



"""



class PlcTypeComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcType],IEquatable[object]):
 """ Composition of PlcTypes """
 def Contains(self,item):
  """
  Contains(self: PlcTypeComposition,item: PlcType) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,*__args):
  """
  CreateFrom(self: PlcTypeComposition,sourceMasterCopy: MasterCopy) -> PlcType

  

   Create PlcType from MasterCopy

  

   sourceMasterCopy: The source master copy

   Returns: Siemens.Engineering.SW.Types.PlcType

  CreateFrom(self: PlcTypeComposition,libraryTypeVersion: PlcTypeLibraryTypeVersion) -> PlcType

  

   Create plc type from type version

  

   libraryTypeVersion: Library type version

   Returns: Siemens.Engineering.SW.Types.PlcType
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcTypeComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: PlcTypeComposition,name: str) -> PlcType

  

   Finds a given Plc type

  

   name: Name to find

   Returns: Siemens.Engineering.SW.Types.PlcType
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcTypeComposition) -> IEnumerator[PlcType]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcTypeComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def Import(self,path,importOptions,swImportOptions=None):
  """
  Import(self: PlcTypeComposition,path: FileInfo,importOptions: ImportOptions) -> IList[PlcType]

  

   Simatic ML import of a Plc type

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import

   Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Types.PlcType>

  Import(self: PlcTypeComposition,path: FileInfo,importOptions: ImportOptions,swImportOptions: SWImportOptions) -> IList[PlcType]

  

   Simatic ML import of a Plc type

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import

   swImportOptions: Sw import options to use for Import

   Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Types.PlcType>
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcTypeComposition,item: PlcType) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcTypeComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcType](enumerable: IEnumerable[PlcType],value: PlcType) -> bool """
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



Get: Count(self: PlcTypeComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcTypeComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcTypeComposition) -> IEngineeringObject



"""



class PlcTypeGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Group containing Plc types & Plc type user groups """
 def Equals(self,obj):
  """
  Equals(self: PlcTypeGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcTypeGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcTypeGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcTypeGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: PlcTypeGroup) -> str

  

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
 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Plc type user groups



Get: Groups(self: PlcTypeGroup) -> PlcTypeUserGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the Plc type group



Get: Name(self: PlcTypeGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcTypeGroup) -> IEngineeringObject



"""

 Types=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Plc types



Get: Types(self: PlcTypeGroup) -> PlcTypeComposition



"""



class PlcTypeLibraryType(LibraryType,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,ILibraryTypeOrFolderSelection,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a library type made from a Plc type """
 def Equals(self,obj):
  """
  Equals(self: PlcTypeLibraryType,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcTypeLibraryType) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcTypeLibraryType) -> str

  

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
 """Name



Get: Name(self: PlcTypeLibraryType) -> str



Set: Name(self: PlcTypeLibraryType)=value

"""



class PlcTypeLibraryTypeVersion(LibraryTypeVersion,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a library type version made from a Plc type """
 def Equals(self,obj):
  """
  Equals(self: PlcTypeLibraryTypeVersion,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcTypeLibraryTypeVersion) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcTypeLibraryTypeVersion) -> str

  

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

class PlcTypeSystemGroup(PlcTypeGroup,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopyTarget,ILibraryTypeInstantiationTarget):
 """ System group containing Plc types & Plc type user groups """
 def Equals(self,obj):
  """
  Equals(self: PlcTypeSystemGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcTypeSystemGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcTypeSystemGroup) -> str

  

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



Get: Parent(self: PlcTypeSystemGroup) -> IEngineeringObject



"""

 SystemTypeGroups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of system data types



Get: SystemTypeGroups(self: PlcTypeSystemGroup) -> PlcSystemTypeGroupComposition



"""



class PlcTypeUserGroup(PlcTypeGroup,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource,IMasterCopyTarget,ILibraryTypeInstantiationTarget):
 """ User group containing Plc types & Plc type user groups """
 def Delete(self):
  """
  Delete(self: PlcTypeUserGroup)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcTypeUserGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcTypeUserGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcTypeUserGroup) -> str

  

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
 """The name of the Plc type user group



Get: Name(self: PlcTypeUserGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcTypeUserGroup) -> IEngineeringObject



"""



class PlcTypeUserGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcTypeUserGroup],IEquatable[object]):
 """ Composition of PlcTypeUserGroups """
 def Contains(self,item):
  """
  Contains(self: PlcTypeUserGroupComposition,item: PlcTypeUserGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self,name):
  """
  Create(self: PlcTypeUserGroupComposition,name: str) -> PlcTypeUserGroup

  

   Create the user folder for the PLC data type collection

  

   name: Name of group to be created

   Returns: Siemens.Engineering.SW.Types.PlcTypeUserGroup
  """
  pass
 def CreateFrom(self,sourceMasterCopy):
  """
  CreateFrom(self: PlcTypeUserGroupComposition,sourceMasterCopy: MasterCopy) -> PlcTypeUserGroup

  

   Create PlcTypeUserGroup from MasterCopy

  

   sourceMasterCopy: The source master copy

   Returns: Siemens.Engineering.SW.Types.PlcTypeUserGroup
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcTypeUserGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: PlcTypeUserGroupComposition,name: str) -> PlcTypeUserGroup

  

   Finds a given Plc type user group

  

   name: Name to find

   Returns: Siemens.Engineering.SW.Types.PlcTypeUserGroup
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcTypeUserGroupComposition) -> IEnumerator[PlcTypeUserGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcTypeUserGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcTypeUserGroupComposition,item: PlcTypeUserGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcTypeUserGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcTypeUserGroup](enumerable: IEnumerable[PlcTypeUserGroup],value: PlcTypeUserGroup) -> bool """
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



Get: Count(self: PlcTypeUserGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcTypeUserGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcTypeUserGroupComposition) -> IEngineeringObject



"""



