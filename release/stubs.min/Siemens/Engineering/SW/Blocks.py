# encoding: utf-8
# module Siemens.Engineering.SW.Blocks calls itself Blocks
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PlcBlock(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Represents a Plc block """
 def Delete(self):
  """
  Delete(self: PlcBlock)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcBlock,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: PlcBlock,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of a Plc block

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetAttribute(self,name):
  """
  GetAttribute(self: PlcBlock,name: str) -> object

  

   Gets an attribute with the given name.

  

   name: The name of the attribute to get.

   Returns: The attribute with the given name; otherwise,null.
  """
  pass
 def GetAttributeInfos(self):
  """
  GetAttributeInfos(self: PlcBlock) -> IList[EngineeringAttributeInfo]

  

   Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.

   Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcBlock,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcBlock) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def SetAttribute(self,name,value):
  """
  SetAttribute(self: PlcBlock,name: str,value: object)

   Sets value of the attribute.

  

   name: The name of the attribute to set.

   value: The value of the attribute to set.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcBlock,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ShowInEditor(self):
  """
  ShowInEditor(self: PlcBlock)

   Show the indicated item in the Plc block editor
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcBlock) -> str

  

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
 AutoNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if the block gets the block number automatically or manually



Get: AutoNumber(self: PlcBlock) -> bool



Set: AutoNumber(self: PlcBlock)=value

"""

 CodeModifiedDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Last code modification date



Get: CodeModifiedDate(self: PlcBlock) -> DateTime



"""

 CompileDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Last compilation date



Get: CompileDate(self: PlcBlock) -> DateTime



"""

 CreationDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Creation date of this Plc block



Get: CreationDate(self: PlcBlock) -> DateTime



"""

 HeaderAuthor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """PLC header attribute author



Get: HeaderAuthor(self: PlcBlock) -> str



"""

 HeaderFamily=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """PLC header attribute family



Get: HeaderFamily(self: PlcBlock) -> str



"""

 HeaderName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """PLC header attribute name



Get: HeaderName(self: PlcBlock) -> str



"""

 HeaderVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """PLC header attribute version



Get: HeaderVersion(self: PlcBlock) -> Version



"""

 InterfaceModifiedDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Last interface modification



Get: InterfaceModifiedDate(self: PlcBlock) -> DateTime



"""

 IsConsistent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True if block and used data is consistent



Get: IsConsistent(self: PlcBlock) -> bool



"""

 IsKnowHowProtected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the know-how protection status of the block



Get: IsKnowHowProtected(self: PlcBlock) -> bool



"""

 MemoryLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if a block has been optimized



Get: MemoryLayout(self: PlcBlock) -> MemoryLayout



"""

 ModifiedDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Last modification date including e.g. comments



Get: ModifiedDate(self: PlcBlock) -> DateTime



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the Plc block



Get: Name(self: PlcBlock) -> str



Set: Name(self: PlcBlock)=value

"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of this Plc block



Get: Number(self: PlcBlock) -> int



Set: Number(self: PlcBlock)=value

"""

 ParameterModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Date of the last parameter modification



Get: ParameterModified(self: PlcBlock) -> DateTime



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcBlock) -> IEngineeringObject



"""

 ProgrammingLanguage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The language of this block



Get: ProgrammingLanguage(self: PlcBlock) -> ProgrammingLanguage



"""

 StructureModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Date of the last structure modification



Get: StructureModified(self: PlcBlock) -> DateTime



"""



class DataBlock(PlcBlock,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource):
 """ Class representing a data block """
 def Equals(self,obj):
  """
  Equals(self: DataBlock,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DataBlock) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: DataBlock) -> str

  

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

class ArrayDB(DataBlock,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource):
 """ Class representing array DBs """
 def Equals(self,obj):
  """
  Equals(self: ArrayDB,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ArrayDB) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: ArrayDB) -> str

  

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



Get: Parent(self: ArrayDB) -> IEngineeringObject



"""



class BlockType(Enum,IComparable,IFormattable,IConvertible):
 """
 The list of possible IECPL block types

 

 enum BlockType,values: FB (1),FBT (4),SDT (5),SFB (2),UDT (3),Undef (0)
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
 FB=None
 FBT=None
 SDT=None
 SFB=None
 UDT=None
 Undef=None
 value__=None


class CodeBlock(PlcBlock,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource):
 """ Class representing a code block """
 def Equals(self,obj):
  """
  Equals(self: CodeBlock,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CodeBlock) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: CodeBlock) -> str

  

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

class CodeBlockLibraryType(LibraryType,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,ILibraryTypeOrFolderSelection,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Class representing a code block library type """
 def Equals(self,obj):
  """
  Equals(self: CodeBlockLibraryType,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CodeBlockLibraryType) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: CodeBlockLibraryType) -> str

  

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



Get: Name(self: CodeBlockLibraryType) -> str



Set: Name(self: CodeBlockLibraryType)=value

"""



class CodeBlockLibraryTypeVersion(LibraryTypeVersion,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Class representing a code block library type version """
 def Equals(self,obj):
  """
  Equals(self: CodeBlockLibraryTypeVersion,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: CodeBlockLibraryTypeVersion) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: CodeBlockLibraryTypeVersion) -> str

  

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

class FB(CodeBlock,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource):
 """ Represents an FB """
 def Equals(self,obj):
  """
  Equals(self: FB,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: FB) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: FB) -> str

  

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



Get: Parent(self: FB) -> IEngineeringObject



"""

 Supervisions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get supervisions



Get: Supervisions(self: FB) -> SupervisionComposition



"""



class FC(CodeBlock,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource):
 """ Represents an FC """
 def Equals(self,obj):
  """
  Equals(self: FC,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: FC) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: FC) -> str

  

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



Get: Parent(self: FC) -> IEngineeringObject



"""



class GlobalDB(DataBlock,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource):
 """ Represents a global DB """
 def Equals(self,obj):
  """
  Equals(self: GlobalDB,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GlobalDB) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: GlobalDB) -> str

  

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



Get: Parent(self: GlobalDB) -> IEngineeringObject



"""



class InstanceDB(DataBlock,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource):
 """ Represents an instance DB """
 def Equals(self,obj):
  """
  Equals(self: InstanceDB,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: InstanceDB) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: InstanceDB) -> str

  

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
 InstanceOfName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The block name of the father instance (FB/SFB/UDT/SDT)



Get: InstanceOfName(self: InstanceDB) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: InstanceDB) -> IEngineeringObject



"""



class InterfaceSnapshot(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Provides Snapshot Value functionality. """
 def Equals(self,obj):
  """
  Equals(self: InterfaceSnapshot,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: InterfaceSnapshot,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of snapshot values.

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: InterfaceSnapshot,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: InterfaceSnapshot) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: InterfaceSnapshot,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: InterfaceSnapshot) -> str

  

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



Get: Parent(self: InterfaceSnapshot) -> IEngineeringObject



"""



class MemoryLayout(Enum,IComparable,IFormattable,IConvertible):
 """
 Determines if a block access is optimized or not

 

 enum MemoryLayout,values: Optimized (1),Standard (0)
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
 Optimized=None
 Standard=None
 value__=None


class OB(CodeBlock,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IGenerateSource,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource):
 """ Represents an OB """
 def Equals(self,obj):
  """
  Equals(self: OB,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: OB) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: OB) -> str

  

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



Get: Parent(self: OB) -> IEngineeringObject



"""

 SecondaryType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Additional information about the type



Get: SecondaryType(self: OB) -> str



"""



class OBDataExchangeMode(Enum,IComparable,IFormattable,IConvertible):
 """
 Enum for OBDataExchangeMode

 

 enum OBDataExchangeMode,values: Cyclic (1),None (0),Synchronous (2)
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
 None=None
 Synchronous=None
 value__=None


class OBExecution(Enum,IComparable,IFormattable,IConvertible):
 """
 Enum for Execution

 

 enum OBExecution,values: Daily (4),End_of_month (8),Every_minute (2),Hourly (3),Monthly (6),Never (0),Once (1),Weekly (5),Yearly (7)
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
 Daily=None
 End_of_month=None
 Every_minute=None
 Hourly=None
 Monthly=None
 Never=None
 Once=None
 value__=None
 Weekly=None
 Yearly=None


class OBTimeMode(Enum,IComparable,IFormattable,IConvertible):
 """
 Enum for TimeMode

 

 enum OBTimeMode,values: Local (1),None (0),System (2)
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
 Local=None
 None=None
 System=None
 value__=None


class PlcBlockComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcBlock],IEquatable[object]):
 """ Composition of PlcBlocks """
 def Contains(self,item):
  """
  Contains(self: PlcBlockComposition,item: PlcBlock) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def CreateFB(self,name,isAutoNumbered,number,programmingLanguage):
  """
  CreateFB(self: PlcBlockComposition,name: str,isAutoNumbered: bool,number: int,programmingLanguage: ProgrammingLanguage) -> FB

  

   Creates a block.

  

   name: Name of the block.

   isAutoNumbered: Indicates if block is autonumbered.

   number: Number of the block.

   programmingLanguage: Language of the block.

   Returns: Siemens.Engineering.SW.Blocks.FB
  """
  pass
 def CreateFrom(self,*__args):
  """
  CreateFrom(self: PlcBlockComposition,sourceMasterCopy: MasterCopy) -> PlcBlock

  

   Create PlcBlock from MasterCopy

  

   sourceMasterCopy: The source master copy

   Returns: Siemens.Engineering.SW.Blocks.PlcBlock

  CreateFrom(self: PlcBlockComposition,libraryTypeVersion: CodeBlockLibraryTypeVersion) -> PlcBlock

  

   Create from version

  

   libraryTypeVersion: type version

   Returns: Siemens.Engineering.SW.Blocks.PlcBlock
  """
  pass
 def CreateInstanceDB(self,name,isAutoNumbered,number,instanceOfName):
  """
  CreateInstanceDB(self: PlcBlockComposition,name: str,isAutoNumbered: bool,number: int,instanceOfName: str) -> InstanceDB

  

   Creates an instance DB for Prodiag block.

  

   name: Name of the block.

   isAutoNumbered: Indicates if block is autonumbered.

   number: Number of the block.

   instanceOfName: Name of the block where db belongs to.

   Returns: Siemens.Engineering.SW.Blocks.InstanceDB
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcBlockComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: PlcBlockComposition,name: str) -> PlcBlock

  

   Finds a given Plc block

  

   name: Name to find

   Returns: Siemens.Engineering.SW.Blocks.PlcBlock
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcBlockComposition) -> IEnumerator[PlcBlock]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcBlockComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def Import(self,path,importOptions,swImportOptions=None):
  """
  Import(self: PlcBlockComposition,path: FileInfo,importOptions: ImportOptions) -> IList[PlcBlock]

  

   Simatic ML import of a Plc block

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import

   Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Blocks.PlcBlock>

  Import(self: PlcBlockComposition,path: FileInfo,importOptions: ImportOptions,swImportOptions: SWImportOptions) -> IList[PlcBlock]

  

   Simatic ML import of a Plc block with ignore flags.

  

   path: Path to the Simatic ML file

   importOptions: Options to use for Import

   swImportOptions: Sw import options to use for Import

   Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Blocks.PlcBlock>
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcBlockComposition,item: PlcBlock) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcBlockComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcBlock](enumerable: IEnumerable[PlcBlock],value: PlcBlock) -> bool """
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



Get: Count(self: PlcBlockComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcBlockComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcBlockComposition) -> IEngineeringObject



"""



class PlcBlockGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object]):
 """ Group containing Plc blocks & Plc block user groups """
 def Equals(self,obj):
  """
  Equals(self: PlcBlockGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcBlockGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcBlockGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcBlockGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: PlcBlockGroup) -> str

  

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
 Blocks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Plc blocks



Get: Blocks(self: PlcBlockGroup) -> PlcBlockComposition



"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Plc block user groups



Get: Groups(self: PlcBlockGroup) -> PlcBlockUserGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the Plc block group



Get: Name(self: PlcBlockGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcBlockGroup) -> IEngineeringObject



"""



class PlcBlockProtectionProvider(ProtectionProviderBase,IEngineeringService,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Provides protection services. """
 def Equals(self,obj):
  """
  Equals(self: PlcBlockProtectionProvider,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcBlockProtectionProvider) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def Protect(self,*__args):
  """
  Protect(self: PlcBlockProtectionProvider,password: SecureString)

   Sets protection for the underlying object

  

   password: the password to protect the object with
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcBlockProtectionProvider) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def Unprotect(self,*__args):
  """
  Unprotect(self: PlcBlockProtectionProvider,password: SecureString)

   Removes protection for the underlying object

  

   password: the password the underlying object is currently protected with
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



Get: Parent(self: PlcBlockProtectionProvider) -> IEngineeringObject



"""



class PlcBlockSystemGroup(PlcBlockGroup,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopyTarget,ILibraryTypeInstantiationTarget):
 """ System group containing Plc blocks & Plc block user groups """
 def Equals(self,obj):
  """
  Equals(self: PlcBlockSystemGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcBlockSystemGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcBlockSystemGroup) -> str

  

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



Get: Parent(self: PlcBlockSystemGroup) -> IEngineeringObject



"""

 SystemBlockGroups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Plc system block groups



Get: SystemBlockGroups(self: PlcBlockSystemGroup) -> PlcSystemBlockGroupComposition



"""



class PlcBlockUserGroup(PlcBlockGroup,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEngineeringServiceProvider,IServiceProvider,IEquatable[object],IMasterCopySource,IMasterCopyTarget,ILibraryTypeInstantiationTarget):
 """ User group containing Plc blocks & Plc block user groups """
 def Delete(self):
  """
  Delete(self: PlcBlockUserGroup)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcBlockUserGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcBlockUserGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcBlockUserGroup) -> str

  

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
 """The name of the Plc block user group



Get: Name(self: PlcBlockUserGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcBlockUserGroup) -> IEngineeringObject



"""



class PlcBlockUserGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcBlockUserGroup],IEquatable[object]):
 """ Composition of PlcBlockUserGroups """
 def Contains(self,item):
  """
  Contains(self: PlcBlockUserGroupComposition,item: PlcBlockUserGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self,name):
  """
  Create(self: PlcBlockUserGroupComposition,name: str) -> PlcBlockUserGroup

  

   Creates a MasterCopy

  

   name: Name of group to be created

   Returns: Siemens.Engineering.SW.Blocks.PlcBlockUserGroup
  """
  pass
 def CreateFrom(self,sourceMasterCopy):
  """
  CreateFrom(self: PlcBlockUserGroupComposition,sourceMasterCopy: MasterCopy) -> PlcBlockUserGroup

  

   Create PlcBlockUserGroup from MasterCopy

  

   sourceMasterCopy: The source master copy

   Returns: Siemens.Engineering.SW.Blocks.PlcBlockUserGroup
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcBlockUserGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: PlcBlockUserGroupComposition,name: str) -> PlcBlockUserGroup

  

   Finds a given Plc block user group

  

   name: Name to find

   Returns: Siemens.Engineering.SW.Blocks.PlcBlockUserGroup
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcBlockUserGroupComposition) -> IEnumerator[PlcBlockUserGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcBlockUserGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcBlockUserGroupComposition,item: PlcBlockUserGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcBlockUserGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcBlockUserGroup](enumerable: IEnumerable[PlcBlockUserGroup],value: PlcBlockUserGroup) -> bool """
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



Get: Count(self: PlcBlockUserGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcBlockUserGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcBlockUserGroupComposition) -> IEngineeringObject



"""



class PlcSystemBlockGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Group containing Plc system blocks & Plc system block groups """
 def Equals(self,obj):
  """
  Equals(self: PlcSystemBlockGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcSystemBlockGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcSystemBlockGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcSystemBlockGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: PlcSystemBlockGroup) -> str

  

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
 Blocks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Plc system blocks



Get: Blocks(self: PlcSystemBlockGroup) -> PlcBlockComposition



"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of Plc system block groups



Get: Groups(self: PlcSystemBlockGroup) -> PlcSystemBlockGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the Plc system block group



Get: Name(self: PlcSystemBlockGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcSystemBlockGroup) -> IEngineeringObject



"""



class PlcSystemBlockGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcSystemBlockGroup],IEquatable[object]):
 """ Composition of PlcSystemBlockGroups """
 def Contains(self,item):
  """
  Contains(self: PlcSystemBlockGroupComposition,item: PlcSystemBlockGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcSystemBlockGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: PlcSystemBlockGroupComposition,name: str) -> PlcSystemBlockGroup

  

   Finds a given Plc system block group

  

   name: Name to find

   Returns: Siemens.Engineering.SW.Blocks.PlcSystemBlockGroup
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcSystemBlockGroupComposition) -> IEnumerator[PlcSystemBlockGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcSystemBlockGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcSystemBlockGroupComposition,item: PlcSystemBlockGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcSystemBlockGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcSystemBlockGroup](enumerable: IEnumerable[PlcSystemBlockGroup],value: PlcSystemBlockGroup) -> bool """
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



Get: Count(self: PlcSystemBlockGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcSystemBlockGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcSystemBlockGroupComposition) -> IEngineeringObject



"""



class ProgrammingLanguage(Enum,IComparable,IFormattable,IConvertible):
 """
 The list of possible creation languages of programming blocks

 

 enum ProgrammingLanguage,values: CFC (8),CPU_DB (7),DB (5),F_CALL (26),F_DB (18),F_FBD (17),F_FBD_LIB (20),F_LAD (16),F_LAD_LIB (19),F_STL (15),FBD (3),FBD_IEC (10),FCP (21),FLD (22),GRAPH (6),LAD (2),LAD_IEC (11),Motion_DB (25),ProDiag (23),ProDiag_OB (24),RSE (14),S7_PDIAG (13),SCL (4),SDB (12),SFC (9),STL (1),Undef (0)
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
 CFC=None
 CPU_DB=None
 DB=None
 FBD=None
 FBD_IEC=None
 FCP=None
 FLD=None
 F_CALL=None
 F_DB=None
 F_FBD=None
 F_FBD_LIB=None
 F_LAD=None
 F_LAD_LIB=None
 F_STL=None
 GRAPH=None
 LAD=None
 LAD_IEC=None
 Motion_DB=None
 ProDiag=None
 ProDiag_OB=None
 RSE=None
 S7_PDIAG=None
 SCL=None
 SDB=None
 SFC=None
 STL=None
 Undef=None
 value__=None


class Supervision(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Supervision """
 def Equals(self,obj):
  """
  Equals(self: Supervision,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: Supervision,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Supervision) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: Supervision,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: Supervision) -> str

  

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



Get: Parent(self: Supervision) -> IEngineeringObject



"""



class SupervisionComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[Supervision],IEquatable[object]):
 """ Supervisions of the block """
 def Contains(self,item):
  """
  Contains(self: SupervisionComposition,item: Supervision) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: SupervisionComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: SupervisionComposition) -> IEnumerator[Supervision]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SupervisionComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: SupervisionComposition,item: Supervision) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: SupervisionComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[Supervision](enumerable: IEnumerable[Supervision],value: Supervision) -> bool """
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



Get: Count(self: SupervisionComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: SupervisionComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: SupervisionComposition) -> IEngineeringObject



"""



