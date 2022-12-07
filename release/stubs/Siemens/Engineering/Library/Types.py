# encoding: utf-8
# module Siemens.Engineering.Library.Types calls itself Types
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IInstanceSearchScope:
    """ Scope of the project to search when performing a 'Find instances in project' operation """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ILibraryTypeInstantiationTarget:
    """ Target for instantiation of a library type-version """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ILibraryTypeOrFolderSelection:
    """ A library type or folder. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IUpdateProjectScope:
    """ Represents the scope of the project that may be updated """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LibraryType(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ILibraryTypeOrFolderSelection, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a library type """
    def Delete(self):
        """
        Delete(self: LibraryType)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: LibraryType, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: LibraryType, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryType) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: LibraryType, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: LibraryType) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def UpdateLibrary(self, targetLibrary):
        """
        UpdateLibrary(self: LibraryType, targetLibrary: ILibrary)
            Updates the target library with the latest content from this type
        
            targetLibrary: Target library to update
        """
        pass

    def UpdateProject(self, updateProjectScope):
        """
        UpdateProject(self: LibraryType, updateProjectScope: IUpdateProjectScope)
            Updates the project with the latest content from this type
        
            updateProjectScope: The scope of the project that will be updated.
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

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Author of the library type

Get: Author(self: LibraryType) -> str

"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The library type's comment

Get: Comment(self: LibraryType) -> MultilingualText

"""

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the GUID of this library type

Get: Guid(self: LibraryType) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the library type

Get: Name(self: LibraryType) -> str

Set: Name(self: LibraryType) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LibraryType) -> IEngineeringObject

"""

    Versions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of library type versions

Get: Versions(self: LibraryType) -> LibraryTypeVersionComposition

"""



class LibraryTypeComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[LibraryType], IEquatable[object]):
    """ Composition of LibraryTypes """
    def Contains(self, item):
        """
        Contains(self: LibraryTypeComposition, item: LibraryType) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: LibraryTypeComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: LibraryTypeComposition, name: str) -> LibraryType
        
            Finds a given library type
        
            name: Name to find
            Returns: Siemens.Engineering.Library.Types.LibraryType
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: LibraryTypeComposition) -> IEnumerator[LibraryType]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryTypeComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: LibraryTypeComposition, item: LibraryType) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: LibraryTypeComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LibraryType](enumerable: IEnumerable[LibraryType], value: LibraryType) -> bool """
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

Get: Count(self: LibraryTypeComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: LibraryTypeComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: LibraryTypeComposition) -> IEngineeringObject

"""



class LibraryTypeFolder(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ILibraryTypeOrFolderSelection, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Folder containing library types & library type folders """
    def Equals(self, obj):
        """
        Equals(self: LibraryTypeFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: LibraryTypeFolder, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryTypeFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: LibraryTypeFolder, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: LibraryTypeFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of library type user folders

Get: Folders(self: LibraryTypeFolder) -> LibraryTypeUserFolderComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the library type folder

Get: Name(self: LibraryTypeFolder) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LibraryTypeFolder) -> IEngineeringObject

"""

    Types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of library types

Get: Types(self: LibraryTypeFolder) -> LibraryTypeComposition

"""



class LibraryTypeInstanceInfo(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IEngineeringService, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Library instance service """
    def Equals(self, obj):
        """
        Equals(self: LibraryTypeInstanceInfo, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: LibraryTypeInstanceInfo, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryTypeInstanceInfo) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: LibraryTypeInstanceInfo, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: LibraryTypeInstanceInfo) -> str
        
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

    LibraryTypeInstance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Library type instance

Get: LibraryTypeInstance(self: LibraryTypeInstanceInfo) -> IEngineeringObject

"""

    LibraryTypeVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Connected version

Get: LibraryTypeVersion(self: LibraryTypeInstanceInfo) -> LibraryTypeVersion

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LibraryTypeInstanceInfo) -> IEngineeringObject

"""



class LibraryTypeSystemFolder(LibraryTypeFolder, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ILibraryTypeOrFolderSelection, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ System folder containing library types & library type folders """
    def Equals(self, obj):
        """
        Equals(self: LibraryTypeSystemFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryTypeSystemFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: LibraryTypeSystemFolder) -> str
        
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
    """The name of the library type system folder

Get: Name(self: LibraryTypeSystemFolder) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LibraryTypeSystemFolder) -> IEngineeringObject

"""



class LibraryTypeUserFolder(LibraryTypeFolder, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ILibraryTypeOrFolderSelection, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ User folder containing library types & library type folders """
    def Delete(self):
        """
        Delete(self: LibraryTypeUserFolder)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: LibraryTypeUserFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryTypeUserFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: LibraryTypeUserFolder) -> str
        
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
    """The name of the library type user folder

Get: Name(self: LibraryTypeUserFolder) -> str

Set: Name(self: LibraryTypeUserFolder) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LibraryTypeUserFolder) -> IEngineeringObject

"""



class LibraryTypeUserFolderComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[LibraryTypeUserFolder], IEquatable[object]):
    """ Composition of LibraryTypeUserFolders """
    def Contains(self, item):
        """
        Contains(self: LibraryTypeUserFolderComposition, item: LibraryTypeUserFolder) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: LibraryTypeUserFolderComposition, name: str) -> LibraryTypeUserFolder
        
            Create
        
            name: The name of the library type user folder to be created
            Returns: Siemens.Engineering.Library.Types.LibraryTypeUserFolder
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: LibraryTypeUserFolderComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: LibraryTypeUserFolderComposition, name: str) -> LibraryTypeUserFolder
        
            Finds a given library type user folder
        
            name: Name to find
            Returns: Siemens.Engineering.Library.Types.LibraryTypeUserFolder
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: LibraryTypeUserFolderComposition) -> IEnumerator[LibraryTypeUserFolder]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryTypeUserFolderComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: LibraryTypeUserFolderComposition, item: LibraryTypeUserFolder) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: LibraryTypeUserFolderComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LibraryTypeUserFolder](enumerable: IEnumerable[LibraryTypeUserFolder], value: LibraryTypeUserFolder) -> bool """
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

Get: Count(self: LibraryTypeUserFolderComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: LibraryTypeUserFolderComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: LibraryTypeUserFolderComposition) -> IEngineeringObject

"""



class LibraryTypeVersion(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a library type version """
    def Delete(self):
        """
        Delete(self: LibraryTypeVersion)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: LibraryTypeVersion, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, exportFileInfo, exportOptions):
        """
        Export(self: LibraryTypeVersion, exportFileInfo: FileInfo, exportOptions: ExportOptions)
            Export Version
        
            exportFileInfo: exportFileInfo
            exportOptions: exportOptions
        """
        pass

    def FindInstances(self, searchScope):
        """
        FindInstances(self: LibraryTypeVersion, searchScope: IInstanceSearchScope) -> IList[LibraryTypeInstanceInfo]
        
            Find all instances in the given scope that are connected to this version.
        
            searchScope: Scope within the project to search when performing a 'Find instance in project' operation. This may be a 
             ControllerTarget, HmiTarget, etc.
        
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Library.Types.LibraryTypeInstanceInfo>
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: LibraryTypeVersion, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryTypeVersion) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: LibraryTypeVersion, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: LibraryTypeVersion) -> str
        
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

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Author of the library type version

Get: Author(self: LibraryTypeVersion) -> str

"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The library type version's comment

Get: Comment(self: LibraryTypeVersion) -> MultilingualText

"""

    Dependencies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns all versions that this version depends on

Get: Dependencies(self: LibraryTypeVersion) -> LibraryTypeVersionAssociation

"""

    Dependents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns all versions that depend on this version

Get: Dependents(self: LibraryTypeVersion) -> LibraryTypeVersionAssociation

"""

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the GUID of this library version

Get: Guid(self: LibraryTypeVersion) -> Guid

"""

    MasterCopiesContainingInstances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the master copies that contain instances of this version

Get: MasterCopiesContainingInstances(self: LibraryTypeVersion) -> MasterCopyAssociation

"""

    ModifiedDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the last modified date and time

Get: ModifiedDate(self: LibraryTypeVersion) -> DateTime

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LibraryTypeVersion) -> IEngineeringObject

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the version

Get: State(self: LibraryTypeVersion) -> LibraryTypeVersionState

"""

    TypeObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the connected type object

Get: TypeObject(self: LibraryTypeVersion) -> LibraryType

"""

    VersionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the library version number. The format is Major.Minor.Build

Get: VersionNumber(self: LibraryTypeVersion) -> Version

"""



class LibraryTypeVersionAssociation(object, IEngineeringAssociation, IEngineeringInstance, IEnumerable, IInternalAssociationAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[LibraryTypeVersion], IEquatable[object]):
    """ Associated library type versions """
    def Contains(self, item):
        """
        Contains(self: LibraryTypeVersionAssociation, item: LibraryTypeVersion) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: LibraryTypeVersionAssociation, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: LibraryTypeVersionAssociation) -> IEnumerator[LibraryTypeVersion]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryTypeVersionAssociation) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: LibraryTypeVersionAssociation, item: LibraryTypeVersion) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: LibraryTypeVersionAssociation) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LibraryTypeVersion](enumerable: IEnumerable[LibraryTypeVersion], value: LibraryTypeVersion) -> bool """
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

Get: Count(self: LibraryTypeVersionAssociation) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: LibraryTypeVersionAssociation) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent..

Get: Parent(self: LibraryTypeVersionAssociation) -> IEngineeringObject

"""



class LibraryTypeVersionComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[LibraryTypeVersion], IEquatable[object]):
    """ Composition of LibraryTypeVersions """
    def Contains(self, item):
        """
        Contains(self: LibraryTypeVersionComposition, item: LibraryTypeVersion) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: LibraryTypeVersionComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, versionNumber):
        """
        Find(self: LibraryTypeVersionComposition, versionNumber: Version) -> LibraryTypeVersion
        
            Finds a given library type version
        
            versionNumber: VersionNumber to find
            Returns: Siemens.Engineering.Library.Types.LibraryTypeVersion
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: LibraryTypeVersionComposition) -> IEnumerator[LibraryTypeVersion]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LibraryTypeVersionComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: LibraryTypeVersionComposition, item: LibraryTypeVersion) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: LibraryTypeVersionComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LibraryTypeVersion](enumerable: IEnumerable[LibraryTypeVersion], value: LibraryTypeVersion) -> bool """
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

Get: Count(self: LibraryTypeVersionComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: LibraryTypeVersionComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: LibraryTypeVersionComposition) -> IEngineeringObject

"""



class LibraryTypeVersionState(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the library version object state
    
    enum LibraryTypeVersionState, values: Committed (1), InWork (0)
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

    Committed = None
    InWork = None
    value__ = None


class UpdateCheckMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Used to control verbosity of logging output from the update check
    
    enum UpdateCheckMode, values: ReportOutOfDateAndUpToDate (1), ReportOutOfDateOnly (0)
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

    ReportOutOfDateAndUpToDate = None
    ReportOutOfDateOnly = None
    value__ = None


class UpdateCheckResult(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Result returned from the update check operation """
    def Equals(self, obj):
        """
        Equals(self: UpdateCheckResult, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: UpdateCheckResult, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UpdateCheckResult) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: UpdateCheckResult, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: UpdateCheckResult) -> str
        
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

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Log messages explaining the details of the update check

Get: Messages(self: UpdateCheckResult) -> UpdateCheckResultMessageComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: UpdateCheckResult) -> IEngineeringObject

"""



class UpdateCheckResultMessage(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Log message explaining the details of the update check """
    def Equals(self, obj):
        """
        Equals(self: UpdateCheckResultMessage, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: UpdateCheckResultMessage, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UpdateCheckResultMessage) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: UpdateCheckResultMessage, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: UpdateCheckResultMessage) -> str
        
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

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the header for this result of the update check

Get: Description(self: UpdateCheckResultMessage) -> str

"""

    MessageParts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the log messages specific to each description explaining the details of the update check.

Get: MessageParts(self: UpdateCheckResultMessage) -> IDictionary[str, str]

"""

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Log messages explaining the details of the update check

Get: Messages(self: UpdateCheckResultMessage) -> UpdateCheckResultMessageComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: UpdateCheckResultMessage) -> IEngineeringObject

"""



class UpdateCheckResultMessageComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[UpdateCheckResultMessage], IEquatable[object]):
    """ Composition of UpdateCheckResultMessages """
    def Contains(self, item):
        """
        Contains(self: UpdateCheckResultMessageComposition, item: UpdateCheckResultMessage) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: UpdateCheckResultMessageComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: UpdateCheckResultMessageComposition) -> IEnumerator[UpdateCheckResultMessage]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UpdateCheckResultMessageComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: UpdateCheckResultMessageComposition, item: UpdateCheckResultMessage) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: UpdateCheckResultMessageComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[UpdateCheckResultMessage](enumerable: IEnumerable[UpdateCheckResultMessage], value: UpdateCheckResultMessage) -> bool """
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

Get: Count(self: UpdateCheckResultMessageComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: UpdateCheckResultMessageComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: UpdateCheckResultMessageComposition) -> IEngineeringObject

"""



