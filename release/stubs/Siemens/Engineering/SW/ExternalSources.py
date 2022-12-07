# encoding: utf-8
# module Siemens.Engineering.SW.ExternalSources calls itself ExternalSources
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class GenerateBlockOption(Enum, IComparable, IFormattable, IConvertible):
    """
    Lists the possible options for block generation from source
    
    enum GenerateBlockOption, values: KeepOnError (1), None (0)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    KeepOnError = None
    None = None
    value__ = None


class GenerateOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Options for source generation
    
    enum GenerateOptions, values: None (0), WithDependencies (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    value__ = None
    WithDependencies = None


class IGenerateSource:
    """ Can generate source. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PlcExternalSource(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IMasterCopySource, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a Plc external source """
    def Delete(self):
        """
        Delete(self: PlcExternalSource)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcExternalSource, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GenerateBlocksFromSource(self, generateBlockOption=None):
        """
        GenerateBlocksFromSource(self: PlcExternalSource)
            Creates a block or blocks from the current source file object
        GenerateBlocksFromSource(self: PlcExternalSource, generateBlockOption: GenerateBlockOption) -> IList[IEngineeringObject]
        
            Creates a block or blocks from the current source file object
        
            generateBlockOption: Option to use for block generation from source
            Returns: System.Collections.Generic.IList<Siemens.Engineering.IEngineeringObject>
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: PlcExternalSource, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSource) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: PlcExternalSource, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: PlcExternalSource) -> str
        
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

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plc external source

Get: Name(self: PlcExternalSource) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: PlcExternalSource) -> IEngineeringObject

"""



class PlcExternalSourceComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[PlcExternalSource], IEquatable[object]):
    """ Composition of PlcExternalSources """
    def Contains(self, item):
        """
        Contains(self: PlcExternalSourceComposition, item: PlcExternalSource) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: PlcExternalSourceComposition, name: str) -> PlcExternalSource
        
            Creates a MasterCopy
        
            name: Name of Plc external source to be created
            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        pass

    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcExternalSourceComposition, sourceMasterCopy: MasterCopy) -> PlcExternalSource
        
            Create External Source from MasterCopy
        
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        pass

    def CreateFromFile(self, name, path):
        """
        CreateFromFile(self: PlcExternalSourceComposition, name: str, path: str) -> PlcExternalSource
        
            Create an external source from a specified file
        
            name: Name of Plc external source to be created
            path: Path to the external source file
            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcExternalSourceComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: PlcExternalSourceComposition, name: str) -> PlcExternalSource
        
            Finds a given Plc external source
        
            name: Name to find
            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PlcExternalSourceComposition) -> IEnumerator[PlcExternalSource]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSourceComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: PlcExternalSourceComposition, item: PlcExternalSource) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcExternalSourceComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcExternalSource](enumerable: IEnumerable[PlcExternalSource], value: PlcExternalSource) -> bool """
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

Get: Count(self: PlcExternalSourceComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: PlcExternalSourceComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: PlcExternalSourceComposition) -> IEngineeringObject

"""



class PlcExternalSourceGroup(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Group containing Plc external sources & Plc external source user groups """
    def Equals(self, obj):
        """
        Equals(self: PlcExternalSourceGroup, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: PlcExternalSourceGroup, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSourceGroup) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: PlcExternalSourceGroup, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: PlcExternalSourceGroup) -> str
        
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

    ExternalSources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Plc external sources

Get: ExternalSources(self: PlcExternalSourceGroup) -> PlcExternalSourceComposition

"""

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Plc external source user groups

Get: Groups(self: PlcExternalSourceGroup) -> PlcExternalSourceUserGroupComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plc external source group

Get: Name(self: PlcExternalSourceGroup) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: PlcExternalSourceGroup) -> IEngineeringObject

"""



class PlcExternalSourceSystemGroup(PlcExternalSourceGroup, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ System group containing Plc external sources & Plc external source user groups """
    def Equals(self, obj):
        """
        Equals(self: PlcExternalSourceSystemGroup, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GenerateSource(self, blocks, sourceFile, generateOption=None):
        """ GenerateSource(self: PlcExternalSourceSystemGroup, blocks: IEnumerable[IGenerateSource], sourceFile: FileInfo)GenerateSource(self: PlcExternalSourceSystemGroup, blocks: IEnumerable[IGenerateSource], sourceFile: FileInfo, generateOption: GenerateOptions) """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSourceSystemGroup) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcExternalSourceSystemGroup) -> str
        
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

Get: Parent(self: PlcExternalSourceSystemGroup) -> IEngineeringObject

"""



class PlcExternalSourceUserGroup(PlcExternalSourceGroup, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ User group containing Plc external sources & Plc external source user groups """
    def Delete(self):
        """
        Delete(self: PlcExternalSourceUserGroup)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcExternalSourceUserGroup, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSourceUserGroup) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcExternalSourceUserGroup) -> str
        
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
    """The name of the Plc external source user group

Get: Name(self: PlcExternalSourceUserGroup) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: PlcExternalSourceUserGroup) -> IEngineeringObject

"""



class PlcExternalSourceUserGroupComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[PlcExternalSourceUserGroup], IEquatable[object]):
    """ Composition of PlcExternalSourceUserGroups """
    def Contains(self, item):
        """
        Contains(self: PlcExternalSourceUserGroupComposition, item: PlcExternalSourceUserGroup) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: PlcExternalSourceUserGroupComposition, name: str) -> PlcExternalSourceUserGroup
        
            Creates a MasterCopy
        
            name: Name of group to be created
            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSourceUserGroup
        """
        pass

    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: PlcExternalSourceUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcExternalSourceUserGroup
        
            Create ExternalSourceUserGroup from MasterCopy
        
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSourceUserGroup
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcExternalSourceUserGroupComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: PlcExternalSourceUserGroupComposition, name: str) -> PlcExternalSourceUserGroup
        
            Finds a given Plc external source user group
        
            name: Name to find
            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSourceUserGroup
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PlcExternalSourceUserGroupComposition) -> IEnumerator[PlcExternalSourceUserGroup]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcExternalSourceUserGroupComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: PlcExternalSourceUserGroupComposition, item: PlcExternalSourceUserGroup) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: PlcExternalSourceUserGroupComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcExternalSourceUserGroup](enumerable: IEnumerable[PlcExternalSourceUserGroup], value: PlcExternalSourceUserGroup) -> bool """
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

Get: Count(self: PlcExternalSourceUserGroupComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: PlcExternalSourceUserGroupComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: PlcExternalSourceUserGroupComposition) -> IEngineeringObject

"""



