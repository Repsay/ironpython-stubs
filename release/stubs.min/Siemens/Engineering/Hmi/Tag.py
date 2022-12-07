# encoding: utf-8
# module Siemens.Engineering.Hmi.Tag calls itself Tag
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HmiUdtLibraryType(LibraryType,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,ILibraryTypeOrFolderSelection,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a library type made from a Udt """
 def Equals(self,obj):
  """
  Equals(self: HmiUdtLibraryType,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HmiUdtLibraryType) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: HmiUdtLibraryType) -> str

  

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



Get: Name(self: HmiUdtLibraryType) -> str



Set: Name(self: HmiUdtLibraryType)=value

"""



class HmiUdtLibraryTypeVersion(LibraryTypeVersion,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a library type version made from a Udt """
 def Equals(self,obj):
  """
  Equals(self: HmiUdtLibraryTypeVersion,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HmiUdtLibraryTypeVersion) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: HmiUdtLibraryTypeVersion) -> str

  

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



Get: Parent(self: HmiUdtLibraryTypeVersion) -> IEngineeringObject



"""



class Tag(object,ILimit,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IMasterCopySource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Represents an Hmi tag """
 def Delete(self):
  """
  Delete(self: Tag)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: Tag,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: Tag,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of a tag

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: Tag,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: Tag) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: Tag,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Tag) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def SetAttribute(self,name,value):
  """
  SetAttribute(self: Tag,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: Tag,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: Tag) -> str

  

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
 """The name of the tag



Get: Name(self: Tag) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: Tag) -> IEngineeringObject



"""



class TagComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[Tag],IEquatable[object]):
 """ Composition of (Hmi)Tags """
 def Contains(self,item):
  """
  Contains(self: TagComposition,item: Tag) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,sourceMasterCopy):
  """
  CreateFrom(self: TagComposition,sourceMasterCopy: MasterCopy) -> Tag

  

   Create Tag from MasterCopy

  

   sourceMasterCopy: The source master copy

   Returns: Siemens.Engineering.Hmi.Tag.Tag
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TagComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TagComposition,name: str) -> Tag

  

   Finds a given tag

  

   name: Name to find

   Returns: Siemens.Engineering.Hmi.Tag.Tag
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TagComposition) -> IEnumerator[Tag]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def Import(self,path,importOptions):
  """
  Import(self: TagComposition,path: FileInfo,importOptions: ImportOptions) -> IList[Tag]

  

   Simatic ML import of a tag

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import

   Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Tag.Tag>
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TagComposition,item: Tag) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TagComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Tag](enumerable: IEnumerable[Tag],value: Tag) -> bool """
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



Get: Count(self: TagComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TagComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TagComposition) -> IEngineeringObject



"""



class TagFolder(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Folder containing Hmi tag tables & Hmi tag user folders """
 def Equals(self,obj):
  """
  Equals(self: TagFolder,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TagFolder,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagFolder) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TagFolder,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TagFolder) -> str

  

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
 Folders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of tag user folders



Get: Folders(self: TagFolder) -> TagUserFolderComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the tag folder



Get: Name(self: TagFolder) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TagFolder) -> IEngineeringObject



"""

 TagTables=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Hmi tag tables



Get: TagTables(self: TagFolder) -> TagTableComposition



"""



class TagSystemFolder(TagFolder,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IMasterCopyTarget):
 """ System folder containing Hmi tag tables & Hmi tag user folders """
 def Equals(self,obj):
  """
  Equals(self: TagSystemFolder,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagSystemFolder) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: TagSystemFolder) -> str

  

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
 DefaultTagTable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the default Hmi tag table



Get: DefaultTagTable(self: TagSystemFolder) -> TagTable



"""

 Folders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of tag user folders



Get: Folders(self: TagSystemFolder) -> TagUserFolderComposition



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TagSystemFolder) -> IEngineeringObject



"""

 TagTables=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Hmi tag tables



Get: TagTables(self: TagSystemFolder) -> TagTableComposition



"""



class TagTable(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IMasterCopySource,IMasterCopyTarget,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents an Hmi tag table """
 def Delete(self):
  """
  Delete(self: TagTable)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TagTable,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: TagTable,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of a tag table

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: TagTable,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagTable) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: TagTable,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: TagTable) -> str

  

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
 """Gets a value that identifies this is the default tag table



Get: IsSystemObject(self: TagTable) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the tag table



Get: Name(self: TagTable) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TagTable) -> IEngineeringObject



"""

 Tags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Hmi tags



Get: Tags(self: TagTable) -> TagComposition



"""



class TagTableComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TagTable],IEquatable[object]):
 """ Composition of (Hmi)TagTables """
 def Contains(self,item):
  """
  Contains(self: TagTableComposition,item: TagTable) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFrom(self,sourceMasterCopy):
  """
  CreateFrom(self: TagTableComposition,sourceMasterCopy: MasterCopy) -> TagTable

  

   Create TagTable from MasterCopy

  

   sourceMasterCopy: The source master copy

   Returns: Siemens.Engineering.Hmi.Tag.TagTable
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TagTableComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TagTableComposition,name: str) -> TagTable

  

   Finds a given tag table

  

   name: Name to find

   Returns: Siemens.Engineering.Hmi.Tag.TagTable
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TagTableComposition) -> IEnumerator[TagTable]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagTableComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def Import(self,path,importOptions):
  """
  Import(self: TagTableComposition,path: FileInfo,importOptions: ImportOptions) -> IList[TagTable]

  

   Simatic ML import of a tag table

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import

   Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Tag.TagTable>
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TagTableComposition,item: TagTable) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TagTableComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TagTable](enumerable: IEnumerable[TagTable],value: TagTable) -> bool """
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



Get: Count(self: TagTableComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TagTableComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TagTableComposition) -> IEngineeringObject



"""



class TagUserFolder(TagFolder,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object],IMasterCopySource,IMasterCopyTarget):
 """ User folder containing Hmi tag tables & Hmi tag user folders """
 def Delete(self):
  """
  Delete(self: TagUserFolder)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TagUserFolder,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagUserFolder) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: TagUserFolder) -> str

  

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
 Folders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of tag user folders



Get: Folders(self: TagUserFolder) -> TagUserFolderComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the tag user folder



Get: Name(self: TagUserFolder) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: TagUserFolder) -> IEngineeringObject



"""

 TagTables=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Hmi tag tables



Get: TagTables(self: TagUserFolder) -> TagTableComposition



"""



class TagUserFolderComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[TagUserFolder],IEquatable[object]):
 """ Composition of (Hmi)TagUserFolders """
 def Contains(self,item):
  """
  Contains(self: TagUserFolderComposition,item: TagUserFolder) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self,name):
  """
  Create(self: TagUserFolderComposition,name: str) -> TagUserFolder

  

   Creates a tag user folder

  

   name: Name of folder to be created

   Returns: Siemens.Engineering.Hmi.Tag.TagUserFolder
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: TagUserFolderComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: TagUserFolderComposition,name: str) -> TagUserFolder

  

   Finds a given tag user folder

  

   name: Name to find

   Returns: Siemens.Engineering.Hmi.Tag.TagUserFolder
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: TagUserFolderComposition) -> IEnumerator[TagUserFolder]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TagUserFolderComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: TagUserFolderComposition,item: TagUserFolder) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: TagUserFolderComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[TagUserFolder](enumerable: IEnumerable[TagUserFolder],value: TagUserFolder) -> bool """
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



Get: Count(self: TagUserFolderComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: TagUserFolderComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: TagUserFolderComposition) -> IEngineeringObject



"""



