# encoding: utf-8
# module Siemens.Engineering.SW.WatchAndForceTables calls itself WatchAndForceTables
# from Siemens.Engineering,Version=15.1.0.0,Culture=neutral,PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PlcForceTable(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a Plc force table """
 def Equals(self,obj):
  """
  Equals(self: PlcForceTable,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: PlcForceTable,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of a Plc force table

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcForceTable,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcForceTable) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcForceTable,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ShowInEditor(self):
  """
  ShowInEditor(self: PlcForceTable)

   Show the indicated item in the Plc force table editor
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcForceTable) -> str

  

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
 Entries=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of ForceTable Entries



Get: Entries(self: PlcForceTable) -> PlcTableCommentEntryComposition



"""

 IsConsistent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Table is consistent or not



Get: IsConsistent(self: PlcForceTable) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the ForceTable



Get: Name(self: PlcForceTable) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcForceTable) -> IEngineeringObject



"""



class PlcForceTableComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcForceTable],IEquatable[object]):
 """ Composition of PlcForceTables """
 def Contains(self,item):
  """
  Contains(self: PlcForceTableComposition,item: PlcForceTable) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcForceTableComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: PlcForceTableComposition,name: str) -> PlcForceTable

  

   Find force table by name

  

   name: Name of the force table

   Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcForceTable
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcForceTableComposition) -> IEnumerator[PlcForceTable]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcForceTableComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def Import(self,path,importOptions):
  """
  Import(self: PlcForceTableComposition,path: FileInfo,importOptions: ImportOptions) -> IList[PlcForceTable]

  

   Import Plc force table from Simatic ML

  

   path: Path of the Simatic ML which will be imported

   importOptions: Options to use for import from Simatic ML

   Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.WatchAndForceTables.PlcForceTable>
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcForceTableComposition,item: PlcForceTable) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcForceTableComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcForceTable](enumerable: IEnumerable[PlcForceTable],value: PlcForceTable) -> bool """
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



Get: Count(self: PlcForceTableComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcForceTableComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcForceTableComposition) -> IEngineeringObject



"""



class PlcTableCommentEntry(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a Plc Force\Watch table comment entry """
 def Delete(self):
  """
  Delete(self: PlcTableCommentEntry)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcTableCommentEntry,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcTableCommentEntry,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcTableCommentEntry) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcTableCommentEntry,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: PlcTableCommentEntry) -> str

  

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



Get: Parent(self: PlcTableCommentEntry) -> IEngineeringObject



"""



class PlcForceTableEntry(PlcTableCommentEntry,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a Plc force table entry """
 def Equals(self,obj):
  """
  Equals(self: PlcForceTableEntry,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcForceTableEntry) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcForceTableEntry) -> str

  

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



Get: Parent(self: PlcForceTableEntry) -> IEngineeringObject



"""



class PlcTableCommentEntryComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcTableCommentEntry],IEquatable[object]):
 """ Represents a Plc Force\Watch table comment entries """
 def Contains(self,item):
  """
  Contains(self: PlcTableCommentEntryComposition,item: PlcTableCommentEntry) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self):
  """
  Create(self: PlcTableCommentEntryComposition) -> PlcTableCommentEntry

  

   Creates a TableCommentEntry

   Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcTableCommentEntry
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcTableCommentEntryComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcTableCommentEntryComposition) -> IEnumerator[PlcTableCommentEntry]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcTableCommentEntryComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcTableCommentEntryComposition,item: PlcTableCommentEntry) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcTableCommentEntryComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcTableCommentEntry](enumerable: IEnumerable[PlcTableCommentEntry],value: PlcTableCommentEntry) -> bool """
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



Get: Count(self: PlcTableCommentEntryComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcTableCommentEntryComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcTableCommentEntryComposition) -> IEngineeringObject



"""



class PlcWatchAndForceTableDisplayFormat(Enum,IComparable,IFormattable,IConvertible):
 """
 Enum for DisplayFormat

 

 enum PlcWatchAndForceTableDisplayFormat,values: Any_pointer (1),BCD (2),Bin (3),Block_number (13),Bool (4),Character (5),Character_sequence (6),Counter (17),Date (7),DATE_AND_TIME (8),DEC_sequence (9),DEC_signed (10),DEC_unsigned (11),Float (16),Hex (12),Octal (14),Pointer (15),SIMATIC_Time (18),String (19),Time (20),TIME_OF_DAY (21),Undef (0),Unicode_character (22),Unicode_character_sequence (23),Unicode_string (24)
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
 Any_pointer=None
 BCD=None
 Bin=None
 Block_number=None
 Bool=None
 Character=None
 Character_sequence=None
 Counter=None
 Date=None
 DATE_AND_TIME=None
 DEC_sequence=None
 DEC_signed=None
 DEC_unsigned=None
 Float=None
 Hex=None
 Octal=None
 Pointer=None
 SIMATIC_Time=None
 String=None
 Time=None
 TIME_OF_DAY=None
 Undef=None
 Unicode_character=None
 Unicode_character_sequence=None
 Unicode_string=None
 value__=None


class PlcWatchAndForceTableGroup(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Group contatining Plc watch tables """
 def Equals(self,obj):
  """
  Equals(self: PlcWatchAndForceTableGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcWatchAndForceTableGroup,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcWatchAndForceTableGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcWatchAndForceTableGroup,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ToString(self):
  """
  ToString(self: PlcWatchAndForceTableGroup) -> str

  

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
 ForceTables=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of PlcWatchTables



Get: ForceTables(self: PlcWatchAndForceTableGroup) -> PlcForceTableComposition



"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of User Groups



Get: Groups(self: PlcWatchAndForceTableGroup) -> PlcWatchAndForceTableUserGroupComposition



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the Plc watch table group



Get: Name(self: PlcWatchAndForceTableGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcWatchAndForceTableGroup) -> IEngineeringObject



"""

 WatchTables=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of PlcWatchTables



Get: WatchTables(self: PlcWatchAndForceTableGroup) -> PlcWatchTableComposition



"""



class PlcWatchAndForceTablePreDefinedTrigger(Enum,IComparable,IFormattable,IConvertible):
 """
 Enum for PreDefinedTrigger

 

 enum PlcWatchAndForceTablePreDefinedTrigger,values: OnceOnlyAtEnd (4),OnceOnlyAtStart (2),OnceOnlyAtStop (6),Permanent (0),PermanentAtEnd (3),PermanentAtStart (1),PermanentAtStop (5),Undef (7)
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
 OnceOnlyAtEnd=None
 OnceOnlyAtStart=None
 OnceOnlyAtStop=None
 Permanent=None
 PermanentAtEnd=None
 PermanentAtStart=None
 PermanentAtStop=None
 Undef=None
 value__=None


class PlcWatchAndForceTableSystemGroup(PlcWatchAndForceTableGroup,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ System group containing Plc watch tables and Plc force tables and user group containing these """
 def Equals(self,obj):
  """
  Equals(self: PlcWatchAndForceTableSystemGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcWatchAndForceTableSystemGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcWatchAndForceTableSystemGroup) -> str

  

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



Get: Parent(self: PlcWatchAndForceTableSystemGroup) -> IEngineeringObject



"""



class PlcWatchAndForceTableUserGroup(PlcWatchAndForceTableGroup,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ User group containing Plc watch tables """
 def Delete(self):
  """
  Delete(self: PlcWatchAndForceTableUserGroup)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcWatchAndForceTableUserGroup,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcWatchAndForceTableUserGroup) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcWatchAndForceTableUserGroup) -> str

  

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
 """Name of the User Group



Get: Name(self: PlcWatchAndForceTableUserGroup) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcWatchAndForceTableUserGroup) -> IEngineeringObject



"""



class PlcWatchAndForceTableUserGroupComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcWatchAndForceTableUserGroup],IEquatable[object]):
 """ Composition of PlcWatchTableUserGroups """
 def Contains(self,item):
  """
  Contains(self: PlcWatchAndForceTableUserGroupComposition,item: PlcWatchAndForceTableUserGroup) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self,name):
  """
  Create(self: PlcWatchAndForceTableUserGroupComposition,name: str) -> PlcWatchAndForceTableUserGroup

  

   Creates user folder for Plc watch and forcetable collection

  

   name: Name of the group to be created

   Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchAndForceTableUserGroup
  """
  pass
 def CreateFrom(self,sourceMasterCopy):
  """
  CreateFrom(self: PlcWatchAndForceTableUserGroupComposition,sourceMasterCopy: MasterCopy) -> PlcWatchAndForceTableUserGroup

  

   Create PlcBlockUserGroup from MasterCopy

  

   sourceMasterCopy: The source master copy

   Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchAndForceTableUserGroup
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcWatchAndForceTableUserGroupComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: PlcWatchAndForceTableUserGroupComposition,name: str) -> PlcWatchAndForceTableUserGroup

  

   Finds given Plc watch table user group

  

   name: Name of the Plcwatchtable group to search for

   Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchAndForceTableUserGroup
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcWatchAndForceTableUserGroupComposition) -> IEnumerator[PlcWatchAndForceTableUserGroup]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcWatchAndForceTableUserGroupComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcWatchAndForceTableUserGroupComposition,item: PlcWatchAndForceTableUserGroup) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcWatchAndForceTableUserGroupComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcWatchAndForceTableUserGroup](enumerable: IEnumerable[PlcWatchAndForceTableUserGroup],value: PlcWatchAndForceTableUserGroup) -> bool """
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



Get: Count(self: PlcWatchAndForceTableUserGroupComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcWatchAndForceTableUserGroupComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcWatchAndForceTableUserGroupComposition) -> IEngineeringObject



"""



class PlcWatchTable(object,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IShowable,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a Plc watch table """
 def Delete(self):
  """
  Delete(self: PlcWatchTable)

   Deletes this instance.
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcWatchTable,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Export(self,path,exportOptions):
  """
  Export(self: PlcWatchTable,path: FileInfo,exportOptions: ExportOptions)

   Simatic ML export of a Plc watch table

  

   path: Path to the Simatic ML file

   exportOptions: Option to use for export (default,readonly,etc.)
  """
  pass
 def GetAttributes(self,names):
  """ GetAttributes(self: PlcWatchTable,names: IEnumerable[str]) -> IList[object] """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcWatchTable) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def SetAttributes(self,attributes):
  """ SetAttributes(self: PlcWatchTable,attributes: IEnumerable[KeyValuePair[str,object]]) """
  pass
 def ShowInEditor(self):
  """
  ShowInEditor(self: PlcWatchTable)

   Show the indicated item in the Plc watch table editor
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcWatchTable) -> str

  

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
 Entries=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Composition of WatchTable Entries



Get: Entries(self: PlcWatchTable) -> PlcTableCommentEntryComposition



"""

 IsConsistent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Table is consistent or not



Get: IsConsistent(self: PlcWatchTable) -> bool



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the WatchTable



Get: Name(self: PlcWatchTable) -> str



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """EOM parent of this object



Get: Parent(self: PlcWatchTable) -> IEngineeringObject



"""



class PlcWatchTableComposition(object,IEngineeringComposition,IEngineeringCompositionOrObject,IEngineeringInstance,IEnumerable,IInternalCompositionAccess,IInternalCollectionAccess,IInternalInstanceAccess,IInternalBaseAccess,IEnumerable[PlcWatchTable],IEquatable[object]):
 """ Composition of PlcWatchTables """
 def Contains(self,item):
  """
  Contains(self: PlcWatchTableComposition,item: PlcWatchTable) -> bool

  

   Determines if item is contained within.

  

   item: The item being sought.

   Returns: true if item is contained within; otherwise false.
  """
  pass
 def Create(self,name):
  """
  Create(self: PlcWatchTableComposition,name: str) -> PlcWatchTable

  

   Creates a watch table from the given parameters

  

   name: Name of the Plc watch table

   Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchTable
  """
  pass
 def Equals(self,obj):
  """
  Equals(self: PlcWatchTableComposition,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def Find(self,name):
  """
  Find(self: PlcWatchTableComposition,name: str) -> PlcWatchTable

  

   Finds a given Plc watch table

  

   name: The name of the WatchTable

   Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchTable
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PlcWatchTableComposition) -> IEnumerator[PlcWatchTable]

  

   Returns an enumerator that iterates through a collection.

   Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcWatchTableComposition) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def Import(self,path,importOptions):
  """
  Import(self: PlcWatchTableComposition,path: FileInfo,importOptions: ImportOptions) -> IList[PlcWatchTable]

  

   Import Plc watch table from Simatic ML

  

   path: Path of the Simatic ML which will be imported

   importOptions: Options to use for import from Simatic ML

   Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.WatchAndForceTables.PlcWatchTable>
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: PlcWatchTableComposition,item: PlcWatchTable) -> int

  

   Searches for item and returns the zero-based index of the first occurrence within.

  

   item: The item for which an index is sought.

   Returns: The zero-based index of item of the first occurrence within.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcWatchTableComposition) -> str

  

   Returns a System.String that represents the current System.Object.

   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __contains__(self,*args):
  """ __contains__[PlcWatchTable](enumerable: IEnumerable[PlcWatchTable],value: PlcWatchTable) -> bool """
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



Get: Count(self: PlcWatchTableComposition) -> int



"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this instance is read only.



Get: IsReadOnly(self: PlcWatchTableComposition) -> bool



"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent.



Get: Parent(self: PlcWatchTableComposition) -> IEngineeringObject



"""



class PlcWatchTableEntry(PlcTableCommentEntry,IEngineeringObject,IEngineeringCompositionOrObject,IEngineeringInstance,IInternalObjectAccess,IInternalInstanceAccess,IInternalBaseAccess,IEquatable[object]):
 """ Represents a Plc watch table entry """
 def Equals(self,obj):
  """
  Equals(self: PlcWatchTableEntry,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to this instance.

  

   obj: The System.Object to compare with this instance.

   Returns: true if the specified System.Object is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PlcWatchTableEntry) -> int

  

   Returns a hash code for this instance.

   Returns: A hash code for this instance,suitable for use in hashing algorithms and data structures like a hash table.
  """
  pass
 def ToString(self):
  """
  ToString(self: PlcWatchTableEntry) -> str

  

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



Get: Parent(self: PlcWatchTableEntry) -> IEngineeringObject



"""



