# encoding: utf-8
# module Siemens.Engineering.SW.Tags calls itself Tags
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PlcConstant(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IMasterCopySource, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a Plc constant """
    def Equals(self, obj):
        """
        Equals(self: PlcConstant, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: PlcConstant, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcConstant) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: PlcConstant, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: PlcConstant) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DataTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the data type of this constant

Get: DataTypeName(self: PlcConstant) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plc constant

Get: Name(self: PlcConstant) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: PlcConstant) -> IEngineeringObject

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the value of this constant.

Get: Value(self: PlcConstant) -> str

"""



class PlcSystemConstant(PlcConstant, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IMasterCopySource, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a Plc system constant """
    def Equals(self, obj):
        """
        Equals(self: PlcSystemConstant, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcSystemConstant) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcSystemConstant) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class PlcSystemConstantComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[PlcSystemConstant], IEquatable[object]):
    """ Composition of PlcSystemConstants """
    def Contains(self, item):
        """
        Contains(self: PlcSystemConstantComposition, item: PlcSystemConstant) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcSystemConstantComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: PlcSystemConstantComposition, name: str) -> PlcSystemConstant
        
            Finds a given Plc system constant
        
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcSystemConstant
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PlcSystemConstantComposition) -> IEnumerator[PlcSystemConstant]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcSystemConstantComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: PlcSystemConstantComposition, item: PlcSystemConstant) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcSystemConstantComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcSystemConstant](enumerable: IEnumerable[PlcSystemConstant], value: PlcSystemConstant) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: PlcSystemConstantComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: PlcSystemConstantComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: PlcSystemConstantComposition) -> IEngineeringObject

"""



class PlcTag(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IMasterCopySource, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringServiceProvider, IServiceProvider, IEquatable[object]):
    """ Represents a Plc tag """
    def Delete(self):
        """
        Delete(self: PlcTag)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcTag, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, path, exportOptions):
        """
        Export(self: PlcTag, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc tag
        
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: PlcTag, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTag) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def SetAttributes(self, attributes):
        """ SetAttributes(self: PlcTag, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: PlcTag) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The multilingual comment of the PlcTag

Get: Comment(self: PlcTag) -> MultilingualText

"""

    DataTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the data type of this tag

Get: DataTypeName(self: PlcTag) -> str

Set: DataTypeName(self: PlcTag) = value
"""

    ExternalAccessible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Internal use only

Get: ExternalAccessible(self: PlcTag) -> bool

Set: ExternalAccessible(self: PlcTag) = value
"""

    ExternalVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this tag should be shown when browsing for tags from an HMI editor

Get: ExternalVisible(self: PlcTag) -> bool

Set: ExternalVisible(self: PlcTag) = value
"""

    ExternalWritable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether this tag can be written to when browsing for tags from an HMI editor

Get: ExternalWritable(self: PlcTag) -> bool

Set: ExternalWritable(self: PlcTag) = value
"""

    LogicalAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address in the PLC's address space

Get: LogicalAddress(self: PlcTag) -> str

Set: LogicalAddress(self: PlcTag) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plc tag

Get: Name(self: PlcTag) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: PlcTag) -> IEngineeringObject

"""



class PlcTagComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[PlcTag], IEquatable[object]):
    """ Composition of PlcTags """
    def Contains(self, item):
        """
        Contains(self: PlcTagComposition, item: PlcTag) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name, dataTypeName=None, logicalAddress=None):
        """
        Create(self: PlcTagComposition, name: str) -> PlcTag
        
            Creates a PLC tag from the given parameters
        
            name: The name of the plc tag to be created
            Returns: Siemens.Engineering.SW.Tags.PlcTag
        Create(self: PlcTagComposition, name: str, dataTypeName: str, logicalAddress: str) -> PlcTag
        
            Creates a PLC tag from the given parameters
        
            name: The name of the plc tag to be created
            dataTypeName: The data type name of the plc tag to be created
            logicalAddress: The logical address of the plc tag to be created
            Returns: Siemens.Engineering.SW.Tags.PlcTag
        """
        pass

    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcTagComposition, sourceMasterCopy: MasterCopy) -> PlcTag
        
            Create PlcTag from MasterCopy
        
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Tags.PlcTag
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcTagComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: PlcTagComposition, name: str) -> PlcTag
        
            Finds a given Plc tag
        
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcTag
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PlcTagComposition) -> IEnumerator[PlcTag]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def Import(self, path, importOptions):
        """
        Import(self: PlcTagComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcTag]
        
            Simatic ML import of a Plc tag
        
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Tags.PlcTag>
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: PlcTagComposition, item: PlcTag) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcTagComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTag](enumerable: IEnumerable[PlcTag], value: PlcTag) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: PlcTagComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: PlcTagComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: PlcTagComposition) -> IEngineeringObject

"""



class PlcTagTable(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IShowable, IMasterCopySource, IMasterCopyTarget, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringServiceProvider, IServiceProvider, IEquatable[object]):
    """ Represents a Plc tag table """
    def Delete(self):
        """
        Delete(self: PlcTagTable)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcTagTable, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, path, exportOptions):
        """
        Export(self: PlcTagTable, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc tag table
        
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: PlcTagTable, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTable) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def SetAttributes(self, attributes):
        """ SetAttributes(self: PlcTagTable, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ShowInEditor(self):
        """
        ShowInEditor(self: PlcTagTable)
            Show the indicated item in the Plc tag table editor
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcTagTable) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if this tag table is the default tag table

Get: IsDefault(self: PlcTagTable) -> bool

"""

    ModifiedTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents the last modified timestamp of this tag table

Get: ModifiedTimeStamp(self: PlcTagTable) -> DateTime

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plc tag table

Get: Name(self: PlcTagTable) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: PlcTagTable) -> IEngineeringObject

"""

    SystemConstants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Plc system constants

Get: SystemConstants(self: PlcTagTable) -> PlcSystemConstantComposition

"""

    Tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Plc tags

Get: Tags(self: PlcTagTable) -> PlcTagComposition

"""

    UserConstants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Plc user constants

Get: UserConstants(self: PlcTagTable) -> PlcUserConstantComposition

"""



class PlcTagTableComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[PlcTagTable], IEquatable[object]):
    """ Composition of PlcTagTables """
    def Contains(self, item):
        """
        Contains(self: PlcTagTableComposition, item: PlcTagTable) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: PlcTagTableComposition, name: str) -> PlcTagTable
        
            Creates a tag table from the given parameters
        
            name: Internal use only
            Returns: Siemens.Engineering.SW.Tags.PlcTagTable
        """
        pass

    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcTagTableComposition, sourceMasterCopy: MasterCopy) -> PlcTagTable
        
            Create PlcTagTable from MasterCopy
        
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Tags.PlcTagTable
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcTagTableComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: PlcTagTableComposition, name: str) -> PlcTagTable
        
            Finds a given Plc tag table
        
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcTagTable
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PlcTagTableComposition) -> IEnumerator[PlcTagTable]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTableComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def Import(self, path, importOptions):
        """
        Import(self: PlcTagTableComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcTagTable]
        
            Simatic ML import of a Plc tag table
        
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Tags.PlcTagTable>
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: PlcTagTableComposition, item: PlcTagTable) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcTagTableComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTagTable](enumerable: IEnumerable[PlcTagTable], value: PlcTagTable) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: PlcTagTableComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: PlcTagTableComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: PlcTagTableComposition) -> IEngineeringObject

"""



class PlcTagTableGroup(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringServiceProvider, IServiceProvider, IEquatable[object]):
    """ Group containing Plc tag tables & Plc tag table user groups """
    def Equals(self, obj):
        """
        Equals(self: PlcTagTableGroup, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: PlcTagTableGroup, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTableGroup) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def SetAttributes(self, attributes):
        """ SetAttributes(self: PlcTagTableGroup, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: PlcTagTableGroup) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Plc tag table user groups

Get: Groups(self: PlcTagTableGroup) -> PlcTagTableUserGroupComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plc tag table group

Get: Name(self: PlcTagTableGroup) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: PlcTagTableGroup) -> IEngineeringObject

"""

    TagTables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Plc tag tables

Get: TagTables(self: PlcTagTableGroup) -> PlcTagTableComposition

"""



class PlcTagTableSystemGroup(PlcTagTableGroup, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringServiceProvider, IServiceProvider, IEquatable[object], IMasterCopyTarget):
    """ System group containing Plc tag tables & Plc tag table user groups """
    def Equals(self, obj):
        """
        Equals(self: PlcTagTableSystemGroup, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTableSystemGroup) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcTagTableSystemGroup) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: PlcTagTableSystemGroup) -> IEngineeringObject

"""



class PlcTagTableUserGroup(PlcTagTableGroup, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringServiceProvider, IServiceProvider, IEquatable[object], IMasterCopySource, IMasterCopyTarget):
    """ User group containing Plc tag tables & Plc tag table user groups """
    def Delete(self):
        """
        Delete(self: PlcTagTableUserGroup)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcTagTableUserGroup, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTableUserGroup) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcTagTableUserGroup) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plc tag table user group

Get: Name(self: PlcTagTableUserGroup) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: PlcTagTableUserGroup) -> IEngineeringObject

"""



class PlcTagTableUserGroupComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[PlcTagTableUserGroup], IEquatable[object]):
    """ Composition of PlcTagTableUserGroups """
    def Contains(self, item):
        """
        Contains(self: PlcTagTableUserGroupComposition, item: PlcTagTableUserGroup) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: PlcTagTableUserGroupComposition, name: str) -> PlcTagTableUserGroup
        
            Create user folder for PLC tag collection
        
            name: Name of group to be created
            Returns: Siemens.Engineering.SW.Tags.PlcTagTableUserGroup
        """
        pass

    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcTagTableUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcTagTableUserGroup
        
            Create PlcTagTableUserGroup from MasterCopy
        
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Tags.PlcTagTableUserGroup
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcTagTableUserGroupComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: PlcTagTableUserGroupComposition, name: str) -> PlcTagTableUserGroup
        
            Finds a given Plc tag table user group
        
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcTagTableUserGroup
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PlcTagTableUserGroupComposition) -> IEnumerator[PlcTagTableUserGroup]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcTagTableUserGroupComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: PlcTagTableUserGroupComposition, item: PlcTagTableUserGroup) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcTagTableUserGroupComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTagTableUserGroup](enumerable: IEnumerable[PlcTagTableUserGroup], value: PlcTagTableUserGroup) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: PlcTagTableUserGroupComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: PlcTagTableUserGroupComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: PlcTagTableUserGroupComposition) -> IEngineeringObject

"""



class PlcUserConstant(PlcConstant, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IMasterCopySource, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object], IEngineeringServiceProvider, IServiceProvider):
    """ Represents a Plc user constant """
    def Delete(self):
        """
        Delete(self: PlcUserConstant)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcUserConstant, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, path, exportOptions):
        """
        Export(self: PlcUserConstant, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc constant
        
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcUserConstant) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def ToString(self):
        """
        ToString(self: PlcUserConstant) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The comment of the user constant

Get: Comment(self: PlcUserConstant) -> MultilingualText

"""

    DataTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the data type of this constant

Get: DataTypeName(self: PlcUserConstant) -> str

Set: DataTypeName(self: PlcUserConstant) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plc constant

Get: Name(self: PlcUserConstant) -> str

Set: Name(self: PlcUserConstant) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the value of this constant.

Get: Value(self: PlcUserConstant) -> str

Set: Value(self: PlcUserConstant) = value
"""



class PlcUserConstantComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[PlcUserConstant], IEquatable[object]):
    """ Composition of PlcUserConstants """
    def Contains(self, item):
        """
        Contains(self: PlcUserConstantComposition, item: PlcUserConstant) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name, dataTypeName=None, value=None):
        """
        Create(self: PlcUserConstantComposition, name: str) -> PlcUserConstant
        
            Creates a plc user constant from the given parameters
        
            name: The name of the user constant to be created
            Returns: Siemens.Engineering.SW.Tags.PlcUserConstant
        Create(self: PlcUserConstantComposition, name: str, dataTypeName: str, value: str) -> PlcUserConstant
        
            Creates a plc user constant from the given parameters
        
            name: The name of the user constant to be created
            dataTypeName: The name of the data type of the user constant to be created
            value: The value of the user constant to be created
            Returns: Siemens.Engineering.SW.Tags.PlcUserConstant
        """
        pass

    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcUserConstantComposition, sourceMasterCopy: MasterCopy) -> PlcUserConstant
        
            Create PlcUserConstant from MasterCopy
        
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Tags.PlcUserConstant
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcUserConstantComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: PlcUserConstantComposition, name: str) -> PlcUserConstant
        
            Finds a given Plc user constant
        
            name: Name to find
            Returns: Siemens.Engineering.SW.Tags.PlcUserConstant
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PlcUserConstantComposition) -> IEnumerator[PlcUserConstant]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcUserConstantComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def Import(self, path, importOptions):
        """
        Import(self: PlcUserConstantComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcUserConstant]
        
            Simatic ML import of a Plc constant
        
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Tags.PlcUserConstant>
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: PlcUserConstantComposition, item: PlcUserConstant) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcUserConstantComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcUserConstant](enumerable: IEnumerable[PlcUserConstant], value: PlcUserConstant) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: PlcUserConstantComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: PlcUserConstantComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: PlcUserConstantComposition) -> IEngineeringObject

"""



